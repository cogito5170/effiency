# W5 · 이미지 경로 (Codex)

`ws:w5-image-pipeline` · 도메인 software · 계약 [ws-module/1](../CONTRACT.md) · 상태 기준 2026-10-16T03:30Z

짧은 image-spec 을 받아 VM Codex 가 만든 이미지와 response.json 을 돌려준다. 이미지는 모두 이 모듈을 거친다.

## 인터페이스 (ops.json)

| op | 하는 일 | 입력 | 출력 | 실행 | 부수 효과 | 부르는 모듈 |
|---|---|---|---|---|---|---|
| `image` | 의미 스펙 하나로 VM Codex 가 이미지를 만들게 하고 결과 파일을 돌려준다 (gentleMonster CLAUDE.md: 모든 비렌더 이미지의 유일한 경로) | repo, branch, task, spec, spec_path | status, image_png, image_prompt_md, image_json, response, result_commit | 허브 (스펙·요청·대기) + VM (생성·결과 커밋) | 요청 브랜치에 request 커밋 git push; VM 이 같은 브랜치에 결과 커밋 git push. status=failed|stale 이면 다른 방법으로 이미지를 만들지 않고 output_tail 을 사용자에게 그대로 전달 | — |
| `status` | 이미 보낸 image 요청의 상태를 읽기만 한다 | repo, branch, task | state, response, files, hint | 허브 | none | — |

입력 · 출력 필드의 타입과 설명은 [ops.json](ops.json). 내부 구현(`impl`)은 참고용이며 호출자는 기대지 않는다.

## 마지막 확정 상태

W5-D8: gentleMonster CLAUDE.md '이미지는 모두 Codex 로 만든다 (2026-10-15 사용자 결정)' — 사용자가 PR #14 를 머지(6acff99, 2026-10-15T14:39Z). 로컬 확산 · Gemini · Midjourney 프롬프트 경로를 대체. 경로: image-spec.json → claude/* 푸시 → VM relay inbox → codex exec 이미지 → 같은 브랜치 커밋.

## 이어 할 곳 (resume_point)

- op: `image`
- 입력: 경로 정상(status 확인 완료). 다음 이미지는 W2.cover_image · W3.band_image · W4.portrait · W6.cover 가 spec 만 넘겨 부른다.
- 조건: 요청 모듈 쪽 사용자 결정(무엇을 그릴지)이 먼저

## 열린 일

| id | 일 | 기다리는 것 | 막힘 | 출처 |
|---|---|---|---|---|
| W5-O1 | VM 워커(relay-inbox.timer) 마지막 확인 2026-10-15T14:28Z 이후 상태 미확인 — 다음 image 요청이 10분 안에 'relay inbox:' 커밋을 받는지로 판정 | VM | 아니오 | 추론·미검증 |
| W5-O2 | 테스트 브랜치 정리: gentleMonster@claude/project-thread-95j1zd (001-codex-test, cb7027b) 와 effiency@claude/context-archive (6f7510c, 005 결과 중복) 가 main 미머지 — 머지 또는 삭제 결정 | 사용자 | 아니오 | 도구출력 |
| W5-O3 | Gemini 경로(gentleMonster_gemini, agy 블록 A/B)와 Codex 이미지 규칙의 관계: 이미지 외 용도로 계속 쓸지 미정. 맥 설치 `gentlemonster-agy --check` 결과 미보고, CMD-WUG1 담당 질문 미답 | 사용자 | 아니오 | 추론·미검증 |
| W5-O4 | 로컬 확산(diffusion_model) 'Real-ESRGAN 크게 키우기' 제안 · 윈도우 sd-turbo 결과 보고 요청은 답 없음 — D8 로 대체되어 진행 불필요로 보임, 닫을지 사용자 확인 | 사용자 | 아니오 | 추론·미검증 |

## 확정 사항 (저장소 파일로 확인)

