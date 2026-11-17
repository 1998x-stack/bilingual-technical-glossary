"""Final AI Infrastructure Wiki publication checks for terms 121–142.

Machine checks prove page/index/ledger consistency and teaching arithmetic,
not that a human expert has attested each article or checked every external URL.
"""
import json
import math
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE_LINK=re.compile(r"\[[^\]]+\]\((https://[^)\s]+)\)")


class AIInfraFinal22Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-infrastructure/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.index["articles"]=[entry for entry in cls.index["articles"] if entry["category"]=="ai-infrastructure"]
        cls.batches=json.loads((ROOT/"wiki/ai-infrastructure/batches.json").read_text(encoding="utf-8"))
        cls.review=json.loads((ROOT/"wiki/reviews/ai-infrastructure.json").read_text(encoding="utf-8"))

    def test_all_22_articles_match_source_and_pages_mirror(self):
        selected=self.manifest["terms"][120:142]
        self.assertEqual([x["n"] for x in selected],list(range(121,143)))
        self.assertEqual([x["topic"] for x in selected],
                         ["可靠性与可观测性"]*8+["成本、能效与资源治理"]*14)
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
                self.assertGreaterEqual(len(body),1700)
                self.assertIn(row["en"],body)
                self.assertIn(row["zh"],body)
                for heading in ("核心定义","形象理解","技术原理","工程实践",
                                "易混概念","面试题","考试题","权威来源"):
                    self.assertIn(heading,body)
                self.assertEqual(body.count("**问："),2)
                self.assertEqual(body.count("**题："),2)
                self.assertGreaterEqual(len(set(SOURCE_LINK.findall(body))),2)
                self.assertNotRegex(body,r"(?i)\bbatch[-\s]*0[1-8]\b|生产批次|PR状态")

    def test_all_142_long_form_articles_have_unique_public_index_entries(self):
        entries=self.index["articles"]
        self.assertEqual(len(entries),142)
        self.assertEqual(self.manifest["readyArticles"],142)
        self.assertEqual(self.manifest["readyInPr"],142)
        self.assertTrue(all(x["ready"] and x["file"] for x in self.manifest["terms"]))
        self.assertEqual([x["chapter"] for x in entries[120:142]],[7]*8+[8]*14)
        self.assertEqual([x["path"] for x in entries[120:142]],
                         ["wiki/ai-infrastructure/"+x["file"]
                          for x in self.manifest["terms"][120:142]])
        self.assertEqual(len({x["path"] for x in entries}),142)
        self.assertEqual([x["en"] for x in entries],
                         [x["en"] for x in self.manifest["terms"]])

    def test_all_142_reviews_still_pending_without_fake_human_signatures(self):
        ledger={x["path"]:x for x in self.review["articles"]}
        self.assertEqual(len(ledger),142)
        for article in self.index["articles"]:
            with self.subTest(path=article["path"]):
                record=ledger[article["path"]]
                self.assertEqual(record["status"],"pending")
                self.assertNotIn("reviewer",record)
                self.assertNotIn("sha256",record)

    def test_final_two_author_batches_are_internal_only(self):
        for n,start,end,count in [(7,121,140,20),(8,141,142,2)]:
            batch=self.batches["batches"][n-1]
            self.assertEqual((batch["start"],batch["end"],batch["count"]),
                             (start,end,count))
            self.assertEqual(batch["status"],"merged")
            self.assertTrue(all(x["status"]=="merged" and x["wiki"]
                                for x in batch["terms"]))
            self.assertTrue((ROOT/f"wiki/ai-infrastructure/BATCH-0{n}.md").is_file())
            self.assertFalse((ROOT/f"docs/wiki/ai-infrastructure/BATCH-0{n}.md").exists())

    def test_core_concept_boundaries_for_finops_gpu_and_cloud_purchasing(self):
        def article(n):
            row=self.manifest["terms"][n-1]
            return (ROOT/"wiki/ai-infrastructure"/row["file"]).read_text(encoding="utf-8")
        self.assertIn("TraceId",article(121))
        self.assertIn("span_id",article(122))
        self.assertIn("OTLP",article(123))
        self.assertIn("Alertmanager",article(126))
        self.assertIn("coordinated omission",article(127))
        self.assertIn("CapEx",article(129))
        self.assertIn("busy",article(132))
        self.assertIn("FB_USED",article(133))
        self.assertIn("MFU",article(134))
        self.assertIn("PUE",article(135))
        self.assertIn("单位",article(136))
        self.assertIn("NetworkPolicy",article(138))
        self.assertIn("goodput",article(139))
        self.assertIn("2 分钟",article(141))
        self.assertIn("Regional RI",article(142))
        self.assertIn("Zonal RI",article(142))

    def test_unit_sensitive_technical_and_cost_examples(self):
        self.assertAlmostEqual(5000*600*3600/1e9,10.8) # log GB
        self.assertEqual(max(80,120),120) # parallel spans ms
        self.assertEqual(80000*.25,20000) # OTel spans/s
        self.assertEqual((16000-10000)/300,20) # RPS
        self.assertEqual(sum([20,40,60,80])/4,50) # dashboard gauge
        self.assertEqual((600-6)/600,.99) # grouped notification reduction
        self.assertEqual(3000/30,100) # offered load RPS
        self.assertEqual(5400/600,9) # goodput req/s
        self.assertEqual(500*.02,10) # chaos blast radius
        self.assertEqual(600+120*3-60,900) # TCO 10k CNY
        self.assertEqual((240-24)/3,72) # annual straight-line depreciation
        self.assertEqual(80+10+5+15,110) # monthly OpEx 10k CNY
        self.assertAlmostEqual(780/1000,.78) # sampled GPU busy ratio
        self.assertEqual(60/80,.75) # allocated FB capacity fraction
        self.assertEqual(50-38,12) # reserved vs allocated GiB
        self.assertEqual(800/(8*100*2),.5) # MFU
        self.assertEqual(400*100/20000,2) # joules / output token
        self.assertEqual(480000/(1200000000/1000000),400) # unit token cost
        self.assertEqual((120-90)/120,.25) # consolidation savings
        self.assertEqual(64-24-16-8,16) # unallocated quota GPUs
        self.assertEqual(math.ceil(450/(75*.8)),8) # capacity with 20% headroom
        self.assertEqual(math.ceil(4*2.2),9) # HPA desired replicas
        self.assertEqual((10-3)/10,.7) # Spot example discount
        self.assertEqual((12-8)*720,2880) # RI example savings


if __name__=="__main__":
    unittest.main()
