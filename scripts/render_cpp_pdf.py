#!/usr/bin/env python3
"""Generate a self-contained C++ bilingual glossary (Markdown and searchable PDF).

Usage: python scripts/render_cpp_pdf.py --source data/cpp-glossary.tsv --markdown glossaries/cpp.md --pdf pdf/cpp.pdf
Requires reportlab and a Chinese TTF font; default probes common Linux font paths.
"""
import argparse
import html
import re
from pathlib import Path
from collections import Counter
from xml.sax.saxutils import escape

VERSIONS = 'C++11 / C++14 / C++17 / C++20 / C++23'
DISTINCTIONS = [
 ('声明 vs 定义', '声明说明实体存在及属性；定义进一步提供标准所需完整信息。并非每个声明都是定义。'),
 ('类型 vs 对象', '类型给出值与操作的规则；对象具备自己的存储和生存期。同一类型可以有多个对象。'),
 ('存储期 vs 生存期', '存储期谈底层存储何时可用；生存期谈对象何时已构造、可使用并最终销毁。'),
 ('左值 vs 纯右值 vs 将亡值', 'lvalue 具有身份；prvalue 主要用于计算值和初始化；xvalue 具有身份且资源可能被重用。'),
 ('引用 vs 指针', '引用以绑定对象的别名方式使用；指针有自身值、可空且通常可重新赋值。'),
 ('std::move vs 移动操作', 'std::move 本身通常仅转换值类别；真正资源转移取决于后续构造或赋值等操作。'),
 ('复制消除 vs 移动语义', '复制消除可使预期复制或移动根本不发生；移动语义仍对应具体构造或赋值。'),
 ('const vs constexpr vs consteval vs constinit', 'const 限制修改，constexpr 可参与常量求值，consteval 要求立即函数的规定调用常量求值，constinit 保证静态初始化。'),
 ('未定义 vs 未指定 vs 实现定义行为', 'UB 没有行为要求；unspecified 允许多种行为但不必文档说明；implementation-defined 需要实现记录选择。'),
 ('volatile vs std::atomic', 'volatile 不是线程间同步手段；atomic 通过原子操作和内存序参加标准并发模型。'),
 ('数据竞争 vs 竞态条件', '数据竞争有严格的标准内存模型条件且导致 UB；竞态条件是更宽泛的时序依赖逻辑问题。'),
 ('重载 vs 覆盖 vs 隐藏', 'overload 是同名不同参数候选；override 是派生类覆写虚函数；name hiding 则是名称查找屏蔽。'),
 ('全特化 vs 偏特化', '全特化针对确切模板参数；偏特化为类或变量模板指定更窄参数模式，函数模板不允许偏特化。'),
 ('容器 vs 视图', '容器通常拥有元素；view 主要描述可遍历范围，可惰性计算且通常不拥有元素。'),
 ('unique_ptr vs shared_ptr vs weak_ptr', 'unique_ptr 独占所有权；shared_ptr 共享所有权；weak_ptr 只观察共享对象且不保持其存活。'),
 ('模块 vs 头文件', '模块具有语言级导入和可见性规则；传统头文件使用预处理文本包含，两者并不等价。'),
]
REFERENCES = [
 ('ISO C++ 标准委员会（WG21）', 'https://www9.open-std.org/JTC1/SC22/WG21/'),
 ('cppreference：C++ language', 'https://en.cppreference.com/cpp/language'),
 ('cppreference：C++ library', 'https://en.cppreference.com/cpp'),
 ('C++ Core Guidelines', 'https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines'),
 ('C++ working draft（非正式发布标准）', 'https://eel.is/c++draft/'),
]

