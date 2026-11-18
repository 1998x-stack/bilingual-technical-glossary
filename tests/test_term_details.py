"""Reader-facing term detail and published Wiki integration contracts."""
import json
import re
import unittest
from pathlib import Path

from scripts.build_wiki_index import generate_index, check_index

ROOT = Path(__file__).resolve().parents[1]


class TermDetailTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus = json.loads((ROOT / "data/terms.json").read_text(encoding="utf-8"))
        cls.index = json.loads((ROOT / "docs/data/wiki-index.json").read_text(encoding="utf-8"))
        cls.app = (ROOT / "site/app.js").read_text(encoding="utf-8")
        cls.detail = (ROOT / "site/term.js").read_text(encoding="utf-8")

    def test_published_wiki_index_is_deterministic_and_synced(self):
        self.assertEqual(self.index, generate_index(ROOT))
        check_index(ROOT)
        self.assertEqual(self.index["schemaVersion"], 1)
        manifests = sorted((ROOT / "docs/wiki").glob("*/manifest.json"))
        expected = sum(sum(1 for entry in json.loads(p.read_text(encoding="utf-8"))["terms"] if entry["ready"]) for p in manifests)
        self.assertEqual(len(self.index["articles"]), expected)

    def test_public_index_uses_real_glossary_identity(self):
        identities = {
            (r["category"], r["chapter"], r["en"], r["zh"]) for r in self.corpus
        }
        seen = set()
        for page in self.index["articles"]:
            key = (page["category"], page["chapter"], page["en"], page["zh"])
            self.assertIn(key, identities)
            self.assertNotIn(key, seen)
            seen.add(key)
            self.assertRegex(page["path"], r"^wiki/[a-z0-9-]+/[0-9]{3}-[a-z0-9-]+\.md$")
            self.assertTrue((ROOT / "docs" / page["path"]).is_file())
            self.assertFalse(any(k in page for k in ("batch", "status", "readyInPr")))
        self.assertEqual(len(seen), len(self.index['articles']))

    def test_reinforcement_learning_and_all_categories_have_clickthrough(self):
        rl = [r for r in self.corpus if r["category"] == "reinforcement-learning"]
        self.assertGreater(len(rl), 0)
        self.assertIn("const url=escaped(termURL(item))", self.app)
        self.assertIn('class="term-english term-link"', self.app)
        self.assertIn('class="term-chinese term-link"', self.app)
        self.assertIn("state.wikiLinks.has(termKey(item))", self.app)
        self.assertIn("category:term.category", self.app)
        self.assertIn("chapter:String(term.chapter)", self.app)

    def test_reader_opens_full_article_or_honest_fallback(self):
        self.assertIn("wiki.articles.find(a => termKey(a) === termKey(entry))", self.detail)
        self.assertIn("entry.definition", self.detail)
        self.assertIn("wiki-fallback", self.detail)
        self.assertIn("No matching term", self.detail)
        self.assertIn("return-explorer", self.detail)
        self.assertIn("detail-neighbors", (ROOT / "site/term.html").read_text(encoding="utf-8"))

    def test_no_batch_navigation_on_public_pages(self):
        pages = [
            ROOT / "site/index.html",
            ROOT / "site/term.html",
            ROOT / "docs/wiki/ai-infrastructure/index.html",
        ]
        for path in pages:
            with self.subTest(path=path):
                content = path.read_text(encoding="utf-8")
                self.assertNotRegex(content, r"(?i)batch\s*0?[1-9]|batches|批次|BATCH-0")
        home = pages[0].read_text(encoding="utf-8")
        self.assertNotIn('href="./wiki/ai-infrastructure/index.html"', home)
        self.assertIn('id="explorer"', home)

    def test_legacy_wiki_landing_redirects_to_explorer_or_term(self):
        legacy = (ROOT / "docs/wiki/ai-infrastructure/index.html").read_text(encoding="utf-8")
        self.assertIn("location.replace(fallback)", legacy)
        self.assertIn("location.replace('../../term.html?'", legacy)

    def test_unsafe_wiki_links_not_executed_as_html(self):
        self.assertIn("escapeHTML(raw)", self.detail)
        self.assertIn("target.origin !== location.origin", self.detail)
        self.assertIn("url.protocol === 'https:' || url.protocol === 'http:'", self.detail)
        self.assertIn("/^wiki\\/[a-z0-9-]+", self.detail)


if __name__ == "__main__":
    unittest.main()
