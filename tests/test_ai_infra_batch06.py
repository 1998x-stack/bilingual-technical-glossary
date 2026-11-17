"""Publication and technical calculation integrity for AI Infra 101–120.

This checks source/mirror consistency, public chapters, structural quality, and
sample arithmetic. It does not attest independent peer review or live HTTP URLs.
"""
import json
import math
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE_LINK=re.compile(r"\[[^\]]+\]\((https://[^)\s]+)\)")


class AIInfraBatch06Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-infrastructure/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.batches=json.loads((ROOT/"wiki/ai-infrastructure/batches.json").read_text(encoding="utf-8"))
        cls.review=json.loads((ROOT/"wiki/reviews/ai-infrastructure.json").read_text(encoding="utf-8"))

    def test_full_articles_match_canonical_source_and_pages_mirror(self):
        selected=self.manifest["terms"][100:120]
        self.assertEqual([x["n"] for x in selected],list(range(101,121)))
        self.assertEqual([x["topic"] for x in selected],["存储与数据管道"]*11+["可靠性与可观测性"]*9)
        for row in selected:
            with self.subTest(term=row["n"],english=row["en"]):
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
                self.assertEqual(body.count("**问："),2)
                self.assertEqual(body.count("**题："),2)
                self.assertGreaterEqual(len(set(SOURCE_LINK.findall(body))),2)
                self.assertNotRegex(body,r"(?i)\bbatch[-\s]*0[1-8]\b|生产批次|PR状态")

    def test_all_public_index_entries_and_pending_reviews_are_consistent(self):
        entries=self.index["articles"]
        self.assertEqual(len(entries),120)
        self.assertEqual(self.manifest["readyArticles"],120)
        self.assertEqual(self.manifest["readyInPr"],120)
        self.assertEqual([x["chapter"] for x in entries[100:120]],[6]*11+[7]*9)
        self.assertEqual([x["path"] for x in entries[100:120]],
            ["wiki/ai-infrastructure/"+x["file"] for x in self.manifest["terms"][100:120]])
        self.assertEqual(len({x["path"] for x in entries}),120)
        ledger={x["path"]:x for x in self.review["articles"]}
        self.assertEqual(len(ledger),120)
        for x in entries[100:120]:
            self.assertEqual(ledger[x["path"]]["status"],"pending")
            self.assertNotIn("reviewer",ledger[x["path"]])
            self.assertNotIn("sha256",ledger[x["path"]])

    def test_author_plan_is_not_public_navigation(self):
        plan=self.batches["batches"][5]
        self.assertEqual((plan["start"],plan["end"],plan["count"]),(101,120,20))
        self.assertEqual(plan["status"],"merged")
        self.assertTrue(all(x["status"]=="merged" and x["wiki"] for x in plan["terms"]))
        self.assertTrue((ROOT/"wiki/ai-infrastructure/BATCH-06.md").is_file())
        self.assertFalse((ROOT/"docs/wiki/ai-infrastructure/BATCH-06.md").exists())

    def test_unit_sensitive_storage_training_and_reliability_worked_examples(self):
        self.assertEqual(640/4,160) # NFS read seconds
        self.assertEqual(4*1.5,6) # Lustre 4 OST GiB/s bound
        self.assertEqual(25000*32/1024,781.25) # MiB/s and KiB blocks
        self.assertEqual(1200000/40,30000) # IOPS
        self.assertEqual(10000*.004,40) # Little's law mean in-flight
        self.assertEqual(100*(1-.30),70) # data lake curated TiB
        self.assertAlmostEqual(.995**8,.96069,places=4) # pipeline success
        self.assertEqual(12288000//2048,6000) # data shards
        self.assertEqual(math.ceil(10000/128),79) # loader batches
        self.assertEqual(6*3,18) # prefetch batches
        self.assertEqual(max(70,100),100) # ideal overlapped ms
        self.assertEqual(12*80,960) # prefetched MiB
        self.assertEqual(18600/24000,.775) # cache hit ratio
        self.assertEqual(870000/1000000,.87) # CDN request cache ratio
        self.assertEqual(2000000*.001,2000) # SLO error budget
        self.assertEqual(1000-650,350) # remaining budget
        self.assertEqual(48750/50000,.975) # latency SLI
        self.assertEqual(30*24*60*.0005,21.6) # time-based SLA minutes
        self.assertAlmostEqual(28*24*60*.001,40.32) # time-based availability
        self.assertAlmostEqual(1000/(1000+2),.99800399,places=7)
        self.assertAlmostEqual(math.exp(-.1),.9048374,places=6)
        self.assertAlmostEqual(.99**2,.9801)
        self.assertEqual(10000/5,2000) # uptime-based MTBF hours
        self.assertEqual((5+12+8+15)/4,10) # MTTR minutes
        self.assertAlmostEqual(500*60*24/1048576,.6866455,places=5)
        self.assertEqual((53000-50000)/60,50) # requests/s

    def test_article_semantics_clarify_known_confusions(self):
        def article(n):
            row=self.manifest["terms"][n-1]
            return (ROOT/"wiki/ai-infrastructure"/row["file"]).read_text(encoding="utf-8")
        self.assertIn("租约",article(101))
        self.assertIn("缓存一致性",article(101))
        self.assertIn("分位数",article(120))
        self.assertIn("MTTF",article(117))
        self.assertIn("RPO",article(118))
        self.assertIn("字节命中率",article(110))
        self.assertIn("请求",article(112))


if __name__=="__main__":
    unittest.main()
