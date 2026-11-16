from pathlib import Path
from collections import defaultdict
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT,TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'data/signal-processing.tsv'
MD = ROOT / 'glossaries/signal-processing.md'
PDF = ROOT / 'pdf/signal-processing.pdf'

def load():
    rows=[]; chapter=0; topic=''; counts=defaultdict(int); seen=set()
    for line_no,line in enumerate(SRC.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():continue
        if line.startswith('# '):
            chapter+=1; topic=line[2:].strip(); continue
        fields=[x.strip() for x in line.split('|')]
        if len(fields)!=4 or not all(fields[i] for i in (0,1,3)):
            raise ValueError(f'invalid source line {line_no}')
        en,zh,abbr,definition=fields
        key=(chapter,en.casefold(),zh)
        if key in seen:raise ValueError(f'duplicate {key}')
        seen.add(key);counts[chapter]+=1
        rows.append(dict(category='signal-processing',chapter=chapter,topic=topic,en=en,zh=zh,abbr=abbr,definition=definition))
    assert chapter==18 and len(rows)==295
    return rows

DISTINCTIONS = [
('FFT 与 DFT','DFT 是有限序列的数学变换；FFT 是快速计算 DFT 的算法族。'),
('DTFT 与 DFT','DTFT 在频率上连续且以 2π 为周期；DFT 对有限序列只给出 N 个频点。'),
('采样率与奈奎斯特频率','采样率 fs 是每秒样本数；奈奎斯特频率 fs/2；基带带限信号的奈奎斯特速率为最高频率的两倍。'),
('混叠与频谱泄漏','混叠由采样引起频谱重叠；泄漏由有限观测窗使频谱能量扩散。'),
('补零与分辨率','补零细化频率采样网格，通常不提高区分相近真实频率分量的能力。'),
('卷积与互相关','卷积涉及时间反转后相乘积分或求和；互相关衡量两个信号随相对位移的相似程度。'),
('FIR 与 IIR','FIR 冲激响应有限；IIR 响应通常无限延续。两者不是简单按是否使用反馈直接等价分类。'),
('Hann 与 Hamming','Hann 窗和 Hamming 窗采用不同余弦系数；“Hanning”是常见俗称，规范英文为 Hann。'),
('谱与功率谱密度','谱的幅值、平方幅值与 PSD 的频率单位及归一化不同，不能直接比较数值。'),
('LTI 稳定性与因果性','稳定性约束输入输出有界关系；因果性约束输出对未来输入的依赖，两者独立。'),
('群时延与相位时延','群时延为负相位斜率；相位时延为负相位除以角频率，二者一般并不相同。'),
('插值与上采样','单纯插入零是上采样的一个步骤；插值还需要适当滤波以恢复中间值。'),
]

REFS = [
('MIT OCW — Signals and Systems','https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/'),
('SciPy — Signal Processing Reference','https://docs.scipy.org/doc/scipy/reference/signal.html'),
('IEEE Signal Processing Society — Technical Committees','https://signalprocessingsociety.org/community-involvement/technical-committees'),
]

def markdown(rows):
    groups=defaultdict(list)
    for r in rows:groups[(r['chapter'],r['topic'])].append(r)
    out=['# 信号处理专有名词中英文对照表','', '# Signal Processing · Chinese–English Technical Glossary','',
        '> TERM/ATLAS · 2026 Edition · 术语采用常见信号与系统、DSP 与工程实现语境；释义为独立编写的教学性简述，不代表标准组织的强制译名。','',
        f'**{len(rows)} 条术语 · {len(groups)} 个主题 · 中英文对照 / 常用缩写 / 简明释义**','',
        '## 学科目录','']
    for (n,topic),items in groups.items():out.append(f'- {n:02d}. {topic}（{len(items)} 条）')
    out+=['','## 阅读说明','','- 连续时间角频率通常用 rad/s，离散时间角频率通常用 rad/sample；Hz 与角频率不可直接混用。','- 常见缩写只在技术文献中广泛使用时标注；空白表示不强行编造缩写。','- 某些译名存在不同学派或行业习惯，遇到不确定情况应结合英文原文与上下文。','','---','']
    for (n,topic),items in groups.items():
        out += [f'## {n:02d}. {topic}', '', '| # | English term | 中文术语 | Abbr. | 简明释义 |','|---:|---|---|---|---|']
        for i,r in enumerate(items,1):
            v=[str(i),r['en'],r['zh'],r['abbr'],r['definition']]
            out.append('| '+' | '.join(x.replace('|','\\|').replace('\n',' ') for x in v)+' |')
        out.append('')
    out += ['---','','## 重点易混术语辨析','']
    for name,desc in DISTINCTIONS:out.extend([f'**{name}**：{desc}',''])
    out += ['## 参考资料与术语核验入口','','以下资料用于知识结构与术语核对，并非逐条翻译来源：','']
    for name,url in REFS:out.append(f'- [{name}]({url})')
    out += ['','## 数据与版本说明','','- 数据源：`data/signal-processing.tsv`（英文、中文、缩写、释义，以 `|` 分隔）。', '- 结构化检索：`data/terms.json` / `data/terms.csv`。','- PDF 下载：[`pdf/signal-processing.pdf`](../pdf/signal-processing.pdf)。','- 术语总量按本手册实际逐行统计，不进行跨领域去重。', '- 欢迎通过 Pull Request 提交来源充分、上下文明确的修订。','']
    MD.write_text('\n'.join(out),encoding='utf-8')

FONT='/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf'
if not Path(FONT).is_file():
    raise RuntimeError('Install fonts-arphic-gbsn00lp before rendering signal processing PDF')
pdfmetrics.registerFont(TTFont('CJK',FONT))
ink=colors.HexColor('#182741');muted=colors.HexColor('#64748B');blue=colors.HexColor('#2563EB');lt=colors.HexColor('#EEF3FB');line=colors.HexColor('#DEE6F0')
small=ParagraphStyle('small',fontName='CJK',fontSize=7.65,leading=12.15,textColor=ink,wordWrap='CJK')
header=ParagraphStyle('header',parent=small,fontSize=8.2,leading=12.5,textColor=ink)
body=ParagraphStyle('body',parent=small,fontSize=9.1,leading=15.5)
muted_style=ParagraphStyle('muted',parent=body,textColor=muted)
sub=ParagraphStyle('sub',parent=body,fontSize=15,leading=23,spaceBefore=12,spaceAfter=8)
title=ParagraphStyle('title',parent=body,fontSize=27,leading=43,spaceAfter=12)
cover=ParagraphStyle('cover',parent=body,fontSize=11,leading=20,textColor=muted)
label=ParagraphStyle('label',parent=body,fontSize=9,leading=14,textColor=blue)

def P(s,sty=small):return Paragraph(escape(str(s)),sty)

def draw(canvas,doc):
    w,h=A4
    canvas.setFillColor(blue);canvas.rect(0,h-8,w,8,fill=1,stroke=0)
    canvas.setStrokeColor(line);canvas.line(45,46,w-45,46)
    canvas.setFont('CJK',8);canvas.setFillColor(muted)
    canvas.drawString(45,30,'TERM/ATLAS  /  信号处理 · Signal Processing')
    canvas.drawRightString(w-45,30,f'{doc.page:02d}')

def pdf(rows):
    groups=defaultdict(list)
    for r in rows:groups[(r['chapter'],r['topic'])].append(r)
    doc=SimpleDocTemplate(str(PDF),pagesize=A4,leftMargin=44,rightMargin=44,topMargin=54,bottomMargin=59,
                          title='信号处理专有名词中英文对照表 | Signal Processing Glossary',author='TERM/ATLAS · 1998x-stack',subject='295 bilingual signal processing terminology entries')
    story=[Spacer(1,44),P('BILINGUAL TECHNICAL GLOSSARY  /  2026 EDITION',label),Spacer(1,24),
           P('信号处理',title),P('专有名词中英文对照表',title),Spacer(1,10),P('Signal Processing',sub),P('Chinese–English Terminology Handbook',cover),Spacer(1,23),
           P('295 TERMS   /   18 TOPICS   /   12 CONCEPT CONTRASTS',sub),Spacer(1,15),
           P('覆盖信号与系统、频域变换、采样与量化、数字滤波、多速率处理、随机过程、谱估计、时频分析、通信、音频、阵列与实时实现。',body),Spacer(1,25),
           P('适用于课程复习、论文阅读、系统设计、工程实践与技术面试。',muted_style),Spacer(1,20),
           P('专业审校提醒：不同文献对频率、谱密度和功率的归一化约定可能不同；应以具体定义为准。',muted_style),PageBreak(),
           P('主题目录  /  CONTENTS',sub),Spacer(1,8)]
    for (n,topic),items in groups.items():
        story.append(P(f'{n:02d}   {topic}    /    {len(items)} terms',body))
    story.extend([Spacer(1,18),P('阅读提示',sub),P('中英文译名采用常见教材与工程语境。缩写仅收录常用形式；正文按章节排序，可全文搜索。',body),PageBreak()])
    width=A4[0]-88
    col=[139,95,49,width-283]
    for (n,topic),items in groups.items():
        story.extend([P(f'{n:02d}  /  {topic}',sub),P(f'{len(items)} TERMS   ·   ENGLISH / 中文 / ABBR. / DEFINITION',label),Spacer(1,4)])
        data=[[P('ENGLISH TERM',header),P('中文译名',header),P('ABBR.',header),P('简明释义',header)]]
        for r in items:data.append([P(r['en']),P(r['zh']),P(r['abbr']),P(r['definition'])])
        t=Table(data,colWidths=col,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([
         ('BACKGROUND',(0,0),(-1,0),lt),('LINEBELOW',(0,0),(-1,0),1,blue),
         ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#FAFCFF')]),
         ('LINEBELOW',(0,1),(-1,-1),0.33,line),('VALIGN',(0,0),(-1,-1),'TOP'),
         ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
         ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
        story.extend([t,Spacer(1,15)])
    story.extend([PageBreak(),P('重点易混术语辨析  /  CONCEPT CONTRASTS',sub),Spacer(1,10)])
    for i,(name,desc) in enumerate(DISTINCTIONS,1):
        story.append(KeepTogether([P(f'{i:02d}  {name}',body),P(desc,small),Spacer(1,8)]))
    story.extend([Spacer(1,8),P('参考资料  /  SOURCES',sub)])
    for ref_title,url in REFS:story.extend([P(ref_title,body),P(url,small),Spacer(1,5)])
    story.extend([Spacer(1,14),P('术语说明：独立撰写；资料用于概念框架与术语核验，不构成逐条官方标准译名。',muted_style)])
    doc.build(story,onFirstPage=draw,onLaterPages=draw)

if __name__=='__main__':
    rows=load();MD.parent.mkdir(parents=True,exist_ok=True);PDF.parent.mkdir(parents=True,exist_ok=True);markdown(rows);pdf(rows)
    print('terms=',len(rows),'md_bytes=',MD.stat().st_size,'pdf_bytes=',PDF.stat().st_size)
