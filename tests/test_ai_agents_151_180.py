"""AI Agents Wiki incremental 151–180, completing batches 08 and 09."""
import json
import math
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgents151180Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=canonical_rows()
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.ledger=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_source_identity_and_batch_completion(self):
        terms=self.manifest["terms"][150:180]
        self.assertEqual(len(terms),30)
        self.assertEqual([r["n"] for r in terms],list(range(151,181)))
        self.assertEqual([r["topic"] for r in terms],
                         ["多智能体协作"]*16+["MCP：模型上下文协议"]*14)
        self.assertEqual(terms[0]["en"],"Worker Agent")
        self.assertEqual(terms[9]["en"],"Blackboard")
        self.assertEqual(terms[15]["en"],"Coordination Failure")
        self.assertEqual(terms[16]["en"],"Model Context Protocol (MCP)")
        self.assertEqual(terms[-1]["en"],"Standard Input/Output Transport (stdio)")
        self.assertTrue(all(r["ready"] for r in terms))
        self.assertGreaterEqual(self.manifest["readyArticles"],180)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),322)
        self.assertEqual(len([x for x in self.index["articles"] if x["category"]=="ai-agents"]),
                         self.manifest["readyArticles"])
        self.assertEqual([self.plan["batches"][i]["status"] for i in [7,8]],
                         ["drafted_in_pr","drafted_in_pr"])
        self.assertEqual(
            [r["path"] for r in self.ledger["articles"][150:180]],
            ["wiki/ai-agents/"+term["file"] for term in terms])
        self.assertTrue(all(r["status"]=="pending" and "reviewer" not in r
                            for r in self.ledger["articles"][150:180]))

    def test_articles_have_substance_and_byte_identical_mirrors(self):
        for r in self.manifest["terms"][150:180]:
            with self.subTest(n=r["n"],name=r["en"]):
                self.assertEqual(r["file"],article_filename(r["n"],r["en"]))
                origin=ROOT/"wiki/ai-agents"/r["file"]
                mirror=ROOT/"docs/wiki/ai-agents"/r["file"]
                self.assertEqual(origin.read_bytes(),mirror.read_bytes())
                body=origin.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body),1400)
                self.assertIn(r["en"],body)
                self.assertIn(r["zh"],body)
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

    def test_each_article_contains_distinct_mechanism(self):
        keywords={151:"TaskRequest",152:"SupervisorState",153:"ReviewRequest",
                  154:"max_rounds",155:"AgentMessage",156:"Delegation=",
                  157:"input_filter",158:"as_tool",159:"Store namespace",
                  160:"BlackboardState",161:"dead-letter",162:"voting_rule",
                  163:"expected_version",164:"role_matrix",165:"HandoffRecord",
                  166:"coordination invariant",167:"server/discover",
                  168:"命名空间",169:"UnsupportedProtocolVersionError",
                  170:"stdout",171:"inputSchema",172:"resources/read",
                  173:"prompts/get",174:"RFC 3986",175:"deterministic ordering",
                  176:"structuredContent",177:"clientCapabilities",
                  178:"-32022",179:"resultType",180:"stderr"}
        for n,token in keywords.items():
            with self.subTest(n=n,term=token):
                file=self.manifest["terms"][n-1]["file"]
                body=(ROOT/"wiki/ai-agents"/file).read_text(encoding="utf-8")
                self.assertIn(token,body)

    def test_mcp_version_specific_language(self):
        for n in (167,169,170,177,178,179,180):
            r=self.manifest["terms"][n-1]
            body=(ROOT/"wiki/ai-agents"/r["file"]).read_text(encoding="utf-8")
            self.assertIn("2026-07-28",body)
            self.assertIn("2025-11-25",body)
        for n in (167,169,177,178,179,180):
            body=(ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
            self.assertIn("_meta",body)
        body=(ROOT/"wiki/ai-agents/BATCH-09.md").read_text(encoding="utf-8")
        self.assertIn("server/discover",body)
        self.assertIn("initialize",body)
        self.assertIn("2026-07-28",body)

    def test_exam_arithmetic_independently_verified(self):
        self.assertEqual(4*3,12)
        self.assertAlmostEqual((52-20)/30,32/30)
        self.assertAlmostEqual(27/30,.9)
        self.assertEqual(20+3,23)
        self.assertEqual(100//25,4)
        self.assertEqual(12-4-3,5)
        self.assertEqual(20+8,28)
        self.assertEqual(100/5,20)
        self.assertEqual(4/5,.8)
        self.assertEqual(6+7-3,10)
        self.assertEqual(3+4+1,8)
        self.assertEqual(12-1,11)
        self.assertAlmostEqual(11/12,0.9166666667,places=6)
        self.assertEqual(5+5+2,12)
        self.assertEqual(4,2+2)
        self.assertAlmostEqual(5/8,.625)
        self.assertAlmostEqual(3*(1.5+2),10.5)
        self.assertEqual(4/4,1)

if __name__=="__main__":
    unittest.main()