def parse_source(path):
    chapters = []
    seen = set()
    current = None
    for lineno, raw in enumerate(Path(path).read_text(encoding='utf-8').splitlines(), 1):
        line=raw.strip()
        if not line or line.startswith('//'): continue
        if line.startswith('# '):
            p=line[2:].split('|')
            if len(p)!=4: raise ValueError(f'{lineno}: chapter needs number, Chinese, English, intro')
            number, zh, en, intro=(x.strip() for x in p)
            if int(number)!=len(chapters)+1: raise ValueError(f'{lineno}: chapter sequence error')
            current=dict(number=int(number),zh=zh,en=en,intro=intro,terms=[])
            chapters.append(current)
        else:
            p=[x.strip() for x in line.split('|')]
            if len(p)!=3 or not all(p): raise ValueError(f'{lineno}: need EN|ZH|definition')
            if not current: raise ValueError(f'{lineno}: term without chapter')
            en,zh,definition=p
            if en.casefold() in seen: raise ValueError(f'{lineno}: duplicate English {en}')
            seen.add(en.casefold())
            current['terms'].append(dict(en=en,zh=zh,definition=definition))
    if not chapters: raise ValueError('No chapters')
    return chapters

def markdown(chapters):
    n=sum(len(c['terms']) for c in chapters)
    out=[
     '# C++ 专有名词中英文对照表',
     '',
     f'> C++ Technical Terminology: English–Chinese Glossary · **{n} 条术语 / {len(chapters)} 章** · 2026-11-16',
     '',
     '本手册围绕 **C++ 语言核心、对象模型、泛型模板、STL、内存模型与现代工程实践** 编排。术语中译采用教材与工程领域常见用法，少数词汇可能因语境有不同译名。',
     '',
     f'**适用范围：** 以 {VERSIONS} 的稳定概念为主体；所列库类型对应其首次引入时的标准版本。对 C++26 等持续演进的工作草案，不默认认定其特性已获所有主流编译器实现。',
     '',
     '**阅读提示：** 本表的定义均为原创简释，便于查阅而非替代标准中的精确定义；标准支持情况应查看对应版本的标准文本与实现文档。',
     '',
     '## 目录',''
    ]
    for c in chapters:
        out.append(f'- [{c["number"]:02d} {c["zh"]} / {c["en"]}](#chapter-{c["number"]:02d})（{len(c["terms"])} 条）')
    out.extend(['- [附录 A：易混淆概念速查](#appendix-a)', '- [附录 B：参考资料与编辑原则](#appendix-b)','','---',''])
    for c in chapters:
        out.extend([f'<a id="chapter-{c["number"]:02d}"></a>','',f'## {c["number"]:02d} {c["zh"]} / {c["en"]}','',c['intro'],'','| English term | 中文术语 | 简明释义 |','| --- | --- | --- |'])
        for t in c['terms']:
            pieces=[t['en'],t['zh'],t['definition']]
            out.append('| '+' | '.join(x.replace('|','\\|').replace('\n',' ') for x in pieces)+' |')
        out.append('')
    out.extend(['---','','<a id="appendix-a"></a>','','## 附录 A：易混淆概念速查','','| 术语对照 | 核心区别 |','| --- | --- |'])
    for a,b in DISTINCTIONS: out.append(f'| {a} | {b} |')
    out.extend(['','<a id="appendix-b"></a>','','## 附录 B：参考资料与编辑原则','','参考资料（用于术语核对与进一步阅读）：',''])
    for name,url in REFERENCES:out.append(f'- [{name}]({url})')
    out.extend(['', '**编辑原则：**', '', '1. 优先使用标准规范中的英文原词与主流中文译名，必要时给出英文缩写。', '2. 区分语言保证、标准库保证、常见实现策略与工程习惯。', '3. 不将某一编译器、STL 实现或平台 ABI 的细节当作通用 C++ 规则。', '4. 对每个术语保持唯一英文主键；新条目须包含简明定义和明确章节。', '5. 编辑 `data/cpp-glossary.tsv` 后运行生成脚本，使 Markdown 与 PDF 保持一致。', '', '欢迎通过 [GitHub Pull Request](https://github.com/1998x-stack/bilingual-technical-glossary/pulls) 修正术语或补充权威来源。', ''])
    return '\n'.join(out)

