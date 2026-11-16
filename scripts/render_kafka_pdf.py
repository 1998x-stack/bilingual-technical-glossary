#!/usr/bin/env python3
"""Publish the authored Apache Kafka glossary as a searchable A4 PDF."""
from collections import defaultdict
from pathlib import Path
from html import escape
import json
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "pdf" / "apache-kafka.pdf"
SOURCE = ROOT / "data" / "terms.json"

def main():
    font_candidates = [
        Path("/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf"),
        Path("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    font = next((p for p in font_candidates if p.exists()), None)
    if font is None:
        if DEST.is_file():
            print("CJK font missing; preserving existing Kafka PDF")
            return
        raise SystemExit("Install fonts-arphic-gbsn00lp before rendering Kafka PDF")
    pdfmetrics.registerFont(TTFont("KafkaCJK", str(font)))
    entries = [t for t in json.loads(SOURCE.read_text(encoding="utf-8"))
               if t["category"] == "apache-kafka"]
    if len(entries) != 283:
        raise ValueError(f"Expected 283 curated Kafka terms, got {len(entries)}")
    groups = defaultdict(list)
    for entry in entries:
        groups[(entry["chapter"], entry["topic"])].append(entry)
    if len(groups) != 16:
        raise ValueError(f"Expected 16 Kafka topics, got {len(groups)}")

    navy = colors.HexColor("#17263F")
    blue = colors.HexColor("#265BD5")
    ink = colors.HexColor("#25334D")
    muted = colors.HexColor("#66758C")
    faint = colors.HexColor("#E0E7F2")
    light = colors.HexColor("#EDF3FC")
    name = "KafkaCJK"
    title = ParagraphStyle("title", fontName=name, fontSize=27, leading=40,
                           textColor=navy, spaceAfter=16)
    subtitle = ParagraphStyle("subtitle", fontName=name, fontSize=11,
                              leading=19, textColor=muted, spaceAfter=15)
    heading = ParagraphStyle("heading", fontName=name, fontSize=14,
                             leading=24, textColor=navy, spaceBefore=14, spaceAfter=10)
    body = ParagraphStyle("body", fontName=name, fontSize=9, leading=16,
                          textColor=ink, wordWrap="CJK")
    cell = ParagraphStyle("cell", parent=body, fontSize=7.8, leading=13)
    small = ParagraphStyle("small", parent=body, fontSize=8, leading=14)
    def p(s, style=cell):
        return Paragraph(escape(str(s)), style)
    def decorate(canvas, document):
        canvas.saveState()
        canvas.setFillColor(blue)
        canvas.rect(0, A4[1] - 6, A4[0], 6, stroke=0, fill=1)
        canvas.setStrokeColor(faint)
        canvas.line(42, 42, A4[0] - 42, 42)
        canvas.setFont(name, 8)
        canvas.setFillColor(muted)
        canvas.drawString(42, 29, "TERM/ATLAS  ·  Apache Kafka  ·  Bilingual Reference")
        canvas.drawRightString(A4[0] - 42, 29, f"{document.page:02d}")
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(DEST), pagesize=A4, leftMargin=42, rightMargin=42,
        topMargin=50, bottomMargin=58, title="Apache Kafka 专有名词中英文对照表",
        author="TERM/ATLAS · 1998x-stack")
    story = [
        Spacer(1, 80),
        p("TERM / ATLAS       EVENT STREAMING REFERENCE", small),
        Spacer(1, 26),
        Paragraph("Apache Kafka<br/>专有名词中英文对照表", title),
        Paragraph("Apache Kafka · Chinese–English Technical Glossary", subtitle),
        Spacer(1, 20),
        Paragraph("283 TERMS   /   16 TOPICS   /   2026 EDITION", heading),
        Spacer(1, 9),
        p("覆盖事件流、Broker 与网络、KRaft、分区与 Offset、生产者和消费者、"
          "可靠性与事务、Share Groups、Kafka Connect、Kafka Streams、"
          "安全、性能、运维及工程实践。", body),
        Spacer(1, 18),
        p("说明：以 Apache Kafka 4.x 相关官方资料为主要参考；具体 API、配置项、"
          "新特性状态请以对应版本文档为准。此手册为学习参考，不是 ASF 官方出版物。", body),
        PageBreak(),
        Paragraph("专题目录 / Contents", heading),
    ]
    for (chapter, topic), rows in sorted(groups.items()):
        story.append(p(f"{chapter:02d}   {topic}     /     {len(rows)} terms", small))
        story.append(Spacer(1, 4))
    story += [
        Spacer(1, 18),
        p("资料来源：kafka.apache.org/documentation/（Apache Kafka 官方文档）。", small),
        PageBreak(),
    ]
    for (chapter, topic), rows in sorted(groups.items()):
        story.append(Paragraph(f"{chapter:02d}  /  {escape(topic)}", heading))
        story.append(p(f"{len(rows)} terms  ·  English / 中文 / 简明释义", small))
        story.append(Spacer(1, 9))
        grid = [[p("ENGLISH TERM"), p("中文译名"), p("简明释义")]]
        grid.extend([p(t["en"]), p(t["zh"]), p(t["definition"])] for t in rows)
        table = Table(grid, colWidths=[151, 120, 240], repeatRows=1, hAlign="LEFT")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), light),
            ("LINEBELOW", (0,0), (-1,0), 1, blue),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F9FBFE")]),
            ("LINEBELOW", (0,1), (-1,-1), 0.3, faint),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING", (0,0), (-1,-1), 7),
            ("RIGHTPADDING", (0,0), (-1,-1), 7),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ]))
        story.extend([table, Spacer(1, 14)])
    DEST.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    with DEST.open("rb") as f:
        if f.read(5) != b"%PDF-":
            raise RuntimeError("Invalid generated PDF")
    print("Created", DEST, DEST.stat().st_size, "bytes")

if __name__ == "__main__":
    main()
