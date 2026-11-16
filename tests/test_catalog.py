import json,unittest
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/terms.json').read_text(encoding='utf8'))
class CatalogTests(unittest.TestCase):
 def test_nine_domains(self):
  self.assertEqual(len(set(t['category'] for t in DATA)),9)
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
  for phrase in ['transformer','markov','linear','gradient','agent','gpu','缓存','微积分','integral']:
   self.assertIn(phrase,text)
 def test_publication_files_exist(self):
  for slug in set(t['category'] for t in DATA):
   self.assertTrue((ROOT/'pdf'/f'{slug}.pdf').exists())
   self.assertTrue((ROOT/'glossaries'/f'{slug}.md').exists())
if __name__=='__main__':unittest.main()
