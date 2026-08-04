import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class NotebookStructureTest(unittest.TestCase):
    def test_repository_contains_notebooks(self):
        self.assertGreater(len(list(ROOT.rglob("*.ipynb"))), 0)

    def test_all_notebooks_are_valid_jupyter_documents(self):
        for path in ROOT.rglob("*.ipynb"):
            with self.subTest(path=path.relative_to(ROOT)):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(notebook.get("nbformat"), 4)
                self.assertIsInstance(notebook.get("cells"), list)
                self.assertIn("metadata", notebook)
                for cell in notebook["cells"]:
                    self.assertIn(cell.get("cell_type"), {"code", "markdown", "raw"})
                    self.assertIsInstance(cell.get("source"), list)


if __name__ == "__main__":
    unittest.main()
