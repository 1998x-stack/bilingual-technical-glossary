"""Regress AI Agent terms 311–320: identity, mirrored pages, exam work and source."""
import json
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def name(n,en):
    base=re.sub(r"\([^)]*\)","",en).strip().lower()
    return f"{n:03d}-"+re.sub(r"[^a-z0-9]+","-",base).strip("-")+".md"
class TestAgents311320(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.b=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.r=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))
        cls.i=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
    def test_articles(self):
        self.assertGreaterEqual(self.m["readyArticles"],320)
        for n in range(311,321):
            entry=self.m["terms"][n-1];fn=name(n,entry["en"])
            self.assertTrue(entry["ready"])
            self.assertEqual(entry["file"],fn)
            a=ROOT/"wiki/ai-agents"/fn;b=ROOT/"docs/wiki/ai-agents"/fn
            self.assertEqual(a.read_bytes(),b.read_bytes())
            body=a.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(body),1900)
            self.assertIn(entry["en"],body)
            self.assertIn(entry["zh"],body)
            for h in ("核心定义","形象理解","技术原理","工程实践","关联知识与易混辨析","面试题","考试题","权威来源","类比的局限"):
                self.assertIn(h,body)
            self.assertEqual(body.count("**问："),2)
            self.assertEqual(body.count("**题："),2)
            self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)]+\)",body)),2)
            self.assertIn({"path":"wiki/ai-agents/"+fn,"status":"pending"},self.r["articles"])
            self.assertEqual(self.b["batches"][(n-1)//20]["terms"][(n-1)%20]["status"],"drafted_in_pr")
    def test_index_identity(self):
        a=[e for e in self.i["articles"] if e["category"]=="ai-agents"]
        self.assertGreaterEqual(len(a),320)
        self.assertEqual([e["en"] for e in a[310:320]],[e["en"] for e in self.m["terms"][310:320]])
    def test_examples(self):
        expected={311:"60 分钟",312:"25%",313:"5%",314:"6 个文件",315:"20%",316:"90%",317:"3 个",318:"15 个",319:"缺少 1 个",320:"不合规"}
        for n,phrase in expected.items():
            content=(ROOT/"wiki/ai-agents"/name(n,self.m["terms"][n-1]["en"])).read_text(encoding="utf-8")
            self.assertIn(phrase,content)
if __name__=="__main__":unittest.main()
