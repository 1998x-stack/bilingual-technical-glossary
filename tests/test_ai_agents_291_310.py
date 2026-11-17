"""AI Agents 291–310: canonical identity, mirrors, exercises and state checks."""
import json
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def filename(n,en):
    base=re.sub(r"\([^)]*\)","",en).strip().lower()
    return f"{n:03d}-"+re.sub(r"[^a-z0-9]+","-",base).strip("-")+".md"
class TestAgents291310(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=json.loads((ROOT/"docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.b=json.loads((ROOT/"wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.r=json.loads((ROOT/"wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))
        cls.i=json.loads((ROOT/"docs/data/wiki-index.json").read_text(encoding="utf-8"))
    def test_contiguous_articles(self):
        self.assertGreaterEqual(self.m["readyArticles"],310)
        for n in range(291,311):
            t=self.m["terms"][n-1];name=filename(n,t["en"])
            self.assertEqual(t["file"],name)
            self.assertTrue(t["ready"])
            src=ROOT/"wiki/ai-agents"/name
            mirror=ROOT/"docs/wiki/ai-agents"/name
            self.assertEqual(src.read_bytes(),mirror.read_bytes())
            text=src.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(text),1800)
            self.assertIn(t["en"],text)
            self.assertIn(t["zh"],text)
            for h in ("## 1. 核心定义","## 2. 形象理解","## 3. 技术原理","## 4. 工程实践","## 5. 关联知识与易混辨析","## 6. 中等难度面试题","## 7. 中等难度考试题","## 8. 权威来源"):
                self.assertIn(h,text)
            self.assertEqual(text.count("**问："),2)
            self.assertEqual(text.count("**题："),2)
            self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)]+\)",text)),2)
            self.assertIn({"path":"wiki/ai-agents/"+name,"status":"pending"},self.r["articles"])
            self.assertEqual(self.b["batches"][(n-1)//20]["terms"][(n-1)%20]["status"],"drafted_in_pr")
    def test_index(self):
        a=[x for x in self.i["articles"] if x["category"]=="ai-agents"]
        self.assertGreaterEqual(len(a),310)
        self.assertEqual([v["en"] for v in a[290:310]],[x["en"] for x in self.m["terms"][290:310]])
    def test_calculations(self):
        checks={291:"18 MB",292:"94%",295:"2.4 秒",296:"2.5 tasks/s",298:"2.5 倍",299:"8 个令牌",300:"2,300 tokens",302:"$0.25",303:"$2.50",305:"50ms",307:"30%",308:"20 个",309:"99.8001%",310:"80%"}
        for n,expected in checks.items():
            text=(ROOT/"wiki/ai-agents"/filename(n,self.m["terms"][n-1]["en"])).read_text(encoding="utf-8")
            self.assertIn(expected,text)
if __name__=="__main__":unittest.main()
