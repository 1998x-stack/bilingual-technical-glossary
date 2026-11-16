"""Signal Processing glossary regression checks."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class SignalProcessingTests(unittest.TestCase):
 def test_index_count_and_core_terms(self):
  terms=json.loads((ROOT/'data/terms.json').read_text(encoding='utf8'))
  records=[r for r in terms if r['category']=='signal-processing']
  self.assertEqual(len(records),295)
  self.assertEqual(len({r['chapter'] for r in records}),18)
  source=(ROOT/'data/signal-processing.tsv').read_text(encoding='utf8').splitlines()
  self.assertEqual(sum(bool(s.strip()) and not s.startswith('# ') for s in source),295)
  known={r['en'] for r in records}
  for name in ('Discrete Fourier Transform','Fast Fourier Transform','Power Spectral Density'):
   self.assertIn(name,known)
 def test_publications_mirrored(self):
  for a,b in [('glossaries/signal-processing.md','docs/glossaries/signal-processing.md'),
              ('pdf/signal-processing.pdf','docs/pdf/signal-processing.pdf')]:
   left,right=ROOT/a,ROOT/b
   self.assertTrue(left.is_file() and right.is_file())
   self.assertEqual(left.read_bytes(),right.read_bytes())
  self.assertTrue((ROOT/'pdf/signal-processing.pdf').read_bytes().startswith(b'%PDF-'))

if __name__=='__main__': unittest.main()
