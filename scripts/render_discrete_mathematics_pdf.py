#!/usr/bin/env python3
"""Curated discrete-mathematics glossary: parse TSV and render a searchable PDF."""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
SLUG = "discrete-mathematics"

def load_terms(path: Path | None = None) -> list[dict]:
    path = path or ROOT / "data" / f"{SLUG}.tsv"
    chapter, topic, rows, seen = 0, "", [], set()
    for line_number, raw in enumerate(path.read_text(encoding="utf8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            chapter += 1
            topic = line[2:].strip()
            continue
        fields = [part.strip() for part in line.split("|")]
        if len(fields) != 4 or chapter < 1:
            raise ValueError(f"Invalid term at line {line_number}")
        en, zh, abbr, definition = fields
        if not (en and zh and definition):
            raise ValueError(f"Required value missing at line {line_number}")
        key = chapter, en.casefold(), zh
        if key in seen:
            raise ValueError(f"Duplicate term at line {line_number}: {en}")
        seen.add(key)
        rows.append(dict(category=SLUG, chapter=chapter, topic=topic,
                         en=en, zh=zh, abbr=abbr, definition=definition))
    if len(rows) < 300 or chapter != 16:
        raise ValueError("Expected at least 300 terms in 16 topics")
    return rows

def render_pdf(entries: list[dict], destination: Path | None = None) -> Path:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, CondPageBreak

    dest = destination or ROOT / "pdf" / f"{SLUG}.pdf"
    dest.parent.mkdir(parents=True, exist_ok=True)
    fonts = [Path("/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf"),
             Path("/usr/share/fonts/truetype/arphic-gkai00mp/gkai00mp.ttf")]
    font = next((path for path in fonts if path.is_file()), None)
    if font is None:
        raise RuntimeError("Install fonts-arphic-gbsn00lp before rendering the PDF")
    pdfmetrics.registerFont(TTFont("DiscreteCJK", str(font)))
    INK = colors.HexColor("#162640")
    SKY = colors.HexColor("#2668B9")
    MUTED = colors.HexColor("#66758B")
    LIGHT = colors.HexColor("#F4F8FD")
    BORDER = colors.HexColor("#DFE7F0")
    styles = {
      "eyebrow": ParagraphStyle("DMeyebrow",fontName="DiscreteCJK",fontSize=10,leading=17,textColor=SKY,spaceAfter=15),
      "title": ParagraphStyle("DMtitle",fontName="DiscreteCJK",fontSize=27,leading=40,textColor=INK,spaceAfter=20),
      "subtitle": ParagraphStyle("DMsubtitle",fontName="DiscreteCJK",fontSize=12,leading=19,textColor=MUTED),
      "heading": ParagraphStyle("DMheading",fontName="DiscreteCJK",fontSize=14,leading=22,textColor=INK,spaceBefore=13,spaceAfter=8),
      "body": ParagraphStyle("DMbody",fontName="DiscreteCJK",fontSize=9.1,leading=16,textColor=INK),
      "small": ParagraphStyle("DMsmall",fontName="DiscreteCJK",fontSize=7.6,leading=11.9,textColor=INK,wordWrap="CJK"),
      "table_head": ParagraphStyle("DMtableHead",fontName="DiscreteCJK",fontSize=8.3,leading=12,textColor=INK),
      "hint": ParagraphStyle("DMhint",fontName="DiscreteCJK",fontSize=8.4,leading=14.8,textColor=MUTED),
    }
    def p(text: str, key: str = "small") -> Paragraph:
        return Paragraph(escape(str(text)), styles[key])
    groups = defaultdict(list)
    for entry in entries:
        groups[entry["chapter"], entry["topic"]].append(entry)
    ordered = sorted(groups)
    W, H = A4
    def decorate(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(SKY)
        canvas.rect(0, H - 7, W, 7, fill=1, stroke=0)
        canvas.setStrokeColor(BORDER)
        canvas.line(42, 44, W - 42, 44)
        canvas.setFillColor(MUTED)
        canvas.setFont("DiscreteCJK", 8)
        canvas.drawString(42, 29, "TERM/ATLAS    /    DISCRETE MATHEMATICS    /    离散数学")
        canvas.drawRightString(W - 42, 29, f"{doc.page:02d}")
        canvas.restoreState()
    doc = SimpleDocTemplate(str(dest), pagesize=A4, leftMargin=42, rightMargin=42,
                            topMargin=56, bottomMargin=60,
                            title="离散数学专有名词中英文对照表",
                            author="TERM/ATLAS · bilingual-technical-glossary",
                            subject="Discrete mathematics: 324 bilingual terminology entries")
    story = [
      Spacer(1, 60),
      p("TERM/ATLAS  /  MATHEMATICS & COMPUTER SCIENCE  /  2026", "eyebrow"),
      Paragraph("离散数学<br/>专有名词中英文对照表", styles["title"]),
      p("Discrete Mathematics · Chinese–English Technical Glossary", "subtitle"),
      Spacer(1, 30),
      p(f"{len(entries)} TERMS    /    {len(ordered)} TOPICS", "heading"),
      Spacer(1, 15),
      p("从命题逻辑和证明方法出发，覆盖集合、函数、二元关系、排列组合、离散概率、递推关系、数论、图论、树、布尔代数与计算理论。", "body"),
      Spacer(1, 12),
      p("适用于计算机科学基础课程、英文教材阅读、算法学习、专业考试与技术面试。", "body"),
      Spacer(1, 20),
      p("编校说明：本表使用常见数学与计算机教材译法。部分术语在不同教材中有约定差异，需结合上下文理解；简明定义不代替形式化证明。", "hint"),
      PageBreak(),
      p("专题目录 / CONTENTS", "heading"),
      Spacer(1, 10),
    ]
    for chapter, topic in ordered:
        story.extend([p(f"{chapter:02d}. {topic}     /     {len(groups[chapter, topic])} TERMS", "body"),
                      Spacer(1, 6)])
    story.extend([Spacer(1, 14),
                  p("重点辨析：蕴涵与因果；自反与反自反；反对称与非对称；最小元与极小元；路径与迹；全序与偏序；单射、满射与双射。", "hint"),
                  PageBreak()])
    widths = [160, 106, 48, 197]
    for chapter, topic in ordered:
        rows = groups[chapter, topic]
        story.append(CondPageBreak(105))
        story.append(Paragraph(f"{chapter:02d} / {escape(topic)}", styles["heading"]))
        story.append(p(f"{len(rows)} terms · English / 中文 / 缩写 / 简明释义", "hint"))
        story.append(Spacer(1, 9))
        cells = [[p("ENGLISH TERM", "table_head"), p("中文译名", "table_head"),
                  p("ABBR.", "table_head"), p("简明释义", "table_head")]]
        for term in rows:
            cells.append([p(term["en"]), p(term["zh"]),
                          p(term["abbr"]), p(term["definition"])])
        table = Table(cells, colWidths=widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
        table.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E9F1FC")),
            ("LINEBELOW",(0,0),(-1,0),0.8,SKY),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,LIGHT]),
            ("LINEBELOW",(0,1),(-1,-1),0.24,BORDER),
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),6),
            ("RIGHTPADDING",(0,0),(-1,-1),6),
            ("TOPPADDING",(0,0),(-1,-1),5),
            ("BOTTOMPADDING",(0,0),(-1,-1),5),
        ]))
        story.extend([table,Spacer(1,17)])
    story.extend([
      PageBreak(),
      p("术语辨析与编辑参考 / EDITORIAL NOTES", "heading"),
      Spacer(1, 10),
      p("1. Implication 表示命题的真值条件，不应直接译作现实因果关系。", "body"),
      p("2. Antisymmetric（反对称）不等于 Asymmetric（非对称）；反对称允许自反边。", "body"),
      p("3. Minimal Element（极小元）不一定是 Least Element（最小元）。", "body"),
      p("4. Range（值域）与 Codomain（陪域）应明确区分；满射要求两者相同。", "body"),
      p("5. Path、Walk、Trail 在不同教材的约定有差异，使用时请注明定义。", "body"),
      Spacer(1, 17),
      p("主要学习参考（仅参考章节架构与通用术语，不转载教材原文）", "heading"),
      p("• Kenneth H. Rosen, Discrete Mathematics and Its Applications.", "body"),
      p("• Susanna S. Epp, Discrete Mathematics with Applications.", "body"),
      p("• MIT Mathematics for Computer Science (Lehman, Leighton, Meyer).", "body"),
      Spacer(1, 16),
      p("维护与勘误：github.com/1998x-stack/bilingual-technical-glossary", "hint"),
    ])
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    return dest

if __name__ == "__main__":
    items = load_terms()
    output = render_pdf(items)
    print(f"Rendered {output} with {len(items)} terms; {output.stat().st_size} bytes")