| id | 내용 | 출처 | 근거 | 파일 확인 |
|---|---|---|---|---|
| W5-C1 | 새 이미지는 종류를 가리지 않고 .claude/skills/codex-image/SKILL.md 를 따른다 (VM Codex). 세션이 PIL·SVG·다른 이미지 모델로 직접 그리지 않는다. 렌더링(three.js·평면도·PDF·차트)은 이미지가 아니며 코드가 만든다. 실패 시 대체 수단 없이 response.json 이유를 전한다. | 사용자 | `main:CLAUDE.md:3` 12ecdbd (merge 6acff99, PR #14, 머지한 사람 cogito5170) | ✓ |
| W5-C2 | codex-image 스킬: 스펙은 .relay/tasks/<번호>-<이름>/image-spec.json, subject 만 필수, 허용 필드 subject·purpose·style·mood·composition·palette·lighting·text·size·avoid·notes (그 외 거부, 필드당 600자), size 1024x1024|1536x1024|1024x1536. `relay request <T> image` → commit → claude/* 브랜치 push → VM 30초 폴링·생성 1~3분 → 'relay inbox: <T>' 커밋, 10분 무응답이면 사용자에게 relay-inbox.timer 확인 요청. | 도구출력 | `main:.claude/skills/codex-image/SKILL.md:11` 5e8645b (merge 8ea9db8, PR #12) + 93dbe64 · 12ecdbd | ✓ |
| W5-C3 | effiency relay image / VM inbox 구현이 main 에 있다: relay image(imagegen.py, codex exec --sandbox workspace-write -c features.image_generation=true, 실패 시 플래그 없이 재시도, 이미지 도구 없으면 IMAGE_TOOL_UNAVAILABLE, 한도 소진 보고), relay request(image|advise|delegate), relay inbox(claude/* 만 감시, 셸 없음, 설치된 relay 실행), systemd 서비스가 effiency·gentleMonster 두 저장소를 본다. | 도구출력 | `main:relay/inbox.py:37` 298fab9 · ed4b28f · c88ddef · 6764c1c · cd26a2e (merges ab9e694 PR #2, b323773 PR #4, 8724b6c PR #5 — 머지한 사람 cogito5170) | ✓ |
| W5-C4 | VM Codex 경로 실측 성공 2건: effiency task 005 (13:32Z 첫 시도 failed '이미지 생성 도구가 없습니다' → Codex 재로그인 후 13:42Z done, 78.3s), gentleMonster 001-cover-gm (14:28Z done, 124.5s, 1536x1024 청사진 표지). | 도구출력 | `main:.relay/tasks/001-cover-gm/response.json:4` 05ef106 | ✓ |
| W5-C5 | 청사진 표지는 손으로 스펙을 쓰지 않는다: `python3 -m gentle_monster cover <작업> [--print] [--attach <task폴더>]` 가 three.js 장면·도면 데이터로 image-spec.json + request.json 을 쓰고, blueprint 는 cover.png 가 있으면 1쪽에 넣는다. | 도구출력 | `main:gentle_monster/__main__.py:63` 93dbe64 (+ gentle_monster/cover.py 9ff47fd) | ✓ |
| W5-C6 | 사용자 전제: Codex 는 VM 에서 OAuth 로그인되어 있고, Claude Code 세션에서 Codex 이미지 엔진을 쓰고 싶다. | 사용자 | `main:docs/vm-inbox.md:3` | ✓ |
| W5-C7 | (대체됨) 로컬 확산 경로: 확산 모델 학습이 아니라 기존 모델 + 서브에이전트 시스템, '미드저니처럼 프롬프트만 입력' UI, 맥 램 8GB(16 → 8 정정), zsh. | 사용자 | `claude/code-agent-image-gen-cz6kfx:335cfcc3-80a9-4f82-8551-4bcff0bf09bf · 8a8ebb73-04a0-457a-9297-168f842791d6 · 12d46b06-cc7b-4e0a-8d91-9cc0ebf18d84 · 3a946ea6-d334-4fd0-aea5-12a33aad9524` | 이벤트만 |
| W5-C8 | (이미지 용도로는 대체됨) Gemini 경로: 모든 부분 gemini-3-flash-preview, 대체 모델 없음, Gemini CLI 0.62.0; agy 기본 모델 gemini-3.8-flash-high. | 사용자 | `claude/sleepy-cori-h0ug3b:00471a47-9bb6-4155-8dba-74749bbdc5e0 · 077259fc-c7c0-404f-803f-1c0f4540afa3` | 이벤트만 |
| W5-C9 | 2026-10-16 status 재확인: gentleMonster 001-cover-gm response.json status=done, exit_code=0, 124.475s | 도구출력 | `main:.relay/tasks/001-cover-gm/response.json` 6acff99 | ✓ |

## 의사결정 이력 (오래된 것 → 최신)

| id | 날짜 | 결정 | 누가 | 대체한 것 |
|---|---|---|---|---|
| W5-D1 | 2026-10-03T16:21Z | gentleMonster_gemini: 모든 부분 gemini-3-flash-preview, fallback 없음, Gemini CLI 0.62.0 (앞선 flash-lite 운용을 대체) | 사용자 | — |
| W5-D2 | 2026-10-03T16:30Z | agy 기본 모델 gemini-3.8-flash-high | 사용자 | — |
| W5-D3 | 2026-10-10T08:03Z | 이미지 시스템은 확산 모델 학습이 아니라 기존 모델 + 서브에이전트(diffusion_model atelier) | 사용자 | — |
| W5-D4 | 2026-10-10T10:39Z | 미드저니처럼 프롬프트만 넣으면 뽑아 주는 UI | 사용자 | — |
| W5-D5 | 2026-10-10T17:13Z | 맥 램 8GB (앞선 'Ram 16' 정정) | 사용자 | 10-10T10:56Z 'Ram 16' (event c6f60848-050e-4074-9c6e-041f90ce606d) |
| W5-D6 | 2026-10-15T13:22Z | effiency relay image + VM inbox 머지 (PR #2), 이후 PR #4·#5 (Codex 재시도·여러 저장소 감시) | 사용자 (PR 머지) | — |
| W5-D7 | 2026-10-15T13:54Z | gentleMonster 에 codex-image 스킬 (세션은 스펙만 쓰고 VM 인박스로 요청) 머지 (PR #12) | 사용자 (PR 머지) | — |
| W5-D8 | 2026-10-15T14:39Z | 이미지는 모두 Codex 로 만든다 (CLAUDE.md, '2026-10-15 사용자 결정'); 렌더링은 코드 그대로; 실패 시 대체 수단 금지. 가장 최근 확정. | 사용자 (PR #14 머지, CLAUDE.md 에 사용자 결정으로 기록) | W5-D3, W5-D4 (로컬 확산 · 미드저니형 UI), W5-D1/D2 의 이미지 용도, gentleMonster@claude/midjourney-574x172-image-sy9gq3 의 Midjourney 프롬프트 방식 |

## 산출물

| 상태 | 종류 | 위치 |
|---|---|---|
| final | code | `effiency@main:relay/imagegen.py · relay/inbox.py · relay/cli.py(cmd_image, cmd_request) · relay/config.py` 8724b6c |
| final | doc | `effiency@main:docs/image-pipeline.md · docs/vm-inbox.md` 8724b6c |
| final | code | `effiency@main:scripts/systemd/relay-inbox.service · relay-inbox.timer` cd26a2e |
| final | doc | `gentleMonster@main:.claude/skills/codex-image/SKILL.md` 12ecdbd |
| final | doc | `gentleMonster@main:CLAUDE.md` 12ecdbd |
| final | code | `gentleMonster@main:gentle_monster/cover.py · __main__.py(cover)` 93dbe64 |
| final | image | `gentleMonster@main:.relay/tasks/001-cover-gm/image.png (+ image-spec.json, response.json)` 05ef106 |
| final | image | `effiency@main:.relay/tasks/005-codex-이미지-파이프라인-첫-생성/image.png` 17f28c2 |
| draft | image | `gentleMonster@claude/project-thread-95j1zd:.relay/tasks/001-codex-test/` cb7027b |
| superseded | code | `diffusion_model@claude/code-agent-image-gen-cz6kfx:atelier/ · .claude/agents/ · studio.py · install_mac.sh (모델 보고, 클론 없음)` d3dc611 (보고값) |
| superseded | code | `gentleMonster_gemini@claude/sleepy-cori-h0ug3b:PREP.md · USAGE.md · PREVIEW.md · bench/ (모델 보고, 클론 없음)` 216efc2 (보고값) |

## 미검증 (다른 세션 모델의 말, 결론으로 쓰지 않음)

- diffusion_model 브랜치 커밋 체인 8548e43 → … → d3dc611, sd-turbo 첫 장 10.3초, 클라우드 huggingface/pypi 403 — session_0148K7k8z954TzbiEnuhyCir
- 모델이 run_steel-light · run_foam-vitrine 작업 기록 폴더를 실수로 삭제했다고 보고 — session_0148K7k8z954TzbiEnuhyCir
- GMG1~GMG11 산출물(gmg 래퍼, MCP 도구, CLI 0.60.0 고정 cf028dc, 블록 B 216efc2, gentlemonster -p 'OK' 057ef4f) 과 baseline BD-301 성공 판정, BD-242 무료 키 유지 — session_01KHd6Ft8vzjYffMcwhTDwcy / cogito5170/baseline#16
- W5 작업 공간 파일은 codex-image 를 '다른 세션에서 해결된 것으로 보임'이라 했으나, 저장소상 실제 작성 세션은 session_01WSyRrhmyx2Mhnxw2gM4sy1 · session_013ZwA36yTZqoHvjCaoKW82A (커밋 trailer) — 작업 공간 구성원 명단에 없음 — gentleMonster 5e8645b, 12ecdbd 커밋 메시지
- 허브: VM 은 설치된 relay 를 실행하므로 코드 변경 후 `pipx install --force` 필요 — docs/vm-inbox.md:3,43 의 '업데이트는 같은 명령에 --force' 와 일치 — W0-hub.md / effiency docs/vm-inbox.md
