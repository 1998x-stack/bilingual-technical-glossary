#!/usr/bin/env python3
"""Fail-fast validation; no external dependencies."""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,sys
from corpus_integrity import csv_differences
ROOT=Path(__file__).resolve().parents[1]
TERMS=json.loads((ROOT/'data/terms.json').read_text(encoding='utf8'))
CATALOG=json.loads((ROOT/'docs/data/catalog.json').read_text(encoding='utf8'))
REQUIRED=['category','chapter','topic','en','zh','abbr','definition']
fail=[]
def check(test,message):
 if not test:fail.append(message)
check(len(CATALOG)==len({t['category'] for t in TERMS}),'Catalog does not cover all indexed domains')
check(len(TERMS)>=7554,'Dataset unexpectedly truncated')
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
for slug,expected in {'operating-systems':396,'sql-database':394,'python':429,'junior-high-mathematics':400,'parallel-computing':205}.items():
 check(counts[slug]==expected,f'Unexpected {slug} term count')
check(counts['university-mathematics']==627,'University Mathematics must have 627 terms')
check((ROOT/'sources/university-mathematics.html').is_file(),'University Mathematics source HTML missing')
check(counts['machine-learning']==447,'ML must have 447 terms')
check(sum(bool(x.get('notation')) for x in TERMS if x['category']=='calculus')==361,
      'Calculus notation values must not be silently dropped')
for cat in CATALOG:
 slug=cat['slug'];check(cat['count']==counts[slug],f'Count mismatch: {slug}')
 check(cat['topics']==len(set(t['topic'] for t in TERMS if t['category']==slug)),f'Topic count mismatch: {slug}')
 md=ROOT/'glossaries'/f'{slug}.md';pdf=ROOT/'pdf'/f'{slug}.pdf'
 check(md.is_file() and md.stat().st_size>1000,f'Missing Markdown {slug}')
 check(pdf.is_file() and pdf.stat().st_size>10000,f'Missing PDF {slug}')
 check((ROOT/'docs/glossaries'/md.name).is_file(),f'Missing Pages Markdown {slug}')
 check((ROOT/'docs/pdf'/pdf.name).is_file(),f'Missing Pages PDF {slug}')
 if md.is_file() and (ROOT/'docs/glossaries'/md.name).is_file():
  check(md.read_bytes()==(ROOT/'docs/glossaries'/md.name).read_bytes(),f'Markdown mirror differs: {slug}')
 if pdf.is_file() and (ROOT/'docs/pdf'/pdf.name).is_file():
  check(pdf.read_bytes()==(ROOT/'docs/pdf'/pdf.name).read_bytes(),f'PDF mirror differs: {slug}')
 if pdf.is_file():
  with pdf.open('rb') as f:check(f.read(5)==b'%PDF-',f'Invalid PDF header {slug}')
site=json.loads((ROOT/'docs/data/terms.json').read_text(encoding='utf8'))
check(site==TERMS,'Pages search index differs from source data')
check(sum(c['count'] for c in CATALOG)==len(TERMS),'Catalog total differs from indexed terms')
with (ROOT/'data/terms.csv').open(encoding='utf8',newline='') as f:
 reader=csv.DictReader(f)
 rows=list(reader)
 fail.extend(csv_differences(TERMS,reader.fieldnames,rows))
for path in ['docs/index.html','docs/styles.css','docs/app.js','docs/favicon.svg','site/index.html','site/styles.css','site/app.js','README.md','README.zh-CN.md','AGENTS.md','.github/workflows/pages.yml']:
 check((ROOT/path).is_file(),f'Missing required file: {path}')
for name in ['index.html','app.js','styles.css','favicon.svg']:
 source=ROOT/'site'/name
 mirror=ROOT/'docs'/name
 if source.is_file() and mirror.is_file():
  check(source.read_bytes()==mirror.read_bytes(),f'Site/Pages asset mismatch: {name}')
for name in ['README.md','README.zh-CN.md']:
 source=(ROOT/name).read_text(encoding='utf8')
 total=f'{len(TERMS):,}'
 check(total in source,f'{name} missing current indexed total')
if fail:
 print('FAIL —',len(fail),'issues');[print(' -',x) for x in fail[:60]];sys.exit(1)
print(f'PASS — {len(TERMS):,} terms · {len(CATALOG)} domains · {len(topics)} topics · Markdown/PDF/CSV/JSON/Pages consistent')
