#!/usr/bin/env python3
"""Synchronize the authored Data Structures handbook with the searchable atlas."""
from collections import Counter
from pathlib import Path
import csv
import json
import re
import shutil

R=Path(__file__).resolve().parents[1]
S="data-structures"
FIELDS=["category","chapter","topic","en","zh","abbr","definition"]

def read(p):
    return (R/p).read_text(encoding="utf-8")

def write(p,s):
    p=R/p
    p.parent.mkdir(parents=True,exist_ok=True)
    if not p.exists() or p.read_text(encoding="utf-8")!=s:
        p.write_text(s,encoding="utf-8")

def extract():
    out=[]
    chapter=0
    topic=""
    for line in read("glossaries/data-structures.md").splitlines():
        m=re.match(r"## (\d{2}) · (.+?) / ",line)
        if m:
            chapter=int(m.group(1));topic=m.group(2);continue
        if line.startswith("## 易混淆概念"):
            chapter=0;continue
        if chapter==0 or not line.startswith("| ") or line.startswith("| English") or line.startswith("|---"):
            continue
        cells=[x.strip() for x in line.strip().strip("|").split("|")]
        assert len(cells)==3,line
        en,zh,definition=cells
        abbr=re.search(r"\(([A-Z][A-Z0-9+./_-]{1,18})\)",en)
        out.append(dict(category=S,chapter=chapter,topic=topic,en=en,zh=zh,abbr=abbr.group(1) if abbr else "",definition=definition))
    assert len(out)==352 and len({x["chapter"] for x in out})==14
    assert len({(x["chapter"],x["en"].lower(),x["zh"]) for x in out})==352
    return out

def update_readmes(n,total,topics):
    for path,is_cn in [("README.md",False),("README.zh-CN.md",True)]:
        s=read(path)
        row=("| 数据结构 / Data Structures | 352 | 14 | [阅读](glossaries/data-structures.md) | [下载](pdf/data-structures.pdf) |"
             if is_cn else
             "| Data Structures | 数据结构 | 352 | 14 | [Read](glossaries/data-structures.md) | [Download](pdf/data-structures.pdf) |")
        marker="| **合计** |" if is_cn else "| **Total** |"
        if row not in s:
            assert marker in s
            s=s.replace(marker,row+"\n"+marker,1)
        if is_cn:
            s=re.sub(r"(?m)^\| \*\*合计\*\* \|[^\n]*$",f"| **合计** | **{total:,}** | **{topics}** | | |",s)
            s=re.sub(r"\d+ 个学科、\d+ 个专题",f"{n} 个学科、{topics} 个专题",s)
        else:
            s=re.sub(r"(?m)^\| \*\*Total\*\* \|[^\n]*$",f"| **Total** | **{n} domains** | **{total:,}** | **{topics}** | | |",s)
            s=re.sub(r"- \*\*\d+ topic chapters:\*\*",f"- **{topics} topic chapters:**",s)
        write(path,s)

def main():
    fresh=extract()
    terms=json.loads(read("data/terms.json"))
    first=next((i for i,t in enumerate(terms) if t.get("category")==S),len(terms))
    terms=[t for t in terms if t.get("category")!=S]
    terms[first:first]=fresh
    assert len(terms)==len({(x["category"],x["chapter"],x["en"].casefold(),x["zh"]) for x in terms})
    write("data/terms.json",json.dumps(terms,ensure_ascii=False,indent=2)+"\n")
    write("docs/data/terms.json",json.dumps(terms,ensure_ascii=False,separators=(",",":")))
    with (R/"data/terms.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,extrasaction='ignore');w.writeheader();w.writerows(terms)
    catalog=json.loads(read("docs/data/catalog.json"))
    if not any(x["slug"]==S for x in catalog):
        catalog.append(dict(slug=S,en="Data Structures",zh="数据结构",description="Arrays, linked lists, hashing, trees, graphs and advanced structures",icon="network",count=352,topics=14))
    counts=Counter(x["category"] for x in terms)
    topics={c:{(x["chapter"],x["topic"]) for x in terms if x["category"]==c} for c in counts}
    assert {x["slug"] for x in catalog}==set(counts)
    for item in catalog:
        item["count"]=counts[item["slug"]];item["topics"]=len(topics[item["slug"]])
    write("docs/data/catalog.json",json.dumps(catalog,ensure_ascii=False,indent=2)+"\n")
    build=read("scripts/build.py")
    if "('data-structures'," not in build and '("data-structures",' not in build:
        needle="\n]\nMETA="
        assert needle in build
        row="\n ('data-structures','Data Structures','数据结构','Arrays, lists, hashing, trees, graphs and advanced structures','network'),"
        build=build.replace(needle,row+needle,1)
    if "if slug == 'data-structures': continue" not in build and "if slug=='data-structures':continue" not in build:
        build=build.replace(" for slug in META:\n"," for slug in META:\n  if slug == 'data-structures': continue  # Preserve authored Markdown and appendix.\n",1)
    write("scripts/build.py",build)
    verify=read("scripts/verify.py")
    verify=re.sub(r"check\(len\(CATALOG\)==\d+,'Expected [^']*subject categories'\)",
                  "check(len(CATALOG)==len(set(x['category'] for x in TERMS)),'Catalog and data categories differ')",verify)
    write("scripts/verify.py",verify)
    test=read("tests/test_catalog.py")
    test=re.sub(r"self.assertEqual\(len\(set\(t\['category'\] for t in DATA\)\),\s*\d+\)",
                f"self.assertEqual(len(set(t['category'] for t in DATA)),{len(catalog)})",test)
    if "def test_data_structures_domain(" not in test:
        block=(" def test_data_structures_domain(self):\n"
               "  rows=[t for t in DATA if t['category']=='data-structures']\n"
               "  self.assertEqual(len(rows),352)\n"
               "  self.assertEqual(len({t['chapter'] for t in rows}),14)\n")
        pos=test.find(" def test_required_fields(self):")
        if pos<0:pos=test.index("if __name__")
        test=test[:pos]+block+test[pos:]
    write("tests/test_catalog.py",test)
    for p in ("site/app.js","docs/app.js"):
        js=read(p)
        if "'#2c8c7b'" not in js:
            js=re.sub(r"(const SUBJECT_COLORS = \[[^\n]*?)(\];)",r"\1,'#2c8c7b'\2",js,count=1)
        if "'◇'" not in js:
            js=re.sub(r"(const SUBJECT_GLYPHS = \[[^\n]*?)(\];)",r"\1,'◇'\2",js,count=1)
        write(p,js)
    update_readmes(len(catalog),len(terms),sum(x["topics"] for x in catalog))
    shutil.copyfile(R/"glossaries/data-structures.md",R/"docs/glossaries/data-structures.md")
    shutil.copyfile(R/"pdf/data-structures.pdf",R/"docs/pdf/data-structures.pdf")
    print("PASS: Data Structures",len(fresh),"entries; indexed total",len(terms))

if __name__=="__main__":
    main()
