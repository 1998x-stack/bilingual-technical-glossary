"""Regression: AI Agents 271–290 article identity, double mirror and exercises."""
import json
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def name(n,en):
    slug=re.sub(r"[^a-z0-9]+","-",re.sub(r"\([^)]*\)","",en).strip().lower()).strip("-")
    return f"{n:03d}-{slug}.md"
class TestAgents271290(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.b=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.i=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.r=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))
    def test_article_structure_and_mirrors(self):
        self.assertGreaterEqual(self.m["readyArticles"],290)
        for n in range(271,291):
            row=self.m["terms"][n-1]; fn=name(n,row["en"])
            self.assertEqual(row["file"],fn)
            self.assertTrue(row["ready"])
            a=ROOT/"wiki/ai-agents"/fn
            d=ROOT/"docs/wiki/ai-agents"/fn
            self.assertEqual(a.read_bytes(),d.read_bytes())
            body=a.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(body),1400)
            self.assertIn(row["en"],body)
            self.assertIn(row["zh"],body)
            for phrase in ("核心定义","形象理解","技术原理","工程实践","易混辨析","面试题","考试题","权威来源","类比的局限"):
                self.assertIn(phrase,body)
            self.assertGreaterEqual(body.count("**问："),2)
            self.assertGreaterEqual(body.count("**题："),2)
            self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)]+\)",body)),2)
            self.assertIn({"path":"wiki/ai-agents/"+fn,"status":"pending"},self.r["articles"])
            self.assertEqual(self.b["batches"][(n-1)//20]["terms"][(n-1)%20]["status"],"drafted_in_pr")
    def test_index(self):
        rows=[a for a in self.i["articles"] if a["category"]=="ai-agents"]
        self.assertGreaterEqual(len(rows),290)
        self.assertEqual([a["en"] for a in rows[270:290]],[a["en"] for a in self.m["terms"][270:290]])
    def test_math_examples(self):
        checks={271:"15%",275:"3.5%",277:"0.4%",280:"6%",282:"2.5%",285:"6 美元",286:"80 个 Span",288:"900ms",289:"350ms",290:"10 条"}
        for n,answer in checks.items():
            txt=(ROOT/"wiki/ai-agents"/name(n,self.m["terms"][n-1]["en"])).read_text(encoding="utf-8")
            self.assertIn(answer,txt)
if __name__=="__main__":unittest.main()
