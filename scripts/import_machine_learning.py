#!/usr/bin/env python3
"""Merge authored Machine Learning terms into the latest TERM/ATLAS main branch."""
from pathlib import Path
from collections import Counter
from io import StringIO
import csv, json, re, shutil
R = Path(__file__).resolve().parents[1]
SLUG = "machine-learning"
DESC = "Foundations, classical algorithms, model evaluation, tuning and MLOps"

def read(name):
    return (R / name).read_text(encoding="utf8")

def put(name, data):
    path = R / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf8") != data:
        path.write_text(data, encoding="utf8")

def entries():
    chapter = 0
    topic = ""
    rows = []
    chapters = set()
    for line in read("sources/machine-learning.md").splitlines():
        heading = re.match(r"^## (\d{2})\.\s+(.+?)\s+/\s+.+$", line)
        if heading:
            chapter, topic = int(heading.group(1)), heading.group(2).strip()
            chapters.add(chapter)
        elif chapter and line.startswith("|") and not re.match(r"^\|\s*(English term|-{3,})", line):
            cells = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(cells) != 3 or not all(cells):
                raise ValueError("Invalid Machine Learning row: " + line[:60])
            en, zh, meaning = cells
            m = re.search(r"\(([A-Z][A-Z0-9-]{1,12})\)$", en)
            rows.append(dict(category=SLUG, chapter=chapter, topic=topic,
                             en=en, zh=zh, abbr=m.group(1) if m else "",
                             definition=meaning))
    if len(rows) != 447 or len(chapters) != 19:
        raise ValueError("Expected 447 entries in 19 Machine Learning chapters")
    return rows

def patch_code():
    build = read("scripts/build.py")
    if "('machine-learning'," not in build:
        anchor = " ('reinforcement-learning'"
        if anchor not in build:
            raise ValueError("Build catalog insertion anchor unavailable")
        new = " ('machine-learning','Machine Learning','机器学习','" + DESC + "','target'),\n"
        put("scripts/build.py", build.replace(anchor, new + anchor, 1))
    verify = read("scripts/verify.py")
    if "counts['machine-learning']" not in verify:
        anchor = "counts=Counter(r['category'] for r in TERMS)"
        if anchor not in verify:
            raise ValueError("Verification code changed; cannot insert assertion")
        put("scripts/verify.py", verify.replace(anchor, anchor + "\ncheck(counts['machine-learning']==447,'ML must have 447 terms')", 1))
    tests = read("tests/test_catalog.py")
    if "def test_machine_learning_volume" not in tests:
        anchor = " def test_required_fields(self):"
        if anchor not in tests:
            raise ValueError("Test code changed; cannot insert regression")
        test = (" def test_machine_learning_volume(self):\n"
                "  ml=[t for t in DATA if t['category']=='machine-learning']\n"
                "  self.assertEqual(len(ml),447)\n"
                "  self.assertEqual(len(set(t['chapter'] for t in ml)),19)\n")
        put("tests/test_catalog.py", tests.replace(anchor, test + anchor, 1))
    app = read("site/app.js")
    colors = ("const SUBJECT_COLORS = ['#6d86e8','#4c9e88','#7f73d7','#449bd2',"
              "'#4bb69d','#5b88c5','#e5a760','#db7d97','#6195ab','#7c8cd6',"
              "'#6f9d87','#d59875'];")
    glyphs = "const SUBJECT_GLYPHS = ['⌘','⚙','↗','λ','∇','◉','∞','⊞','∑','◇','✦','◎'];"
    app = re.sub(r"const SUBJECT_COLORS = \[[^\n]+\];", colors, app, count=1)
    app = re.sub(r"const SUBJECT_GLYPHS = \[[^\n]+\];", glyphs, app, count=1)
    app = app.replace("SUBJECT_COLORS[i]", "SUBJECT_COLORS[i % SUBJECT_COLORS.length]")
    app = app.replace("SUBJECT_GLYPHS[i]", "SUBJECT_GLYPHS[i % SUBJECT_GLYPHS.length]")
    put("site/app.js", app)
    put("docs/app.js", app)

