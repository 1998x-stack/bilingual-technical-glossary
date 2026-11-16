"""Regression tests for the curated discrete-mathematics publication."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "discrete-mathematics"

class DiscreteMathematicsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data" / "terms.json").read_text(encoding="utf8"))
        cls.rows = [t for t in cls.data if t["category"] == SLUG]

    def test_coverage(self):
        self.assertEqual(len(self.rows), 324)
        self.assertEqual(len(set(t["chapter"] for t in self.rows)), 16)
        self.assertEqual(len(set(t["topic"] for t in self.rows)), 16)

    def test_curated_source_matches_index(self):
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        from render_discrete_mathematics_pdf import load_terms
        self.assertEqual(self.rows, load_terms())

    def test_core_foundations(self):
        english = {t["en"] for t in self.rows}
        for term in ("Proof by Contradiction", "Equivalence Relation",
                     "Inclusion–Exclusion Principle", "Pigeonhole Principle",
                     "Euler's Formula for Planar Graphs", "Chinese Remainder Theorem",
                     "NP-Completeness"):
            self.assertIn(term, english)

    def test_publication_and_pages_mirrors(self):
        for folder, name in (("glossaries", f"{SLUG}.md"),
                             ("pdf", f"{SLUG}.pdf")):
            src = ROOT / folder / name
            site = ROOT / "docs" / folder / name
            self.assertTrue(src.is_file())
            self.assertEqual(src.read_bytes(), site.read_bytes())

if __name__ == "__main__":
    unittest.main()
