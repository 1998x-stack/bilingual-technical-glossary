#!/usr/bin/env python3
"""Import the authored university-mathematics volume without PDF text extraction.

The original HTML publication is preserved in sources/university-mathematics.html.
This importer creates the 627 searchable entries, Markdown appendices and print PDF.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/university-mathematics.html"
SLUG = "university-mathematics"
EXPECTED_TERMS = 627
EXPECTED_CHAPTERS = 17


def _source():
    from bs4 import BeautifulSoup
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Missing authored source: {SOURCE}")
    return BeautifulSoup(SOURCE.read_text(encoding="utf-8"), "html.parser")


def load_entries():
    soup = _source()
    chapters = soup.select("section.chapter")
    if len(chapters) != EXPECTED_CHAPTERS:
        raise ValueError(f"Expected {EXPECTED_CHAPTERS} chapters, got {len(chapters)}")

    entries = []
    chapter_counts = []
    for number, section in enumerate(chapters, 1):
        section_id = section.get("id", "")
        if section_id != f"c{number:02d}":
            raise ValueError(f"Unexpected section ID {section_id!r} for chapter {number}")
        heading = section.select_one(".chapter-heading h2")
        if heading is None:
            raise ValueError(f"Missing heading for chapter {number}")
        topic = heading.get_text(" ", strip=True)
        rows = section.select("table.terms tbody tr")
        chapter_counts.append(len(rows))
        for expected_index, tr in enumerate(rows, 1):
            cells = tr.find_all("td", recursive=False)
            if len(cells) != 4:
                raise ValueError(f"Chapter {number}, row {expected_index}: expected 4 columns")
            index, zh, en, definition = [cell.get_text(" ", strip=True) for cell in cells]
            if int(index) != expected_index or not all((zh, en, definition)):
                raise ValueError(f"Malformed term in chapter {number}, row {expected_index}")
            abbr_match = re.search(r"\(([A-Z][A-Z0-9-]{1,10})\)", en)
            entries.append({
                "category": SLUG,
                "chapter": number,
                "topic": topic,
                "en": en,
                "zh": zh,
                "abbr": abbr_match.group(1) if abbr_match else "",
                "definition": definition,
            })
    if len(entries) != EXPECTED_TERMS:
        raise ValueError(f"Expected {EXPECTED_TERMS} terms, got {len(entries)}")
    if len(set((x["chapter"], x["en"].casefold(), x["zh"]) for x in entries)) != len(entries):
        raise ValueError("Duplicate university mathematics records")
    return entries


def merge_entries(all_terms):
    # Stable, idempotent update. Existing mathematics volumes are preserved.
    old = [term for term in all_terms if term.get("category") != SLUG]
    return old + load_entries()


def appendix_markdown():
    soup = _source()
    sections = [
        ("confuse", "A. 易混数学术语辨析"),
        ("symbols", "B. 常用数学符号"),
        ("abbr", "C. 高频英文缩写"),
    ]
    output = ["", "---", "", "## 附录 / Appendices", "",
              "> 与本卷 PDF 附录对应；译法和符号读法可能随学科语境变化。", ""]
    for section_id, title in sections:
        section = soup.find("section", id=section_id)
        if section is None:
            raise ValueError(f"Missing appendix: {section_id}")
        header = [th.get_text(" ", strip=True) for th in section.select("table thead th")]
        rows = section.select("table tbody tr")
        if not header or not rows:
            raise ValueError(f"Missing appendix table: {section_id}")
        escape_cell = lambda s: s.replace("|", "\\|").replace("\n", " ")
        output += [f"### {title}", "",
                   "| " + " | ".join(escape_cell(h) for h in header) + " |",
                   "|" + "|".join("---" for _ in header) + "|"]
        for tr in rows:
            cells = [td.get_text(" ", strip=True) for td in tr.find_all("td", recursive=False)]
            if len(cells) != len(header):
                raise ValueError(f"Invalid appendix row in {section_id}")
            output.append("| " + " | ".join(escape_cell(s) for s in cells) + " |")
        output.append("")
    return "\n".join(output) + "\n"


def render_source_pdf():
    from weasyprint import HTML
    target = ROOT / "pdf" / f"{SLUG}.pdf"
    target.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(SOURCE), base_url=str(ROOT)).write_pdf(str(target))
    with target.open("rb") as stream:
        if stream.read(5) != b"%PDF-" or target.stat().st_size < 10000:
            raise RuntimeError("University mathematics PDF render failed")
    return target


if __name__ == "__main__":
    import json
    data_file = ROOT / "data" / "terms.json"
    all_terms = json.loads(data_file.read_text(encoding="utf-8"))
    result = merge_entries(all_terms)
    print(f"Source parsed: {len(load_entries())} terms across {EXPECTED_CHAPTERS} chapters; "
          f"merged searchable total: {len(result)}")
