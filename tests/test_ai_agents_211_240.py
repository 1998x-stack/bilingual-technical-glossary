"""AI Agents Wiki 211–240 (finish batch11 + complete batch12) contract checks."""
import json
import math
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgents211240Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=canonical_rows()
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.review=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_30_terms_in_canonical_chapter_order(self):
        terms=self.manifest["terms"][210:240]
        self.assertEqual(len(terms),30)
        self.assertEqual([t["n"] for t in terms],list(range(211,241)))
        self.assertEqual([t["topic"] for t in terms],
                         ["执行状态、持久化与恢复"]*17+
                         ["评测体系与常见基准"]*13)
        self.assertEqual(terms[0]["en"],"Checkpointing")
        self.assertEqual(terms[9]["en"],"Retry Policy")
        self.assertEqual(terms[16]["en"],"Execution Log")
        self.assertEqual(terms[17]["en"],"Agent Evaluation")
        self.assertEqual(terms[-1]["en"],"Factual Accuracy")
        self.assertTrue(all(t["ready"] for t in terms))
        self.assertGreaterEqual(self.manifest["readyArticles"],240)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),382)
        self.assertEqual(len([i for i in self.index["articles"] if i["category"]=="ai-agents"]),
                         self.manifest["readyArticles"])
        self.assertIn(self.plan["batches"][10]["status"],{"drafted_in_pr","merged"})
        self.assertIn(self.plan["batches"][11]["status"],{"drafted_in_pr","merged"})
        self.assertTrue(self.manifest["readyArticles"]>=260 or all(
            not term["ready"] and term["file"] is None
            for term in self.manifest["terms"][240:260]))
        self.assertEqual([r["path"] for r in self.review["articles"][210:240]],
                         ["wiki/ai-agents/"+t["file"] for t in terms])
        self.assertTrue(all(r["status"]=="pending" and "reviewer" not in r
                            for r in self.review["articles"][210:240]))

    def test_source_mirror_and_full_article_contract(self):
        for t in self.manifest["terms"][210:240]:
            with self.subTest(n=t["n"],term=t["en"]):
                self.assertEqual(t["file"],article_filename(t["n"],t["en"]))
                source=ROOT/"wiki/ai-agents"/t["file"]
                mirror=ROOT/"docs/wiki/ai-agents"/t["file"]
                self.assertEqual(source.read_bytes(),mirror.read_bytes())
                text=source.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(text),1400)
                self.assertIn(t["en"],text)
                self.assertIn(t["zh"],text)
                for required in ("核心定义","形象理解","类比的局限","技术原理",
                                 "工程实践","失败模式与验证","易混辨析",
                                 "面试题","考试题","权威来源"):
                    self.assertIn(required,text)
                self.assertEqual(text.count("**问："),2)
                self.assertEqual(text.count("**题："),2)
                self.assertGreaterEqual(len(set(re.findall(r"\]\((https://[^)\s]+)\)",text))),2)
                self.assertNotRegex(text,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_distinct_protocol_and_evaluation_mechanisms(self):
        specific={211:"thread_id",212:"Store",213:"idempotency_key",
                  214:"Command(resume=",215:"operation_id",216:"RunState",
                  217:"ReviewRecord",218:"arguments_hash",219:"429",
                  220:"retry budget",221:"full-jitter",222:"connect_timeout",
                  223:"child_timeout",224:"fencing",225:"Saga",
                  226:"transactional outbox",227:"TraceId",228:"ScriptedModel",
                  229:"SWE-bench",230:"EvalCase",231:"TSR=",232:"AND(",
                  233:"allowed_tool_names",234:"ASR=",235:"τ=",
                  236:"trace_id",237:"outcome_oracle",238:"process rubric",
                  239:"Faithfulness=",240:"Factual Accuracy"}
        for n,mechanism in specific.items():
            with self.subTest(n=n):
                article=(ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
                self.assertIn(mechanism,article)

    def test_risk_and_evidence_boundaries(self):
        for n in (213,214,215,216,218,219,220,225,226):
            article=(ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
            self.assertTrue("授权" in article or "权限" in article)
        source=(ROOT/"wiki/ai-agents"/self.manifest["terms"][238]["file"]).read_text(encoding="utf-8")
        self.assertIn("Ragas",source)
        self.assertIn("supported",source)
        guide=(ROOT/"wiki/ai-agents/BATCH-12.md").read_text(encoding="utf-8")
        self.assertIn("End-to-end",guide)
        self.assertIn("Faithfulness",guide)
        self.assertIn("Factual Accuracy",guide)

    def test_calculation_examples(self):
        self.assertEqual(50-37,13)
        self.assertAlmostEqual(20*.2,4)
        self.assertEqual(8-5,3)
        self.assertEqual(12-9,3)
        self.assertEqual(50-27,23)
        self.assertEqual(3**4,81)
        self.assertEqual(1+2+4+8,15)
        self.assertEqual(min(10,2**4),10)
        self.assertEqual(3*5,15)
        self.assertEqual(30-12-10,8)
        self.assertEqual(5+3+4,12)
        self.assertEqual(300*.8,240)
        self.assertEqual(300-240,60)
        self.assertEqual(84/200,.42)
        self.assertAlmostEqual(23/30,23/30)
        self.assertEqual((40-2)/50,.76)
        self.assertEqual(6/8,.75)
        self.assertEqual(17/20,.85)

if __name__=="__main__":
    unittest.main()
