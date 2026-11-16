#!/usr/bin/env python3
"""Idempotently register the authored Kafka source in TERM/ATLAS and Pages."""
from pathlib import Path
from collections import Counter
import csv
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "glossaries" / "apache-kafka.md"
DATA = ROOT / "data" / "terms.json"
CATALOG = ROOT / "docs" / "data" / "catalog.json"
KAFKA = {
    "slug": "apache-kafka",
    "en": "Apache Kafka",
    "zh": "Apache Kafka / 事件流平台",
    "description": "Event streaming, KRaft, partitions, consumers, transactions and Streams",
    "icon": "network",
}

def read(path):
    return path.read_text(encoding="utf-8")

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or read(path) != text:
        path.write_text(text, encoding="utf-8")
        print("Updated", path.relative_to(ROOT))

def kafka_rows():
    chapter = None
    topic = None
    rows = []
    chapters = set()
    for line in read(MD).splitlines():
        match = re.match(r"^## (\d{2}) (.+?) · ", line)
        if match:
            chapter, topic = int(match.group(1)), match.group(2)
            chapters.add(chapter)
            continue
        if chapter is None or not line.startswith("| "):
            continue
        parts = [x.strip().replace(r"\|", "|")
                 for x in re.split(r"(?<!\\)\|", line.strip(" |"))]
        if len(parts) != 3 or parts[0] == "English":
            continue
        en, zh, definition = parts
        paren = re.search(r"\(([A-Z][A-Z0-9-]{1,10})\)", en)
        abbr = paren.group(1) if paren else en if re.fullmatch(r"[A-Z][A-Z0-9]{1,9}", en) else ""
        rows.append(dict(category="apache-kafka", chapter=chapter, topic=topic,
                         en=en, zh=zh, abbr=abbr, definition=definition))
    if len(rows) != 283 or chapters != set(range(1, 17)):
        raise ValueError(f"Kafka Markdown expected 283 terms and 16 chapters; got {len(rows)} and {len(chapters)}")
    keys = [(x["chapter"], x["en"].casefold(), x["zh"]) for x in rows]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate Kafka terms in authored Markdown")
    return rows

