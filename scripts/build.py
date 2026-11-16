#!/usr/bin/env python3
"""Build Markdown, CSV, site indexes, and AI Infra PDF; preserve GPU Kernel PDF."""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, shutil, re
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/terms.json'
CATALOG=[
 ('high-school-mathematics','High School Mathematics','高中数学','Sets, functions, trigonometry, geometry, calculus, statistics and probability','book'),
 ('ai-infrastructure','AI Infrastructure / AI Infra','AI 基础设施','Accelerators, distributed systems, GPU serving and operations','cpu'),
 ('gpu-kernel','GPU Kernel Engineering','GPU Kernel / GPU 核函数','CUDA, PTX, Triton, GPU programming and kernel performance','cpu'),
 ('ai-agents','AI Agents','AI 智能体','Planning, tools, protocols, memory and multi-agent systems','bot'),
 ('large-language-models','Large Language Models','大语言模型 LLM','Tokenization, transformer, training, inference and alignment','brain'),
 ('deep-learning','Deep Learning','深度学习','Neural networks, optimization, computer vision and generation','layers'),
 ('machine-learning','Machine Learning','机器学习','Foundations, classical algorithms, model evaluation, tuning and MLOps','target'),
 ('reinforcement-learning','Reinforcement Learning','强化学习','MDPs, value learning, policy optimization and reward models','route'),
 ('calculus','Calculus','微积分','Limits, derivatives, integrals, series, multivariable and vector calculus','integral'),
 ('linear-algebra','Linear Algebra','线性代数','Vectors, matrices, spaces, eigensystems and factorization','grid'),
 ('discrete-mathematics','Discrete Mathematics','离散数学','Logic, proofs, sets, relations, counting, graph theory, number theory and automata','grid'),
 ('compiler-principles','Compiler Principles','编译原理','Lexing, grammars, parsing, semantics, SSA, optimization, code generation and runtime','code'),
 ('probability-theory','Probability Theory','概率论','Random variables, distributions, stochastic processes and inference','sigma'),
 ('university-mathematics','University Mathematics','大学数学','Calculus, analysis, geometry, probability, differential equations and optimization','integral'),
 ('apache-kafka','Apache Kafka','Apache Kafka / 事件流平台','Event streaming, KRaft, partitions, consumers, transactions and Streams','network'),
 ('data-structures','Data Structures','数据结构','Arrays, lists, hashing, trees, graphs and advanced structures','network'),
 ('linux','Linux','Linux 操作系统','Kernel, processes, memory, networking, containers and performance','terminal'),
 ('operating-systems','Operating Systems','操作系统','Processes, scheduling, concurrency, memory, file systems, security, Linux and virtualization','server'),
 ('computer-networks','Computer Networks','计算机网络','Layers, Ethernet, Wi-Fi, IPv4/IPv6, routing, TCP, QUIC, DNS, HTTP, TLS and network operations','network'),
 ('sql-database','SQL Database','SQL 数据库','Relational modeling, SQL syntax, indexes, optimizers, transactions and operations','database'),
 ('cpp','C++ Programming Language','C++ 编程语言','Core language, object lifetime, templates, STL, concurrency and modern C++','code'),
 ('python','Python','Python 编程语言','Language, runtime, data model, typing, packaging and performance','code'),
 ('junior-high-mathematics','Junior High School Mathematics','初中数学','Grade 7–9 numbers, algebra, functions, geometry, statistics and probability','triangle'),
 ('parallel-computing','Parallel Computing','并行计算','Parallel algorithm design, communication, performance, MPI, OpenMP, GPU and HPC','cpu'),
 ('signal-processing','Signal Processing','信号处理','Signals, sampling, transforms, spectral analysis, digital filters and real-time DSP','sigma'),
]
META={x[0]:{'slug':x[0],'en':x[1],'zh':x[2],'description':x[3],'icon':x[4]} for x in CATALOG}

def merge_infra(data):
 if any(t['category']=='ai-infrastructure' for t in data): return data
 topic='';chapter=0;add=[]
 for line in (ROOT/'data/ai-infrastructure.tsv').read_text(encoding='utf8').splitlines():
  if not line.strip():continue
  if line.startswith('#'):
   chapter+=1;topic=line.lstrip('# ').strip();continue
  pieces=line.split('|')
  if len(pieces)!=4:raise ValueError(f'Invalid AI Infra term: {line}')
  en,zh,abbr,desc=pieces
  add.append(dict(category='ai-infrastructure',chapter=chapter,topic=topic,en=en,zh=zh,abbr=abbr,definition=desc))
 return add+data

