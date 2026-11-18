"""Machine Learning Batch 03: 25 published draft articles 051-075."""
import json
import math
import re
import unittest
from scripts.verify_machine_learning_wiki import ROOT, source_terms, validate


class MLBatch03Tests(unittest.TestCase):
    def test_source_order_and_batch_progress(self):
        terms = source_terms(ROOT)
        self.assertEqual(len(terms), 447)
        self.assertEqual([t["n"] for t in terms[50:75]], list(range(51, 76)))
        self.assertEqual([t["chapter"] for t in terms[50:75]], [2] * 2 + [3] * 23)
        self.assertEqual(terms[50]["en"], "Outlier")
        self.assertEqual(terms[74]["en"], "TF–IDF")
        self.assertGreaterEqual(validate(ROOT), 75)

    def test_mirror_sections_questions_references(self):
        m = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        self.assertGreaterEqual(m["readyArticles"], 75)
        self.assertGreaterEqual(m["readyInPr"], 75)
        for t in m["terms"][50:75]:
            with self.subTest(term=t["n"]):
                self.assertEqual(t["batch"], 3)
                self.assertTrue(t["ready"])
                src = ROOT / "wiki/machine-learning" / t["file"]
                mirror = ROOT / "docs/wiki/machine-learning" / t["file"]
                self.assertTrue(src.is_file())
                self.assertEqual(src.read_bytes(), mirror.read_bytes())
                text = src.read_text("utf-8")
                self.assertGreaterEqual(len(text), 1100)
                self.assertIn(t["en"], text.splitlines()[0])
                self.assertIn(t["zh"], text.splitlines()[0])
                for section in ("核心定义", "形象理解", "技术原理与核心内容",
                                "工程实践与设计权衡", "关联知识与易混辨析",
                                "中等难度面试题", "中等难度考试题", "权威来源"):
                    self.assertIn(section, text)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*问：", text, re.M)), 2)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*题：", text, re.M)), 2)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)]+\)", text)), 2)
                self.assertNotIn("BATCH-03", text)

    def test_index_is_additive_and_reviews_not_faked(self):
        m = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        index = json.loads((ROOT / "docs/data/wiki-index.json").read_text("utf-8"))["articles"]
        ledger = json.loads((ROOT / "wiki/reviews/machine-learning.json").read_text("utf-8"))["articles"]
        ml = [x for x in index if x["category"] == "machine-learning"]
        self.assertGreaterEqual(len(ml), 75)
        self.assertGreaterEqual(len(index), 142 + 332 + 75)
        self.assertGreaterEqual(len(ledger), 75)
        self.assertEqual([x["path"] for x in ml[:75]],
                         ["wiki/machine-learning/" + t["file"] for t in m["terms"][:75]])
        self.assertTrue(all(x["status"] == "pending" and not x.get("reviewer")
                            for x in ledger[:75]))

    def test_independent_numeric_examples(self):
        self.assertEqual(sorted(abs(x - 2) for x in [1, 2, 2, 3, 12])[2], 1)
        self.assertAlmostEqual((.9 - .5) / (1 - .5), .8)             # 052 kappa
        self.assertEqual(1000 - 40, 960)                            # 053 cleaning
        self.assertEqual((1 + 3 + 8) / 3, 4)                         # 059 impute
        self.assertAlmostEqual(10 / math.sqrt(200 / 3), math.sqrt(3 / 2), places=10)  # 060 exact identity
        self.assertEqual((25 - 10) / (30 - 10), .75)                 # 062 min max
        self.assertEqual((98 - 10) / (14 - 6), 11)                   # 063 robust
        self.assertAlmostEqual((2 * .5 + 3 * .2) / (2 + 3), .32)    # 066 target
        self.assertEqual(math.comb(5, 2) - 1, 9)                   # 069 degree 2
        self.assertEqual((4**1 - 1) / 1, 3)                         # 072 Box-Cox
        self.assertEqual(13 % 8, 21 % 8)                            # 073 collision
        self.assertAlmostEqual(math.log(10 / 2) + 1, 2.609438, places=6)  # 075 rounded IDF


if __name__ == "__main__":
    unittest.main()