def main():
    source = kafka_rows()
    data = json.loads(read(DATA))
    current = [x for x in data if x["category"] == "apache-kafka"]
    if current:
        if len(current) != len(source):
            raise ValueError(f"Kafka index has {len(current)} rows; expected 283")
    else:
        data.extend(source)
    write(DATA, json.dumps(data, ensure_ascii=False, indent=2))

    names = ["category", "chapter", "topic", "en", "zh", "abbr", "definition"]
    import io
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=names, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(data)
    write(ROOT / "data" / "terms.csv", out.getvalue())
    write(ROOT / "docs" / "data" / "terms.json",
          json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    write(ROOT / "docs" / "glossaries" / "apache-kafka.md", read(MD))

    catalog = json.loads(read(CATALOG))
    indexed = Counter(x["category"] for x in data)
    for item in catalog:
        slug = item["slug"]
        item["count"] = indexed[slug]
        item["topics"] = len({x["topic"] for x in data if x["category"] == slug})
    if not any(x["slug"] == KAFKA["slug"] for x in catalog):
        catalog.append({**KAFKA, "count": 283, "topics": 16})
    if len(catalog) != len(indexed):
        raise ValueError("Catalog and indexed categories differ")
    write(CATALOG, json.dumps(catalog, ensure_ascii=False, indent=2))
    total = len(data)
    topics = sum(x["topics"] for x in catalog)

    build_path = ROOT / "scripts" / "build.py"
    build = read(build_path)
    if "('apache-kafka'," not in build:
        marker = "\n]\nMETA="
        if marker not in build:
            raise ValueError("Could not locate build CATALOG end")
        tup = "\n ('apache-kafka','Apache Kafka','Apache Kafka / 事件流平台'," \
              "'Event streaming, KRaft, partitions, consumers, transactions and Streams','network'),"
        build = build.replace(marker, tup + marker, 1)
    if "if slug=='apache-kafka':continue" not in build:
        marker = "def write_markdown(data):\n for slug in META:\n"
        if marker not in build:
            raise ValueError("Could not locate build Markdown loop")
        build = build.replace(marker, marker +
                              "  if slug=='apache-kafka':continue  # Preserve original editorial Markdown.\n", 1)
    if "scripts/render_kafka_pdf.py" not in build:
        marker = "\n write_site_data(data)\n"
        if marker not in build:
            raise ValueError("Could not locate build site stage")
        build = build.replace(marker,
                              "\n import subprocess,sys\n"
                              " subprocess.run([sys.executable,str(ROOT/'scripts/render_kafka_pdf.py')],check=True)\n" +
                              marker, 1)
    write(build_path, build)

    eng = ROOT / "README.md"
    english = read(eng)
    en_row = "| Apache Kafka | Apache Kafka / 事件流平台 | 283 | 16 | [Read](glossaries/apache-kafka.md) | [Download](pdf/apache-kafka.pdf) |"
    if en_row not in english:
        english = re.sub(r"(?m)^\| \*\*Total\*\*", en_row + "\n| **Total**", english, count=1)
    english = re.sub(r"(?m)^\| \*\*Total\*\* \|.*$",
                     f"| **Total** | **{len(catalog)} domains** | **{total:,}** | **{topics}** | | |", english)
    english = re.sub(r"\*\*\d+ topic chapters:\*\*", f"**{topics} topic chapters:**", english)
    if "Kafka volume contributes" not in english:
        english = english.replace("> **Data provenance.**",
            "> **Data provenance.** The Kafka volume contributes 283 original, fully indexed terms in 16 chapters, with curated Markdown and searchable PDF editions. ")
    write(eng, english)

    cn = ROOT / "README.zh-CN.md"
    chinese = read(cn)
    zh_row = "| Apache Kafka / 事件流平台 | 283 | 16 | [阅读](glossaries/apache-kafka.md) | [下载](pdf/apache-kafka.pdf) |"
    if zh_row not in chinese:
        chinese = re.sub(r"(?m)^\| \*\*合计\*\*", zh_row + "\n| **合计**", chinese, count=1)
    chinese = re.sub(r"(?m)^\| \*\*合计\*\* \|.*$",
                     f"| **合计** | **{total:,}** | **{topics}** | | |", chinese)
    if "Kafka 专题新增" not in chinese:
        chinese = chinese.replace("**数据说明：**",
            "**Kafka 专题新增：**283 条术语、16 个章节，Markdown 原稿和可检索 PDF 均已收录，且同步到网页、JSON 与 CSV 索引。\n\n**数据说明：**")
    write(cn, chinese)

    app_path = ROOT / "site" / "app.js"
    js = read(app_path)
    js = js.replace("SUBJECT_COLORS[i]", "SUBJECT_COLORS[i%SUBJECT_COLORS.length]")
    js = js.replace("SUBJECT_GLYPHS[i]", "SUBJECT_GLYPHS[i%SUBJECT_GLYPHS.length]")
    write(app_path, js)
    write(ROOT / "docs" / "app.js", js)

    agents = ROOT / "AGENTS.md"
    instructions = read(agents)
    if "Kafka editorial provenance" not in instructions:
        instructions += ("\n## Kafka editorial provenance\n"
          "The 283-row, 16-chapter `glossaries/apache-kafka.md` is an original reference "
          "with a preface and concept contrasts. The build intentionally preserves this "
          "Markdown and renders its indexed rows to `pdf/apache-kafka.pdf` using "
          "`scripts/render_kafka_pdf.py`; mirror to `docs/pdf/`.\n")
    write(agents, instructions)

    changelog = ROOT / "CHANGELOG.md"
    log = read(changelog)
    if "Apache Kafka glossary" not in log:
        log = log.replace("# Changelog\n\n",
            "# Changelog\n\n## 2026-11-16 — Apache Kafka glossary\n\n"
            "- Added 283 Kafka terms across 16 chapters in Markdown, PDF, and search indexes.\n"
            "- Updated bilingual README navigation and added Kafka regression coverage.\n\n", 1)
    write(changelog, log)

    test = ROOT / "tests" / "test_kafka.py"
    write(test, '''import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TERMS = json.loads((ROOT / "data" / "terms.json").read_text(encoding="utf-8"))
class KafkaGlossaryTests(unittest.TestCase):
    def test_coverage(self):
        rows = [x for x in TERMS if x["category"] == "apache-kafka"]
        self.assertEqual(len(rows), 283)
        self.assertEqual(sorted({x["chapter"] for x in rows}), list(range(1, 17)))
        self.assertEqual(len({x["topic"] for x in rows}), 16)
    def test_publications(self):
        for file in ("glossaries/apache-kafka.md", "pdf/apache-kafka.pdf",
                     "docs/glossaries/apache-kafka.md", "docs/pdf/apache-kafka.pdf"):
            self.assertTrue((ROOT / file).is_file(), file)
if __name__ == "__main__":
    unittest.main()
''')
    print(f"Kafka integrated: {total:,} searchable terms, {len(catalog)} domains, {topics} topics")

if __name__ == "__main__":
    main()
