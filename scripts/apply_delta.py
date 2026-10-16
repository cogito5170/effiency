"""동기화 한 번의 결과(작은 JSON 패치)를 모듈 state.json 에 반영하고, 대체 · 종료된 항목을 history.jsonl 로 옮긴다.

    python3 scripts/apply_delta.py docs/workspace-context/modules patch.json

패치 모양 (모듈 id 마다, 모든 키는 선택):
    {"W2": {"at": "2026-10-16T06:50Z",
            "add": {"confirmed": [...], "decisions": [...], "open": [...], "artifacts": [...], "unverified": [...]},
            "close": {"open": {"W2-O10": "006 · 007 결과 도착"}, "confirmed": {"W2-C9": "…"}},
            "artifact_status": {"<path>": "superseded"},
            "refs": {"gentleMonster@claude/…": "<commit>"},
            "sessions": {"session_…": {"last_event_id": "…", "at": "…"}},
            "latest_confirmed": "…", "resume_point": {...}}}

- 어떤 결정의 supersedes 가 가리키는 결정, close 에 적은 항목, status 가 superseded 인 산출물은 history.jsonl 로 간다 (덧붙이기만).
- 같은 id 를 다시 add 하면 덮어쓴다. checkpoint.refs 는 주어진 키만 바꾼다.
모델이 state.json 전체를 다시 쓰지 않고 바뀐 몇 줄만 넘기게 하려는 도구다. 표준 라이브러리만 쓴다.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ORDER = ["module", "title", "as_of", "checkpoint", "latest_confirmed", "resume_point",
         "confirmed", "decisions", "open", "artifacts", "unverified"]


def upsert(items: list[dict], new: list[dict], key: str) -> list[dict]:
    index = {x.get(key): i for i, x in enumerate(items) if x.get(key)}
    for n in new:
        if n.get(key) in index:
            items[index[n[key]]] = n
        else:
            items.append(n)
    return items


def apply(root: Path, patch: dict) -> dict[str, int]:
    moved: dict[str, int] = {}
    for mid, p in patch.items():
        folder = next(root.glob(f"{mid}-*"))
        s = json.loads((folder / "state.json").read_text(encoding="utf-8"))
        at = p.get("at") or s.get("as_of")
        add = p.get("add", {})
        for k in ("confirmed", "decisions", "open"):
            s[k] = upsert(s.get(k, []), add.get(k, []), "id")
        s["artifacts"] = upsert(s.get("artifacts", []), add.get("artifacts", []), "path")
        s["unverified"] = s.get("unverified", []) + add.get("unverified", [])
        for path, st in p.get("artifact_status", {}).items():
            for a in s["artifacts"]:
                if a.get("path") == path:
                    a["status"] = st
        hist: list[dict] = []
        by = {d["supersedes"]: d["id"] for d in s["decisions"] if d.get("supersedes")}
        keep = []
        for d in s["decisions"]:
            if d["id"] in by:
                hist.append({"kind": "decision", "moved_at": at, "superseded_by": by[d["id"]], **d})
            else:
                keep.append(d)
        s["decisions"] = keep
        for k, closing in p.get("close", {}).items():
            keep = []
            for item in s.get(k, []):
                if item.get("id") in closing:
                    hist.append({"kind": k, "moved_at": at, "closed_because": closing[item["id"]], **item})
                else:
                    keep.append(item)
            s[k] = keep
        keep = []
        for a in s["artifacts"]:
            (hist.append({"kind": "artifact", "moved_at": at, **a}) if a.get("status") == "superseded" else keep.append(a))
        s["artifacts"] = keep
        cp = s.setdefault("checkpoint", {})
        prev = {"at": cp.get("at"), "refs": dict(cp.get("refs", {}))}
        cp.setdefault("refs", {}).update(p.get("refs", {}))
        cp.setdefault("sessions", {}).update(p.get("sessions", {}))
        if not cp["sessions"]:
            cp.pop("sessions")
        cp["at"] = at
        for k in ("latest_confirmed", "resume_point"):
            if k in p:
                s[k] = p[k]
        s["as_of"] = at
        hist.insert(0, {"kind": "sync", "at": at, "previous": prev,
                        "added": {k: [x.get("id") or x.get("path") for x in v] for k, v in add.items()}})
        s = {k: s[k] for k in ORDER if k in s} | {k: v for k, v in s.items() if k not in ORDER}
        (folder / "state.json").write_text(json.dumps(s, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        with (folder / "history.jsonl").open("a", encoding="utf-8") as f:
            for h in hist:
                f.write(json.dumps(h, ensure_ascii=False) + "\n")
        moved[mid] = len(hist) - 1
    return moved


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("root", type=Path)
    ap.add_argument("patch", type=Path)
    args = ap.parse_args(argv)
    for mid, n in apply(args.root, json.loads(args.patch.read_text(encoding="utf-8"))).items():
        print(f"{mid}: 반영, history 로 {n}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