def merge_compiler(data):
 # Compiler TSV is the editable source; replace indexed compiler rows on rebuild.
 data=[t for t in data if t['category']!='compiler-principles']
 topic='';chapter=0;add=[]
 for line in (ROOT/'data/compiler-principles.tsv').read_text(encoding='utf8').splitlines():
  if not line.strip():continue
  if line.startswith('#'):
   chapter+=1;topic=line.lstrip('# ').strip();continue
  parts=line.split('|')
  if len(parts)!=4:raise ValueError(f'Invalid Compiler Principles term: {line}')
  en,zh,abbr,definition=(part.strip() for part in parts)
  if not (topic and en and zh and definition):raise ValueError(f'Missing required value: {line}')
  add.append(dict(category='compiler-principles',chapter=chapter,topic=topic,
                  en=en,zh=zh,abbr=abbr,definition=definition))
 return data+add

def merge_high_school(data):
 from render_high_school_pdf import load_terms
 return [t for t in data if t['category']!='high-school-mathematics']+load_terms(ROOT/'data/high-school-mathematics.tsv')

def merge_signal_processing(data):
 # Canonical Signal Processing vocabulary source.
 src=ROOT/'data/signal-processing.tsv';topic='';chapter=0;added=[]
 for lineno,line in enumerate(src.read_text(encoding='utf8').splitlines(),1):
  if not line.strip():continue
  if line.startswith('# '):
   chapter+=1;topic=line[2:].strip();continue
  values=[p.strip() for p in line.split('|')]
  if len(values)!=4 or not topic or not values[0] or not values[1] or not values[3]:
   raise ValueError(f'Invalid signal processing source record at line {lineno}')
  en,zh,abbr,definition=values
  added.append(dict(category='signal-processing',chapter=chapter,topic=topic,
                    en=en,zh=zh,abbr=abbr,definition=definition))
 if len(added)!=295 or chapter!=18:
  raise ValueError(f'Signal Processing should have 295 terms and 18 topics; got {len(added)} and {chapter}')
 return [item for item in data if item['category']!='signal-processing']+added

def merge_computer_networks(data):
 from ingest_computer_networks import load_records
 additions=load_records(ROOT/'data/computer-networks.tsv')
 return [row for row in data if row['category']!='computer-networks']+additions

def merge_cpp(data):
 chapter=0;topic='';rows=[]
 for raw in (ROOT/'data/cpp-glossary.tsv').read_text(encoding='utf8').splitlines():
  line=raw.strip()
  if not line:continue
  if line.startswith('# '):
   cols=line[2:].split('|')
   if len(cols)!=4:raise ValueError('Malformed C++ chapter: '+line)
   chapter=int(cols[0]);topic=cols[1].strip()
  else:
   cols=line.split('|')
   if len(cols)!=3 or not all(c.strip() for c in cols):raise ValueError('Malformed C++ term: '+line)
   en,zh,definition=(c.strip() for c in cols)
   rows.append(dict(category='cpp',chapter=chapter,topic=topic,en=en,zh=zh,abbr='',definition=definition))
 return [t for t in data if t['category']!='cpp']+rows

def md_table_value(x):return str(x).replace('|','\\|').replace('\n',' ').strip()

def write_markdown(data):
 for slug in META:
  if slug in ('operating-systems', 'sql-database', 'python', 'junior-high-mathematics', 'gpu-kernel', 'computer-networks', 'parallel-computing', 'cpp', 'signal-processing'):
   continue  # Preserve independently authored Markdown and appendices.
  if slug == 'data-structures': continue  # Preserve authored Markdown and appendix.
  if slug=='apache-kafka':continue  # Preserve original editorial Markdown.
  if slug=='linux': continue  # Preserve independently authored Linux Markdown and appendix.
  entries=[x for x in data if x['category']==slug]
  groups=defaultdict(list)
  for x in entries:groups[(x['chapter'],x['topic'])].append(x)
  m=META[slug]
  out=[f'# {m["zh"]} · {m["en"]}', '', '> 中英双语专业术语手册 | Chinese-English Technical Glossary', '',f'**术语总量：{len(entries)} 条 · 专题：{len(groups)} 类**','',m['description'],'','> 译法以常见教材和工程文献为参考；具体技术版本与词义以原始规范及上下文为准。','', '## 专题目录','']
  for (chapter,name),items in sorted(groups.items()):out.append(f'- {chapter:02d}. {name}（{len(items)} 条）')
  out+=['','---','']
  for (chapter,name),items in sorted(groups.items()):
   out += [f'## {chapter:02d}. {name}','', ('| # | English term | 中文译名 | 符号 / 示例 | 简明释义 |' if slug=='calculus' else '| # | English term | 中文译名 | Abbr. | 简明释义 |'),'|---:|---|---|---|---|']
   for i,item in enumerate(items,1):out.append('| '+ ' | '.join([str(i)]+[md_table_value(item.get(k,'')) for k in (['en','zh','notation','definition'] if slug=='calculus' else ['en','zh','abbr','definition'])])+' |')
   out.append('')
  if slug=='compiler-principles':out += ['> 术语辨析：CFG 在形式语言中指上下文无关文法，在程序分析中指控制流图。','', '参考资料：[LLVM Language Reference](https://llvm.org/docs/LangRef.html) · [GNU Bison Manual](https://www.gnu.org/software/bison/manual/) · [GCC Internals](https://gcc.gnu.org/onlinedocs/gccint/)','']
  out+=['---','',f'原始数据：[JSON](../data/terms.json) · [CSV](../data/terms.csv) · [PDF](../pdf/{slug}.pdf)','', '本术语表仅用于学习与参考，欢迎通过 Pull Request 提交译名修正、例证及权威来源。','']
  (ROOT/'glossaries'/f'{slug}.md').write_text('\n'.join(out),encoding='utf8')

