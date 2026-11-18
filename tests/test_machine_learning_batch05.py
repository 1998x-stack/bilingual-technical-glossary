"""ML Wiki Batch 05: 101-125 theory, distribution shift, classification and regression."""
import json
import math
import re
import unittest
from scripts.verify_machine_learning_wiki import ROOT, source_terms, validate


class MLBatch05Tests(unittest.TestCase):
    def test_canonical_source_and_chapter_boundary(self):
        src = source_terms(ROOT)
        self.assertEqual(len(src), 447)
        self.assertEqual([x["n"] for x in src[100:125]], list(range(101, 126)))
        self.assertEqual([x["chapter"] for x in src[100:125]], [4] * 7 + [5] * 18)
        self.assertEqual(src[100]["en"], "Sample Complexity")
        self.assertEqual(src[124]["en"], "Decision Boundary")
        self.assertGreaterEqual(validate(ROOT), 125)

    def test_all_pages_have_verified_mirrors_and_qa(self):
        manifest = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        self.assertGreaterEqual(manifest["readyArticles"], 125)
        self.assertGreaterEqual(manifest["readyInPr"], 125)
        for term in manifest["terms"][100:125]:
            with self.subTest(n=term["n"], term=term["en"]):
                self.assertEqual(term["batch"], 5)
                self.assertTrue(term["ready"])
                original = ROOT / "wiki/machine-learning" / term["file"]
                published = ROOT / "docs/wiki/machine-learning" / term["file"]
                self.assertTrue(original.is_file())
                self.assertEqual(original.read_bytes(), published.read_bytes())
                content = original.read_text("utf-8")
                self.assertGreaterEqual(len(content), 1275)
                self.assertIn(term["en"], content.splitlines()[0])
                self.assertIn(term["zh"], content.splitlines()[0])
                for section in (
                    "核心定义", "形象理解", "技术原理与核心内容",
                    "工程实践与设计权衡", "关联知识与易混辨析",
                    "中等难度面试题", "中等难度考试题", "权威来源与延伸阅读"
                ):
                    self.assertIn(section, content)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*问：", content, re.M)), 2)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*题：", content, re.M)), 2)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://[^) ]+\)", content)), 2)
                self.assertIn("pending", content)
                self.assertNotIn("BATCH-05", content)

    def test_review_ledger_and_cross_domain_index(self):
        index = json.loads((ROOT / "docs/data/wiki-index.json").read_text("utf-8"))["articles"]
        manifest = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        ledger = json.loads((ROOT / "wiki/reviews/machine-learning.json").read_text("utf-8"))["articles"]
        ml = [x for x in index if x["category"] == "machine-learning"]
        self.assertGreaterEqual(len(ml), 125)
        self.assertGreaterEqual(len(index), 142 + 332 + 125)
        self.assertEqual([x["path"] for x in ml[:125]],
                         ["wiki/machine-learning/" + x["file"] for x in manifest["terms"][:125]])
        self.assertTrue(all(x["status"] == "pending" and not x.get("reviewer")
                            for x in ledger[:125]))
        self.assertEqual(sum(x["category"] == "ai-infrastructure" for x in index), 142)
        self.assertEqual(sum(x["category"] == "ai-agents" for x in index), 332)
        self.assertIn("10.1162/089976602753284446",
                      (ROOT / "wiki/machine-learning/106-label-shift-prior-shift.md").read_text("utf-8"))

    def test_independent_numeric_and_theory_examples(self):
        # PAC finite-class realizable sufficient-sample bound.
        n = (math.log(20) + math.log(1 / .05)) / .1
        self.assertEqual(math.ceil(n), 60)                    # 101 sample complexity
        self.assertAlmostEqual((.24 - .18) / .24, .25)       # 102 learning curve
        self.assertAlmostEqual((.3 / .1), 3)                      # 105 covariate weight
        self.assertAlmostEqual(1 / (1 + .375), .727272727)  # 106 label-shift Bayes
        self.assertAlmostEqual(30 / 40, .75)               # 107 drift recall
        self.assertAlmostEqual((abs(3-2)+abs(6-4)) / 2, 1.5) # 108 regression MAE
        self.assertAlmostEqual(40 / (40+10), .8)            # 110 precision
        self.assertAlmostEqual(40 / (40+20), 2/3)           # 110 recall
        self.assertAlmostEqual(-math.log(.25), math.log(4)) # 111 cross-entropy
        self.assertAlmostEqual(1 / 6, .1666666667)         # 112 Hamming loss
        self.assertEqual(5 + 2*4 - 3*2, 7)                 # 114 linear prediction
        self.assertEqual(1 + 4 + 9, 14)                    # 115 residual sum squares
        self.assertAlmostEqual(12 / (8+2), 1.2)            # 116 Ridge
        self.assertEqual(max(4 - 1, 0), 3)                 # 117 Lasso soft threshold
        self.assertAlmostEqual(.6 * .25, .15)              # 118 Elastic Net
        self.assertAlmostEqual(-math.log(.8), .2231435513) # 119 log loss
        self.assertAlmostEqual(2 / (2+1), 2/3)             # 120 Softmax
        self.assertAlmostEqual(math.exp(math.log(4)), 4)         # 121 GLM
        self.assertAlmostEqual(math.exp(-2), .1353352832) # 122 Poisson
        self.assertAlmostEqual(.9 * (12-10), 1.8)          # 123 quantile
        self.assertEqual(2 * (5 - 1), 8)                   # 124 Huber
        self.assertAlmostEqual(math.log(.8 / .2), math.log(4)) # 125 boundary


if __name__ == "__main__":
    unittest.main()
