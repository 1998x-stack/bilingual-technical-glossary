"""The final 12 AI Agent terms must be mirrored, indexed and grounded."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def wiki_filename(n, en):
    slug = re.sub(r"[^a-z0-9]+", "-", re.sub(r"\([^)]*\)", "", en).strip().lower()).strip("-")
    return f"{n:03d}-{slug}.md"

class TestAgents321332(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads((ROOT / "docs/wiki/ai-agents/manifest.json").read_text(encoding="utf-8"))
        cls.b = json.loads((ROOT / "wiki/ai-agents/batches.json").read_text(encoding="utf-8"))
        cls.r = json.loads((ROOT / "wiki/reviews/ai-agents.json").read_text(encoding="utf-8"))
        cls.i = json.loads((ROOT / "docs/data/wiki-index.json").read_text(encoding="utf-8"))

    def test_last_batch_articles(self):
        self.assertEqual(self.m["readyArticles"], 332)
        self.assertEqual(self.m["readyInPr"], 332)
        self.assertEqual(self.m["total"], 332)
        self.assertEqual(len(self.m["terms"]), 332)
        self.assertTrue(all(x["ready"] for x in self.m["terms"]))
        for n in range(321, 333):
            t = self.m["terms"][n-1]
            filename = wiki_filename(n, t["en"])
            self.assertEqual(t["n"], n)
            self.assertEqual(t["file"], filename)
            src = ROOT / "wiki/ai-agents" / filename
            mirror = ROOT / "docs/wiki/ai-agents" / filename
            self.assertEqual(src.read_bytes(), mirror.read_bytes())
            content = src.read_text(encoding="utf-8")
            self.assertGreaterEqual(len(content), 1800)
            self.assertIn(t["en"], content)
            self.assertIn(t["zh"], content)
            for h in ("## 1. 核心定义", "## 2. 形象理解",
                      "## 3. 技术原理", "## 4. 工程实践",
                      "## 5. 关联知识与易混辨析", "## 6. 中等难度面试题",
                      "## 7. 中等难度考试题", "## 8. 权威来源", "类比的局限"):
                self.assertIn(h, content)
            self.assertEqual(content.count("**问："), 2)
            self.assertEqual(content.count("**题："), 2)
            self.assertGreaterEqual(len(re.findall(r"\]\(https://[^)]+\)", content)), 2)
            self.assertIn({"path": "wiki/ai-agents/" + filename, "status": "pending"}, self.r["articles"])
            bterm = self.b["batches"][(n-1)//20]["terms"][(n-1)%20]
            self.assertEqual(bterm["status"], "drafted_in_pr")
            self.assertEqual(bterm["wiki"], "wiki/ai-agents/" + filename)

    def test_full_index_and_reviews(self):
        articles = [a for a in self.i["articles"] if a["category"] == "ai-agents"]
        self.assertEqual(len(articles), 332)
        self.assertGreaterEqual(len(self.i["articles"]), 474)  # other Wiki domains may be added
        self.assertEqual(sum(a["category"] == "ai-infrastructure" for a in self.i["articles"]), 142)
        self.assertEqual(len(self.r["articles"]), 332)
        self.assertEqual([x["en"] for x in articles], [x["en"] for x in self.m["terms"]])
        self.assertEqual(len(set(x["path"] for x in articles)), 332)
        self.assertEqual(self.b["batches"][-1]["status"], "drafted_in_pr")
        self.assertTrue(all(x["status"] == "pending" for x in self.r["articles"]))

    def test_example_reasoning(self):
        expected = {
            321: "8 秒", 322: "10 秒", 323: "7 秒",
            324: "2300 tokens", 325: "9 个",
            326: "2 次", 327: "83.33%", 328: "96%",
            329: "2,000 个", 330: "18 个提交",
            331: "6 分钟", 332: "18 分钟",
        }
        for n, phrase in expected.items():
            file = ROOT / "wiki/ai-agents" / wiki_filename(n, self.m["terms"][n-1]["en"])
            self.assertIn(phrase, file.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
