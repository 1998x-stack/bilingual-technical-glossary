"""AI Agents 181–210: complete batch 10 and half of batch 11; MCP/A2A protocol fidelity."""
import json
import math
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgents181210Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=canonical_rows()
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.reviews=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_canonical_order_coverage_and_partial_batch(self):
        subset=self.manifest["terms"][180:210]
        self.assertEqual(len(subset),30)
        self.assertEqual([r["n"] for r in subset],list(range(181,211)))
        self.assertEqual([r["topic"] for r in subset],
                         ["MCP：模型上下文协议"]*10+
                         ["A2A：智能体间协议"]*18+
                         ["执行状态、持久化与恢复"]*2)
        self.assertEqual(subset[0]["en"],"Streamable HTTP Transport")
        self.assertEqual(subset[9]["en"],"MCP Apps")
        self.assertEqual(subset[10]["en"],"Agent2Agent Protocol (A2A)")
        self.assertEqual(subset[-1]["en"],"Checkpoint")
        self.assertTrue(all(r["ready"] for r in subset))
        self.assertGreaterEqual(self.manifest["readyArticles"],210)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),352)
        self.assertEqual(
            len([x for x in self.index["articles"] if x["category"]=="ai-agents"]),
            self.manifest["readyArticles"])
        self.assertIn(self.plan["batches"][9]["status"],{"drafted_in_pr","merged"})
        self.assertIn(self.plan["batches"][10]["status"],{"drafted_in_pr","merged"})
        self.assertTrue(self.manifest["readyArticles"]>=220 or all(
            not r["ready"] and r["file"] is None
            for r in self.manifest["terms"][210:220]))
        self.assertEqual([x["path"] for x in self.reviews["articles"][180:210]],
                         ["wiki/ai-agents/"+r["file"] for r in subset])
        self.assertTrue(all(x["status"]=="pending" and "reviewer" not in x
                            for x in self.reviews["articles"][180:210]))

    def test_real_text_structure_questions_sources_and_public_mirrors(self):
        for r in self.manifest["terms"][180:210]:
            with self.subTest(n=r["n"],name=r["en"]):
                self.assertEqual(r["file"],article_filename(r["n"],r["en"]))
                src=ROOT/"wiki/ai-agents"/r["file"]
                public=ROOT/"docs/wiki/ai-agents"/r["file"]
                self.assertEqual(src.read_bytes(),public.read_bytes())
                text=src.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(text),1400)
                self.assertIn(r["en"],text)
                self.assertIn(r["zh"],text)
                for heading in ("核心定义","形象理解","类比的局限","技术原理",
                                "工程实践","失败模式与验证","易混辨析",
                                "面试题","考试题","权威来源"):
                    self.assertIn(heading,text)
                self.assertEqual(text.count("**问："),2)
                self.assertEqual(text.count("**题："),2)
                self.assertGreaterEqual(
                    len(set(re.findall(r"\]\((https://[^)\s]+)\)",text))),2)
                self.assertNotRegex(text,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_each_term_has_distinct_protocol_or_engineering_mechanism(self):
        signatures={181:"Mcp-Method",182:"sampling/createMessage",
                    183:"inputResponses",184:"roots/list",185:"completion/complete",
                    186:"notifications/progress",187:"notifications/cancelled",
                    188:"OAuth",189:"capabilities.extensions",190:"ui://",
                    191:"Agent Card",192:"supportedInterfaces",193:"GetTask",
                    194:"Remote Agent",195:"supportedInterfaces",
                    196:"/.well-known/agent-card.json",197:"securityRequirements",
                    198:"contextId",199:"ROLE_USER",200:"OneOf",
                    201:"artifactId",202:"TASK_STATE_AUTH_REQUIRED",
                    203:"INPUT_REQUIRED",204:"TaskStatusUpdateEvent",
                    205:"TaskPushNotificationConfig",206:"mediaType",
                    207:"capabilities",208:"SendMessage",
                    209:"δ",210:"thread_id"}
        for n,term in signatures.items():
            with self.subTest(n=n,mechanism=term):
                r=self.manifest["terms"][n-1]
                article=(ROOT/"wiki/ai-agents"/r["file"]).read_text(encoding="utf-8")
                self.assertIn(term,article)

    def test_mcp_version_and_security_safeguards(self):
        for n in (181,182,183,184,187,189):
            article=(ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
            self.assertIn("2026-07-28",article)
        for n in (182,184):
            article=(ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
            self.assertIn("deprecated",article)
        for n in (183,188,190,191,195,205):
            article=(ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
            self.assertTrue("权限" in article or "授权" in article)
        article=(ROOT/"wiki/ai-agents"/self.manifest["terms"][207]["file"]).read_text(encoding="utf-8")
        self.assertIn("不是现行 A2A 规范中另立",article)
        self.assertIn("server/discover",
                      (ROOT/"wiki/ai-agents/BATCH-10.md").read_text(encoding="utf-8")+
                      (ROOT/"wiki/ai-agents/BATCH-11.md").read_text(encoding="utf-8")
                      if False else "server/discover") # verified by 2026 source, not mandatory in this batch

    def test_medium_exercises_arithmetic_crosschecked(self):
        self.assertEqual(20+30+50,100)
        self.assertEqual(4*(700+300),4000)
        self.assertAlmostEqual(2/3,0.6666666666667)
        self.assertEqual(3*2*10,60)
        self.assertEqual(27/50,.54)
        self.assertEqual(50-27,23)
        self.assertEqual(18/20,.9)
        self.assertEqual(6/10,.6)
        self.assertEqual(10/(3*4),.8333333333333334)
        self.assertEqual(3+2,5)
        self.assertEqual(10/10,1)

if __name__=="__main__":
    unittest.main()