def render_pdf(data):
 dest=ROOT/'pdf/ai-infrastructure.pdf'
 try:
  from reportlab.lib import colors
  from reportlab.lib.pagesizes import A4
  from reportlab.lib.styles import ParagraphStyle
  from reportlab.lib.enums import TA_LEFT
  from reportlab.lib.units import mm
  from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
  from reportlab.pdfbase import pdfmetrics
  from reportlab.pdfbase.ttfonts import TTFont
 except ImportError:print('reportlab not installed: skipping PDF');return
 font='/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf'
 if not Path(font).exists():
  from glob import glob
  c=glob('/usr/share/fonts/**/*gbsn*.ttf',recursive=True)
  if c:font=c[0]
 if not Path(font).exists():
  print('Chinese TTF unavailable: PDF generation skipped');return
 pdfmetrics.registerFont(TTFont('GlossaryCJK',font))
 NAVY=colors.HexColor('#17233C');MUTED=colors.HexColor('#64748B');BLUE=colors.HexColor('#2563EB')
 head=ParagraphStyle('head',fontName='GlossaryCJK',fontSize=21,leading=31,textColor=NAVY,spaceAfter=16)
 sub=ParagraphStyle('sub',fontName='GlossaryCJK',fontSize=12,leading=20,textColor=NAVY,spaceBefore=20,spaceAfter=12)
 body=ParagraphStyle('body',fontName='GlossaryCJK',fontSize=8.3,leading=13,textColor=NAVY,spaceAfter=4)
 small=ParagraphStyle('small',fontName='GlossaryCJK',fontSize=7.1,leading=11,textColor=NAVY)
 title=ParagraphStyle('ttl',fontName='GlossaryCJK',fontSize=30,leading=42,textColor=NAVY,spaceAfter=25)
 all_entries=[x for x in data if x['category']=='ai-infrastructure']
 def P(s,style=small):
  import html
  return Paragraph(html.escape(str(s)),style)
 def decorate(canv,doc):
  canv.setStrokeColor(colors.HexColor('#DEE4EF'));canv.line(44,43,A4[0]-44,43)
  canv.setFont('GlossaryCJK',8);canv.setFillColor(MUTED)
  canv.drawString(44,30,'Bilingual Technical Glossary  ·  AI Infra')
  canv.drawRightString(A4[0]-44,30,f'{doc.page:02d}')
  canv.setFillColor(BLUE);canv.rect(0,A4[1]-7,A4[0],7,fill=1,stroke=0)
 doc=SimpleDocTemplate(str(dest),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=54,bottomMargin=62,author='1998x-stack',title='AI Infrastructure — Bilingual Technical Glossary')
 story=[Spacer(1,46),P('AI INFRASTRUCTURE  /  REFERENCE HANDBOOK',body),Spacer(1,24),Paragraph('AI 基础设施<br/>中英文专业术语对照表',title),Paragraph('AI Infrastructure · Chinese-English Technical Glossary',sub),Spacer(1,26),Paragraph(f'{len(all_entries)} TERMS    /    {len(set(x["chapter"] for x in all_entries))} TOPICS    /    2026 EDITION',head),Spacer(1,12),Paragraph('覆盖 GPU 与加速器、集群网络、分布式训练、LLM 推理服务、容器调度、数据存储、可观测性与成本治理。',body),Spacer(1,15),P('用于 AI Infra 架构学习、论文检索、技术文档和工程面试。',body),PageBreak()]
 groups=defaultdict(list)
 for x in all_entries:groups[(x['chapter'],x['topic'])].append(x)
 for (chapter,topic),rows in sorted(groups.items()):
  story += [Paragraph(f'{chapter:02d} / {topic}',sub),P(f'{len(rows)} terms · English / 中文 / 缩写 / 简明释义',body),Spacer(1,5)]
  header=[P('ENGLISH TERM'),P('中文'),P('缩写'),P('简明解释')]
  grid=[header]
  for r in rows:grid.append([P(r['en']),P(r['zh']),P(r['abbr']),P(r['definition'])])
  table=Table(grid,colWidths=[155,86,58,210],repeatRows=1,hAlign='LEFT')
  table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E8EFFC')),('LINEBELOW',(0,0),(-1,0),0.8,BLUE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,1),(-1,-1),0.3,colors.HexColor('#E1E7F0')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F8FAFE')])]))
  story.extend([table,Spacer(1,12)])
 doc.build(story,onFirstPage=decorate,onLaterPages=decorate)
 print('Generated PDF',dest,round(dest.stat().st_size/1024),'KB')

