"""Regression tests for non-mutating CI publication architecture."""
from pathlib import Path
import tempfile
import unittest

from scripts.verify_workflow_policy import check_workflows, ROOT

class WorkflowSafetyTests(unittest.TestCase):
    def test_checked_in_publication_workflows_are_safe(self):
        self.assertEqual(check_workflows(ROOT), [])

    def test_detects_repository_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            base=root/'.github/workflows';base.mkdir(parents=True)
            for i in range(10):
                (base/f'safe-{i}.yml').write_text('permissions:\n  contents: read\n',encoding='utf-8')
            (base/'unsafe.yml').write_text('permissions:\n  contents: write\nsteps:\n  - run: git push origin HEAD:main\n')
            errors=check_workflows(root)
            self.assertTrue(any('git push' in error for error in errors))
            self.assertTrue(any('contents:write' in error for error in errors))

if __name__=='__main__':
    unittest.main()
