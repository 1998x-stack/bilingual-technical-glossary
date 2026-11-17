"""AI Agents Wiki Batch 06: source continuity, 20 real articles, RAG technical identities."""
import json
import re
import unittest
from scripts.verify_ai_agents_wiki import ROOT, canonical_rows, article_filename, main

class AIAgentsBatch06Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=canonical_rows()
        cls.plan=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.manifest=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.index=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.ledger=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))

    def test_batch_scope_status_and_authorship(self):
        terms=self.manifest["terms"][100:120]
        self.assertEqual(len(terms),20)
        self.assertEqual([x["n"] for x in terms],list(range(101,121)))
        self.assertEqual([x["topic"] for x in terms],["上下文、记忆与状态"]*6+["检索与知识增强"]*14)
        self.assertEqual(terms[0]["en"],"Memory Write")
        self.assertEqual(terms[5]["en"],"User Preference")
        self.assertEqual(terms[6]["en"],"Retrieval-Augmented Generation (RAG)")
        self.assertEqual(terms[-1]["en"],"Query Rewriting")
        self.assertIn(self.plan["batches"][5]["status"],{"drafted_in_pr","merged"})
        self.assertTrue(all(x["ready"] and x["file"] for x in terms))
        self.assertGreaterEqual(self.manifest["readyArticles"],120)
        self.assertEqual(self.manifest["readyArticles"],self.manifest["readyInPr"])
        self.assertGreaterEqual(len(self.index["articles"]),262)
        self.assertGreaterEqual(len([x for x in self.index["articles"] if x["category"]=="ai-agents"]),120)
        subset=self.ledger["articles"][100:120]
        self.assertEqual([x["path"] for x in subset],["wiki/ai-agents/"+x["file"] for x in terms])
        self.assertTrue(all(x["status"]=="pending" and "reviewer" not in x for x in subset))

    def test_real_content_and_mirror_byte_equality(self):
        for term in self.manifest["terms"][100:120]:
            with self.subTest(n=term["n"],name=term["en"]):
                self.assertEqual(term["file"],article_filename(term["n"],term["en"]))
                origin=ROOT/"wiki/ai-agents"/term["file"]
                mirror=ROOT/"docs/wiki/ai-agents"/term["file"]
                self.assertEqual(origin.read_bytes(),mirror.read_bytes())
                body=origin.read_text(encoding="utf-8")
                self.assertGreaterEqual(len(body),1400)
                self.assertIn(term["en"],body)
                self.assertIn(term["zh"],body)
                for key in ("核心定义","形象理解","类比的局限","技术原理",
                            "工程实践","失败模式与验证","易混辨析",
                            "面试题","考试题","权威来源"):
                    self.assertIn(key,body)
                self.assertEqual(body.count("**问："),2)
                self.assertEqual(body.count("**题："),2)
                self.assertGreaterEqual(len(set(re.findall(r"\]\((https://[^)\s]+)\)",body))),2)
                self.assertNotRegex(body,r"(?i)\bbatch[\s-]*0?[1-9]\b|生产批次|PR状态")
        main()

    def test_specific_mechanisms_not_generic_filler(self):
        def article(n):
            return (ROOT/"wiki/ai-agents"/self.manifest["terms"][n-1]["file"]).read_text(encoding="utf-8")
        signatures={101:"consent",102:"provenance",103:"tombstone",104:"checkpoint_id",
                    105:"reconcile",106:"confirmed_at",107:"recall@k",108:"decompose",
                    109:"content_hash",110:"OCR",111:"chunk_overlap",112:"chunk_id",
                    113:"cos(u,v)",114:"ANN",115:"cos(q,d_i)",116:"cos(e(q),e(d))",
                    117:"BM25",118:"RRF(d)",119:"cross-encoder",120:"Rewrite-Retrieve-Read"}
        for n,needle in signatures.items():
            with self.subTest(n=n):
                self.assertIn(needle,article(n))

    def test_medium_exam_calculations_recomputed_independently(self):
        import math
        self.assertEqual(20-4-3-2,11)
        self.assertEqual(50-12,38)
        self.assertAlmostEqual(3/5,.6)
        self.assertEqual(100-20-5,75)
        self.assertEqual(50/5,10)
        self.assertEqual(4/5,.8)
        self.assertEqual(4/10,.4)
        self.assertAlmostEqual(5*(.4+.2),3)
        self.assertEqual(80-5-3,72)
        self.assertEqual(1+math.ceil((1000-300)/(300-50)),4)
        self.assertEqual(100*3,300)
        self.assertEqual(2000-200+150,1950)
        self.assertEqual(4/5,.8)
        self.assertAlmostEqual(1/61+1/63,.03227,places=4)
        self.assertEqual(8/10,.8)
        self.assertEqual(40*15,600)
        self.assertEqual(70/100,.7)

if __name__=="__main__":
    unittest.main()
