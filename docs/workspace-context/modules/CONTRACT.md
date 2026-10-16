# 모듈 계약 `ws-module/1`

W1~W6 은 서로의 속(세션 · 브랜치 · 스크립트 · 중간 파일)을 보지 않는다. 밖으로 내놓는 것은 세 파일과 요청 · 응답 봉투뿐이다.
MCP 서버가 `tools/list` 로 도구 이름과 입력 스키마만 알리고 구현은 숨기는 것과 같은 모양이다.

## 모듈이 내놓는 것

| 파일 | MCP 에 비유하면 | 내용 |
|---|---|---|
| `module.json` | 서버 정보 | id · 이름 · 태그 · 도메인 · 목적, `exposes`(내놓는 op), `consumes`(부르는 다른 모듈 op), `internal`(참고용 구현 정보) |
| `ops.json` | `tools/list` | op 마다 `input` · `output` 필드와 설명, 실행 위치, 부수 효과, `calls` |
| `state.json` | resource | 마지막 확정 상태: confirmed · decisions · open · artifacts · unverified · resume_point |

호출자는 `internal` 과 op 의 `impl` 에 기대지 않는다. 구현을 바꿔도(세션 교체, 스크립트 교체) 세 파일의 계약이 같으면 다른 모듈은 바뀌지 않는다.

## 요청 · 응답 봉투

relay VM 인박스의 `request.json` · `response.json` 과 같은 모양이다 ([vm-inbox.md](../../vm-inbox.md)).

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
- `decisions` 는 오래된 것부터 쌓고, 정정 · 전환은 `supersedes` 로 앞 결정을 가리킨다. 최신이 이긴다. 지우지 않는다 (P6).
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
