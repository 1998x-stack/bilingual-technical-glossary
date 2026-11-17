"""AI Agents 241–270: benchmark/security taxonomy, original order, article fidelity."""
import json
import math
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgents241270Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=canonical_rows()
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.ledger=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_source_identity_progress_and_partial_batch14(self):
        terms=self.manifest["terms"][240:270]
        self.assertEqual(len(terms),30)
        self.assertEqual([t["n"] for t in terms],list(range(241,271)))
        self.assertEqual([t["topic"] for t in terms],
                         ["评测体系与常见基准"]*13+
                         ["安全防护与治理"]*16+
                         ["智能体攻击与风险"])
        self.assertEqual(terms[0]["en"],"Robustness")
        self.assertEqual(terms[2]["en"],"LLM-as-a-Judge")
        self.assertEqual(terms[12]["en"],"Berkeley Function Calling Leaderboard (BFCL)")
        self.assertEqual(terms[13]["en"],"Guardrail")
        self.assertEqual(terms[19]["en"],"Authorization (AuthZ)")
        self.assertEqual(terms[-1]["en"],"Prompt Injection")
        self.assertTrue(all(t["ready"] for t in terms))
        self.assertGreaterEqual(self.manifest["readyArticles"],270)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),412)
        self.assertEqual(len([x for x in self.index["articles"] if x["category"]=="ai-agents"]),
                         self.manifest["readyArticles"])
        self.assertIn(self.plan["batches"][12]["status"],{"drafted_in_pr","merged"})
        self.assertIn(self.plan["batches"][13]["status"],{"drafted_in_pr","merged"})
        self.assertTrue(self.manifest["readyArticles"]>=280 or all(
            not t["ready"] and t["file"] is None for t in self.manifest["terms"][270:280]))
        self.assertEqual([r["path"] for r in self.ledger["articles"][240:270]],
                         ["wiki/ai-agents/"+t["file"] for t in terms])
        self.assertTrue(all(r["status"]=="pending" and "reviewer" not in r
                            for r in self.ledger["articles"][240:270]))

    def test_full_articles_have_questions_evidence_and_identical_mirrors(self):
        for t in self.manifest["terms"][240:270]:
            with self.subTest(n=t["n"],name=t["en"]):
                self.assertEqual(t["file"],article_filename(t["n"],t["en"]))
                source=ROOT/"wiki/ai-agents"/t["file"]
                mirror=ROOT/"docs/wiki/ai-agents"/t["file"]
                self.assertEqual(source.read_bytes(),mirror.read_bytes())
                article=source.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(article),1400)
                self.assertIn(t["en"],article)
                self.assertIn(t["zh"],article)
                for section in ("核心定义","形象理解","类比的局限",
                                "技术原理","工程实践","失败模式与验证",
                                "易混辨析","面试题","考试题","权威来源"):
                    self.assertIn(section,article)
                self.assertEqual(article.count("**问："),2)
                self.assertEqual(article.count("**题："),2)
                self.assertGreaterEqual(len(set(
                    re.findall(r"\]\((https://[^)\s]+)\)",article))),2)
                self.assertNotRegex(article,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_benchmark_specificity_and_security_mechanisms(self):
        specifics={241:"robustness_ratio",242:"run_manifest",243:"judge_prompt",
                   244:"GroundTruthRecord",245:"LabelRecord",
                   246:"RegressionCase",247:"ScenarioSpec",248:"GAIA",
                   249:"base_commit",250:"WebArena",251:"OSWorld",
                   252:"τ-bench",253:"BFCL V4",254:"GuardrailDecision",
                   255:"policy engine",256:"Capability=",257:"Resource Server",
                   258:"PEP",259:"OIDC",260:"authorize(",
                   261:"seccomp",262:"arguments_hash",263:"OversightPlan",
                   264:"fail-closed",265:"FallbackDecision",
                   266:"AuditEvent",267:"boundary_map",268:"data_taint",
                   269:"data inventory",270:"attacker-controlled content"}
        for n,token in specifics.items():
            with self.subTest(n=n,token=token):
                t=self.manifest["terms"][n-1]
                body=(ROOT/"wiki/ai-agents"/t["file"]).read_text(encoding="utf-8")
                self.assertIn(token,body)

    def test_security_review_and_trust_boundary(self):
        for n in range(254,271):
            body=(ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
            self.assertTrue("权限" in body or "授权" in body or "安全" in body)
        guide=(ROOT/"wiki/ai-agents/BATCH-13.md").read_text(encoding="utf-8")
        self.assertIn("BFCL",guide)
        self.assertIn("AuthN / AuthZ",guide)
        b14=(ROOT/"wiki/ai-agents/BATCH-14.md").read_text(encoding="utf-8")
        self.assertIn("271–280",b14)
        self.assertIn("Prompt Injection",b14)

    def test_math_examples_independently_recomputed(self):
        self.assertAlmostEqual(.72/.90,.8)
        self.assertEqual((42+44+40)/3,42)
        self.assertAlmostEqual(42/50,.84)
        self.assertEqual(82/100,.82)
        self.assertEqual(34/40,.85)
        self.assertEqual(112/120,14/15)
        self.assertEqual(23/50,.46)
        self.assertEqual(37/100,.37)
        self.assertEqual(12/40,.3)
        self.assertEqual(18/50,.36)
        self.assertAlmostEqual(.8**3,.512)
        self.assertEqual(166/200,.83)
        self.assertEqual(3/20,.15)
        self.assertEqual(7/100,.07)
        self.assertEqual(96/100,.96)

if __name__=="__main__":
    unittest.main()
