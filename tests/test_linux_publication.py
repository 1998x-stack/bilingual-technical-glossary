import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class LinuxGlossaryTests(unittest.TestCase):
    def test_394_indexed_terms_and_16_chapters(self):
        rows = json.loads((ROOT/'data/terms.json').read_text(encoding='utf-8'))
        terms = [t for t in rows if t['category']=='linux']
        self.assertEqual(len(terms),394)
        self.assertEqual(len({t['chapter'] for t in terms}),16)
        md=(ROOT/'glossaries/linux.md').read_text(encoding='utf-8')
        self.assertEqual(len([s for s in md.splitlines() if s.startswith('| ') and s.count('|')>=4 and not s.startswith('| English /') and not s.startswith('|---')]),394)
        self.assertEqual(md.count('- **'),18)
    def test_publication_mirrors(self):
        for d,f in [('glossaries','linux.md'),('pdf','linux.pdf')]:
            self.assertEqual((ROOT/d/f).read_bytes(),(ROOT/'docs'/d/f).read_bytes())
        self.assertTrue((ROOT/'pdf/linux.pdf').read_bytes().startswith(b'%PDF-'))
if __name__=='__main__':
    unittest.main()
