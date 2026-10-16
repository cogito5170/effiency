import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_modules  # noqa: E402

MODULES = ROOT / "docs" / "workspace-context" / "modules"


class ModuleContractTest(unittest.TestCase):
    def test_workspace_modules_follow_contract(self):
        self.assertEqual(check_modules.check(MODULES), [])

    def copy(self) -> Path:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        dst = tmp / "modules"
        shutil.copytree(MODULES, dst)
        return dst

    def edit(self, root: Path, module: str, fname: str, fn) -> None:
        path = next(root.glob(f"{module}-*")) / fname
        data = json.loads(path.read_text(encoding="utf-8"))
        fn(data)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_model_claim_cannot_be_confirmed(self):
        root = self.copy()
        self.edit(root, "W1", "state.json", lambda s: s["confirmed"][0].update(source="추론·미검증"))
        self.assertTrue(any("출처" in e for e in check_modules.check(root)))

    def test_cycle_is_rejected(self):
        root = self.copy()

        def add_call(ops):
            ops[0]["calls"] = ["W2.storyline"]
        self.edit(root, "W5", "ops.json", add_call)
        self.edit(root, "W5", "module.json", lambda m: m.update(consumes=["W2.storyline"]))
        errors = check_modules.check(root)
        self.assertTrue(any("순환" in e for e in errors), errors)

    def test_undeclared_dependency_is_rejected(self):
        root = self.copy()
        self.edit(root, "W2", "module.json", lambda m: m.update(consumes=[]))
        self.assertTrue(any("consumes" in e for e in check_modules.check(root)))


if __name__ == "__main__":
    unittest.main()
