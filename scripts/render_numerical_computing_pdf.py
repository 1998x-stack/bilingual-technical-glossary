#!/usr/bin/env python3
"""Create the numerical computing bilingual glossary from its curated TSV source.

Requires reportlab and a bundled system CJK font; writes an editable Markdown
publication and a searchable, font-embedded PDF. Does not modify other domains.
"""
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable

BASE = Path(__file__).resolve().parents[1]
SRC=BASE/'data/numerical-computing.tsv'
MD=BASE/'glossaries/numerical-computing.md'
PDF=BASE/'pdf/numerical-computing.pdf'

CONTRASTS = [
('机器精度间隔 vs 单位舍入误差界', 'binary64 的 nextafter(1,+∞)-1 是 2^-52；在最近舍入模型下常取 u=2^-53。两者常被混称 machine epsilon，使用时需说明约定。'),
('病态问题 vs 不稳定算法', '病态是数学问题本身对输入扰动敏感；不稳定是特定算法会额外放大舍入或计算扰动。两者相互独立。'),
('前向误差 vs 后向误差 vs 残差', '前向误差比较解的距离；后向误差寻找使计算结果精确成立所需的输入改动；残差直接代入方程，量纲与尺度需额外处理。'),
('相容性 vs 收敛性 vs 稳定性', '相容性描述离散算子逼近原问题；稳定性控制误差传播；收敛性描述最终解趋近真解。不能在所有问题上不加前提地互推。'),
('截断误差 vs 舍入误差', '截断误差通常随步长变小而下降；舍入误差可能在步长太小时被放大，因此更小步长不一定更准。'),
('插值 vs 回归拟合', '插值要求在节点处匹配数据；回归拟合通常允许残差以抑制噪声或追求泛化。'),
('LU vs QR vs SVD', 'LU 通常用于一般可逆方程组；QR 常用于最小二乘；SVD 便于秩分析和病态问题处理，但成本往往较高。'),
('正规方程 vs QR 最小二乘', '正规方程通过 A* A 求解，2-范数条件数在满列秩时通常被平方；QR 避免显式形成 A* A，数值上通常更稳健。'),
('浮点格式精度 vs 算法精度', '使用 FP64 并不意味着获得约 16 位可靠数字；条件数、离散误差、算法稳定性和输入误差都会影响可信位数。'),
('CG vs GMRES', '经典 CG 要求线性算子对应对称正定矩阵；GMRES 可处理更一般非对称系统，但需要存储/正交化克里洛夫基。'),
('显式法 vs 隐式法', '显式时间步常无需求解联立非线性方程，刚性问题步长可能受限；隐式法常更稳定但每步求解更昂贵。'),
('FDM vs FEM vs FVM', '有限差分直接近似微分；有限元通过弱形式和基函数离散；有限体积通过控制体积通量表达守恒。'),
('FMA vs 分开乘加', 'FMA 在融合运算中对乘积加和作一次结果舍入，因此通常可降低舍入误差；它不保证与两步执行逐位一致。'),
('绝对容差 vs 相对容差', '接近零时绝对容差尤为重要；量级很大时相对容差更合适。常见策略是 |err| ≤ atol + rtol·scale。'),
('确定性 vs 跨硬件逐位复现', '固定随机种子只是必要条件之一；多线程归约次序、FMA、库实现和硬件差异仍可能改变浮点末位。'),
]
REFERENCES = [
('IEEE 754-2019 - IEEE Standard for Floating-Point Arithmetic','https://standards.ieee.org/ieee/754/6210/'),
('Nicholas J. Higham - Accuracy and Stability of Numerical Algorithms','https://epubs.siam.org/doi/book/10.1137/1.9780898718027'),
('Fundamentals of Numerical Computation - T. A. Driscoll and R. J. Braun','https://fncbook.com/'),
('Netlib LAPACK User Guide','https://www.netlib.org/lapack/lug/'),
('NumPy Linear Algebra Reference','https://numpy.org/doc/stable/reference/routines.linalg.html'),
('SciPy Reference - Optimization, Integration, Sparse and Linear Algebra','https://docs.scipy.org/doc/scipy/reference/'),
('NIST DLMF - Digital Library of Mathematical Functions','https://dlmf.nist.gov/'),
]

