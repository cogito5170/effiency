"""작업 공간 모듈(W1~W6)의 인터페이스 · 상태 파일이 공통 계약(ws-module/1)을 지키는지 검사한다.

    python3 scripts/check_modules.py docs/workspace-context/modules
    python3 scripts/check_modules.py docs/workspace-context/modules --git ../gentleMonster --git .

검사하는 것 (모델 호출 없음, 표준 라이브러리만):
- 모듈마다 module.json · ops.json · state.json 이 있고 필수 필드가 있다.
- ops.json 의 `calls` 는 존재하는 모듈 오퍼레이션만 가리키고, 모듈 의존 그래프에 순환이 없다.
- state.json 의 confirmed 는 출처가 `사용자` 또는 `도구출력` 이다 (모델 추론은 unverified 로).
- decisions 의 supersedes 는 같은 모듈의 앞선 결정을 가리킨다.
- --git 을 주면 evidence 의 (ref, path) 가 그 클론에 실제로 있는지 본다 (경로 하나짜리만).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CONTRACT = "ws-module/1"
MODULE_KEYS = {"contract", "id", "name", "domain", "purpose", "exposes", "consumes", "state", "owner_tag"}
OP_KEYS = {"op", "purpose", "input", "output", "runs_where", "side_effects"}
STATE_KEYS = {"module", "as_of", "confirmed", "decisions", "open", "artifacts", "resume_point"}
CONFIRMED_SOURCES = {"사용자", "도구출력"}


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def git_has(clones: list[Path], repo: str, ref: str, path: str) -> bool | None:
    """repo 이름이 맞는 클론에서 ref:path 가 있는지. 맞는 클론이 없으면 None (검사 안 함)."""
    name = repo.split("/")[-1].lower()
    for clone in clones:
        if clone.resolve().name.lower() != name:
            continue
        for candidate in (f"origin/{ref}", ref):
            r = subprocess.run(["git", "-C", str(clone), "cat-file", "-e", f"{candidate}:{path}"],
                               capture_output=True)
            if r.returncode == 0:
                return True
        return False
    return None


def check(root: Path, clones: list[Path] | None = None) -> list[str]:
    errors: list[str] = []
    modules: dict[str, dict] = {}
    ops: dict[str, list[dict]] = {}
    states: dict[str, dict] = {}
    for d in sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith("W")):
        mid = d.name.split("-")[0]
        for fname in ("module.json", "ops.json", "state.json"):
            if not (d / fname).exists():
                errors.append(f"{mid}: {fname} 없음")
        if errors and any(e.startswith(f"{mid}:") for e in errors):
            continue
        m, o, s = load(d / "module.json"), load(d / "ops.json"), load(d / "state.json")
        modules[mid], ops[mid], states[mid] = m, o, s
        if m.get("contract") != CONTRACT:
            errors.append(f"{mid}: module.json contract 가 {CONTRACT} 가 아님")
        if m.get("id") != mid:
            errors.append(f"{mid}: module.json id 가 폴더와 다름 ({m.get('id')})")
        missing = MODULE_KEYS - m.keys()
        if missing:
            errors.append(f"{mid}: module.json 필드 없음 {sorted(missing)}")
        for op in o:
            miss = OP_KEYS - op.keys()
            if miss:
                errors.append(f"{mid}.{op.get('op')}: 필드 없음 {sorted(miss)}")
        exposed = {op["op"] for op in o if "op" in op}
        for name in m.get("exposes", []):
            if name not in exposed:
                errors.append(f"{mid}: exposes 의 {name} 이 ops.json 에 없음")
        miss = STATE_KEYS - s.keys()
        if miss:
            errors.append(f"{mid}: state.json 필드 없음 {sorted(miss)}")
        if s.get("module") != mid:
            errors.append(f"{mid}: state.json module 이 다름 ({s.get('module')})")
        for c in s.get("confirmed", []):
            if c.get("source") not in CONFIRMED_SOURCES:
                errors.append(f"{mid}: confirmed {c.get('id')} 출처가 {c.get('source')!r} (사용자/도구출력만)")
            if not c.get("evidence"):
                errors.append(f"{mid}: confirmed {c.get('id')} 에 evidence 없음")
        seen: set[str] = set()
        for i, dec in enumerate(s.get("decisions", [])):
            sup = dec.get("supersedes")
            if sup and re.fullmatch(r"W\d-D\d+", sup) and sup not in seen:
                errors.append(f"{mid}: decision {dec.get('id', i)} 의 supersedes {sup} 가 앞선 결정이 아님")
            if dec.get("id"):
                seen.add(dec["id"])
        if clones:
            for c in s.get("confirmed", []) + s.get("artifacts", []):
                ev = c.get("evidence", c)
                repo, ref, path = ev.get("repo"), ev.get("ref"), ev.get("path")
                if not (repo and ref and path) or c.get("file_verified") is False:
                    continue
                if any(ch in path + ref for ch in "{*( ,·") or path.endswith("/"):
                    continue  # 여러 파일을 묶어 적은 산출물 줄은 사람이 읽는 표시로 보고 건너뛴다
                if git_has(clones, repo, ref, path) is False:
                    errors.append(f"{mid}: {repo}@{ref}:{path} 를 찾을 수 없음")

    # 의존: calls 와 consumes 는 존재하는 op 만, 순환 없음
    graph: dict[str, set[str]] = {mid: set() for mid in modules}
    for mid, oplist in ops.items():
        declared = set(modules[mid].get("consumes", []))
        for op in oplist:
            for call in op.get("calls", []):
                target, _, name = call.partition(".")
                if target not in ops or name not in {x.get("op") for x in ops[target]}:
                    errors.append(f"{mid}.{op.get('op')}: 없는 오퍼레이션 {call} 호출")
                    continue
                if call not in declared:
                    errors.append(f"{mid}: {call} 을 부르지만 module.json consumes 에 없음")
                if target != mid:
                    graph[mid].add(target)

    state_mark: dict[str, int] = {}

    def visit(n: str, trail: list[str]) -> None:
        if state_mark.get(n) == 1:
            errors.append("의존 순환: " + " → ".join(trail + [n]))
            return
        if state_mark.get(n) == 2:
            return
        state_mark[n] = 1
        for nxt in sorted(graph[n]):
            visit(nxt, trail + [n])
        state_mark[n] = 2

    for n in sorted(graph):
        visit(n, [])
    return errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("root", type=Path)
    ap.add_argument("--git", type=Path, action="append", default=[], help="evidence 를 확인할 클론 (여러 번)")
    args = ap.parse_args(argv)
    errors = check(args.root, args.git)
    for e in errors:
        print("FAIL", e)
    n = len([p for p in args.root.iterdir() if p.is_dir() and p.name.startswith("W")])
    print(f"{n} modules, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
