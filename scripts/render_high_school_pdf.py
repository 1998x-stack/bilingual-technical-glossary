#!/usr/bin/env python3
"""Render the high-school mathematics volume from its curated TSV source.

Usage:
    python3 scripts/render_high_school_pdf.py
The same curated rows are used by scripts/build.py and the PDF book.
"""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
from html import escape
import argparse

ROOT = Path(__file__).resolve().parents[1]
SLUG = "high-school-mathematics"

def load_terms(path: Path | None = None) -> list[dict]:
    path = path or ROOT / "data" / f"{SLUG}.tsv"
    chapter = 0
    topic = ""
    rows = []
    seen = set()
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("# 高中数学中英文") or line.startswith("# 每个专题") or line.startswith("# EDITION"):
            continue
        if line.startswith("# "):
            chapter += 1
            topic = line[2:].strip()
            continue
        fields = [part.strip() for part in line.split("|")]
        if len(fields) != 4 or chapter < 1:
            raise ValueError(f"Bad glossary source at line {number}")
        en, zh, abbr, definition = fields
        if not all((en, zh, definition)):
            raise ValueError(f"Missing term value at line {number}")
        key = (chapter, en.casefold(), zh)
        if key in seen:
            raise ValueError(f"Duplicate term at line {number}: {en}")
        seen.add(key)
        rows.append(dict(category=SLUG, chapter=chapter, topic=topic,
                         en=en, zh=zh, abbr=abbr, definition=definition))
    if not rows:
        raise ValueError("No high-school mathematics terminology found")
    return rows