def write_site_data(data):
 d=ROOT/'docs';(d/'data').mkdir(parents=True,exist_ok=True)
 (d/'data/terms.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf8')
 (d/'data/catalog.json').write_text(json.dumps([{**META[k],'count':sum(x['category']==k for x in data),'topics':len(set(x['topic'] for x in data if x['category']==k))} for k in META],ensure_ascii=False,indent=2),encoding='utf8')
 for source in ['glossaries','pdf']:
  (d/source).mkdir(parents=True,exist_ok=True)
  for original in (ROOT/source).glob('*'):
   if original.is_file():shutil.copy2(original,d/source/original.name)
 # Preserve source-data citations in published Wiki Markdown.
 shutil.copy2(ROOT/'data/ai-infrastructure.tsv', d/'data/ai-infrastructure.tsv')
 for fn in ['index.html','styles.css','app.js','favicon.svg','term.html','term.css','term.js']:
  if (ROOT/'site'/fn).exists():shutil.copy2(ROOT/'site'/fn,d/fn)
 from build_wiki_index import write_index
 write_index(ROOT)
 (d/'.nojekyll').write_text('',encoding='utf8')

def run():
 data=json.loads(DATA.read_text(encoding='utf8'));data=merge_compiler(merge_infra(data));data=merge_high_school(data)
 from render_discrete_mathematics_pdf import load_terms as load_discrete_terms
 data=[t for t in data if t['category']!='discrete-mathematics']+load_discrete_terms()
 from import_university_mathematics import merge_entries
 data=merge_entries(data)
 data=merge_computer_networks(data)
 data=merge_cpp(data)
 data=merge_signal_processing(data)
 # Validate core field presence and duplicate pairs within each category
 errors=[];seen=set()
 for i,r in enumerate(data):
  if not all(r.get(k) for k in ['category','chapter','topic','en','zh','definition']):errors.append(i)
  key=(r['category'],r['chapter'],r['en'].casefold().strip(),r['zh'].strip())
  if key in seen:errors.append(i)
  seen.add(key)
 assert not errors,f'invalid / duplicate rows at: {errors[:15]}'
 DATA.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
 with (ROOT/'data/terms.csv').open('w',encoding='utf8',newline='') as f:
  fields=['category','chapter','topic','en','zh','abbr','definition']
  fields+=sorted({key for row in data for key in row}-set(fields))
  writer=csv.DictWriter(f,fieldnames=fields,extrasaction='raise');writer.writeheader();writer.writerows(data)
 write_markdown(data)
 from import_university_mathematics import appendix_markdown,render_source_pdf
 md=ROOT/'glossaries/university-mathematics.md'
 md.write_text(md.read_text(encoding='utf8')+'\n'+appendix_markdown(),encoding='utf8')
 render_source_pdf()
 render_pdf(data)
 from render_discrete_mathematics_pdf import render_pdf as render_discrete_pdf
 render_discrete_pdf([t for t in data if t['category']=='discrete-mathematics'])
 from compiler_pdf import render_compiler_pdf
 render_compiler_pdf(data, ROOT/'pdf/compiler-principles.pdf')
 import subprocess,sys
 subprocess.run([sys.executable,str(ROOT/'scripts/render_kafka_pdf.py')],check=True)

 from render_high_school_pdf import render_pdf as render_hs
 render_hs([t for t in data if t['category']=='high-school-mathematics'])
 # Regenerate the authored C++ publications before mirroring.
 subprocess.run([sys.executable,str(ROOT/'scripts/render_cpp_pdf.py'),
                 '--source',str(ROOT/'data/cpp-glossary.tsv'),
                 '--markdown',str(ROOT/'glossaries/cpp.md'),
                 '--pdf',str(ROOT/'pdf/cpp.pdf')],check=True)
 write_site_data(data)
 print('Complete:',len(data),'terms,',len(META),'subjects')
if __name__=='__main__':run()
