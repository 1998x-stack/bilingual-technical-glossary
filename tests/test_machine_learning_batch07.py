"""Machine Learning Wiki Batch 07: 151–175, ensemble algorithms, SVM/kernels and neighbors."""
import json
import math
import re
import unittest

from scripts.verify_machine_learning_wiki import ROOT, source_terms, validate


class MachineLearningBatch07Tests(unittest.TestCase):
    def test_25_canonical_terms_and_chapter_transition(self):
        terms = source_terms(ROOT)
        self.assertEqual(len(terms), 447)
        self.assertEqual([x["n"] for x in terms[150:175]], list(range(151, 176)))
        self.assertEqual([x["chapter"] for x in terms[150:175]], [6] * 7 + [7] * 18)
        self.assertEqual(terms[150]["en"], "XGBoost")
        self.assertEqual(terms[174]["en"], "Cosine Similarity")
        self.assertGreaterEqual(validate(ROOT), 175)

    def test_two_mirrors_eight_sections_four_solved_questions_and_sources(self):
        manifest = json.loads(
            (ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8")
        )
        self.assertGreaterEqual(manifest["readyArticles"], 175)
        self.assertGreaterEqual(manifest["readyInPr"], 175)
        for term in manifest["terms"][150:175]:
            with self.subTest(term=term["n"], name=term["en"]):
                self.assertEqual(term["batch"], 7)
                self.assertTrue(term["ready"])
                canonical = ROOT / "wiki/machine-learning" / term["file"]
                mirror = ROOT / "docs/wiki/machine-learning" / term["file"]
                self.assertTrue(canonical.is_file())
                self.assertEqual(canonical.read_bytes(), mirror.read_bytes())
                text = canonical.read_text("utf-8")
                self.assertGreaterEqual(len(text), 1300)
                self.assertIn(term["en"], text.splitlines()[0])
                self.assertIn(term["zh"], text.splitlines()[0])
                for section in (
                    "核心定义", "形象理解", "技术原理与核心内容",
                    "工程实践与设计权衡", "关联知识与易混辨析",
                    "中等难度面试题", "中等难度考试题",
                    "权威来源与延伸阅读",
                ):
                    self.assertIn(section, text)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*问：", text, re.M)), 2)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*题：", text, re.M)), 2)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)\s]+\)", text)), 2)
                self.assertIn("pending", text)
                self.assertNotIn("BATCH-07", text)

    def test_index_cumulative_and_no_fabricated_expert_review(self):
        articles = json.loads((ROOT / "docs/data/wiki-index.json").read_text("utf-8"))["articles"]
        terms = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))["terms"]
        reviews = json.loads((ROOT / "wiki/reviews/machine-learning.json").read_text("utf-8"))["articles"]
        ml = [a for a in articles if a["category"] == "machine-learning"]
        self.assertGreaterEqual(len(articles), 142 + 332 + 175)
        self.assertGreaterEqual(len(ml), 175)
        self.assertGreaterEqual(len(reviews), 175)
        self.assertEqual(
            [a["path"] for a in ml[:175]],
            ["wiki/machine-learning/" + t["file"] for t in terms[:175]],
        )
        self.assertTrue(
            all(r["status"] == "pending" and not r.get("reviewer") for r in reviews[:175])
        )
        self.assertEqual(sum(a["category"] == "ai-infrastructure" for a in articles), 142)
        self.assertEqual(sum(a["category"] == "ai-agents" for a in articles), 332)

    def test_important_implementation_distinctions(self):
        def content(n, slug):
            return (ROOT / "wiki/machine-learning" / f"{n:03d}-{slug}.md").read_text("utf-8")
        self.assertIn("GOSS", content(152, "lightgbm"))
        self.assertIn("num_leaves", content(152, "lightgbm"))
        self.assertIn("Plain", content(153, "catboost"))
        self.assertIn("OOF", content(154, "stacking"))
        self.assertIn("bootstrap=True", content(156, "out-of-bag-error"))
        self.assertIn("MDI", content(157, "feature-importance"))
        self.assertIn("半正定", content(164, "kernel-trick"))
        self.assertIn("ε-insensitive", content(169, "support-vector-regression"))
        self.assertIn("三角不等式", content(172, "distance-metric"))
        self.assertIn("零向量", content(175, "cosine-similarity"))

    def test_independent_numeric_example_recomputations(self):
        self.assertAlmostEqual(-(-6)/(3+1), 1.5)             # 151 XGBoost leaf
        self.assertEqual((2 + 2*.5)/(3+2), .6)              # 153 ordered category
        self.assertAlmostEqual((.2+3*.8)/(1+3), .65)        # 155 soft voting
        self.assertAlmostEqual((99/100)**100, .366032341, places=6)  # 156 OOB
        self.assertAlmostEqual(.90-.76, .14)                # 157 importance
        self.assertAlmostEqual(1/math.sqrt(3**2+4**2), .2)  # 158 margin
        self.assertEqual(sum(a > 0 for a in [0,.4,1]), 2)   # 159 supports
        self.assertAlmostEqual(2/5, .4)                     # 160 geometry
        self.assertAlmostEqual(2/math.sqrt(0**2+2**2), 1)  # 161 hard width
        self.assertEqual(max(0, 1 - (-1)*2), 3)             # 162 hinge
        self.assertAlmostEqual(.5*4 + 2*(.5+1), 5)          # 163 soft primal
        self.assertEqual(2*3 + 4*9, 42)                     # 164 feature inner product
        self.assertEqual(1 - 2 - 2 + 1, -2)                 # 165 Gram cT K c
        self.assertEqual((2, -1), (2*1, -.5*2))            # 166 linear w
        self.assertEqual((1*2+2*1+1)**2, 25)               # 167 poly
        self.assertAlmostEqual(math.exp(-.5*2), math.exp(-1))  # 168 rbf
        self.assertAlmostEqual(1/(2*2**2), .125)            # 168 gamma
        self.assertAlmostEqual(max(0, abs(5-4.4)-.5), .1)  # 169 SVR epsilon
        self.assertEqual((2+4+9)/3, 5)                      # 170 KNN regression
        self.assertAlmostEqual(3/5, .6)                    # 171 recall@5
        self.assertEqual(math.dist((1,2),(4,6)), 5)        # 173 Euclidean
        self.assertEqual(abs(1-4)+abs(2-6), 7)             # 174 Manhattan
        self.assertEqual((3*6+4*8)/(5*10), 1)              # 175 cosine


if __name__ == "__main__":
    unittest.main()
