"""모듈마다 state.json 에서 RESUME.md 를 만든다. 의뢰인 세션이 새로 열릴 때 처음 읽는 단 하나의 파일이다.

    python3 scripts/build_resume.py docs/workspace-context/modules

- 상한 MAX_CHARS(2000자, 한국어 기준 약 2천 토큰 이하). 넘으면 아래 칸부터 항목을 줄이고 "외 N개" 로 state.json 을 가리킨다.
- 같은 state.json 이면 같은 RESUME.md 가 나온다 (모델 호출 없음, 표준 라이브러리만).
- 이력은 넣지 않는다. 대체된 결정 · 닫힌 항목은 history.jsonl 에만 있다.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

MAX_CHARS = 2000
CAPS = {"now": 300, "hint": 420, "pre": 200, "item": 140, "decision": 120}
LIMITS = [(4, 6, 5), (3, 4, 4), (2, 3, 3), (1, 2, 2), (1, 1, 1)]  # (물을 것, 결정, 산출물) 단계별 개수


def cut(text: str, n: int) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= n else text[: n - 1] + "…"


def render(d: Path, s: dict, limits: tuple[int, int, int]) -> str:
    n_open, n_dec, n_art = limits
    cp = s.get("checkpoint", {})
    rp = s.get("resume_point", {})
    lines = [f"# {s['module']} {s.get('title', '')}".rstrip(),
             f"기준 {s.get('as_of')} · 체크포인트 " + ", ".join(f"{k.split('@')[-1]}@{v}" for k, v in list(cp.get('refs', {}).items())[:3]),
             "", "## 지금", cut(s.get("latest_confirmed"), CAPS["now"]),
             "", f"## 이어 할 일: `{rp.get('op')}`", cut(rp.get("input_hint"), CAPS["hint"]),
             f"- 조건: {cut(rp.get('precondition'), CAPS['pre'])}"]
    asks = [o for o in s.get("open", []) if o.get("blocking")]
    if asks:
        lines += ["", "## 사용자에게 물을 것"]
        lines += [f"- {o['id']} {cut(o['item'], CAPS['item'])}" for o in asks[:n_open]]
        if len(asks) > n_open:
            lines.append(f"- 외 {len(asks) - n_open}개 → state.json open")
    decs = s.get("decisions", [])
    if decs:
        lines += ["", "## 지금 유효한 결정 (최근순)"]
        lines += [f"- {x['id']} {cut(x['decision'], CAPS['decision'])}" for x in reversed(decs[-n_dec:])]
        if len(decs) > n_dec:
            lines.append(f"- 외 {len(decs) - n_dec}개 → state.json decisions")
    arts = [a for a in s.get("artifacts", []) if a.get("status") == "draft"]
    if arts:
        lines += ["", "## 작업 중인 파일"]
        lines += [f"- {a['path']}" + (f" @{a['commit']}" if a.get("commit") else "") for a in arts[-n_art:]]
        if len(arts) > n_art:
            lines.append(f"- 외 {len(arts) - n_art}개 → state.json artifacts")
    unv = len(s.get("unverified", []))
    lines += ["", "## 읽는 법",
              f"- 이 파일만 읽고 시작한다. 더 필요하면 `{d.name}/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.",
              f"- 미확인 {unv}개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.",
              "- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다."]
    return "\n".join(lines) + "\n"


def build(root: Path) -> list[tuple[str, int]]:
    out = []
    for d in sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith("W")):
        s = json.loads((d / "state.json").read_text(encoding="utf-8"))
        for lim in LIMITS:
            text = render(d, s, lim)
            if len(text) <= MAX_CHARS:
                break
        else:
            text = text[: MAX_CHARS - 2] + "…\n"
        (d / "RESUME.md").write_text(text, encoding="utf-8")
        out.append((s["module"], len(text)))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("root", type=Path)
    args = ap.parse_args(argv)
    for mid, n in build(args.root):
        print(f"{mid} RESUME.md {n}자")
    return 0


if __name__ == "__main__":
    sys.exit(main())
