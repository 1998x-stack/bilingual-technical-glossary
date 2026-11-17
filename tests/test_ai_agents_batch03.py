"""AI Agents Batch 03: source continuity, real article contents, calculations and publication integrity."""
import json
import math
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgentsBatch03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = canonical_rows()
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.ledger=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))

    def test_batch_identity_order_and_progress(self):
        subset=self.manifest["terms"][40:60]
        self.assertEqual(len(subset),20)
        self.assertEqual([r["n"] for r in subset],list(range(41,61)))
        self.assertEqual([r["topic"] for r in subset],["模型能力与推理"]*2+["任务规划与决策"]*18)
        self.assertEqual(subset[0]["en"],"Uncertainty")
        self.assertEqual(subset[1]["en"],"Confidence Calibration")
        self.assertEqual(subset[-1]["en"],"Lookahead Search")
        self.assertEqual(self.plan["batches"][2]["status"],"drafted_in_pr")
        self.assertGreaterEqual(self.manifest["readyArticles"],60)
        self.assertGreaterEqual(self.manifest["readyInPr"],60)
        self.assertGreaterEqual(len(self.index["articles"]),202)
        self.assertGreaterEqual(len([r for r in self.index["articles"] if r["category"]=="ai-agents"]),60)
        self.assertGreaterEqual(len(self.ledger["articles"]),60)
        self.assertTrue(all(r["status"]=="pending" and "reviewer" not in r for r in self.ledger["articles"][40:60]))
        self.assertEqual([r["path"] for r in self.ledger["articles"][40:60]],
                         ["wiki/ai-agents/"+r["file"] for r in subset])

    def test_20_real_wiki_articles_have_bilingual_identity_and_questions(self):
        for r in self.manifest["terms"][40:60]:
            with self.subTest(n=r["n"],en=r["en"]):
                self.assertEqual(r["file"],article_filename(r["n"],r["en"]))
                src=ROOT/"wiki/ai-agents"/r["file"]
                dst=ROOT/"docs/wiki/ai-agents"/r["file"]
                self.assertEqual(src.read_bytes(),dst.read_bytes())
                body=src.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body),1400)
                self.assertIn(r["en"],body)
                self.assertIn(r["zh"],body)
                for h in ("核心定义","形象理解","类比的局限","技术原理","工程实践","失败模式与验证","易混辨析","面试题","考试题","权威来源"):
                    self.assertIn(h,body)
                self.assertEqual(body.count("**问："),2)
                self.assertEqual(body.count("**题："),2)
                urls=re.findall(r"\]\((https://[^)\s]+)\)",body)
                self.assertGreaterEqual(len(set(urls)),2)
                self.assertNotRegex(body,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_technical_identity_is_not_generic_filler(self):
        def body(n):
            return (ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
        checks={41:"epistemic",42:"ECE",43:"PDDL",44:"DAG",45:"HTN",46:"phase",47:"precondition",48:"replan",49:"patch",50:"Kahn",51:"aging",52:"A_valid",53:"A(s)",54:"2^k",55:"π(a",56:"EU(",57:"reward hacking",58:"b^",59:"f(n)",60:"Q_H"}
        for n,term in checks.items():
            with self.subTest(n=n):
                self.assertIn(term,body(n))

    def test_intermediate_exercises_independently_checked(self):
        self.assertAlmostEqual(.4*abs(.75-.9)+.6*abs(.5-.6),.12)
        self.assertEqual(max(3,4)+2,6)
        self.assertEqual(2+max(3,5)+1,8)
        self.assertEqual(1+2+4+8+16,31)
        self.assertEqual(2+5+4,11)
        self.assertEqual(6-2-1,3)
        self.assertEqual(2**4,16)
        self.assertAlmostEqual(.2/(.2+.3),.4)
        self.assertAlmostEqual(.7*100+.3*(-20),64)
        self.assertAlmostEqual(4+.5*10,9)
        self.assertEqual(1+3+9+27,40)
        self.assertEqual(2+.9*10,11)
        self.assertAlmostEqual(5+.9*5,9.5)
        self.assertEqual(3+9+27,39)

if __name__=="__main__":
    unittest.main()
