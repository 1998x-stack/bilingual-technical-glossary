#!/usr/bin/env python3
"""Render an original, searchable Computer Networks PDF from the curated TSV."""
from __future__ import annotations

from collections import defaultdict
from html import escape
from pathlib import Path
import argparse
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, PageBreak, Spacer,
    LongTable, TableStyle, KeepTogether,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "computer-networks.tsv"
OUTPUT = ROOT / "pdf" / "computer-networks.pdf"

def load_source(path: Path):
    chapters = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            match = re.fullmatch(r"# (\d{2}) (.*?) / (.+)", line)
            if not match:
                raise ValueError(f"Bad chapter on line {number}: {line}")
            chapters.append((int(match.group(1)), match.group(2), match.group(3), []))
            continue
        columns = [value.strip() for value in line.split("|")]
        if len(columns) != 3 or not all(columns) or not chapters:
            raise ValueError(f"Bad term on line {number}: {line}")
        chapters[-1][3].append(columns)
    rows = sum(len(group[3]) for group in chapters)
    if len(chapters) != 18 or rows != 359:
        raise ValueError(f"Unexpected publication size: {len(chapters)} topics / {rows} terms")
    if sorted(group[0] for group in chapters) != list(range(1, 19)):
        raise ValueError("Invalid chapter ordering")
    return chapters

def choose_font():
    options = [
        "/usr/share/fonts/truetype/arphic-gbsn00lp/gbsn00lp.ttf",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/truetype/arphic-gkai00mp/gkai00mp.ttf",
    ]
    for item in options:
        if Path(item).is_file() and item.endswith(".ttf"):
            pdfmetrics.registerFont(TTFont("NetworkCJK", item))
            return "NetworkCJK"
    raise RuntimeError("A compatible Chinese TTF font is required; install fonts-arphic-gbsn00lp")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    chapters = load_source(args.source)
    font = choose_font()

    NAVY = colors.HexColor("#17263F")
    BLUE = colors.HexColor("#2453B2")
    INK = colors.HexColor("#2A3850")
    MUTED = colors.HexColor("#66758B")
    PALE = colors.HexColor("#EEF3FB")
    LINE = colors.HexColor("#DEE6F1")
    title = ParagraphStyle("title", fontName=font, fontSize=27, leading=41,
                           textColor=NAVY, spaceAfter=18, wordWrap="CJK")
    chapter_style = ParagraphStyle("chapter", fontName=font, fontSize=14, leading=23,
                                   textColor=NAVY, spaceBefore=8, spaceAfter=12, wordWrap="CJK")
    body = ParagraphStyle("body", fontName=font, fontSize=9, leading=16,
                          textColor=INK, wordWrap="CJK", spaceAfter=4)
    small = ParagraphStyle("small", fontName=font, fontSize=8, leading=13,
                           textColor=MUTED, wordWrap="CJK")
    cell = ParagraphStyle("cell", fontName=font, fontSize=8, leading=13,
                          textColor=INK, wordWrap="CJK")
    header = ParagraphStyle("columnhead", parent=cell, textColor=NAVY)

    def p(value, style=cell):
        return Paragraph(escape(str(value)), style)

    def decorate(canvas, document):
        canvas.saveState()
        width, height = A4
        canvas.setFillColor(BLUE)
        canvas.rect(0, height - 6, width, 6, stroke=0, fill=1)
        canvas.setStrokeColor(LINE)
        canvas.line(42, 45, width - 42, 45)
        canvas.setFillColor(MUTED)
        canvas.setFont(font, 8)
        canvas.drawString(42, 30, "TERM/ATLAS   ·   Computer Networks   ·   Bilingual Glossary")
        canvas.drawRightString(width - 42, 30, f"{document.page:02d}")
        canvas.restoreState()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(args.output), pagesize=A4,
                            leftMargin=42, rightMargin=42,
                            topMargin=48, bottomMargin=61,
                            title="计算机网络专有名词中英文对照表",
                            author="TERM/ATLAS · 1998x-stack",
                            subject="Computer Networks Chinese-English Technical Glossary")
    story = [
        Spacer(1, 76),
        p("TERM / ATLAS       COMPUTER NETWORKING", body),
        Spacer(1, 27),
        Paragraph("计算机网络<br/>专有名词中英文对照表", title),
        p("Computer Networks · Chinese-English Technical Glossary", body),
        Spacer(1, 26),
        Paragraph("359 TERMS    /    18 TOPICS    /    2026 EDITION", chapter_style),
        Spacer(1, 10),
        p("涵盖分层模型、物理层、以太网与 WLAN、IPv4/IPv6、路由、TCP/UDP/QUIC、DNS、HTTP、TLS、QoS、云网络与故障排查。", body),
        Spacer(1, 15),
        p("面向计算机网络课程学习、协议检索、系统设计与工程面试。以经典教材和 IETF RFC、IEEE 802 等规范为参考独立整理。", body),
        Spacer(1, 22),
        p("说明：术语解释为教学和工程速查摘要，不代替完整协议规范；不同技术版本的具体行为以对应标准和实现为准。", small),
        PageBreak(),
        Paragraph("专题目录 / Contents", chapter_style),
        Spacer(1, 14),
    ]
    for chapter, zh, en, entries in chapters:
        story.append(p(f"{chapter:02d}   {zh} / {en}   ·   {len(entries)} terms", body))
        story.append(Spacer(1, 5))
    story.extend([
        Spacer(1, 20),
        p("Reference: RFC 9293 (TCP), RFC 8200 (IPv6), RFC 9000 (QUIC), RFC 9110 (HTTP), RFC 9114 (HTTP/3), RFC 8446 (TLS 1.3); IEEE 802.", small),
        PageBreak(),
    ])
    for chapter, zh, en, entries in chapters:
        story.append(Paragraph(f"{chapter:02d} / {escape(zh)}", chapter_style))
        story.append(p(f"{en}   ·   {len(entries)} terms", small))
        story.append(Spacer(1, 8))
        rows = [[p("ENGLISH", header), p("中文译名", header), p("简明释义", header)]]
        for english, chinese, definition in entries:
            rows.append([p(english), p(chinese), p(definition)])
        table = LongTable(rows, colWidths=[162, 104, 245], repeatRows=1,
                          splitByRow=1, hAlign="LEFT")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), PALE),
            ("LINEBELOW", (0, 0), (-1, 0), 1.0, BLUE),
            ("LINEBELOW", (0, 1), (-1, -1), 0.3, LINE),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFCFF")]),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]))
        story.extend([table, Spacer(1, 16)])
    story.extend([
        PageBreak(),
        Paragraph("资料与术语校订 / Editorial notes", chapter_style),
        p("本手册保持与仓库中的 data/computer-networks.tsv 和 glossaries/computer-networks.md 一致。", body),
        p("主参考：Kurose & Ross, Computer Networking: A Top-Down Approach；RFC 9293、8200、9000、9110、9114、8446；IEEE 802。", body),
        p("GitHub: https://github.com/1998x-stack/bilingual-technical-glossary", body),
    ])
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    if not args.output.read_bytes().startswith(b"%PDF-"):
        raise RuntimeError("Invalid generated PDF")
    print(f"Published {args.output}, {args.output.stat().st_size} bytes")

if __name__ == "__main__":
    main()
