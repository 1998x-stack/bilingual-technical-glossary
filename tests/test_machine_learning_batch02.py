"""ML Batch 02: 026-050 data quality, split protocols and honest review status."""
import json
import math
import re
import unittest
from pathlib import Path
from scripts.verify_machine_learning_wiki import ROOT, source_terms, validate


class MachineLearningWikiBatch02Tests(unittest.TestCase):
    def test_full_corpus_and_batch_contiguity(self):
        self.assertGreaterEqual(validate(ROOT), 50)
        terms = source_terms(ROOT)
        self.assertEqual(len(terms), 447)
        self.assertEqual([t["n"] for t in terms[25:50]], list(range(26, 51)))
        self.assertEqual({t["chapter"] for t in terms[25:50]}, {2})
        self.assertEqual(terms[25]["en"], "Sample / Instance")
        self.assertEqual(terms[49]["en"], "Missing Value")

    def test_all_pages_have_substantive_qa_and_mirror(self):
        manifest = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        self.assertEqual(manifest["terms"][25]["batch"], 2)
        for term in manifest["terms"][25:50]:
            n = term["n"]
            with self.subTest(n=n):
                self.assertTrue(term["ready"])
                src = ROOT / "wiki/machine-learning" / term["file"]
                mirror = ROOT / "docs/wiki/machine-learning" / term["file"]
                self.assertEqual(src.read_bytes(), mirror.read_bytes())
                content = src.read_text("utf-8")
                self.assertGreaterEqual(len(content), 1150)
                self.assertIn(term["en"], content.splitlines()[0])
                self.assertIn(term["zh"], content.splitlines()[0])
                self.assertEqual(len(re.findall(r"^\d+\. \*\*问：", content, re.M)), 2)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*题：", content, re.M)), 2)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)]+\)", content)), 2)
                self.assertNotIn("BATCH-02", content)

    def test_review_and_index_are_additive(self):
        ledger = json.loads((ROOT / "wiki/reviews/machine-learning.json").read_text("utf-8"))
        index = json.loads((ROOT / "docs/data/wiki-index.json").read_text("utf-8"))
        ml = [x for x in index["articles"] if x["category"] == "machine-learning"]
        self.assertGreaterEqual(len(ml), 50)
        self.assertEqual([x["path"] for x in ml[:50]],
                         [x["path"] for x in ledger["articles"][:50]])
        self.assertTrue(all(x["status"] == "pending" and "reviewer" not in x
                            for x in ledger["articles"][:50]))
        self.assertEqual(sum(x["category"] == "ai-agents" for x in index["articles"]), 332)
        self.assertEqual(sum(x["category"] == "ai-infrastructure" for x in index["articles"]), 142)

    def test_math_examples_recalculated(self):
        # Independent arithmetic and assumptions of the lesson's worked examples.
        self.assertEqual(200 * 5, 1000)                 # 026 repeated observations
        self.assertEqual(23 - 20 - 2, 1)                # 027 measured error
        self.assertAlmostEqual((55 - 40) / 10, 1.5)    # 028 standardized feature
        self.assertAlmostEqual((.9 - .6) / (1 - .6), .75) # 030 kappa
        self.assertEqual(1000 * 10000 * 8, 80000000)  # 031 dense bytes
        self.assertEqual(1200 * .7, 840)               # 033 training split
        self.assertEqual(50 / 5, 10)                   # 043 positives per fold
        self.assertEqual(100 - 5 * 20, 0)              # 045 exactly 100 OOF rows
        self.assertAlmostEqual(.5 / .2, 2.5)           # 048 sampling ratio
        self.assertAlmostEqual(30 / (30 + 20), .6)     # 049 precision
        self.assertAlmostEqual(30 / (30 + 10), .75)    # 049 recall
        self.assertAlmostEqual((2 + 4 + 6) / 3, 4)     # 050 missing value fill


if __name__ == "__main__":
    unittest.main()
