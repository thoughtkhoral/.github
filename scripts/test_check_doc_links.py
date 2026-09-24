import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).with_name("check_doc_links.py")


class DocumentationLinkCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.root = self.workspace / "project"
        self.org = self.workspace / "org"
        self.root.mkdir()
        self.org.mkdir()

    def run_check(self):
        return subprocess.run(
            [sys.executable, str(CHECKER), "--root", str(self.root), "--org", str(self.org)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_accepts_existing_relative_and_organization_links(self):
        (self.root / "docs").mkdir()
        (self.root / "docs" / "roadmap.md").write_text("# Roadmap\n")
        contracts = self.root / "thought-khoral-contracts"
        contracts.mkdir()
        (contracts / "protocol.md").write_text("# Protocol\n")
        (self.root / "README.md").write_text(
            "[Roadmap](docs/roadmap.md) and "
            "[Protocol](https://github.com/thoughtkhoral/thought-khoral-contracts/blob/main/protocol.md)\n"
        )
        (self.org / "README.md").write_text(
            "[Project](https://github.com/thoughtkhoral/thought-khoral)\n"
        )

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_missing_relative_target(self):
        (self.root / "README.md").write_text("[Missing](docs/roadmap.md)\n")

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("docs/roadmap.md", result.stdout)

    def test_rejects_missing_organization_target(self):
        contracts = self.root / "thought-khoral-contracts"
        contracts.mkdir()
        (self.root / "README.md").write_text(
            "[Missing](https://github.com/thoughtkhoral/thought-khoral-contracts/blob/main/protocol.md)\n"
        )

        result = self.run_check()

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("thought-khoral-contracts/blob/main/protocol.md", result.stdout)

    def test_ignores_historical_worktree_reports(self):
        report = self.root / ".superpowers" / "sdd" / "old-report.md"
        report.parent.mkdir(parents=True)
        report.write_text("[Old design](../../missing.md)\n")
        (self.root / "README.md").write_text("# Current project\n")

        result = self.run_check()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
