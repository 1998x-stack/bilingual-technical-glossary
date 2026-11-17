"""AI Agents Wiki corpus, source order, article quality and mirror tests."""
import json
import unittest
from pathlib import Path
from scripts.verify_ai_agents_wiki import canonical_rows, article_filename, main, ROOT

class AIAgentsWikiTests(unittest.TestCase):
    def test_source_and_batch_plan(self):
        rows = canonical_rows()
        self.assertEqual(len(rows), 332)
        self.assertEqual(rows[0]["en"], "AI Agent")
        self.assertEqual(rows[19]["en"], "Observation")
        self.assertEqual(rows[20]["en"], "Action")
        self.assertEqual(rows[-1]["chapter"], 16)
        self.assertEqual(article_filename(4, rows[3]["en"]), "004-large-language-model.md")

    def test_mirrors_manifest_and_index(self):
        main()

    def test_review_ledger_starts_honestly_pending(self):
        manifest = json.loads((ROOT / "docs/wiki/ai-agents/manifest.json").read_text())
        ledger = json.loads((ROOT / "wiki/reviews/ai-agents.json").read_text())
        self.assertEqual(len(ledger["articles"]), manifest["readyInPr"])
        self.assertTrue(all(x["status"] == "pending" for x in ledger["articles"]))

if __name__ == "__main__":
    unittest.main()
