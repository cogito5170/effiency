# W6 · 도구 · 인프라

`ws:w6-tools-infra` · 도메인 software · 계약 [ws-module/1](../CONTRACT.md) · 상태 기준 2026-10-16T03:30Z

relay(토큰 절감 · VM 요청 · 보관), gentle_monster 기억 · 프론트엔드 · 커버 도구를 오퍼레이션으로 제공한다.

## 인터페이스 (ops.json)

| op | 하는 일 | 입력 | 출력 | 실행 | 부수 효과 | 부르는 모듈 |
|---|---|---|---|---|---|---|
| `relay_run` | task 하나를 explore(agy) → pack → implement(Codex) → verify → review(Claude lean) 로 돌려 VERDICT 를 받는다 | task, only, skip, max_iterations, review_max_turns, verify, dry_run | verdict, files, run | 사용자 (맥/로컬: claude · codex · agy 로그인 필요) | task 폴더와 작업 트리에 파일 생성 (커밋·푸시는 하지 않음) | — |
| `relay_ask` | PDF 에서 드래그한 부분을 토큰 분산(agy→codex, 깊은 질문만 Claude)으로 설명한다; diagnose 모드는 맥 Quick Action 실패 원인 판정 | mode, text, question, source, deep, ask_log | answer_html, qa_md, diagnosis | 사용자 (맥: 미리보기/Chrome · poppler · agy/codex) | none (로컬 파일만; diagnose 는 읽기) | — |
| `relay_request` | VM 인박스로 agy 자문(advise) 또는 codex/agy 위임(delegate)을 보낸다 (이미지는 W5.image) | repo, branch, task, action, agent, instruction | response, files, result_commit | 허브 (요청) + VM (실행) | 요청 브랜치 git push; VM 이 같은 브랜치에 결과 커밋 push (delegate 는 코드 변경 포함) | — |
| `archive_recall` | 긴 세션 원문을 보관하고, 비슷한 요청일 때만 출처 표지가 붙은 요약·발췌를 불러온다 | words, open, lines, budget, supersede, retract | hits, excerpt | 허브 (Claude Code 세션 안 hook) 또는 사용자 로컬 | none (.relay/archive 는 gitignore, 로컬 파일만) | — |
| `memory_context` | gentleMonster 작업의 기억(사용자 말·원자료·모델 추론 구분)을 보거나, 정정 지시를 기억에 반영해 초안을 다시 만든다 | job, instruction, all, no_verify | records, trace, job_version | 허브 또는 사용자 (revise 는 Gemini 키 필요) | memory.jsonl · job.json 갱신 (작업 폴더, git 아님) | — |
| `frontend_render` | 작업(방)을 웹 페이지로 만들고 브라우저 심판으로 변형을 진화시킨다 | job, rounds | page, scores | 허브 | none (작업 폴더에 파일) | — |
| `cover` | 청사진 표지용 image-spec.json 을 three.js 장면·도면 데이터에서 결정적으로 쓰고, 생성된 cover 를 청사진 1쪽에 붙인다 | job, print_only, attach | task, blueprint_pdf | 허브 | W5.image 를 통한 git push (claude/* 브랜치); 그 외 작업 폴더 파일 | W5.image |

입력 · 출력 필드의 타입과 설명은 [ops.json](ops.json). 내부 구현(`impl`)은 참고용이며 호출자는 기대지 않는다.

## 마지막 확정 상태

2026-10-15 사용자가 gentleMonster PR #9(기억·맥락 0eeccc8) · #10(정정 슬롯 386f7ae) · #11(relay 보관소 hook b688f77) 과 effiency PR #3(archive 6b0cd32) 를 머지 — 머지된 도구 상태의 최신. 미머지 최신은 effiency@claude/zealous-goodall-wkb3yz 의 relay ask(03eb32a), 맥 Quick Action 실패 원인(ask.log) 대기.

## 이어 할 곳 (resume_point)

- op: `relay_ask`
- 입력: mode=diagnose: 사용자 맥의 빠른 동작 실행 출력 + `cat ~/.relay/ask.log` (없으면 `ls -la ~/.relay`) 를 받아 effiency@claude/zealous-goodall-wkb3yz 03eb32a 의 relay/ask.py 단계 로그와 대조
- 조건: 사용자 확인 필요 — 맥 출력이 있어야 진행. 사용자 없이 할 수 있는 일은 읽기(브랜치 diff 검토)뿐이고 머지·push 는 사용자 결정.

## 열린 일

| id | 일 | 기다리는 것 | 막힘 | 출처 |
|---|---|---|---|---|
| W6-O1 | 맥 relay ask Quick Action 동작 안 함 ('~/.relay/ask.log: No such file') — 사용자의 빠른 동작 실행 출력과 ask.log 를 받아 원인 판정 | 사용자 | 예 | 도구출력 |
| W6-O2 | relay ask 9파일(effiency@claude/zealous-goodall-wkb3yz 03eb32a) main 미머지 — O1 해결 후 PR/머지 여부 | 사용자 | 아니오 | 도구출력 |
| W6-O3 | `relay run pdf-professor` 가 iteration 1 에서 멈춤 — 해결 여부 불명 (pdf-professor 는 brief.md 만 있고 run 산출물 없음) | 사용자 | 아니오 | 도구출력 |
| W6-O4 | effiency@claude/project-thread-susdx3 ddc7904 (relay recall: 흔한 낱말만 겹치면 붙이지 않음) main 미머지 | 사용자 | 아니오 | 도구출력 |
| W6-O5 | 기억 구조 출력 수준 평가 `python3 eval/context_eval.py --live --repeat 3` 미실행 — Gemini 키 있는 환경 필요 | 사용자 | 아니오 | 도구출력 |
| W6-O6 | auto-agy.exp 엔터 자동화 · `agy -c` 래핑이 동작했는지 확인 없음 (산출물 브랜치 없음) | 사용자 | 아니오 | 추론·미검증 |
| W6-O7 | se_new compact.py 가 모델 답을 노트에 적는 문제 — gentleMonster docs/MEMORY.md 에 진단만, 수정 안 함 | 사용자 | 아니오 | 도구출력 |

## 확정 사항 (저장소 파일로 확인)

| id | 내용 | 출처 | 근거 | 파일 확인 |
|---|---|---|---|---|
| W6-C1 | frontend engine: `python3 -m gentle_monster site <작업> [--rounds 6]` / `!젠몬 방금 거 웹 사이트로`; gentle_monster/engine/{color,compose,judge,policy,tokens}.py, docs/FRONTEND_ENGINE.md. 사용자 'PR 만들고 머지해' 로 PR #2 머지. | 사용자 | `main:README.md:30` 97ded21 / merge c2204cc | ✓ |
| W6-C2 | 기억·맥락 구조: memory.jsonl 저장과 context.build 입력 선택을 분리, 모델 답은 미검증(model_inference)으로 격하, 정정은 옛 사용자 말을 superseded 로, 작업 한도 12k(DEFAULT_CAP=12000), LangChain·벡터DB 미도입; `python3 -m gentle_monster revise <job> "<말>" [--no-verify]`, `memory <job> [--all]`. | 도구출력 | `main:gentle_monster/context.py:43` 239166b · 0649ecb / merge 0eeccc8 (PR #9, 머지 cogito5170) | ✓ |
| W6-C3 | 정정 슬롯 보완: '5.5m 말고 6m' 소수점 처리, 정정 대상 절 좁히기 (PR #10). | 도구출력 | `main:gentle_monster/memory.py` 76b219b · 5fd19f4 / merge 386f7ae | ✓ |
| W6-C4 | gentleMonster 세션 hook: SessionStart · UserPromptSubmit · PreCompact → scripts/relay_hook.sh → `relay hook <event>` (relay 없으면 설치 시도, 항상 exit 0). effiency 쪽 `relay archive` / `relay recall` (원문 보관 + 색인, --supersede/--retract, 도메인 전환 감지). | 도구출력 | `main:.claude/settings.json:3` 5870b7c / merge b688f77 (PR #11); effiency 6a890f4 · 3598677 · 4921a33 / merge 6b0cd32 (PR #3) | ✓ |
| W6-C5 | relay 목표: Claude Pro 로 30일간 한도 초과 없이 운용. Claude 는 판단·리뷰만, 탐색·구현·문서는 agy/Codex/ChatGPT. Gemini API 미사용. | 사용자 | `main:docs/HANDOFF.md:8` fa7614e (PR #1 merge 48cd71f) | ✓ |
| W6-C6 | RAG 대신 다른 방법 — 저장소에 'RAG 보류'(탐색은 agy→pack 으로 Claude 토큰 0, 큰 비용은 고정 부분·세션 길이·thinking). | 사용자 | `main:docs/HANDOFF.md:35` | ✓ |
| W6-C7 | 사용자 개입 최소화 — `relay auto <goal>` (세션 자동 순환, 사용자 개입 없음). | 사용자 | `main:relay/cli.py:657` | ✓ |
| W6-C8 | task 기록을 git 으로 공유하고 main 에 머지 — PR #1 머지, .relay/tasks/ 공유 커밋(사용자 로컬 커밋 포함). | 사용자 | `main:.relay/tasks/` 77caf9a · 540f312(작성자 윤경, +0900) · merge 48cd71f | ✓ |
| W6-C9 | relay 러너 목록에서 gemini 제외 (`relay check` = claude · codex · agy), agy 사용. | 사용자 | `main:relay/auto.py` 2bf1bc1 · 9f676ab | ✓ |
| W6-C10 | PDF 드래그 질문 기능(relay ask)의 목적은 토큰 절감 — 쉬운 설명 agy→codex(Claude 0), 깊은 질문만 Claude 1턴. 브랜치에만 있음(main 미머지). | 사용자 | `claude/zealous-goodall-wkb3yz:docs/ask.md:25` 409cf63 … 03eb32a | ✓ |
| W6-C11 | pd-portfolio-proposal: `relay run --only implement review --max-iterations 2 --review-max-turns 4` 1회 반복으로 VERDICT: APPROVE, task 종료 (W6 작업 공간 파일의 '결과 미확인' 은 해소). | 도구출력 | `main:.relay/tasks/pd-portfolio-proposal/out-claude.md:1` | ✓ |
| W6-C12 | agy 대신 `agy -c` 로 세션 이어받기 (auto-agy.exp). | 사용자 | `claude/zen-bell-gd7gdj (원격 없음):a0cc38af-a6e5-4fbb-89be-36c66b226edc` | 이벤트만 |

## 의사결정 이력 (오래된 것 → 최신)

| id | 날짜 | 결정 | 누가 | 대체한 것 |
|---|---|---|---|---|
| W6-D1 | 2026-10-01T08:49Z | frontend engine PR #2 생성·머지 | 사용자 | — |
| W6-D2 | 2026-10-07T20:27Z | auto-agy: `agy -c` 로 세션 이어받기 | 사용자 | auto-agy.exp 의 `spawn agy` |
| W6-D3 | 2026-10-07T21:31Z | (범위: 진로, 도구 아님) 방향을 'QA나 DevOps 중 하나로' | 사용자 | — |
| W6-D4 | 2026-10-12T20:06Z | RAG 대신 다른 방법 (포트폴리오 목적 아님) → 저장소에 RAG 보류 | 사용자 | — |
| W6-D5 | 2026-10-12T20:53Z | HANDOFF.md, 목표 = Pro 요금제 30일 안정 운용 | 사용자 | — |
| W6-D6 | 2026-10-13T08:38Z | 사용자 개입 최소화 (매번 /clear·[force] 불가) → relay auto | 사용자 | hook 이 /clear 를 요구하던 방식 |
| W6-D7 | 2026-10-13T15:57Z | task 기록 git 공유 + main 머지 (PR #1 48cd71f) | 사용자 | — |
| W6-D8 | 2026-10-13T16:36Z | relay 목록에서 gemini 제외, agy 사용 | 사용자 | gemini 를 탐색 러너로 두던 v0.4 이전 구성 |
| W6-D9 | 2026-10-14T02:13Z | (범위: 진로, 도구 아님) 16주 Platform/DevOps 취업 계획 task 002·003 을 사용자 로컬 커밋으로 추가 — D3 의 'QA나 DevOps' 를 Platform/DevOps 로 좁힌 것으로 읽힘 | 사용자 (로컬 커밋 5656b0a, 작성자 윤경) | W6-D3 |
| W6-D10 | 2026-10-15T08:17Z | PDF 기능(relay ask) 목적은 토큰 절감; 08:32 agy 도 사용 | 사용자 | — |
| W6-D11 | 2026-10-15T13:17Z | 기억·맥락 구조 PR #9 머지 (다른 세션의 'PR 열지 말 것' 은 머지 뒤 도착) | 사용자 (지시 e328bac9… + PR 머지) | — |
| W6-D12 | 2026-10-15T13:44Z | PR #10(정정 슬롯) · #11(relay 보관소 hook) · effiency PR #3(archive) 머지 — PR #9 위에 쌓였으므로 PR #9 되돌리기 안 함으로 읽힘. 가장 최근 확정(머지). | 사용자 (PR 머지) | PR #9 revert 검토(미검증 열린 일) |

## 산출물

| 상태 | 종류 | 위치 |
|---|---|---|
| final | code | `gentleMonster@main:gentle_monster/engine/*.py · tests/test_engine.py · docs/FRONTEND_ENGINE.md` c2204cc |
| final | code | `gentleMonster@main:gentle_monster/memory.py · context.py · verify.py · eval/context_eval.py · docs/MEMORY.md` 386f7ae |
| final | code | `gentleMonster@main:.claude/settings.json · scripts/relay_hook.sh · .relay/config.toml` b688f77 |
| final | code | `effiency@main:relay/ (run · lean · auto · watch · archive · recall · request · inbox · check · cloud-run)` 8724b6c |
| final | doc | `effiency@main:docs/HANDOFF.md · docs/archive.md · docs/pipeline.md · docs/STATE.md` 8724b6c |
| draft | code | `effiency@claude/zealous-goodall-wkb3yz:relay/ask.py · docs/ask.md · tests/test_ask.py · .relay/tasks/pdf-professor/brief.md` 03eb32a |
| draft | code | `effiency@claude/project-thread-susdx3:relay/ (recall 오탐 수정)` ddc7904 |
| final | doc | `effiency@main:notes/pd-portfolio/project-proposal.md` 8724b6c |

## 미검증 (다른 세션 모델의 말, 결론으로 쓰지 않음)

- relay 측정값 35.1k → 7.9k(−78%) → 4.0k, relay run 리뷰 1턴 5.5~6.5k (HANDOFF.md:25 에 적혀 있으나 모델이 측정·기록한 값) — session_01DK8uaSBXFMiLZbhtqgWjy4 / effiency docs/HANDOFF.md:25
- PR #9 성공 기준 7개 통과(입력 수준만), Playwright 미실행 — session_01WmF4xunApKVcUzRM7EN111
- frontend engine 4 예제 × 12 변형 V 검사 통과 — session_01DFhceYvuVFeYdA3KHy1b4c
- 진로 조언(정보처리기사·CTFL 추천, 현대오토에버 Embedded SW Process Engineer 적합 등) — session_01EKnjXV12oRn3AMLTqp1RFZ
- pd-portfolio state.md 의 'User chose a PD portfolio project and removed AI workflow automation from scope' 는 모델이 쓴 state 기록 — 사용자 원문 미확인. 진로 D9(Platform/DevOps)과의 관계 미정 — effiency .relay/tasks/pd-portfolio-proposal/state.md
- 파일과 기억의 차이: W6 파일은 'pd-portfolio-proposal 결과 미확인' 이라 했으나 main 에 APPROVE 기록(W6-C11). 또 `relay delegate` help 문구가 아직 'Codex(구현) / Gemini(탐색)' (choices 는 codex·agy) — 문구만 낡음 — effiency relay/cli.py delegate parser
