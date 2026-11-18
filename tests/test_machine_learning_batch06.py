"""Machine Learning Wiki Batch 06, contiguous terms 126–150, including decision trees and ensembles."""
import json
import math
import re
import unittest

from scripts.verify_machine_learning_wiki import ROOT, source_terms, validate


class MachineLearningBatch06Tests(unittest.TestCase):
    def test_canonical_sequence_and_two_chapters(self):
        terms = source_terms(ROOT)
        self.assertEqual(len(terms), 447)
        self.assertEqual([x["n"] for x in terms[125:150]], list(range(126, 151)))
        self.assertEqual([x["chapter"] for x in terms[125:150]], [5] * 8 + [6] * 17)
        self.assertEqual(terms[125]["en"], "Decision Function")
        self.assertEqual(terms[149]["en"], "GBDT")
        self.assertGreaterEqual(validate(ROOT), 150)

    def test_article_sections_mirrors_and_qa(self):
        manifest = json.loads(
            (ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8")
        )
        self.assertGreaterEqual(manifest["readyArticles"], 150)
        self.assertGreaterEqual(manifest["readyInPr"], 150)
        for term in manifest["terms"][125:150]:
            with self.subTest(index=term["n"], en=term["en"]):
                self.assertEqual(term["batch"], 6)
                self.assertTrue(term["ready"])
                canonical = ROOT / "wiki/machine-learning" / term["file"]
                mirror = ROOT / "docs/wiki/machine-learning" / term["file"]
                self.assertTrue(canonical.is_file())
                self.assertEqual(canonical.read_bytes(), mirror.read_bytes())
                content = canonical.read_text("utf-8")
                self.assertGreaterEqual(len(content), 1280)
                self.assertIn(term["en"], content.splitlines()[0])
                self.assertIn(term["zh"], content.splitlines()[0])
                for heading in (
                    "核心定义", "形象理解", "技术原理与核心内容",
                    "工程实践与设计权衡", "关联知识与易混辨析",
                    "中等难度面试题", "中等难度考试题",
                    "权威来源与延伸阅读",
                ):
                    self.assertIn(heading, content)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*问：", content, re.M)), 2)
                self.assertEqual(len(re.findall(r"^\d+\. \*\*题：", content, re.M)), 2)
                self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)\s]+\)", content)), 2)
                self.assertIn("pending", content)
                self.assertNotIn("BATCH-06", content)

    def test_index_growth_and_independent_review_status(self):
        idx = json.loads((ROOT / "docs/data/wiki-index.json").read_text("utf-8"))["articles"]
        manifest = json.loads((ROOT / "docs/wiki/machine-learning/manifest.json").read_text("utf-8"))
        review = json.loads((ROOT / "wiki/reviews/machine-learning.json").read_text("utf-8"))["articles"]
        ml = [x for x in idx if x["category"] == "machine-learning"]
        self.assertGreaterEqual(len(idx), 142 + 332 + 150)
        self.assertGreaterEqual(len(ml), 150)
        self.assertGreaterEqual(len(review), 150)
        self.assertEqual(
            [x["path"] for x in ml[:150]],
            [f"wiki/machine-learning/{t['file']}" for t in manifest["terms"][:150]],
        )
        self.assertTrue(all(
            x["status"] == "pending" and not x.get("reviewer") for x in review[:150]
        ))
        self.assertEqual(sum(x["category"] == "ai-infrastructure" for x in idx), 142)
        self.assertEqual(sum(x["category"] == "ai-agents" for x in idx), 332)

    def test_technical_distinctions_from_authoritative_sources(self):
        extra = (ROOT / "wiki/machine-learning/146-extra-trees.md").read_text("utf-8")
        forest = (ROOT / "wiki/machine-learning/145-random-forest.md").read_text("utf-8")
        boosting = (ROOT / "wiki/machine-learning/149-gradient-boosting.md").read_text("utf-8")
        self.assertIn("bootstrap=False", extra)
        self.assertIn("随机阈值", extra)
        self.assertIn("平均各树", forest)
        self.assertIn("负梯度", boosting)
        info = (ROOT / "wiki/machine-learning/141-information-gain.md").read_text("utf-8")
        self.assertIn("10.1007/BF00116251", info)

    def test_numerical_examples(self):
        self.assertAlmostEqual(1 / (1 + math.exp(-math.log(3))), .75)   # 128 sigmoid
        self.assertAlmostEqual(math.log(.8 / .2), math.log(4))          # 127 logit
        self.assertAlmostEqual(1 / (1 - .9), 10)                        # 133 VIF
        self.assertAlmostEqual(1 - .6**2 - .4**2, .48)                 # 135 root Gini
        self.assertAlmostEqual(1 - (.75**2 + .25**2), .375)            # 140 Gini
        self.assertAlmostEqual(1 - (.25 * 0 + .75 * .8), .4)           # 141 info gain
        self.assertEqual(2**4, 16)                                     # 138 leaves
        self.assertEqual(2**5 - 1, 31)                                 # 138 nodes
        self.assertAlmostEqual(.25 + .02*3, .31)                       # 142 pruning
        self.assertAlmostEqual((99 / 100)**100, .36603234, places=6)   # 144 OOB
        self.assertAlmostEqual(.5 * math.log(.8/.2), .69314718, places=6) # 148 AdaBoost
        self.assertAlmostEqual(10 + .1*2 + .1*(-1), 10.1)             # 150 GBDT
        self.assertAlmostEqual(5 + .2*2.5, 5.5)                       # 149 boosting


if __name__ == "__main__":
    unittest.main()
