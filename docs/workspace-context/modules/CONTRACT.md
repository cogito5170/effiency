# 모듈 계약 `ws-module/1`

W1~W6 은 서로의 속(세션 · 브랜치 · 스크립트 · 중간 파일)을 보지 않는다. 밖으로 내놓는 것은 세 파일과 요청 · 응답 봉투뿐이다.
MCP 서버가 `tools/list` 로 도구 이름과 입력 스키마만 알리고 구현은 숨기는 것과 같은 모양이다.

## 모듈이 내놓는 것

| 파일 | MCP 에 비유하면 | 내용 |
|---|---|---|
| `module.json` | 서버 정보 | id · 이름 · 태그 · 도메인 · 목적, `exposes`(내놓는 op), `consumes`(부르는 다른 모듈 op), `internal`(참고용 구현 정보) |
| `ops.json` | `tools/list` | op 마다 `input` · `output` 필드와 설명, 실행 위치, 부수 효과, `calls` |
| `state.json` | resource | 지금 유효한 것만: confirmed · decisions · open · artifacts · unverified · resume_point · checkpoint |
| `RESUME.md` | prompt | state.json 에서 만든 2000자 이하 요약. 의뢰인 세션이 새로 열릴 때 처음 읽는 단 하나의 파일 |
| `history.jsonl` | (내부) | 대체된 결정 · 닫힌 항목 · superseded 산출물 · 동기화 기록. 덧붙이기만 한다 |

호출자는 `internal` 과 op 의 `impl` 에 기대지 않는다. 구현을 바꿔도(세션 교체, 스크립트 교체) 세 파일의 계약이 같으면 다른 모듈은 바뀌지 않는다.

## 요청 · 응답 봉투

