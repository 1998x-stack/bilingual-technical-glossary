"""Regression coverage for the canonical JSON-to-CSV export contract."""
import csv
import json
import unittest
from io import StringIO
from pathlib import Path

from scripts.corpus_integrity import csv_differences


ROOT = Path(__file__).resolve().parents[1]


def as_csv(terms, columns):
    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=columns)
    writer.writeheader()
    writer.writerows(terms)
    buf.seek(0)
    reader = csv.DictReader(buf)
    return reader.fieldnames, list(reader)


class CorpusIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.term = {
            "category": "calculus",
            "chapter": 1,
            "topic": "基础概念",
            "en": "Derivative",
            "zh": "导数",
            "abbr": "",
            "definition": "函数的瞬时变化率",
            "notation": "f'(x)",
        }

    def test_repository_csv_matches_json_cell_by_cell(self):
        terms = json.loads((ROOT / "data/terms.json").read_text(encoding="utf-8"))
        with (ROOT / "data/terms.csv").open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            problems = csv_differences(terms, reader.fieldnames, list(reader))
        self.assertEqual(problems, [])

    def test_extra_field_is_not_discarded(self):
        columns = [key for key in self.term if key != "notation"]
        headings, rows = as_csv([{k: self.term[k] for k in columns}], columns)
        problems = csv_differences([self.term], headings, rows)
        self.assertTrue(any("notation" in problem for problem in problems))

    def test_changed_translation_fails_even_if_row_count_matches(self):
        headings, rows = as_csv([self.term], list(self.term))
        rows[0]["zh"] = "错误译名"
        self.assertTrue(csv_differences([self.term], headings, rows))

    def test_reordered_rows_fail(self):
        other = dict(self.term, en="Integral", zh="积分")
        headings, rows = as_csv([self.term, other], list(self.term))
        self.assertTrue(csv_differences([other, self.term], headings, rows))

    def test_count_change_fails(self):
        headings, rows = as_csv([self.term], list(self.term))
        self.assertTrue(csv_differences([self.term, self.term], headings, rows))

    def test_full_schema_supports_new_optional_fields(self):
        extended = dict(self.term, example="dy / dx")
        headings, rows = as_csv([extended], list(extended))
        self.assertEqual(csv_differences([extended], headings, rows), [])


class PublishingInvariantsTests(unittest.TestCase):
    def test_static_site_is_mirrored(self):
        for name in ("index.html", "app.js", "styles.css", "favicon.svg", "term.html", "term.css", "term.js"):
            with self.subTest(name=name):
                self.assertEqual(
                    (ROOT / "site" / name).read_bytes(),
                    (ROOT / "docs" / name).read_bytes(),
                )

    def test_navigation_survives_rebuild(self):
        page = (ROOT / "site/index.html").read_text(encoding="utf-8")
        self.assertIn('id="explorer"', page)
        self.assertNotIn('href="./wiki/ai-infrastructure/index.html"', page)
        detail = (ROOT / "site/term.html").read_text(encoding="utf-8")
        self.assertIn('id="detail-content"', detail)
        self.assertIn("./pdf/computer-organization.pdf", page)
        self.assertIn("./glossaries/computer-organization.md", page)


if __name__ == "__main__":
    unittest.main()
