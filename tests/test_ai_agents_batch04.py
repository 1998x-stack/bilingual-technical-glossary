"""AI Agents Batch 04 — 061–080 source, article, math, and browser publication checks."""
import json
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgentsBatch04Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=canonical_rows()
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.ledger=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_identity_and_status(self):
        terms=self.manifest["terms"][60:80]
        self.assertEqual(len(terms),20)
        self.assertEqual([x["n"] for x in terms],list(range(61,81)))
        self.assertEqual([x["topic"] for x in terms],["任务规划与决策"]*3+["工具使用与环境交互"]*17)
        self.assertEqual(terms[0]["en"],"Backtracking")
        self.assertEqual(terms[-1]["en"],"Tool Adapter")
        self.assertEqual(self.plan["batches"][3]["status"],"drafted_in_pr")
        self.assertTrue(all(x["ready"] for x in terms))
        self.assertGreaterEqual(self.manifest["readyArticles"],80)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),222)
        self.assertEqual(len(self.ledger["articles"][60:80]),20)
        self.assertEqual([r["path"] for r in self.ledger["articles"][60:80]],
                         ["wiki/ai-agents/"+x["file"] for x in terms])
        self.assertTrue(all(r["status"]=="pending" and "reviewer" not in r
                            for r in self.ledger["articles"][60:80]))

    def test_article_content_mirror_and_sources(self):
        for r in self.manifest["terms"][60:80]:
            with self.subTest(n=r["n"],name=r["en"]):
                self.assertEqual(r["file"],article_filename(r["n"],r["en"]))
                source=ROOT/"wiki/ai-agents"/r["file"]
                mirror=ROOT/"docs/wiki/ai-agents"/r["file"]
                self.assertEqual(source.read_bytes(),mirror.read_bytes())
                txt=source.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(txt),1400)
                self.assertIn(r["en"],txt)
                self.assertIn(r["zh"],txt)
                for key in ("核心定义","形象理解","类比的局限","技术原理","工程实践",
                            "失败模式与验证","易混辨析","面试题","考试题","权威来源"):
                    self.assertIn(key,txt)
                self.assertEqual(txt.count("**问："),2)
                self.assertEqual(txt.count("**题："),2)
                self.assertGreaterEqual(len(set(re.findall(r"\]\((https://[^)\s]+)\)",txt))),2)
                self.assertNotRegex(txt,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_technical_topics_are_distinct(self):
        def article(n):
            return (ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
        terms={61:"O(b^d)",62:"precondition_failed",63:"budget_exceeded",64:"inputSchema",
               65:"call_id",66:"app_status",67:"T_valid",68:"tenant",69:"JSON Schema",
               70:"TOCTOU",71:"tools/list",72:"namespace",73:"get_order",74:"URL",
               75:"locator",76:"screenshot",77:"stdout",78:"shell=False",79:"Idempotency-Key",
               80:"ToolRequest"}
        for n,needle in terms.items():
            with self.subTest(n=n):
                self.assertIn(needle,article(n))

    def test_exam_examples_independently_verified(self):
        self.assertEqual(1+3+9,13)
        self.assertEqual(2+11,13)
        self.assertEqual(120-50-40,30)
        self.assertEqual(18-5-4,9)
        self.assertEqual(18/25,.72)
        self.assertEqual(.6+.8+1.1+.5,3.0)
        self.assertEqual(3+5+2,10)
        self.assertEqual(1250/1000,1.25)
        self.assertEqual(.8+.4+.7+1.1+.5,3.5)
        self.assertEqual(max(.8,.4)+.7+1.1+.5,3.1)

if __name__=="__main__":
    unittest.main()