def load():
  rows=[]; topic=''; chapter=0; seen=set(); chapters=[]
  for line_no,raw in enumerate(SRC.read_text(encoding='utf-8').splitlines(),1):
    line=raw.strip()
    if not line: continue
    if line.startswith('# '):
      number,topic=line[2:].split(' ',1)
      chapter += 1
      if int(number)!=chapter: raise ValueError(f'Nonsequential chapter {line_no}')
      chapters.append((chapter,topic)); continue
    parts=[v.strip() for v in line.split('|')]
    if len(parts)!=4 or not (parts[0] and parts[1] and parts[3]): raise ValueError(f'Malformed line {line_no}')
    en,zh,abbr,definition=parts
    key=(chapter,en.casefold(),zh)
    if key in seen:raise ValueError(f'Duplicate term {key}')
    if not topic:raise ValueError(f'No chapter before line {line_no}')
    seen.add(key)
    rows.append(dict(category='numerical-computing',chapter=chapter,topic=topic,en=en,zh=zh,abbr=abbr,definition=definition))
  assert len(rows)==259 and len(chapters)==17
  return rows

def markdown(rows):
  groups=defaultdict(list)
  for r in rows:groups[(r['chapter'],r['topic'])].append(r)
  lines=['# 数值计算专有名词中英文对照表','', '# Numerical Computing · Chinese–English Technical Glossary', '',
    '> TERM/ATLAS · 2026 Edition · 原创教学性简明释义；术语在数值分析、科学计算、线性代数与计算工程语境下使用，不代表标准机构的唯一官方译法。','',
    f'**{len(rows)} 条术语 · {len(groups)} 个主题 · {len(CONTRASTS)} 组易混概念辨析**','',
    '## 主题目录','']
  for (n,name),items in groups.items():lines.append(f'- {n:02d}. {name}（{len(items)} 条）')
  lines += ['', '## 阅读约定', '',
    '- `abbr` 仅填写真实常用缩写；空白不是缺失数据。数学符号另在正文解释，不将数学符号伪装成缩写。',
    '- 区分 problem conditioning、algorithm stability 与 computed residual；不同误差指标须指定尺度、范数和误差模型。',
    '- 本手册是专业术语学习材料，不应当作为 IEEE 标准、教科书公式或软件 API 的替代。', '', '---','']
  for (n,name),items in groups.items():
    lines += [f'## {n:02d}. {name}', '', '| # | English term | 中文译名 | Abbr. | 简明释义 |', '|---:|---|---|---|---|']
    for i,r in enumerate(items,1):
      cols=[str(i),r['en'],r['zh'],r['abbr'],r['definition']]
      lines.append('| '+' | '.join(s.replace('|','\\|') for s in cols)+' |')
    lines.append('')
  lines += ['---','','## 重点易混术语辨析','']
  for i,(t,desc) in enumerate(CONTRASTS,1):lines.extend([f'**{i:02d}. {t}**', '',desc,''])
  lines+=['## 参考资料与术语核验入口','','参考资料用于核对核心定义、算法分类与工程实现；并不表示每个译名由相应组织正式批准。','']
  for name,url in REFERENCES:lines.append(f'- [{name}]({url})')
  lines+=['','## 数据来源与维护','','- 权威可编辑词表：`data/numerical-computing.tsv`。','- GitHub 仓库：<https://github.com/1998x-stack/bilingual-technical-glossary>。','- 此版本共计 259 条领域条目，不代表全站跨学科去重数量。','- 专业审稿状态：待独立领域专家逐条校对；欢迎提交附权威证据的 PR。','']
  MD.write_text('\n'.join(lines),encoding='utf8')

FONT='/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf'
if not Path(FONT).exists():raise RuntimeError('Install fonts-arphic-gbsn00lp to render portable Chinese PDF')
pdfmetrics.registerFont(TTFont('CJK',FONT))
ink=colors.HexColor('#17253B'); muted=colors.HexColor('#64748b'); accent=colors.HexColor('#0D6B8A'); accentlight=colors.HexColor('#EEF8FB'); pale=colors.HexColor('#F8FBFE'); line=colors.HexColor('#DCE5ED')
base=ParagraphStyle('b',fontName='CJK',fontSize=7.7,leading=12,wordWrap='CJK',textColor=ink,allowWidows=0,allowOrphans=0)
small=ParagraphStyle('s',parent=base,fontSize=7.35,leading=11)
head=ParagraphStyle('h',parent=base,fontSize=8,leading=13,textColor=accent)
sub=ParagraphStyle('sub',parent=base,fontSize=14,leading=22,spaceAfter=8,spaceBefore=11,keepWithNext=True)
cover_t=ParagraphStyle('ct',parent=base,fontSize=28,leading=43,spaceAfter=10)
cover_en=ParagraphStyle('ce',parent=base,fontSize=14,leading=24,textColor=muted)
body=ParagraphStyle('body',parent=base,fontSize=9.3,leading=16)
label=ParagraphStyle('label',parent=base,fontSize=9,leading=15,textColor=accent)
footer=ParagraphStyle('foot',parent=base,fontSize=8,leading=13,textColor=muted)

