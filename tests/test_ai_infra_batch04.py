"""Publication and worked-example integrity for AI Infra concepts 061–080.

Checks scope, bilingual source identities and exercise arithmetic; passing does
not imply external URL live status or independent expert review.
"""
import json
import math
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE_LINK=re.compile(r"\[[^\]]+\]\((https://[^)\s]+)\)")


class AIInfraBatch04Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-infrastructure/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.batches=json.loads((ROOT/"wiki/ai-infrastructure/batches.json").read_text(encoding="utf-8"))
        cls.review=json.loads((ROOT/"wiki/reviews/ai-infrastructure.json").read_text(encoding="utf-8"))

    def test_all_20_full_articles_match_canonical_terms_and_pages_mirror(self):
        selected=self.manifest["terms"][60:80]
        self.assertEqual([e["n"] for e in selected],list(range(61,81)))
        self.assertEqual([x["topic"] for x in selected],["推理与服务"]*19+["调度与容器"])
        for row in selected:
            with self.subTest(number=row["n"],english=row["en"]):
                self.assertTrue(row["ready"])
                name=row["file"]
                self.assertRegex(name,rf"^{row['n']:03}-[a-z0-9-]+\.md$")
                source=ROOT/"wiki/ai-infrastructure"/name
                mirror=ROOT/"docs/wiki/ai-infrastructure"/name
                self.assertTrue(source.is_file())
                self.assertEqual(source.read_bytes(),mirror.read_bytes())
                text=source.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(text),1400)
                self.assertIn(row["en"],text)
                self.assertIn(row["zh"],text)
                for heading in ("核心定义","形象理解","技术原理","工程实践","易混概念","面试题","考试题","权威来源"):
                    self.assertIn(heading,text)
                self.assertGreaterEqual(text.count("**问："),2)
                self.assertGreaterEqual(text.count("**题："),2)
                self.assertGreaterEqual(len(set(SOURCE_LINK.findall(text))),2)
                self.assertNotRegex(text,r"(?i)\bbatch[-\s]*0[1-8]\b|生产批次|PR状态")

    def test_index_and_editorial_ledger_are_consistent_with_published_pages(self):
        entries=self.index["articles"]
        self.assertEqual(len(entries),self.manifest["readyArticles"])
        self.assertEqual(self.manifest["readyArticles"],len(entries))
        self.assertEqual(self.manifest["readyInPr"],len(entries))
        self.assertEqual([x["chapter"] for x in entries[60:80]],[4]*19+[5])
        self.assertEqual([x["path"] for x in entries[60:80]],
            ["wiki/ai-infrastructure/"+r["file"] for r in self.manifest["terms"][60:80]])
        self.assertEqual(len({x["path"] for x in entries}),len(entries))
        ledger={x["path"]:x for x in self.review["articles"]}
        self.assertEqual(len(ledger),len(entries))
        for x in entries[60:80]:
            self.assertEqual(ledger[x["path"]]["status"],"pending")
            self.assertNotIn("reviewer",ledger[x["path"]])
            self.assertNotIn("sha256",ledger[x["path"]])

    def test_batch_work_plan_remains_internal(self):
        plan=self.batches["batches"][3]
        self.assertEqual((plan["start"],plan["end"],plan["count"]),(61,80,20))
        self.assertEqual(plan["status"],"merged")
        self.assertTrue(all(x["status"]=="merged" and x["wiki"] for x in plan["terms"]))
        self.assertTrue((ROOT/"wiki/ai-infrastructure/BATCH-04.md").is_file())
        self.assertFalse((ROOT/"docs/wiki/ai-infrastructure/BATCH-04.md").exists())

    def test_worked_math_with_independent_recalculation(self):
        self.assertEqual(25+70+15+10,120) # TTFT
        self.assertAlmostEqual((1.22-.22)/(101-1)*1000,10) # TPOT
        self.assertEqual(((72-50)+(110-72)+(125-110))/3,25) # ITL
        self.assertEqual(24000/20,1200) # TPS
        self.assertEqual(200/10,20) # RPS
        self.assertEqual(2048-1536,512) # uncached prefill
        self.assertEqual(2*32*4096*8*128*2/2**20,512) # KV cache MiB
        self.assertEqual(math.ceil(1000/16),63) # paged blocks
        self.assertEqual(math.ceil(19/8),3) # dynamic batching
        self.assertEqual(20/(50/4),1.6) # speculative speedup
        self.assertAlmostEqual((512/1024)/8*1000,62.5) # KV transfer ms
        self.assertAlmostEqual(abs(round(.26/.1)*.1-.26),.04) # symmetric quantization
        self.assertEqual(16/128,.125) # group scale bits per weight
        self.assertEqual(25/100,.25) # PTQ calibration share
        self.assertAlmostEqual(round(1.13/.2)*.2-1.13,.07) # QAT fake quant
        self.assertEqual(48/6,8) # model sharding
        self.assertEqual(14+16,30) # overlapping model reload
        self.assertEqual(min(16//2,48//8),6) # container pod capacity


if __name__=="__main__":
    unittest.main()
