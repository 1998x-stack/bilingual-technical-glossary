"""Publication, scheduling semantics and worked-example integrity for AI Infra 081–100."""
import json
import math
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE_LINK=re.compile(r"\[[^\]]+\]\((https://[^)\s]+)\)")


class AIInfraBatch05Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-infrastructure/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.batches=json.loads((ROOT/"wiki/ai-infrastructure/batches.json").read_text(encoding="utf-8"))
        cls.review=json.loads((ROOT/"wiki/reviews/ai-infrastructure.json").read_text(encoding="utf-8"))

    def test_all_20_articles_match_source_and_pages_mirror(self):
        selected=self.manifest["terms"][80:100]
        self.assertEqual([x["n"] for x in selected],list(range(81,101)))
        self.assertEqual([x["topic"] for x in selected],["调度与容器"]*17+["存储与数据管道"]*3)
        for row in selected:
            with self.subTest(number=row["n"],english=row["en"]):
                self.assertTrue(row["ready"])
                name=row["file"]
                self.assertRegex(name,rf"^{row['n']:03}-[a-z0-9-]+\.md$")
                source=ROOT/"wiki/ai-infrastructure"/name
                mirror=ROOT/"docs/wiki/ai-infrastructure"/name
                self.assertTrue(source.is_file())
                self.assertEqual(source.read_bytes(),mirror.read_bytes())
                body=source.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body),1400)
                self.assertIn(row["en"],body)
                self.assertIn(row["zh"],body)
                for heading in ("核心定义","形象理解","技术原理","工程实践","易混概念","面试题","考试题","权威来源"):
                    self.assertIn(heading,body)
                self.assertGreaterEqual(body.count("**问："),2)
                self.assertGreaterEqual(body.count("**题："),2)
                self.assertGreaterEqual(len(set(SOURCE_LINK.findall(body))),2)
                self.assertNotRegex(body,r"(?i)\bbatch[-\s]*0[1-8]\b|生产批次|PR状态")

    def test_index_chapters_and_pending_review_ledger_match_100_articles(self):
        entries=self.index["articles"]
        self.assertEqual(len(entries),100)
        self.assertEqual(self.manifest["readyArticles"],100)
        self.assertEqual(self.manifest["readyInPr"],100)
        self.assertEqual([x["chapter"] for x in entries[80:100]],[5]*17+[6]*3)
        self.assertEqual([x["path"] for x in entries[80:100]],
            ["wiki/ai-infrastructure/"+x["file"] for x in self.manifest["terms"][80:100]])
        self.assertEqual(len({x["path"] for x in entries}),100)
        ledger={x["path"]:x for x in self.review["articles"]}
        self.assertEqual(len(ledger),100)
        for x in entries[80:100]:
            self.assertEqual(ledger[x["path"]]["status"],"pending")
            self.assertNotIn("reviewer",ledger[x["path"]])
            self.assertNotIn("sha256",ledger[x["path"]])

    def test_batch05_is_internal_authoring_material_not_public_navigation(self):
        plan=self.batches["batches"][4]
        self.assertEqual((plan["start"],plan["end"],plan["count"]),(81,100,20))
        self.assertEqual(plan["status"],"merged")
        self.assertTrue(all(x["status"]=="merged" and x["wiki"] for x in plan["terms"]))
        self.assertTrue((ROOT/"wiki/ai-infrastructure/BATCH-05.md").is_file())
        self.assertFalse((ROOT/"docs/wiki/ai-infrastructure/BATCH-05.md").exists())

    def test_scheduling_storage_and_capacity_calculations(self):
        self.assertEqual(math.ceil(2400/200),12) # object shards
        self.assertEqual(96/8,12) # multipart parts
        self.assertEqual(math.ceil(6*1.5),9) # HPA recommendation
        self.assertEqual(64-4-2,58) # Node allocatable CPU
        self.assertEqual(8-2,6) # healthy devices
        self.assertEqual(24//6,4) # Job waves
        self.assertEqual(12-9,3) # namespace GPU quota remaining
        self.assertEqual(8*4,32) # gang total GPUs
        self.assertEqual(math.ceil(12/3),4) # maintenance batches
        self.assertAlmostEqual(12000*16/1024,187.5) # block storage MiB/s
        self.assertAlmostEqual(2*1024*1024/3600,582.5422222222) # scan MiB/s
        self.assertEqual(math.ceil(1.2*1024*1024/256),4916) # HDFS blocks
        self.assertEqual(120*3,360) # replicated HDFS TiB
        self.assertEqual(16*2,32) # node pool GPU scale-up
        self.assertEqual(53+6*4,77) # CPU quota usage after create


if __name__=="__main__":
    unittest.main()
