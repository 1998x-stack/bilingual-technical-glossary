"""Machine Learning Batch 01: 25 deep articles in canonical glossary order."""
import math
import unittest
from pathlib import Path

from scripts.verify_machine_learning_wiki import ROOT, source_terms, validate


class MachineLearningWikiBatch01Test(unittest.TestCase):
    def test_corpus_mapping_and_all_pages(self):
        self.assertGreaterEqual(validate(ROOT), 25)
        self.assertEqual(len(source_terms(ROOT)), 447)

    def test_first_batch_crosses_chapter_boundary(self):
        t = source_terms(ROOT)
        self.assertEqual([x["chapter"] for x in t[:25]], [1] * 24 + [2])
        self.assertEqual(t[24]["en"], "Dataset")

    def test_review_ledger_unattested(self):
        import json
        ledger = json.loads((ROOT / "wiki/reviews/machine-learning.json").read_text("utf-8"))
        self.assertGreaterEqual(len(ledger["articles"]), 25)
        self.assertEqual({x["status"] for x in ledger["articles"][:25]}, {"pending"})
        self.assertTrue(all(not x.get("reviewer") for x in ledger["articles"][:25]))

    def test_independent_math_examples(self):
        cases = {
            1: ("75%", 3 / 4),
            4: ("0.805", (-math.log(0.8) - math.log(0.25)) / 2),
            5: ("SSE=4", 4),
            9: ("1.2", 1 - 0.1 * (-2)),
            12: ("0.249%", 20000 / 8020000 * 100),
            15: ("15", 5 * 3),
            17: ("0.625", 0.5 / 0.8),
            20: ("8/3", ((2 - 4) ** 2 + (4 - 4) ** 2 + (6 - 4) ** 2) / 3),
            23: ("0.6,0.8", 3 / 5),
            25: ("240", 1200 * .2),
        }
        for index, (result, expected) in cases.items():
            matching = sorted((ROOT / "wiki/machine-learning").glob(f"{index:03d}-*.md"))
            self.assertEqual(len(matching), 1)
            content = matching[0].read_text("utf-8")
            self.assertIn(result, content)
            self.assertTrue(math.isfinite(expected))


if __name__ == "__main__":
    unittest.main()
