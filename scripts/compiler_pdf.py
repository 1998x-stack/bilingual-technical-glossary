#!/usr/bin/env python3
"""Generate the Compiler Principles glossary PDF from canonical indexed terms."""
from __future__ import annotations
from collections import defaultdict
from html import escape
from pathlib import Path

SLUG = "compiler-principles"
TITLE_ZH = "编译原理专有名词中英文对照表"
TITLE_EN = "Compiler Principles · Bilingual Technical Glossary"

def render_compiler_pdf(data, output: Path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        CondPageBreak, KeepTogether, PageBreak, Paragraph,
        SimpleDocTemplate, Spacer, Table, TableStyle,
    )
    terms = [t for t in data if t["category"] == SLUG]
    if not terms:
        raise ValueError("Missing Compiler Principles entries")
    font_candidates = [
        Path("/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf"),
        Path("/usr/share/fonts/truetype/arphic-gkai00mp/gkai00mp.ttf"),
    ]
    import glob
    font_candidates += [Path(s) for s in glob.glob("/usr/share/fonts/**/*gbsn*.ttf", recursive=True)]
    font = next((x for x in font_candidates if x.exists()), None)
    if font is None:
        raise FileNotFoundError("A Chinese TrueType font is required (fonts-arphic-gbsn00lp).")
    if "CompilerCJK" not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont("CompilerCJK", str(font)))

    NAVY = colors.HexColor("#0F1F36")
    INK = colors.HexColor("#263952")
    TEAL = colors.HexColor("#007C91")
    PALE = colors.HexColor("#E9F4F7")
    LINE = colors.HexColor("#DFE7ED")
    MUTED = colors.HexColor("#62748A")
    PAPER = colors.HexColor("#F8FAFC")
    body = ParagraphStyle("body", fontName="CompilerCJK", fontSize=8, leading=12,
                          textColor=INK, wordWrap="CJK")
    tiny = ParagraphStyle("tiny", parent=body, fontSize=7.35, leading=11.1)
    th = ParagraphStyle("th", parent=body, fontSize=7.8, leading=12, textColor=NAVY)
    heading = ParagraphStyle("heading", parent=body, fontSize=15, leading=22,
                             textColor=NAVY, spaceBefore=6, spaceAfter=7)
    section_sub = ParagraphStyle("section_sub", parent=body, fontSize=8.1,
                                 leading=12, textColor=MUTED, spaceAfter=8)
    cover_title = ParagraphStyle("cover_title", fontName="CompilerCJK", fontSize=28,
                                 leading=43, textColor=NAVY)
    cover_sub = ParagraphStyle("cover_sub", parent=body, fontSize=13,
                               leading=19, textColor=TEAL)
    chapter_line = ParagraphStyle("chapter_line", parent=body, fontSize=9.5,
                                  leading=19, textColor=NAVY)
    def p(s, style=tiny):
        return Paragraph(escape(str(s)), style)

    def decorate(canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setFillColor(TEAL)
        canvas.rect(0, h - 7, w, 7, fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.line(45, 45, w - 45, 45)
        canvas.setFont("CompilerCJK", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(45, 30, "TERM/ATLAS    /    COMPILER PRINCIPLES")
        canvas.drawRightString(w - 45, 30, f"{doc.page:02d}")
        canvas.restoreState()

    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(output), pagesize=A4, leftMargin=45, rightMargin=45,
        topMargin=56, bottomMargin=62, title=TITLE_ZH,
        author="1998x-stack / TERM-ATLAS",
        subject="Compiler principles Chinese-English terminology reference",
    )
    groups = defaultdict(list)
    for term in terms:
        groups[(term["chapter"], term["topic"])].append(term)
    groups = sorted(groups.items())
    story = [
        Spacer(1, 75), p("TERM / ATLAS      ENGINEERING REFERENCE", cover_sub),
        Spacer(1, 26),
        Paragraph("编译原理<br/>专有名词中英文对照表", cover_title),
        Spacer(1, 22),
        p("COMPILER PRINCIPLES  ·  CHINESE–ENGLISH TECHNICAL GLOSSARY", cover_sub),
        Spacer(1, 52),
        p(f"{len(terms)} 条术语    /    {len(groups)} 个专题    /    2026 年版",
          ParagraphStyle("metric", parent=cover_sub, fontSize=17, leading=26)),
        Spacer(1, 19),
        p("从词法分析、上下文无关文法和 LR 分析，到类型系统、SSA、数据流分析、编译优化、寄存器分配与现代 LLVM/MLIR 工具链。",
          ParagraphStyle("intro", parent=body, fontSize=10, leading=19)),
        Spacer(1, 48),
        p("适用场景：高校编译原理课程、经典教材阅读、LLVM 源码研究、编译器工程面试。", body),
        Spacer(1, 14),
        p("社区共建 · 译名依上下文可能存在差异 · 非官方标准术语表", body),
        PageBreak(),
        Paragraph("阅读导航  /  CONTENTS", heading),
        p("推荐按「语言与文法 → 前端分析 → IR 与优化 → 后端与运行时」的顺序阅读。", section_sub),
        Spacer(1, 13),
    ]
    for (chapter, topic), entries in groups:
        story.append(Paragraph(f"{chapter:02d}    {escape(topic)}   ·   {len(entries)} 条", chapter_line))
    story.extend([Spacer(1, 23), p(
        "每条术语包含英文原名、中文常用译名、缩写（如适用）和一句话解释。"
        "注意 CFG 在不同章节可指上下文无关文法或控制流图，应结合语境理解。", body),
        PageBreak()])
    widths = [155, 94, 55, 201]  # A4 - 2*45 = 505 points
    for (chapter, topic), entries in groups:
        story.extend([
            CondPageBreak(100),
            Paragraph(f"{chapter:02d}  /  {escape(topic)}", heading),
            p(f"{len(entries)} 条  ·  ENGLISH  /  中文  /  ABBR.  /  DEFINITION", section_sub),
        ])
        rows = [[p("ENGLISH TERM", th), p("中文译名", th), p("ABBR.", th), p("简明释义", th)]]
        rows += [[p(t["en"]), p(t["zh"]), p(t["abbr"]), p(t["definition"])] for t in entries]
        table = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT",
                      splitByRow=1)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), PALE),
            ("LINEBELOW", (0, 0), (-1, 0), 1.0, TEAL),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PAPER]),
            ("LINEBELOW", (0, 1), (-1, -1), 0.35, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.extend([table, Spacer(1, 16)])

    story.extend([
        PageBreak(),
        Paragraph("参考与修订  /  SOURCES & CONTRIBUTIONS", heading),
        Spacer(1, 9),
        p("本手册为独立编写的教学与工程术语释义。建议使用以下公开技术参考资料核对具体实现或解析算法：", body),
        Spacer(1, 9),
        p("LLVM Language Reference Manual — https://llvm.org/docs/LangRef.html", body),
        p("GNU Bison Manual — https://www.gnu.org/software/bison/manual/", body),
        p("LLVM Programmer's Manual — https://llvm.org/docs/ProgrammersManual.html", body),
        p("GCC Internals — https://gcc.gnu.org/onlinedocs/gccint/", body),
        Spacer(1, 19),
        p("术语修改请以 data/compiler-principles.tsv 为人工维护源，再运行 scripts/build.py；"
          "同步更新结构化索引、Markdown、PDF 与站点静态资源。", body),
        Spacer(1, 9),
        p("项目主页：https://github.com/1998x-stack/bilingual-technical-glossary", body),
        Spacer(1, 10),
        p("贡献时请补充权威来源，区分语法理论与 LLVM/GCC 等具体实现，不应将某一工具的约定误写为通用标准。", body),
    ])
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    return len(terms)

if __name__ == "__main__":
    import json
    root = Path(__file__).resolve().parents[1]
    data = json.loads((root / "data/terms.json").read_text(encoding="utf-8"))
    count = render_compiler_pdf(data, root / "pdf" / f"{SLUG}.pdf")
    print(f"Created {SLUG}.pdf: {count} terms")