def render_pdf(chapters,path):
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak, Spacer, KeepTogether, HRFlowable
    from reportlab.lib.enums import TA_LEFT
    font_paths=['/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf', '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc']
    chosen=next((x for x in font_paths if Path(x).exists()),None)
    if not chosen: raise RuntimeError('No CJK TrueType font; install fonts-arphic-gbsn00lp')
    pdfmetrics.registerFont(TTFont('CPP-CJK',chosen))
    NAVY=colors.HexColor('#122341'); BLUE=colors.HexColor('#1257B3'); LIGHT=colors.HexColor('#EDF4FB'); MUTED=colors.HexColor('#52627B'); WHITE=colors.white
    title=ParagraphStyle('title',fontName='CPP-CJK',fontSize=26,leading=39,textColor=NAVY)
    intro=ParagraphStyle('intro',fontName='CPP-CJK',fontSize=10,leading=19,textColor=MUTED)
    chapter=ParagraphStyle('chapter',fontName='CPP-CJK',fontSize=17,leading=27,textColor=NAVY,spaceAfter=11)
    body=ParagraphStyle('body',fontName='CPP-CJK',fontSize=8.2,leading=13.8,textColor=NAVY)
    small=ParagraphStyle('small',fontName='CPP-CJK',fontSize=7.55,leading=11.8,textColor=NAVY)
    small_muted=ParagraphStyle('small-muted',fontName='CPP-CJK',fontSize=8.1,leading=13.2,textColor=MUTED)
    table_head=ParagraphStyle('tablehead',fontName='CPP-CJK',fontSize=8.0,leading=11.8,textColor=NAVY)
    count=sum(len(c['terms']) for c in chapters)
    doc=SimpleDocTemplate(str(path),pagesize=A4,leftMargin=44,rightMargin=44,topMargin=58,bottomMargin=54,title='C++ 专有名词中英文对照表',author='TERM/ATLAS · 1998x-stack',subject=f'{count} bilingual C++ technical terms in {len(chapters)} chapters',pageCompression=1)
    W=A4[0]-88
    def P(t,style=small):return Paragraph(escape(str(t)),style)
    def decorate(canvas,doc):
        canvas.saveState()
        canvas.setFillColor(BLUE);canvas.rect(0,A4[1]-7,A4[0],7,stroke=0,fill=1)
        canvas.setStrokeColor(colors.HexColor('#D9E3EF'));canvas.line(44,40,A4[0]-44,40)
        canvas.setFont('CPP-CJK',8);canvas.setFillColor(MUTED)
        canvas.drawString(44,28,'TERM / ATLAS    ·    C++ 术语速查')
        canvas.drawRightString(A4[0]-44,28,f'{doc.page:02d}')
        canvas.restoreState()
    story=[Spacer(1,82),P('TERM / ATLAS      ·      TECHNICAL REFERENCE',intro),Spacer(1,26),Paragraph('C++ 专有名词<br/>中英文对照表',title),Spacer(1,12),P('C++ Technical Terminology · English–Chinese Glossary',intro),Spacer(1,42)]
    h=Table([[P(str(count),chapter),P(str(len(chapters)),chapter),P('2026',chapter)],[P('术语词条',body),P('专题章节',body),P('修订年份',body)]],colWidths=[W/3]*3)
    h.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('BOX',(0,0),(-1,-1),0.6,colors.HexColor('#D9E7F7')),('TOPPADDING',(0,0),(-1,0),11),('BOTTOMPADDING',(0,-1),(-1,-1),14)]))
    story.extend([h,Spacer(1,37),P('覆盖语言基础、类型与对象生存期、值类别、类与多态、资源管理、模板与 Concepts、STL、Ranges、异常安全、并发内存模型、C++20/23 等核心领域。',intro),Spacer(1,25),P('编辑说明：译名采用通行中文表达，定义为面向学习的精炼说明；遇到精确语义或版本差异，应以标准文本与实现文档为准。',small_muted),PageBreak()])
    story.extend([Paragraph('内容目录  /  CONTENTS',chapter),Spacer(1,12)])
    for c in chapters:
        row=Table([[P(f'{c["number"]:02d}',body),P(f'{c["zh"]} / {c["en"]}',body),P(f'{len(c["terms"])} 条',small_muted)]],colWidths=[36,W-100,64]);row.setStyle(TableStyle([('LINEBELOW',(0,0),(-1,-1),.45,colors.HexColor('#DFE6EF')),('BOTTOMPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8)]));story.append(row)
    story.extend([Spacer(1,22),P('附录 A   易混淆概念速查 · 附录 B   参考资料与编辑原则',small_muted),PageBreak()])
    for c in chapters:
        story.extend([Paragraph(f'{c["number"]:02d}  {escape(c["zh"])}',chapter),P(c['en'],small_muted),Spacer(1,7),P(c['intro'],body),Spacer(1,12)])
        grid=[[P('ENGLISH TERM',table_head),P('中文术语',table_head),P('简明释义',table_head)]]
        for term in c['terms']:
            grid.append([P(term['en']),P(term['zh']),P(term['definition'])])
        table=Table(grid,colWidths=[159,115,W-274],repeatRows=1,hAlign='LEFT')
        table.setStyle(TableStyle([
          ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DDEBFA')),
          ('LINEBELOW',(0,0),(-1,0),.8,BLUE),
          ('VALIGN',(0,0),(-1,-1),'TOP'),
          ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
          ('TOPPADDING',(0,0),(-1,-1),6.2),('BOTTOMPADDING',(0,0),(-1,-1),6.2),
          ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,colors.HexColor('#F7FAFE')]),
          ('LINEBELOW',(0,1),(-1,-1),.28,colors.HexColor('#DFE6EF')),
        ]))
        story.append(table)
        story.append(PageBreak())
    story.extend([Paragraph('附录 A  /  易混淆概念速查',chapter),P('学习 C++ 时特别容易发生概念混淆的术语对照。',body),Spacer(1,12)])
    rows=[[P('对照项',table_head),P('辨析',table_head)]]+[[P(a),P(b)] for a,b in DISTINCTIONS]
    appendix=Table(rows,colWidths=[158,W-158],repeatRows=1)
    appendix.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),LIGHT),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,colors.HexColor('#F7FAFE')]),('LINEBELOW',(0,0),(-1,-1),.3,colors.HexColor('#DFE6EF')),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.extend([appendix,PageBreak(),Paragraph('附录 B  /  参考资料与编辑原则',chapter),Spacer(1,8),P('本术语表的定义为原创简释，以下链接可进一步核对标准与库的精确语义。',body),Spacer(1,12)])
    for name,url in REFERENCES:story.extend([P(name,body),P(url,small_muted),Spacer(1,11)])
    story.extend([Spacer(1,15),P('编辑原则：遵循标准英文术语，记录可信译名；区分规范、实现与工程惯例；不在缺乏证据时将特定平台行为写作语言保证；Markdown、PDF 与术语数据保持一致。',body)])
    doc.build(story,onFirstPage=decorate,onLaterPages=decorate)
    return count

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--source',default='data/cpp-glossary.tsv')
    a.add_argument('--markdown',default='glossaries/cpp.md')
    a.add_argument('--pdf',default='pdf/cpp.pdf')
    args=a.parse_args()
    chapters=parse_source(args.source)
    md_path=Path(args.markdown);md_path.parent.mkdir(parents=True,exist_ok=True);md_path.write_text(markdown(chapters),encoding='utf-8')
    pdf_path=Path(args.pdf);pdf_path.parent.mkdir(parents=True,exist_ok=True)
    n=render_pdf(chapters,pdf_path)
    print(f'{n} terms / {len(chapters)} chapters | {md_path} | {pdf_path} ({pdf_path.stat().st_size:,} bytes)')
if __name__=='__main__':main()
