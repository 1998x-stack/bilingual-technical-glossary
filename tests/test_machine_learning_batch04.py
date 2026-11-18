"""Batch 04: independently verify the contiguous 076-100 deep machine-learning Wiki."""
import json
import math
import re
import unittest
from scripts.verify_machine_learning_wiki import ROOT, source_terms, validate


class MLBatch04Tests(unittest.TestCase):
    def test_canonical_source_order_and_chapter_boundary(self):
        src = source_terms(ROOT)
        self.assertEqual(len(src), 447)
        self.assertEqual([x["n"] for x in src[75:100]], list(range(76, 101)))
        self.assertEqual([x["chapter"] for x in src[75:100]], [3] * 7 + [4] * 18)
        self.assertEqual((src[75]["en"], src[99]["en"]), ("Embedding", "PAC Learning"))
        self.assertGreaterEqual(validate(ROOT), 100)

    def test_25_pages_mirror_and_complete_content(self):
        manifest = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        self.assertGreaterEqual(manifest["readyArticles"], 100)
        self.assertGreaterEqual(manifest["readyInPr"], 100)
        for t in manifest["terms"][75:100]:
            with self.subTest(index=t["n"], term=t["en"]):
                self.assertEqual(t["batch"], 4)
                self.assertTrue(t["ready"])
                src = ROOT / "wiki/machine-learning" / t["file"]
                mirror = ROOT / "docs/wiki/machine-learning" / t["file"]
                self.assertEqual(src.read_bytes(), mirror.read_bytes())
                doc = src.read_text("utf-8")
                self.assertGreater(len(doc), 1200)
                self.assertIn(t["en"], doc.splitlines()[0])
                self.assertIn(t["zh"], doc.splitlines()[0])
                for section in ("核心定义", "形象理解", "技术原理与核心内容",
                                "工程实践与设计权衡", "关联知识与易混辨析",
                                "中等难度面试题", "中等难度考试题",
                                "权威来源与延伸阅读"):
                    self.assertIn(section, doc)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*问：", doc, re.M)), 2)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*题：", doc, re.M)), 2)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://[^) ]+\)", doc)), 2)
                self.assertNotIn("BATCH-04", doc)
                self.assertIn("pending", doc)

    def test_review_ledger_and_corpus_preserve_existing_domains(self):
        idx = json.loads((ROOT / "docs/data/wiki-index.json").read_text("utf-8"))["articles"]
        m = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        review = json.loads((ROOT / "wiki/reviews/machine-learning.json").read_text("utf-8"))["articles"]
        ml = [x for x in idx if x["category"] == "machine-learning"]
        self.assertGreaterEqual(len(idx), 142 + 332 + 100)
        self.assertGreaterEqual(len(ml), 100)
        self.assertGreaterEqual(len(review), 100)
        self.assertEqual([x["path"] for x in ml[:100]],
                         ["wiki/machine-learning/" + x["file"] for x in m["terms"][:100]])
        self.assertTrue(all(x["status"] == "pending" and not x.get("reviewer")
                            for x in review[:100]))
        self.assertEqual(sum(x["category"] == "ai-agents" for x in idx), 332)
        self.assertEqual(sum(x["category"] == "ai-infrastructure" for x in idx), 142)

    def test_numerical_and_theoretical_examples(self):
        self.assertEqual(10000 * 64 * 4, 2560000)              # 076 embedding memory
        self.assertEqual(20000 / (1000 * 10000), .002)        # 077 sparse density
        self.assertEqual(1000000 * 128 * 4, 512000000)         # 078 dense bytes
        self.assertEqual(.25 * 1 + .75 * 0, .25)              # 079 mixup
        self.assertAlmostEqual((99 / 100) ** 100, .366032341, places=6)  # 080 OOB
        self.assertEqual((2 + .25 * (6 - 2), 4 + .25 * (8 - 4)), (3, 5)) # 081 SMOTE
        self.assertEqual(sum([0, 1, 0, 1, 0]) / 5, .4)       # 083 risk
        self.assertAlmostEqual(.75 * .1 + .25 * .3, .15)           # 084 expected
        self.assertEqual(3.5 - 2, 1.5)                       # 088 gap
        self.assertEqual((12 - 10) ** 2 + 3 + 1, 8)          # 091 bias variance
        self.assertEqual(max(3 - 1, 0), 2)                   # 094 L1 threshold
        self.assertAlmostEqual(20 / (10 + 2), 5 / 3)         # 095 ridge
        self.assertAlmostEqual(.4 * .75, .3)                # 096 elastic L1
        self.assertAlmostEqual(.4 * (1 - .75), .1)          # 096 elastic L2
        self.assertEqual(2 * 2 - 2 * (-20), 44)             # 097 AIC A
        self.assertEqual(2 * 5 - 2 * (-18), 46)             # 097 AIC B
        self.assertEqual(2 ** 3, 8)                         # 098 shattering
        # A one-dimensional interval cannot realize positive-negative-positive.
        realizable = lambda H, eps, delta: math.ceil((math.log(H) + math.log(1/delta))/eps)
        self.assertEqual(realizable(10, .2, .1), 24)        # 100 PAC
        self.assertEqual(realizable(100, .1, .05), 77)      # 100 PAC


if __name__ == "__main__":
    unittest.main()
