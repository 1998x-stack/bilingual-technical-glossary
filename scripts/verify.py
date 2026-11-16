#!/usr/bin/env python3
"""Fail-fast validation; no external dependencies."""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,sys
ROOT=Path(__file__).resolve().parents[1]
TERMS=json.loads((ROOT/'data/terms.json').read_text(encoding='utf8'))
CATALOG=json.loads((ROOT/'docs/data/catalog.json').read_text(encoding='utf8'))
REQUIRED=['category','chapter','topic','en','zh','abbr','definition']
fail=[]
def check(test,message):
 if not test:fail.append(message)
check(len(CATALOG)==len({t['category'] for t in TERMS}), 'Catalog and term category sets differ')
check(len(TERMS)>=2600,'Dataset unexpectedly truncated')
seen=set();topics={};slugs={c['slug'] for c in CATALOG}
check(slugs=={t['category'] for t in TERMS},'Catalog category slugs differ from terms')
for i,r in enumerate(TERMS):
 check(all(k in r for k in REQUIRED),f'Missing field row {i}')
 if any(k not in r for k in REQUIRED):continue
 check(all(str(r[k]).strip() for k in ('en','zh','definition','topic')),f'Empty required field row {i}')
 check(r['category'] in slugs,f'Unknown category {r["category"]} row {i}')
 check(isinstance(r['chapter'],int) and r['chapter']>0,f'Invalid chapter {i}')
 key=(r['category'],r['chapter'],r['en'].casefold().strip(),r['zh'].strip())
 check(key not in seen,f'Duplicate row {i} {key}')
 seen.add(key)
 topic_key=(r['category'],r['chapter'])
 check(topic_key not in topics or topics[topic_key]==r['topic'],f'Inconsistent topic for {topic_key}')
 topics[topic_key]=r['topic']
counts=Counter(r['category'] for r in TERMS)
check(counts.get('junior-high-mathematics')==400,'Junior mathematics index must contain 400 entries')
check(len({r['chapter'] for r in TERMS if r['category']=='junior-high-mathematics'})==15,'Junior mathematics must have 15 chapters')
for cat in CATALOG:
 slug=cat['slug'];check(cat['count']==counts[slug],f'Count mismatch: {slug}')
 check(cat['topics']==len(set(t['topic'] for t in TERMS if t['category']==slug)),f'Topic count mismatch: {slug}')
 md=ROOT/'glossaries'/f'{slug}.md';pdf=ROOT/'pdf'/f'{slug}.pdf'
 check(md.is_file() and md.stat().st_size>1000,f'Missing Markdown {slug}')
 check(pdf.is_file() and pdf.stat().st_size>10000,f'Missing PDF {slug}')
 check((ROOT/'docs/glossaries'/md.name).is_file(),f'Missing Pages Markdown {slug}')
 check((ROOT/'docs/pdf'/pdf.name).is_file(),f'Missing Pages PDF {slug}')
 if pdf.is_file():
  with pdf.open('rb') as f:check(f.read(5)==b'%PDF-',f'Invalid PDF header {slug}')
  if slug=='junior-high-mathematics' and (ROOT/'docs/pdf'/pdf.name).is_file():check(pdf.read_bytes()==(ROOT/'docs/pdf'/pdf.name).read_bytes(),'Math PDF copies differ')
site=json.loads((ROOT/'docs/data/terms.json').read_text(encoding='utf8'))
check(site==TERMS,'Pages search index differs from source data')
with (ROOT/'data/terms.csv').open(encoding='utf8',newline='') as f:
 rows=list(csv.DictReader(f));check(len(rows)==len(TERMS),'CSV count differs from JSON')
for path in ['docs/index.html','docs/styles.css','docs/app.js','docs/favicon.svg','site/index.html','site/styles.css','site/app.js','README.md','README.zh-CN.md','AGENTS.md','.github/workflows/pages.yml']:
 check((ROOT/path).is_file(),f'Missing required file: {path}')
if fail:
 print('FAIL —',len(fail),'issues');[print(' -',x) for x in fail[:60]];sys.exit(1)
print(f'PASS — {len(TERMS):,} terms · {len(CATALOG)} domains · {len(topics)} topics · Markdown/PDF/CSV/JSON/Pages consistent')