def update_index():
    data = json.loads(read("data/terms.json"))
    ml = [x for x in data if x["category"] == SLUG]
    if ml:
        if len(ml) != 447 or len({x["chapter"] for x in ml}) != 19:
            raise ValueError("Existing Machine Learning corpus is inconsistent")
    else:
        data.extend(entries())
    category_counts = Counter(x["category"] for x in data)
    chapter_counts = {slug: len({x["topic"] for x in data if x["category"] == slug}) for slug in category_counts}
    catalog = json.loads(read("docs/data/catalog.json"))
    if not any(x["slug"] == SLUG for x in catalog):
        idx = next((i for i, x in enumerate(catalog) if x["slug"] == "deep-learning"), None)
        if idx is None:
            raise ValueError("Deep Learning catalog entry unavailable")
        catalog.insert(idx + 1, dict(slug=SLUG, en="Machine Learning", zh="机器学习",
                                     description=DESC, icon="target"))
    if {x["slug"] for x in catalog} != set(category_counts):
        raise ValueError("Another subject is being indexed; retry against new main")
    for item in catalog:
        item["count"] = category_counts[item["slug"]]
        item["topics"] = chapter_counts[item["slug"]]
    keys = ["category", "chapter", "topic", "en", "zh", "abbr", "definition"]
    extra_keys = sorted({key for entry in data for key in entry} - set(keys))
    keys += extra_keys
    buffer = StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=keys, lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(data)
    put("data/terms.json", json.dumps(data, ensure_ascii=False, indent=2))
    put("data/terms.csv", buffer.getvalue())
    put("docs/data/terms.json", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    put("docs/data/catalog.json", json.dumps(catalog, ensure_ascii=False, indent=2))
    put("docs/glossaries/machine-learning.md", read("glossaries/machine-learning.md"))
    pdf = R / "pdf/machine-learning.pdf"
    if not pdf.exists() or pdf.read_bytes()[:5] != b"%PDF-":
        raise ValueError("Machine Learning PDF is not present")
    target = R / "docs/pdf/machine-learning.pdf"
    if not target.exists() or pdf.read_bytes() != target.read_bytes():
        shutil.copyfile(pdf, target)
    return len(data), len(catalog), sum(x["topics"] for x in catalog)

def documentation(terms, domains, topics):
    en = read("README.md")
    row = ("| Machine Learning | 机器学习 | 447 | 19 | [Read](glossaries/machine-learning.md)"
           " | [Download](pdf/machine-learning.pdf) |")
    if "glossaries/machine-learning.md" not in en:
        en = en.replace("| Reinforcement Learning |", row + "\n| Reinforcement Learning |", 1)
    en = re.sub(r"\| \*\*Total\*\* \| \*\*\d+ domains\*\* \| \*\*[\d,]+\*\* \| \*\*\d+\*\* \| \| \|",
                f"| **Total** | **{domains} domains** | **{terms:,}** | **{topics}** | | |", en)
    en = re.sub(r"\*\*\d+ topic chapters:\*\*", f"**{topics} topic chapters:**", en)
    en = re.sub(r"(glossaries/)\s+# \d+ thematic Markdown glossaries", rf"\1                    # {domains} thematic Markdown glossaries", en)
    en = re.sub(r"(pdf/)\s+# \d+ searchable PDF handbooks", rf"\1                           # {domains} searchable PDF handbooks", en)
    if "The Machine Learning volume adds 447" not in en:
        en = re.sub(r"^(> \*\*Data provenance\.\*\*.*)$",
                    r"\1 The Machine Learning volume adds 447 independently authored entries across 19 topics, with matching Markdown and searchable PDF.",
                    en, count=1, flags=re.M)
    if "├── sources/" not in en:
        en = en.replace("├── glossaries/", "├── sources/                       # Authored glossary print materials\n├── glossaries/", 1)
    put("README.md", en)
    zh = read("README.zh-CN.md")
    row = ("| 机器学习 / Machine Learning | 447 | 19 | [阅读](glossaries/machine-learning.md)"
           " | [下载](pdf/machine-learning.pdf) |")
    if "glossaries/machine-learning.md" not in zh:
        zh = zh.replace("| 强化学习 / Reinforcement Learning |", row + "\n| 强化学习 / Reinforcement Learning |", 1)
    zh = re.sub(r"\| \*\*合计\*\* \| \*\*[\d,]+\*\* \| \*\*\d+\*\* \| \| \|",
                f"| **合计** | **{terms:,}** | **{topics}** | | |", zh)
    zh = re.sub(r"\d+ 个学科、\d+ 个专题", f"{domains} 个学科、{topics} 个专题", zh)
    if "机器学习新增 447 条" not in zh:
        zh = re.sub(r"^(\*\*数据说明：\*\*.*)$",
                    r"\1 机器学习新增 447 条原创术语、19 个专题，已同步纳入 Markdown、PDF 和搜索索引。",
                    zh, count=1, flags=re.M)
    put("README.zh-CN.md", zh)
    changelog = read("CHANGELOG.md")
    if "Machine Learning glossary publication" not in changelog:
        addition = (f"\n## Machine Learning glossary publication — 2026-11-16\n\n"
                    f"- Indexed 447 Machine Learning terms in 19 chapters with Markdown and PDF.\n"
                    f"- Expanded search to {terms:,} terms, {domains} domains and {topics} topics.\n")
        put("CHANGELOG.md", changelog.replace("# Changelog\n", "# Changelog\n" + addition, 1))

def main():
    patch_code()
    terms, domains, topics = update_index()
    documentation(terms, domains, topics)
    print(f"Machine Learning indexed: {terms:,} terms; {domains} subjects; {topics} topics")

if __name__ == "__main__":
    main()
