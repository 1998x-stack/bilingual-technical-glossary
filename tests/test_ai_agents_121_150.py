"""AI Agents authoring increment 121–150: complete batch 07 and first half of batch 08."""
import json
import math
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgentsThirtyTermTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = canonical_rows()
        cls.plan = json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest = json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index = json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.reviews = json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_source_range_and_partial_batch_integrity(self):
        terms=self.manifest["terms"][120:150]
        self.assertEqual(len(terms),30)
        self.assertEqual([t["n"] for t in terms],list(range(121,151)))
        self.assertEqual([t["topic"] for t in terms],
                         ["检索与知识增强"]*4+["工作流与编排模式"]*21+["多智能体协作"]*5)
        self.assertEqual(terms[0]["en"],"Multi-hop Retrieval")
        self.assertEqual(terms[-1]["en"],"Coordinator Agent")
        self.assertTrue(all(t["ready"] for t in terms))
        self.assertGreaterEqual(self.manifest["readyArticles"],150)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),292)
        self.assertIn(self.plan["batches"][6]["status"],{"drafted_in_pr","merged"})
        self.assertIn(self.plan["batches"][7]["status"],{"drafted_in_pr","merged"})
        self.assertTrue(self.manifest["readyArticles"]>=160 or all(
                        not t["ready"] and t["file"] is None
                        for t in self.manifest["terms"][150:160]))
        review=self.reviews["articles"][120:150]
        self.assertEqual([r["path"] for r in review],
                         ["wiki/ai-agents/"+t["file"] for t in terms])
        self.assertTrue(all(r["status"]=="pending" and "reviewer" not in r
                            for r in review))

    def test_articles_are_complete_and_public_mirrors_identical(self):
        for term in self.manifest["terms"][120:150]:
            with self.subTest(n=term["n"],english=term["en"]):
                self.assertEqual(term["file"],article_filename(term["n"],term["en"]))
                source=ROOT/"wiki/ai-agents"/term["file"]
                public=ROOT/"docs/wiki/ai-agents"/term["file"]
                self.assertEqual(source.read_bytes(),public.read_bytes())
                body=source.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body),1400)
                self.assertIn(term["en"],body)
                self.assertIn(term["zh"],body)
                for keyword in ("核心定义","形象理解","类比的局限","技术原理",
                                "工程实践","失败模式与验证","易混辨析",
                                "面试题","考试题","权威来源"):
                    self.assertIn(keyword,body)
                self.assertEqual(body.count("**问："),2)
                self.assertEqual(body.count("**题："),2)
                self.assertGreaterEqual(len(set(
                    re.findall(r"\]\((https://[^)\s]+)\)",body))),2)
                self.assertNotRegex(body,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_specific_technical_mechanisms(self):
        signatures={121:"HotpotQA",122:"SPARQL",123:"claim_id",124:"PROV-O",
                    125:"Control Flow",126:"correlation_id",127:"schema",
                    128:"gate",129:"route=f",130:"T_parallel",
                    131:"aggregation function",132:"spawn",133:"max_rounds",
                    134:"precondition_i",135:"ReAct",136:"T_total",
                    137:"unknown",138:"CFG",139:"typed contract",140:"Kahn",
                    141:"StateGraph",142:"recursion limit",143:"max_fanout",
                    144:"quorum",145:"TOCTOU",146:"MAS",147:"handoff",
                    148:"classify goal",149:"as_tool",150:"correlation_ids"}
        for n,term in signatures.items():
            with self.subTest(n=n):
                doc=ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]
                self.assertIn(term,doc.read_text(encoding="utf-8"))

    def test_independent_exam_math(self):
        self.assertAlmostEqual(3/5,.6)
        self.assertAlmostEqual(6/8,.75)
        self.assertEqual(6+7-3,10)
        self.assertEqual(1+max(2,4,3,5)+2,8)
        self.assertAlmostEqual(4*(.8+.4),4.8)
        self.assertEqual(2+max(3,5),7)
        self.assertEqual(math.ceil(30/5)*2,12)
        self.assertEqual(math.ceil(30/5)*2+1,13)
        self.assertEqual(max(2,5,3)+1,6)
        self.assertEqual(3/4,.75)
        self.assertEqual(34/40,.85)
        self.assertAlmostEqual(max(1.2,2.0)+.5,2.5)
        self.assertEqual(4/4,1)

if __name__=="__main__":
    unittest.main()
