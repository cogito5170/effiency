import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_resume  # noqa: E402
import check_modules  # noqa: E402
import subprocess  # noqa: E402
import sync_delta  # noqa: E402

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

    def test_superseded_decision_must_leave_state(self):
        root = self.copy()

        def keep_old(s):
            s["decisions"].insert(0, {"id": "W1-D3", "decision": "옛 결정", "supersedes": None})
        self.edit(root, "W1", "state.json", keep_old)
        self.assertTrue(any("history.jsonl" in e for e in check_modules.check(root)))

    def test_supersedes_may_point_into_history(self):
        root = self.copy()
        hist = next(root.glob("W1-*")) / "history.jsonl"
        ids = [json.loads(x)["id"] for x in hist.read_text(encoding="utf-8").splitlines() if '"decision"' in x and json.loads(x).get("kind") == "decision"]
        self.assertTrue(ids)
        hist.write_text("", encoding="utf-8")
        self.assertTrue(any("앞선 결정" in e for e in check_modules.check(root)))

    def test_resume_is_capped_and_deterministic(self):
        root = self.copy()
        self.edit(root, "W2", "state.json", lambda s: s.update(latest_confirmed="가" * 5000))
        build_resume.build(root)
        first = {p: p.read_text(encoding="utf-8") for p in root.glob("W*/RESUME.md")}
        build_resume.build(root)
        for p, text in first.items():
            self.assertLessEqual(len(text), build_resume.MAX_CHARS)
            self.assertEqual(text, p.read_text(encoding="utf-8"))
        self.assertEqual(check_modules.check(root), [])

    def test_committed_resume_matches_state(self):
        root = self.copy()
        build_resume.build(root)
        for p in root.glob("W*/RESUME.md"):
            committed = MODULES / p.parent.name / "RESUME.md"
            self.assertEqual(p.read_text(encoding="utf-8"), committed.read_text(encoding="utf-8"), p.parent.name)

    def test_sync_delta_reads_only_after_checkpoint(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        origin, clone = tmp / "origin.git", tmp / "demo"
        run = lambda *a, cwd=None: subprocess.run(a, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()
        run("git", "init", "-q", "--bare", "-b", "main", str(origin))
        run("git", "clone", "-q", str(origin), str(clone))
        for i in range(3):
            (clone / "f.txt").write_text(str(i))
            run("git", "add", ".", cwd=clone)
            run("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", f"c{i}", cwd=clone)
            if i == 0:
                base = run("git", "rev-parse", "--short", "HEAD", cwd=clone)
        run("git", "push", "-q", "origin", "main", cwd=clone)
        run("git", "fetch", "-q", cwd=clone)
        mods = tmp / "modules" / "W9-demo"
        mods.mkdir(parents=True)
        (mods / "state.json").write_text(json.dumps({"module": "W9", "as_of": "2000-01-01T00:00Z",
                                                     "checkpoint": {"at": "2000-01-01T00:00Z", "refs": {"demo@main": base}}}))
        res = sync_delta.delta(tmp / "modules", [clone])
        commits = res["modules"]["W9"]["refs"]["demo@main"]["commits"]
        self.assertEqual([c["subject"] for c in commits], ["c1", "c2"])


if __name__ == "__main__":
    unittest.main()
