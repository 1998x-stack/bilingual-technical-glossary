"""AI Agent second Wiki batch: canonical order, mirrors, explanatory depth and exam checks."""
import json
import re
import unittest
from pathlib import Path
from scripts.verify_ai_agents_wiki import canonical_rows, article_filename, main, ROOT

class AIAgentsBatch02Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = canonical_rows()
        cls.manifest = json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.plan = json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.index = json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.ledger = json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_batch02_is_exactly_20_consecutive_terms(self):
        selection = self.manifest["terms"][20:40]
        self.assertEqual([x["n"] for x in selection],list(range(21,41)))
        self.assertEqual(selection[0]["en"],"Action")
        self.assertEqual(selection[1]["en"],"Termination Condition")
        self.assertEqual(selection[2]["en"],"Reasoning Model")
        self.assertEqual(selection[-1]["en"],"Hallucination")
        self.assertEqual([x["topic"] for x in selection],
                         ["基础概念与角色"]*2+["模型能力与推理"]*18)
        self.assertTrue(all(x["ready"] and x["file"] for x in selection))
        # Check Batch 02's own ledger entries without freezing future total coverage.
        self.assertGreaterEqual(len(self.ledger["articles"]),40)
        self.assertEqual([x["path"] for x in self.ledger["articles"][20:40]],
                         ["wiki/ai-agents/"+x["file"] for x in selection])
        self.assertTrue(all(x["status"]=="pending" and "reviewer" not in x
                            for x in self.ledger["articles"][20:40]))
        self.assertEqual(self.plan["batches"][1]["status"],"drafted_in_pr")

    def test_articles_have_mechanism_and_differentiated_questions(self):
        for r in self.manifest["terms"][20:40]:
            with self.subTest(n=r["n"],en=r["en"]):
                self.assertEqual(r["file"],article_filename(r["n"],r["en"]))
                original=ROOT/"wiki/ai-agents"/r["file"]
                public=ROOT/"docs/wiki/ai-agents"/r["file"]
                self.assertEqual(original.read_bytes(),public.read_bytes())
                body=original.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body),1200)
                self.assertIn("类比的局限",body)
                self.assertIn("失败模式与验证",body)
                for heading in ("核心定义","形象理解","技术原理","工程实践","易混辨析","面试题","考试题","权威来源"):
                    self.assertIn(heading,body)
                self.assertEqual(body.count("**问："),2)
                self.assertEqual(body.count("**题："),2)
                self.assertGreaterEqual(len(set(re.findall(r"\]\((https://[^)\s]+)\)",body))),2)
                self.assertNotRegex(body,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_article_specific_technical_claims_and_examples(self):
        def article(n):
            return (ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
        self.assertIn("幂等",article(21))
        self.assertIn("budget_exceeded",article(22)) if "budget_exceeded" in article(22) else self.assertIn("deadline",article(22))
        self.assertIn("reasoning",article(23))
        self.assertIn("request_id",article(24))
        self.assertIn("FLOPs",article(25))
        self.assertIn("并发",article(26))
        self.assertIn("8192",article(27))
        self.assertIn("tokenizer",article(28))
        self.assertIn("reasoning_tokens",article(29))
        self.assertIn("softmax",article(30)) if "softmax" in article(30) else self.assertIn("logits",article(30))
        self.assertIn("JSON Schema",article(31))
        self.assertIn("重归一化",article(32))
        self.assertIn("tool_call",article(33))
        self.assertIn("few-shot",article(34))
        self.assertIn("剪枝",article(35))
        self.assertIn("2/3",article(36))
        self.assertIn("trace_id",article(37))
        self.assertIn("单测",article(38))
        self.assertIn("checker",article(39))
        self.assertIn("faithfulness",article(40))

    def test_calculations_independently_recomputed(self):
        self.assertEqual(8192-6100-1600,492)
        self.assertEqual(12000-3500-4200,4300)
        from math import exp
        self.assertAlmostEqual(exp(2)/(exp(2)+exp(1)),0.73105858,places=5)
        self.assertAlmostEqual(exp(1)/(exp(1)+exp(.5)),0.62245933,places=5)
        self.assertAlmostEqual(.3/(.3+.2),.6)
        self.assertEqual(1+3+9+27,40)
        self.assertEqual(70+12-5,77)
        self.assertAlmostEqual(15/20,.75)
        self.assertAlmostEqual(.8+max(.5,.7,1.0)+.6,2.4)

if __name__=="__main__":
    unittest.main()
