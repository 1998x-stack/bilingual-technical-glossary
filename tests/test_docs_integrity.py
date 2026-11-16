"""Offline documentation integrity test suite."""
import json
import tempfile
import unittest
from pathlib import Path

from scripts.verify_docs import check_documentation, local_link_errors

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_repository_documentation(self):
        self.assertEqual(check_documentation(ROOT), [])

    def test_offline_missing_local_link(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            (root / "README.md").write_text("# Test\n[missing](missing-file.md)\n", encoding="utf-8")
            self.assertTrue(any("broken local link" in x for x in local_link_errors(root, ("README.md",))))

    def test_external_link_and_anchor_do_not_cause_false_failure(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            (root / "README.md").write_text(
                "# Test\n[external](https://docs.python.org/3/)\n[anchor](#top)\n", encoding="utf-8"
            )
            self.assertEqual(local_link_errors(root, ("README.md",)), [])

    def test_published_ai_infra_tsv_matches_source(self):
        self.assertEqual((ROOT / "data/ai-infrastructure.tsv").read_bytes(),
                         (ROOT / "docs/data/ai-infrastructure.tsv").read_bytes())

    def test_dataset_counts_are_computed_not_assumed(self):
        catalog = json.loads((ROOT / "docs/data/catalog.json").read_text(encoding="utf-8"))
        terms = json.loads((ROOT / "data/terms.json").read_text(encoding="utf-8"))
        self.assertEqual(sum(c["count"] for c in catalog), len(terms))
        self.assertEqual(len(catalog), len({t["category"] for t in terms}))


if __name__ == "__main__":
    unittest.main()
