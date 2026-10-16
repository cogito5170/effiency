# gentleMonster 세션 context 저장소

2026-10-15 허브가 만든 스냅숏이다. gentleMonster · effiency 저장소를 쓰는 Claude Code 세션 23개의 context 를
세션마다 카드 한 장으로 정리하고, 원본(세션 · 이벤트 · 브랜치 · 파일)을 가리키는 포인터로 묶었다.

## 읽는 순서

| 파일 | 무엇 | 언제 |
|---|---|---|
| [INDEX.md](INDEX.md) | 세션 23개 포인터 표 (최근 갱신순: 세션 ID · 브랜치 · 역할 · 도메인 · 상태 · 카드) | 어느 세션을 볼지 고를 때 먼저 |
| [WORKSPACES.md](WORKSPACES.md) | 관련 세션을 묶은 작업 단위 W0~W6, 각 묶음의 열린 일과 원본 주소 | 한 작업을 이어받을 때 |
| [TIMELINE.md](TIMELINE.md) | 세션을 가로지른 사용자 요청 201줄, 최근순 | "최근에 무엇을 했나" |
| [sessions/](sessions/) | 세션 카드 (60줄 이내, 줄마다 출처 표지와 event ID) | 원본을 열기 직전 |
| [index.json](index.json) | 같은 포인터의 기계용 목록 | 스크립트 · 다른 세션 |
| [modules/](modules/README.md) | W1~W6 블랙박스 모듈: 인터페이스(ops.json) · 마지막 확정 상태(state.json) · 공통 계약 [CONTRACT.md](modules/CONTRACT.md) | 작업을 이어 할 때 (이것이 최신) |
| [workspaces/](workspaces/README.md) | 작업 공간 7개: 구성원 · 확정 사항 · 산출물 · 열린 일 · 이어받는 법, 태그 `ws:w<n>-…` | 한 작업 공간을 통째로 이어받을 때 |

## 묶음

| WS | 이름 | 세션 |
|---|---|---|
| W1 | 혁주 자기소개서 (CMD-HJ 허브 · 분석 · 편집 3세션) | 3 |
| W2 | 패션 · VMD 지원 포트폴리오 | 3 |
| W3 | 젠틀몬스터 공간 포트폴리오 SPA | 6 |
| W4 | 혁주 CV · 인물 사진 | 3 |
| W5 | 이미지 생성 경로 (로컬 확산 · Gemini · Codex) | 3 |
| W6 | 도구 · 인프라 (relay · 메모리 · 프론트엔드 · agy) | 4 |
| W0 | 허브 | 1 |

## 포인터로 원본 열기

- 세션 대화: `list_events(session_id=<ID>, kinds=["user"])`. 카드의 event ID 로 그 사건만 `get_event` 한다.
  대화를 통째로 읽지 않는다 (workspace.md P1).
- 브랜치: `git log origin/<branch> ^origin/main`. 카드의 "주요 파일" 경로를 연다.
- 확정 여부는 대화가 아니라 파일로 판단한다 (P3): 예를 들어 gentleMonster `docs/portfolio/README.md`, `docs/PROJECT_SETUP.md`.

## 어떻게 만들었나 · 한계

- 대상: `list_sessions` 전체(231개)에서 `workspace:gentlemonster-effiency` 태그 22개와, 태그가 빠졌지만 gentleMonster 를
  연결한 `gentleMonster_gemini`(session_01KHd6Ft8vzjYffMcwhTDwcy) 1개. workspace.md 가 뺀 두 세션(SE_new 세계 일정 계획 엔진,
  LLM-Free 자율 정책 아키텍처 설계)은 넣지 않았다.
- 카드는 `list_events` 를 `user` · `result` 로 좁혀 읽고 git 으로 확인해 썼다. 줄마다 `[사용자]` · `[도구출력]` ·
  `[추론·미검증]` · `[요약]` 표지가 있다. `[추론·미검증]` 줄은 다른 세션의 모델이 한 말이므로 결론으로 옮기지 않는다 (P2, P8).
- 이벤트가 아주 많은 세션(혁주 자소서 등)은 최근 페이지만 읽고 앞부분은 커밋 메시지로 대신했다. 카드에 적혀 있다.
- W0~W6 묶음은 허브의 판단이다. 묶음 사이에 일을 넘길 때 도메인이 다르면 P4 의 주제 전환 줄을 붙인다.
- 스냅숏이다. 세션이 더 진행되면 카드는 낡는다. 다시 만들 때는 같은 방식으로 카드를 다시 쓰고 INDEX · TIMELINE · WORKSPACES 를 카드에서 다시 뽑는다.
- 정책 원문 `docs/workspace.md` 는 이 PR 시점에 effiency `claude/new-session-67e5a5` 브랜치에만 있고 main 에는 없다.
