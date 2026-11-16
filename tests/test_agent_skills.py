"""Regression tests for portable TERM/ATLAS Agent Skills."""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from sync_agent_skills import MIRRORS, REQUIRED, SOURCE, parse_frontmatter, sync_repository, validate_repository


class TestAgentSkills(unittest.TestCase):
    def test_checked_in_skills_have_no_drift(self):
        self.assertEqual(validate_repository(ROOT), [])

    def test_frontmatter_rejects_missing_name(self):
        content = b"---\ndescription: Use when authoring a glossary entry with references.\n---\n# A\n" + b"detail " * 100
        self.assertTrue(any("name" in x or "metadata" in x for x in parse_frontmatter(content, "example-skill")))

    def test_detect_and_repair_mirror_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for location in (SOURCE, *MIRRORS):
                shutil.copytree(ROOT / location, root / location)
            self.assertEqual(validate_repository(root), [])
            changed = root / MIRRORS[0] / sorted(REQUIRED)[0] / "SKILL.md"
            changed.write_text(changed.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
            self.assertTrue(any("content differs" in x for x in validate_repository(root)))
            sync_repository(root)
            self.assertEqual(validate_repository(root), [])

    def test_reject_unexpected_skill_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for location in (SOURCE, *MIRRORS):
                shutil.copytree(ROOT / location, root / location)
            (root / MIRRORS[1] / "unexpected").mkdir()
            self.assertTrue(any("expected" in x for x in validate_repository(root)))


if __name__ == "__main__":
    unittest.main()