def render_pdf(entries: list[dict], dest: Path | None = None) -> Path:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
        KeepTogether, CondPageBreak,
    )
    dest = dest or ROOT / "pdf" / f"{SLUG}.pdf"
    dest.parent.mkdir(parents=True, exist_ok=True)
    fonts = [
        Path("/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf"),
        Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
    ]
    font = next((p for p in fonts if p.is_file()), None)
    if font is None:
        from glob import glob
        candidates = glob("/usr/share/fonts/**/*gbsn*.ttf", recursive=True)
        font = Path(candidates[0]) if candidates else None
    if font is None:
        raise RuntimeError(
            "Chinese TTF font missing. Install fonts-arphic-gbsn00lp to build PDF."
        )
    pdfmetrics.registerFont(TTFont("HSGlossary", str(font)))
    NAVY = colors.HexColor("#13233D")
    BLUE = colors.HexColor("#2458C4")
    GRAY = colors.HexColor("#586B84")
    BORDER = colors.HexColor("#DDE5F0")
    PALE = colors.HexColor("#EDF3FE")
    LIGHT = colors.HexColor("#F8FAFE")
    styles = {
        "eyebrow": ParagraphStyle("HSeyebrow", fontName="HSGlossary", fontSize=10, leading=17, textColor=BLUE, spaceAfter=11),
        "title": ParagraphStyle("HStitle", fontName="HSGlossary", fontSize=28, leading=41, textColor=NAVY, spaceAfter=16),
        "subtitle": ParagraphStyle("HSsubtitle", fontName="HSGlossary", fontSize=11, leading=18, textColor=GRAY),
        "heading": ParagraphStyle("HSheading", fontName="HSGlossary", fontSize=14, leading=22, textColor=NAVY, spaceBefore=13, spaceAfter=8),
        "body": ParagraphStyle("HSbody", fontName="HSGlossary", fontSize=9, leading=16, textColor=NAVY),
        "small": ParagraphStyle("HSsmall", fontName="HSGlossary", fontSize=7.6, leading=11.5, textColor=NAVY),
        "tablehead": ParagraphStyle("HStablehead", fontName="HSGlossary", fontSize=8, leading=12, textColor=NAVY),
        "tiny": ParagraphStyle("HStiny", fontName="HSGlossary", fontSize=8.1, leading=14, textColor=GRAY),
    }
    def p(text, kind="small"):
        return Paragraph(escape(str(text)), styles[kind])
    groups = defaultdict(list)
    for term in entries:
        groups[(term["chapter"], term["topic"])].append(term)
    chapters = sorted(groups)
    W, H = A4
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(BLUE)
        canvas.rect(0, H-6, W, 6, stroke=0, fill=1)
        canvas.setStrokeColor(BORDER)
        canvas.line(42, 44, W-42, 44)
        canvas.setFont("HSGlossary", 8)
        canvas.setFillColor(GRAY)
        canvas.drawString(42, 30, "TERM/ATLAS   ·   高中数学  /  HIGH SCHOOL MATHEMATICS")
        canvas.drawRightString(W-42, 30, f"{doc.page:02d}")
        canvas.restoreState()
    doc = SimpleDocTemplate(
        str(dest), pagesize=A4, leftMargin=42, rightMargin=42,
        topMargin=56, bottomMargin=60,
        title="高中数学专有知识点中英文对照表",
        author="TERM/ATLAS · bilingual-technical-glossary",
        subject="High-school mathematics bilingual terminology and definitions",
    )
    story = [
        Spacer(1, 66),
        p("TERM/ATLAS  /  MATHEMATICS HANDBOOK  /  2026", "eyebrow"),
        Paragraph("高中数学<br/>专有知识点中英文对照表", styles["title"]),
        p("High School Mathematics · Chinese–English Glossary", "subtitle"),
        Spacer(1, 37),
        p(f"{len(entries)} TERMS    /    {len(chapters)} TOPICS", "heading"),
        Spacer(1, 20),
        p("按高中数学主要知识模块编排，覆盖集合与逻辑、函数、三角、数列、几何、导数、统计、概率及拓展内容。", "body"),
        Spacer(1, 11),
        p("适用于课堂教学、双语学习、国际课程阅读、数学论文检索及 Manim 教学动画术语统一。", "body"),
        Spacer(1, 19),
        p("编校说明：术语采用常见教材译法；不同课程版本与英语语境可能存在名称差异。部分章节为选修或拓展内容，并非每地高考的统一要求。", "tiny"),
        PageBreak(),
        p("专题目录  /  CONTENTS", "heading"),
        Spacer(1, 8),
    ]
    for chapter, topic in chapters:
        story.append(p(f"{chapter:02d}.  {topic}     ·     {len(groups[(chapter,topic)])} 条", "body"))
        story.append(Spacer(1, 7))
    story += [
        Spacer(1, 24),
        p("阅读方式：每一条词条依次列出英文术语、中文常用译名、缩写和简明定义。含缩写的词条可用于英语文献关键词检索。", "tiny"),
        PageBreak(),
    ]
    colWidths = [151, 105, 45, 210]
    for chapter, topic in chapters:
        rows = groups[(chapter, topic)]
        story.append(CondPageBreak(80))
        story.append(Paragraph(f"{chapter:02d}  /  {escape(topic)}", styles["heading"]))
        story.append(p(f"{len(rows)} TERMS   •   ENGLISH / 中文 / ABBR. / 释义", "tiny"))
        story.append(Spacer(1, 9))
        cells = [[p("ENGLISH TERM","tablehead"),p("中文译名","tablehead"),
                  p("缩写","tablehead"),p("简明释义","tablehead")]]
        for r in rows:
            cells.append([p(r["en"]),p(r["zh"]),p(r["abbr"]),p(r["definition"])])
        table = Table(cells, colWidths=colWidths, repeatRows=1, hAlign="LEFT", splitByRow=1)
        table.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),PALE),
            ("LINEBELOW",(0,0),(-1,0),0.8,BLUE),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),6),
            ("RIGHTPADDING",(0,0),(-1,-1),6),
            ("TOPPADDING",(0,0),(-1,-1),6),
            ("BOTTOMPADDING",(0,0),(-1,-1),6),
            ("LINEBELOW",(0,1),(-1,-1),0.35,BORDER),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,LIGHT]),
        ]))
        story.extend([table, Spacer(1, 15)])
    story += [
        Spacer(1, 20),
        p("术语来源与维护", "heading"),
        p("本手册为学习用途的独立整理，不复刻第三方受版权保护的教材段落。欢迎在仓库中提交翻译纠错与权威出处。", "body"),
        Spacer(1, 12),
        p("Source: data/high-school-mathematics.tsv · Repository: github.com/1998x-stack/bilingual-technical-glossary", "tiny"),
    ]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return dest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "pdf" / f"{SLUG}.pdf"))
    args = parser.parse_args()
    rows = load_terms()
    path = render_pdf(rows, Path(args.output))
    print(f"PDF generated: {path} ({len(rows)} terms; {path.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
