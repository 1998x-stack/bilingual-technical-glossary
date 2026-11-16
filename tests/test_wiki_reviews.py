"""Assurance that 'pending' articles cannot be mistaken for human-reviewed."""
import unittest
from scripts.verify_wiki_reviews import audit, ROOT

class ReviewLedgerTests(unittest.TestCase):
    def test_ledger_is_complete_with_honest_status(self):
        errors,warnings,verified,total=audit(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(total,40)
        self.assertEqual(verified,0)
        self.assertTrue(any("pending" in warning for warning in warnings))
if __name__=="__main__":unittest.main()