relay VM 인박스의 `request.json` · `response.json` 과 같은 모양이다 ([vm-inbox.md](https://github.com/cogito5170/effiency/blob/main/docs/vm-inbox.md)).

```json
{"contract": "ws-module/1", "id": "20261016T033000", "module": "W5", "op": "image",
 "input": {"spec": {"subject": "…", "mood": "…", "size": "1536x1024"}},
 "context": {"caller": "W4.portrait", "domain_switch": null, "refs": ["gentleMonster@claude/cv-blueprint:docs/cv/ai/…"]}}
```

```json
{"contract": "ws-module/1", "id": "20261016T033000", "module": "W5", "op": "image",
 "status": "done | blocked | failed | rejected",
 "output": {"png": ".relay/tasks/…/image.png", "response": ".relay/tasks/…/response.json"},
 "evidence": [{"repo": "cogito5170/gentleMonster", "ref": "claude/…", "path": "…", "commit": "…"}],
 "unverified": ["Codex 가 쓴 image-prompt.md 의 내용"],
 "state_delta": {"confirmed": [], "decisions": [], "open": []}}
```

- `context.refs` 는 파일 포인터만 넣는다. 다른 세션의 대화를 붙이지 않는다 (workspace.md P1).
- 도메인이 다른 모듈에 넘길 때는 `context.domain_switch` 에 P4 의 주제 전환 줄을 넣는다.
- 응답의 `evidence` 는 도구 출력(파일 · 커밋 · exit code), `unverified` 는 모델이 쓴 것이다 (P2 · P8).
- 받는 모듈은 `state_delta` 를 자기 `state.json` 에 반영한다. 다른 모듈의 state.json 은 고치지 않는다.

## 상태 규칙

- `confirmed` 는 출처가 `사용자` 또는 `도구출력` 이고 근거(경로 · 줄 · 커밋 또는 event id)가 있는 것만. 저장소에서 다시 찾았으면 `file_verified: true`.
- `decisions` 는 지금 유효한 것만 오래된 것부터 둔다. 정정 · 전환은 `supersedes` 로 앞 결정을 가리키고, 대체된 결정은 `history.jsonl` 로 옮긴다. 지우지 않는다 (P6).
- `resume_point` 는 마지막 확정 상태에서 바로 이어 할 op 하나와 입력, 사용자 확인이 필요한지.

## 의존

```
W1 ─┐ (독립)
W2 ─┼─ cover_image ───┐
W3 ─┼─ band_image ────┤
W4 ─┼─ portrait ──────┼──▶ W5.image   (이미지는 모두 이 한 곳: gentleMonster CLAUDE.md)
W6 ─┴─ cover ─────────┘
```

모듈 사이 의존은 `W5.image` 하나뿐이다. W1 은 아무것도 부르지 않는다. 순환은 없다. W0(허브)은 모듈이 아니라 요청을 받아 모듈에 봉투를 보내는 쪽이다.

## 독립 실행 · 교체 · 검증

- **실행:** 새 스레드에 `module.json` · `ops.json` · `state.json` 과 요청 봉투 하나만 주면 그 모듈의 op 를 돌릴 수 있다. 다른 모듈 파일을 읽을 필요가 없다.
- **교체:** op 의 `impl` 을 바꿔도 `input` · `output` 이 같으면 호출자는 그대로다. 예: W5 의 생성기가 Codex 에서 다른 도구로 바뀌어도 W2~W4 는 모른다.
- **검증:** `python3 scripts/check_modules.py docs/workspace-context/modules --git ../gentleMonster --git .`
  필수 필드, `exposes`/`calls`/`consumes` 일치, 의존 순환, confirmed 출처, supersedes 순서, 근거 경로의 실재를 본다.
  CI 의 `tests/test_module_contracts.py` 가 같은 검사를 돈다 (git 근거 확인은 제외).

## 백엔드 동기화 · 세션 교대

의뢰인은 자기 세션(프론트)만 쓴다. 이 프로젝트는 백엔드로, 의뢰인 세션을 읽기만 하고 고치거나 압축하지 않는다.
세션이 길어지는 문제는 세션을 줄여서가 아니라 **갈아타서** 푼다. 기억은 세션이 아니라 이 파일들이 들고 있다.

```
의뢰인 세션 ──커밋──▶ 저장소 ──sync_delta.py──▶ 백엔드 ──state.json · RESUME.md──▶ 저장소 ──▶ 새 의뢰인 세션
```

| 병목 | 규칙 | 수치 |
|---|---|---|
| context (세션 시작) | 새 세션은 `RESUME.md` 하나만 읽고 시작한다 | 2000자 이하 (한국어 약 2천 토큰 이하). `build_resume.py` 가 넘치면 항목을 줄이고 검사기가 막는다 |
| token (백엔드 읽기) | `checkpoint.refs` 의 커밋 뒤만 읽는다: 커밋 제목 · 바뀐 파일 수 → 필요한 파일만 `git show <commit>:<path>` | 파일은 한 번에 200줄 이하 구간. 결정 근거는 그 줄 번호로 남긴다 |
| token (세션 원본) | 저장소 파일에 기록이 없는 사용자 결정만 세션 이벤트에서 찾는다. `kinds=["user"]`, `checkpoint.sessions` 의 마지막 이벤트 뒤부터 | 한 세션에 100개씩 3쪽까지. 넘으면 `unverified` 로 두고 사용자에게 묻는다 |

세션 이벤트를 커밋보다 뒤에 두는 이유: 10-16 06:16~06:25 의 W2 세션 이벤트 15개가 도구 결과(이미지 포함) 때문에 약 150만 자였다. 같은 구간의 커밋 기록은 4줄이다.

**동기화 한 번** (백엔드)
1. `python3 scripts/sync_delta.py docs/workspace-context/modules --git ../gentleMonster --git .` — 모듈별 새 커밋과 어느 모듈에도 없는 새 브랜치.
2. 새 커밋이 있는 모듈만 그 파일 구간을 읽고 `state.json` 에 confirmed · decisions · open · artifacts 를 더한다. 대체된 것은 `history.jsonl` 로 옮기고, `checkpoint` 를 새 커밋으로 올린다.
3. `python3 scripts/build_resume.py docs/workspace-context/modules` → `python3 scripts/check_modules.py …` 통과 뒤 커밋 · 푸시.

**세션 교대** (의뢰인)
- 갈아탈 때: 자동 압축(compaction)이 한 번 일어났을 때, 사용자 메시지가 약 100개를 넘었을 때, 또는 다른 op · 다른 모듈로 넘어갈 때.
- 갈아타기 전: 그 세션의 결정 · 산출물이 저장소에 커밋돼 있어야 한다 (백엔드는 커밋만 본다).
- 새 세션의 첫 줄: `W<n> 이어서` — 세션은 `docs/workspace-context/modules/W<n>-*/RESUME.md` 를 읽고 `resume_point` 의 op 부터 한다.
  저장소가 없는 세션은 `git fetch https://github.com/cogito5170/effiency main && git show FETCH_HEAD:docs/workspace-context/modules/W<n>-…/RESUME.md`.
