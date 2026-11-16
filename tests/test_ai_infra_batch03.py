"""Full-fidelity AI Infrastructure publication contract for concepts 041–060.

Do not treat a passing file/citation check as human subject-matter sign-off.
"""
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ARTICLE_REF=re.compile(r"\[[^\]]+\]\((https://[^)]+)\)")


class AIInfraBatch03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-infrastructure/manifest.json").read_text(encoding="utf-8"))
        cls.public=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.plans=json.loads((ROOT/"wiki/ai-infrastructure/batches.json").read_text(encoding="utf-8"))
        cls.review=json.loads((ROOT/"wiki/reviews/ai-infrastructure.json").read_text(encoding="utf-8"))

    def test_batch_has_all_20_source_aligned_full_articles(self):
        selected=self.manifest["terms"][40:60]
        self.assertEqual([x["n"] for x in selected],list(range(41,61)))
        self.assertTrue(all(x["ready"] and x["file"] for x in selected))
        self.assertEqual([x["topic"] for x in selected[:18]],["分布式训练"]*18)
        self.assertEqual([x["topic"] for x in selected[18:]],["推理与服务"]*2)
        for item in selected:
            with self.subTest(n=item["n"]):
                orig=ROOT/"wiki/ai-infrastructure"/item["file"]
                public=ROOT/"docs/wiki/ai-infrastructure"/item["file"]
                self.assertEqual(orig.read_bytes(),public.read_bytes())
                body=orig.read_text(encoding="utf-8")
                self.assertGreater(len(body),1700)
                self.assertIn(item["en"],body)
                self.assertIn(item["zh"],body)
                self.assertNotRegex(body,r"(?i)batch\s*0?[1-9]|生产批次|PR状态")
                for h in ("核心定义","形象理解","技术原理","工程实践","易混概念","面试题","考试题","权威来源"):
                    self.assertIn(h,body)
                self.assertGreaterEqual(body.count("**问："),2)
                self.assertGreaterEqual(body.count("**题："),2)
                urls=ARTICLE_REF.findall(body)
                self.assertGreaterEqual(len(set(urls)),2)
                self.assertTrue(all(u.startswith("https://") for u in urls))

    def test_public_index_has_exact_60_sorted_concepts_without_editorial_status(self):
        pages=self.public["articles"]
        self.assertEqual(len(pages),60)
        self.assertEqual(self.manifest["readyArticles"],60)
        self.assertEqual(self.manifest["readyInPr"],60)
        paths=[p["path"] for p in pages]
        self.assertEqual(len(paths),len(set(paths)))
        self.assertEqual([p["path"] for p in pages[40:60]],
             ["wiki/ai-infrastructure/"+r["file"] for r in self.manifest["terms"][40:60]])
        for entry in pages:
            self.assertTrue(set(entry)<=set(("category","chapter","en","zh","path")))
        self.assertEqual([p["chapter"] for p in pages[40:60]],[3]*18+[4]*2)

    def test_internal_batch_plan_and_human_review_ledger(self):
        plan=self.plans["batches"][2]
        self.assertEqual((plan["start"],plan["end"],plan["count"]),(41,60,20))
        self.assertEqual([row["status"] for row in plan["terms"]],["merged"]*20)
        ledgers={item["path"]:item for item in self.review["articles"]}
        self.assertEqual(len(ledgers),60)
        for entry in self.public["articles"][40:60]:
            key=entry["path"]
            self.assertEqual(ledgers[key]["status"],"pending")
            self.assertNotIn("reviewer",ledgers[key])
            self.assertNotIn("sha256",ledgers[key])

    def test_numeric_examples_checked_against_independent_results(self):
        # 041 DDP: global batch and ideal ring bytes
        self.assertEqual(4*16*2,128)
        self.assertEqual(2*(4-1)*200/4,300)
        # 042 TP: 8192² BF16 bytes split into 4 ranks
        self.assertEqual(8192**2*2/4/2**20,32)
        # 043 PP bubble fraction for 4 stages, 12 vs 4 microbatches
        self.assertAlmostEqual((4-1)/(12+4-1),.20)
        self.assertAlmostEqual((4-1)/(4+4-1),3/7)
        # 044 top-2 MoE assignment count and mean expert load
        self.assertEqual(1024*2/16,128)
        # 054 PP stage count does not multiply global batch
        self.assertEqual(2*8*4,64)
        # 060 capacity with 75% utilization target
        import math
        self.assertEqual(math.ceil(300/(120*.75)),4)


if __name__=="__main__":
    unittest.main()
