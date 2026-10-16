"""모듈(W1~W6)마다 마지막 동기화 지점(checkpoint) 뒤에 저장소에서 바뀐 것만 짧게 뽑는다.

    python3 scripts/sync_delta.py docs/workspace-context/modules --git ../gentleMonster --git .
    python3 scripts/sync_delta.py <modules> --git … --json        # 기계가 읽을 형태

세션 원본(대화 기록)은 읽지도 고치지도 않는다. 세션은 의뢰인이 쓰는 것이라 압축할 수 없다고 보고,
쌓이는 문제는 읽는 쪽에서 푼다: 확정 사항은 저장소 커밋으로 남으므로 체크포인트 커밋 뒤의 커밋 제목과
바뀐 파일만 보면 된다. 대화를 다시 읽어야 할 때도 이 출력이 가리키는 파일 · 시간대만 본다.

출력:
- 모듈마다 checkpoint.refs 의 각 브랜치에서 `<commit>..origin/<ref>` 커밋(시간 · 제목 · 바뀐 파일 수)
- 어느 모듈 checkpoint 에도 없는 브랜치 중 가장 이른 checkpoint 뒤에 커밋이 생긴 것 (새 세션 · 새 브랜치 후보)
표준 라이브러리만 쓴다. 모델 호출 없음.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HEX = re.compile(r"^[0-9a-f]{7,40}$")


def git(clone: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(clone), *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def refs_of(state: dict) -> dict[str, str]:
    """checkpoint.refs 가 있으면 그것, 없으면 예전 synced_from.branches_checked 에서 커밋처럼 보이는 값만."""
    cp = state.get("checkpoint", {}).get("refs")
    if cp:
        return dict(cp)
    out = {}
    for key, val in state.get("synced_from", {}).get("branches_checked", {}).items():
        first = str(val).split()[0] if val else ""
        if HEX.match(first):
            out[key] = first
    return out


def clone_for(clones: list[Path], repo_key: str) -> Path | None:
    name = repo_key.split("@")[0].lower()
    for c in clones:
        if c.resolve().name.lower() == name:
            return c
    return None


def delta(root: Path, clones: list[Path]) -> dict:
    result: dict = {"modules": {}, "unassigned": []}
    known: set[tuple[str, str]] = set()
    earliest = None
    for d in sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith("W")):
        state = json.loads((d / "state.json").read_text(encoding="utf-8"))
        mid = d.name.split("-")[0]
        at = state.get("checkpoint", {}).get("at") or state.get("as_of")
        earliest = min(earliest or at, at)
        mod = {"checkpoint_at": at, "refs": {}}
        for key, commit in refs_of(state).items():
            repo, _, ref = key.partition("@")
            known.add((repo.lower(), ref))
            clone = clone_for(clones, key)
            if clone is None:
                mod["refs"][key] = {"skipped": "클론 없음"}
                continue
            tip = git(clone, "rev-parse", "--short", f"origin/{ref}").strip()
            if not tip:
                mod["refs"][key] = {"skipped": "원격에 없음"}
                continue
            log = git(clone, "log", "--reverse", "--format=%h\t%cI\t%s", "--shortstat", f"{commit}..origin/{ref}")
            commits = []
            for line in log.splitlines():
                if "\t" in line:
                    h, t, s = line.split("\t", 2)
                    commits.append({"commit": h, "at": t[:16], "subject": s})
                elif line.strip() and commits:
                    commits[-1]["files"] = int(line.split()[0])
            if commits:
                mod["refs"][key] = {"from": commit, "tip": tip, "commits": commits}
        result["modules"][mid] = mod
    for clone in clones:
        repo = clone.resolve().name.lower()
        out = git(clone, "for-each-ref", "--format=%(refname:short)\t%(committerdate:iso-strict)", "refs/remotes/origin")
        for line in out.splitlines():
            ref, _, t = line.partition("\t")
            ref = ref.removeprefix("origin/")
            if ref in ("HEAD", "origin") or (repo, ref) in known:
                continue
            if earliest and t[:16] > earliest.replace("Z", "")[:16]:
                result["unassigned"].append({"repo": repo, "ref": ref, "last_commit_at": t[:16]})
    return result


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("root", type=Path)
    ap.add_argument("--git", type=Path, action="append", default=[])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    res = delta(args.root, args.git)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0
    for mid, mod in res["modules"].items():
        n = sum(len(v.get("commits", [])) for v in mod["refs"].values())
        print(f"{mid}  checkpoint {mod['checkpoint_at']}  새 커밋 {n}")
        for key, v in mod["refs"].items():
            if "commits" in v:
                print(f"  {key} {v['from']}..{v['tip']}")
                for c in v["commits"]:
                    print(f"    {c['commit']} {c['at']} [{c.get('files', 0)}] {c['subject'][:90]}")
    if res["unassigned"]:
        print("모듈에 속하지 않은 새 브랜치:")
        for u in res["unassigned"]:
            print(f"  {u['repo']}@{u['ref']} {u['last_commit_at']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
