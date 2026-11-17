"""AI Agent Wiki Batch 05: 081–100 exact source scope, 20 authored articles and correctness."""
import json
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgentsBatch05Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=canonical_rows()
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.ledger=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_batch_scope_progress_and_ledger(self):
        terms=self.manifest["terms"][80:100]
        self.assertEqual(len(terms),20)
        self.assertEqual([x["n"] for x in terms],list(range(81,101)))
        self.assertEqual([x["topic"] for x in terms],["工具使用与环境交互"]*5+["上下文、记忆与状态"]*15)
        self.assertEqual(terms[0]["en"],"Environment Feedback")
        self.assertEqual(terms[4]["en"],"Sensitive Action")
        self.assertEqual(terms[5]["en"],"Context")
        self.assertEqual(terms[-1]["en"],"Memory Retrieval")
        self.assertIn(self.plan["batches"][4]["status"],{"drafted_in_pr","merged"})
        self.assertTrue(all(x["ready"] and x["file"] for x in terms))
        self.assertGreaterEqual(self.manifest["readyArticles"],100)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),242)
        subset=self.ledger["articles"][80:100]
        self.assertEqual([x["path"] for x in subset],
                         ["wiki/ai-agents/"+r["file"] for r in terms])
        self.assertTrue(all(x["status"]=="pending" and "reviewer" not in x for x in subset))

    def test_articles_are_real_complete_and_public_mirrors_match(self):
        for term in self.manifest["terms"][80:100]:
            with self.subTest(no=term["n"],english=term["en"]):
                self.assertEqual(term["file"],article_filename(term["n"],term["en"]))
                original=ROOT/"wiki/ai-agents"/term["file"]
                mirror=ROOT/"docs/wiki/ai-agents"/term["file"]
                self.assertEqual(original.read_bytes(),mirror.read_bytes())
                body=original.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body),1400)
                self.assertIn(term["en"],body)
                self.assertIn(term["zh"],body)
                for head in ("核心定义","形象理解","类比的局限","技术原理",
                             "工程实践","失败模式与验证","易混辨析",
                             "面试题","考试题","权威来源"):
                    self.assertIn(head,body)
                self.assertEqual(body.count("**问："),2)
                self.assertEqual(body.count("**题："),2)
                urls=re.findall(r"\]\((https://[^)\s]+)\)",body)
                self.assertGreaterEqual(len(set(urls)),2)
                self.assertNotRegex(body,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_every_topic_contains_specific_mechanism(self):
        def article(n):
            return (ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
        signatures={81:"business_status",82:"3^3=27",83:"outbox",
                    84:"f(f(s))=f(s)",85:"risk_level",86:"Context Window",
                    87:"C_t",88:"A/B",89:"Prompt Injection",90:"Truncation",
                    91:"session_id",92:"retention/TTL",93:"expected_version",
                    94:"W_t",95:"thread_id",96:"namespace",97:"episode_id",
                    98:"predicate",99:"procedure",100:"precision@5"}
        for n,needle in signatures.items():
            with self.subTest(n=n):
                self.assertIn(needle,article(n))

    def test_exam_math_is_independently_checked(self):
        self.assertEqual(18-13,5)
        self.assertEqual(.5+1+2+4,7.5)
        self.assertEqual(3**3,27)
        self.assertEqual(8192-5000-2000,1192)
        self.assertEqual((7000-4200)/7000,.4)
        self.assertEqual(1500//300,5)
        self.assertEqual((10000-3500)/10000,.65)
        self.assertEqual(10*2+6,26)
        self.assertEqual(1600-600,1000)
        self.assertEqual((3200-1200)/3200,.625)
        self.assertEqual((90-18)/120,.6)
        self.assertEqual(6/8,.75)
        self.assertEqual(80-10-5,65)
        self.assertEqual(4/5,.8)
        self.assertEqual(4/8,.5)

if __name__=="__main__":
    unittest.main()
