import json,unittest
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/terms.json').read_text(encoding='utf8'))
class CatalogTests(unittest.TestCase):
 def test_reconciled_domains(self):
  expected={'operating-systems':(396,18),'sql-database':(394,13),'python':(429,16),'junior-high-mathematics':(400,15)}
  for slug,(count,chapters) in expected.items():
   rows=[t for t in DATA if t['category']==slug]
   self.assertEqual(len(rows),count,slug)
   self.assertEqual(len({t['chapter'] for t in rows}),chapters,slug)
 def test_parallel_computing_index(self):
  rows=[t for t in DATA if t['category']=='parallel-computing']
  self.assertEqual(len(rows),205)
  self.assertEqual(len({t['chapter'] for t in rows}),12)
  self.assertIn('Parallel Computing',{t['en'] for t in rows})
 def test_compiler_domain(self):
  self.assertIn('compiler-principles',{t['category'] for t in DATA})
  self.assertGreaterEqual(len({t['category'] for t in DATA}),9)
 def test_machine_learning_volume(self):
  ml=[t for t in DATA if t['category']=='machine-learning']
  self.assertEqual(len(ml),447)
  self.assertEqual(len(set(t['chapter'] for t in ml)),19)
 def test_data_structures_domain(self):
  rows=[t for t in DATA if t['category']=='data-structures']
  self.assertEqual(len(rows),352)
  self.assertEqual(len({t['chapter'] for t in rows}),14)
 def test_high_school_mathematics(self):
  rows=[t for t in DATA if t['category']=='high-school-mathematics']
  self.assertEqual(len(rows),351)
  self.assertEqual(len(set(t['chapter'] for t in rows)),16)
  self.assertIn('derivative',{t['en'] for t in rows})
 def test_university_mathematics(self):
  records=[x for x in DATA if x['category']=='university-mathematics']
  self.assertEqual(len(records),627)
  self.assertEqual(len(set(x['chapter'] for x in records)),17)
  self.assertTrue((ROOT/'sources/university-mathematics.html').is_file())
  self.assertTrue((ROOT/'pdf/university-mathematics.pdf').is_file())
 def test_required_fields(self):
  for t in DATA:
   for field in ['category','chapter','topic','en','zh','abbr','definition']:
    self.assertIn(field,t)
    if field!='abbr':self.assertTrue(str(t[field]).strip())
 def test_consistent_chapter_titles(self):
  chapters=defaultdict(set)
  for t in DATA:chapters[(t['category'],t['chapter'])].add(t['topic'])
  self.assertTrue(all(len(values)==1 for values in chapters.values()))
 def test_content_search_cases(self):
  text='\n'.join(t['en']+' '+t['zh'] for t in DATA).lower()
  for phrase in ['transformer','markov','linear','gradient','agent','gpu','缓存']:
   self.assertIn(phrase,text)
 def test_publication_files_exist(self):
  for slug in set(t['category'] for t in DATA):
   self.assertTrue((ROOT/'pdf'/f'{slug}.pdf').exists())
   self.assertTrue((ROOT/'glossaries'/f'{slug}.md').exists())
if __name__=='__main__':unittest.main()
