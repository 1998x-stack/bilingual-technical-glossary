"""Assurance that all published articles are covered, pending remains honest."""
import json
from pathlib import Path
import unittest
from scripts.verify_wiki_reviews import audit, ROOT

class ReviewLedgerTests(unittest.TestCase):
    def test_ledger_is_complete_with_honest_status(self):
        errors,warnings,verified,total=audit(ROOT)
        self.assertEqual(errors, [])
        published=json.loads((ROOT/'docs/data/wiki-index.json').read_text(encoding='utf-8'))
        self.assertEqual(total, len(published['articles']))
        self.assertGreaterEqual(total, 60)
        self.assertLessEqual(verified, total)
        if verified < total:
            self.assertTrue(any('pending' in warning for warning in warnings))
if __name__=="__main__":unittest.main()