def P(s,style=base):return Paragraph(escape(str(s)),style)

def paint(canvas,doc):
  w,h=A4
  canvas.setFillColor(accent); canvas.rect(0,h-8,w,8,stroke=0,fill=1)
  canvas.setStrokeColor(line); canvas.line(42,44,w-42,44)
  canvas.setFillColor(muted);canvas.setFont('CJK',8)
  canvas.drawString(42,27,'TERM/ATLAS    /    数值计算 · Numerical Computing')
  canvas.drawRightString(w-42,27,f'{doc.page:02d}')

def make_pdf(rows):
  groups=defaultdict(list)
  for r in rows:groups[(r['chapter'],r['topic'])].append(r)
  doc=SimpleDocTemplate(str(PDF),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=52,bottomMargin=56,title='数值计算专有名词中英文对照表 | Numerical Computing Glossary',author='TERM/ATLAS',subject='259 curated numerical computing terms across 17 chapters',pageCompression=1)
  story=[Spacer(1,38),P('TERM/ATLAS     ·     BILINGUAL TECHNICAL REFERENCE',label),Spacer(1,23),P('数值计算',cover_t),P('专有名词中英文对照表',cover_t),Spacer(1,18),P('Numerical Computing',cover_en),P('Chinese–English Terminology Handbook · 2026',cover_en),Spacer(1,33),P('259 TERMS    /    17 TOPICS    /    15 CONCEPT CONTRASTS',sub),Spacer(1,14),P('覆盖浮点数、误差分析、条件数、非线性求根、插值、积分、矩阵分解、稀疏迭代、优化、常微分与偏微分方程、随机计算及科学软件。',body),Spacer(1,22),P('面向数值分析课程、科研论文阅读、科学计算与工程实现。',body),Spacer(1,19),P('编排说明：独立原创术语释义；不等同于官方标准全文，也不宣称已完成逐条专家审稿。',footer),PageBreak(),P('目录  /  CONTENTS',sub),Spacer(1,10)]
  for (n,name),items in groups.items():story.append(P(f'{n:02d}    {name}    /    {len(items)} terms',body))
  story += [Spacer(1,13),P('专业阅读提示',sub),P('注意将机器精度间隔与单位舍入误差界区分；算法稳定性不等于问题良态；计算残差也不总能直接代表解误差。',body),PageBreak()]
  width=A4[0]-84
  col=[146,100,47,width-293]
  for (n,name),items in groups.items():
    story.extend([P(f'{n:02d}    {name}',sub),P(f'{len(items)} TERMS  ·  ENGLISH / 中文 / ABBR. / DEFINITION',label),Spacer(1,5)])
    data=[[P('ENGLISH TERM',head),P('中文术语',head),P('ABBR.',head),P('简明释义',head)]]
    data += [[P(r['en'],small),P(r['zh'],small),P(r['abbr'],small),P(r['definition'],small)] for r in items]
    table=Table(data,colWidths=col,repeatRows=1,hAlign='LEFT',splitByRow=1)
    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),accentlight), ('LINEBELOW',(0,0),(-1,0),1.1,accent),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,pale]),('LINEBELOW',(0,1),(-1,-1),0.3,line),
        ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story += [table,Spacer(1,14)]
  story += [PageBreak(),P('核心易混概念辨析  /  CONCEPT CONTRASTS',sub),Spacer(1,8)]
  for i,(t,desc) in enumerate(CONTRASTS,1):
    story.append(KeepTogether([P(f'{i:02d}   {t}',body),P(desc,base),Spacer(1,11)]))
  story += [Spacer(1,10),P('参考资料  /  SOURCES',sub)]
  for name,url in REFERENCES:story.extend([P(name,body),P(url,small),Spacer(1,7)])
  story+=[Spacer(1,11),P('数据源：data/numerical-computing.tsv。所有释义为教学性简述，具体标准和软件语义请以原始文档及使用版本为准。',footer)]
  doc.build(story,onFirstPage=paint,onLaterPages=paint)

if __name__=='__main__':
  r=load();markdown(r);make_pdf(r)
  print(f'{len(r)} terms; Markdown {MD.stat().st_size} bytes; PDF {PDF.stat().st_size} bytes')