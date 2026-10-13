# codex 러너 기본값을 codex-cli 0.152 에 맞게 수정

- id: `001-codex-러너-기본값을-codex-cli-0-152-에-맞게-수정`
- 생성: 2026-10-13 13:49

## Goal
`relay/config.py` 의 `DEFAULTS["runners"]["implement"]` 는 `codex exec --full-auto {prompt}` 를 쓴다.
설치된 codex-cli 0.152.0 에는 `--full-auto` 플래그가 없어서 `relay run` 의 implement 단계가 항상
exit 2 로 실패한다. 쓰기 권한이 있는 비대화형 실행은 `codex exec --sandbox workspace-write` 다
(`exec` 의 승인 모드는 기본이 never).

## Constraints
- 기본값은 `relay/config.py` 의 `DEFAULTS` 한 곳에서만 바꾼다. 다른 모듈의 동작은 바꾸지 않는다.
- `explore` 의 `codex exec --sandbox read-only` 후보와 `gemini -p` 후보는 그대로 둔다 (두 플래그 모두 0.152 / gemini 0.46 에서 확인됨).
- 기존 테스트(48개)는 모두 통과해야 한다. 외부 네트워크·CLI 에 의존하는 테스트는 추가하지 않는다.
- 주석과 문서는 한국어, 기존 문체 유지.

## Done when
- `relay/config.py` 의 implement 러너가 `["codex", "exec", "--sandbox", "workspace-write", "{prompt}"]` 다.
- `--full-auto` 문자열이 저장소 전체(코드·문서)에 남아 있지 않다. `docs/` 와 `HANDOFF.md` 에서 언급된 곳도 함께 고친다.
- `python3 -m unittest discover -s tests` 통과.
- 러너 기본값을 검사하는 테스트가 `tests/` 에 하나 있다 (설치 여부와 무관하게 문자열만 검사).

## Out of scope
- 러너 자동 감지, 플래그 폴백, codex 버전 분기 같은 새 기능.
- 다른 단계(review/lean)의 인자 변경.
