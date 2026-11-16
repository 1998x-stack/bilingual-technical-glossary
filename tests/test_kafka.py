import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
TERMS = json.loads((ROOT / "data" / "terms.json").read_text(encoding="utf-8"))
class KafkaGlossaryTests(unittest.TestCase):
    def test_coverage(self):
        rows = [x for x in TERMS if x["category"] == "apache-kafka"]
        self.assertEqual(len(rows), 283)
        self.assertEqual(sorted({x["chapter"] for x in rows}), list(range(1, 17)))
        self.assertEqual(len({x["topic"] for x in rows}), 16)
    def test_publications(self):
        for file in ("glossaries/apache-kafka.md", "pdf/apache-kafka.pdf",
                     "docs/glossaries/apache-kafka.md", "docs/pdf/apache-kafka.pdf"):
            self.assertTrue((ROOT / file).is_file(), file)
if __name__ == "__main__":
    unittest.main()
