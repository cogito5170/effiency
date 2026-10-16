# W2 · 패션 · VMD 지원 포트폴리오

> 새 세션은 이 문서 대신 [RESUME.md](RESUME.md)(2000자 이하)부터 읽는다. 지금 유효한 상태는 `state.json`, 지난 이력은 `history.jsonl`. 이 문서는 모듈 설명이고 상태 서술은 만든 시점(10-16 03:30) 기준이다.

`ws:w2-fashion-vmd-portfolio` · 도메인 fashion · 계약 [ws-module/1](../CONTRACT.md) · 상태 기준 2026-10-16T03:30Z

브리프와 사용자 결정을 받아 스토리 · 장면 청사진(A3/A4) · 표지 이미지 요청 · 공고 조사 결과를 낸다.

## 인터페이스 (ops.json)

| op | 하는 일 | 입력 | 출력 | 실행 | 부수 효과 | 부르는 모듈 |
|---|---|---|---|---|---|---|
| `storyline` | 포트폴리오의 이야기(스토리라인 · 쪽마다의 문장)를 사용자 관찰과 결정에서 세우고 고친다 | brief, decisions, facts | story, manuscript, to_decide | 허브 | git push (claude/friendly-gates-0u80ge) | — |
| `scene_blueprint` | 장면 · 표지 · 이야기 전체를 코드로 렌더하고 A3 청사진 PDF 로 만든다 (렌더링 — 이미지 생성 아님) | kind, dims, stage, concept_image | pdf, preview, render | 허브 | git push (산출물 커밋 시) | — |
| `cover_image` | 표지 · 장면의 실사풍 컨셉 이미지를 얻는다 | scene, task_name | png, response | VM | W5.image 를 통해 git push (claude/* 브랜치) → VM 결과 커밋 | W5.image |
| `job_scan` | 패션 · 의류 브랜드의 공간 · VMD 직군 공고를 찾고 마감 · 조건을 정리한다 | query, as_of | postings, notes | 허브 | none | — |
| `submission_jpeg` | 제출용 사진을 용량 범위 · sRGB · JPG 로 맞춘다 (EXIF 유지) | files, max_mb, min_mb, long_edge | jpgs | 허브 | none | — |

입력 · 출력 필드의 타입과 설명은 [ops.json](ops.json). 내부 구현(`impl`)은 참고용이며 호출자는 기대지 않는다.

## 마지막 확정 상태

ON DISPLAY 스토리 v3(사용자 관찰 '주체는 가만히, 내가 움직인다') 원고와 한 장면 청사진 THE STILL RUNWAY(Codex 컨셉 이미지 + three.js 장노출 렌더, A3)가 나왔다(10-15 15:10). 판형 A4 가로 · 젠틀몬스터 스토리 무시 · 상품연출/착장 VMD 방향은 사용자 확정. 표지 · 한 줄 · 기획안 등 5가지는 사용자 결정 대기.

## 이어 할 곳 (resume_point)

- op: `storyline`
- 입력: storyline_v3.md '정해야 할 것' 1~5 와 story_text.md 빈칸(____)을 사용자에게 묻고 답을 v3 · 원고에 반영. 표지가 THE STILL RUNWAY 로 정해지고 직접 촬영이 어려우면 cover_image(→W5.image, 002 스펙 재사용·수정), 촬영 가능하면 촬영 준비 목록을 scene_blueprint 값(dims.mjs)으로 만든다.
- 조건: 사용자 확인 필요 (5가지 결정 · 빈칸 사실은 지어낼 수 없음). 확인 없이 할 수 있는 것: READING SHINSEGAE 사실 출처 재확인.

## 열린 일

| id | 일 | 기다리는 것 | 막힘 | 출처 |
|---|---|---|---|---|
| W2-O1 | storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVERSE RUNWAY / 둘 다 ④ 빨강 한 점 ⑤ 표지 직접 촬영 가능 여부 | 사용자 | 예 | 도구출력 |
| W2-O2 | 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처 | 사용자 | 예 | 도구출력 |
| W2-O3 | READING SHINSEGAE 사실(2014년 · 1935년 · 10년 · 레드닷) 재확인, SCENT 향수 브랜드명 노출 여부 | 사용자(브랜드명) · 허브(사실 확인) | 아니오 | 도구출력 |
| W2-O4 | 같은 공고 조건: 포트폴리오는 이메일 첨부 10MB 이내 · 면접 10월 내 · 조기 마감 가능 (W1 공고 파일) | 사용자 | 아니오 | 도구출력 |
| W2-O5 | 청사진 3종은 A3(420×297) 작업 도면, 포트폴리오 본문은 A4 가로 — 지면 배치(레이아웃) 단계는 아직 없음 | 허브 | 아니오 | 추론·미검증 |
| W2-O6 | 채용공고 조사(01Ctu8): 유니클로 VMD Designer(마감 10/19, 경력 3년+) 등 결과가 검색 요약뿐 — 원문 확인 필요, 파일 · 커밋 없음 | 사용자 (후속 요청 없음, REVIEW_READY) | 아니오 | 추론·미검증 |
| W2-O7 | AI×패션 시안: '안경을 만들어주는가?'에 대한 A(시착 검증) / B(얼굴 치수 입력) 선택 없음, 제출 문항(AI 기술 1개 서술) 작성 여부 불명 | 사용자 | 아니오 | 추론·미검증 |
| W2-O8 | claude/friendly-gates-0u80ge 는 PR 없이 원격에만 있음 (main 미병합, main 은 병합해 둠) | 사용자 | 아니오 | 도구출력 |

## 확정 사항 (저장소 파일로 확인)

| id | 내용 | 출처 | 근거 | 파일 확인 |
|---|---|---|---|---|
| W2-C1 | 젠틀몬스터 포트폴리오(SPA) 스토리라인은 쓰지 않고 새로 짠다 (사진 · 스타일 기록 · 공간 작업 도구만 가져옴) | 사용자 | `claude/friendly-gates-0u80ge:docs/shinsegae_vmd/storyline.md:4` ebec462 | ✓ |
| W2-C2 | 포트폴리오 판형 A4 가로 | 사용자 | `claude/friendly-gates-0u80ge:docs/shinsegae_vmd/storyline.md:3` ebec462 | ✓ |
| W2-C3 | 방향: '나는 상품을 연출하고 마네킹에 착장을 입히는 VMD' — 책은 나를 진열한 매장, 읽는 사람이 나를 '소비'하도록 | 사용자 | `claude/friendly-gates-0u80ge:docs/shinsegae_vmd/storyline.md:7` ebec462 | ✓ |
| W2-C4 | 컨셉: 보다 · 집다 · 챙기다 세 행위를 합친 전달 | 사용자 | `claude/friendly-gates-0u80ge:docs/shinsegae_vmd/see_pick_keep.md:1` f350ed8 | ✓ |
| W2-C5 | 사용자 관찰: 쇼핑은 패션쇼 같지만 반대 — 패션쇼는 주체가 걷고 나는 앉아 있고, 쇼핑은 주체가 가만히 있고 내가 움직인다. 조화로운 아이템 앞으로 발걸음을 옮긴다 | 사용자 | `claude/friendly-gates-0u80ge:docs/shinsegae_vmd/storyline_v3.md:5` 1d0ef4c | ✓ |
| W2-C6 | 이미지 안을 만들기 전에 스토리를 문장으로 먼저 다듬는다 | 사용자 | `claude/friendly-gates-0u80ge:docs/shinsegae_vmd/story_text.md:1` 8636a83 | ✓ |
| W2-C7 | 새 이미지는 모두 Codex 로 만든다 (사용자 결정) — 10-15 12:06 의 '프롬프트는 Claude, 생성은 미드저니' 지시를 대체 | 사용자 | `main:CLAUDE.md:3` 6acff99 | ✓ |
| W2-C8 | relay 002-still-runway: VM Codex 이미지 생성 status=done, exit_code=0, image.png (118초) | 도구출력 | `claude/friendly-gates-0u80ge:.relay/tasks/002-still-runway/response.json:4` 467a309 | ✓ |
| W2-C9 | THE STILL RUNWAY 한 장면 청사진 빌드: still_runway_blueprint.pdf(A3 420×297) · _preview.jpg · still_runway_render.jpg | 도구출력 | `claude/friendly-gates-0u80ge:tools/scene_blueprint/build.mjs:50` 8106369 | ✓ |
| W2-C10 | (AI×패션 시안) 3D 렌더링이 필요한 시안은 제외하고 RELIEF(부조)를 쓴다 | 사용자 | `claude/blissful-cori-hookcx (origin 에 없음):36eafa9b-efc1-4813-9989-30736a96dca9` | 이벤트만 |
| W2-C11 | (AI×패션 시안) 표현은 '조형적으로', '트리거가 발생하면 조형물이 움직이는 원리'로 | 사용자 | `:06428777-… / 7ae1337e-… (카드에 축약 id)` | 이벤트만 |

## 의사결정 이력 (오래된 것 → 최신)

| id | 날짜 | 결정 | 누가 | 대체한 것 |
|---|---|---|---|---|
| W2-D1 | 2026-10-09T17:05Z | AI×패션 시안: RELIEF(부조) 사용, 3D 렌더 시안 제외 | 사용자 | — |
| W2-D2 | 2026-10-09T17:21Z | AI×패션 시안 표현을 '조형적 · 트리거로 움직이는 조형물'로 좁힘 (17:12 drift 소설 요청은 사용자가 중단) | 사용자 | W2-D1 |
| W2-D3 | 2026-10-15T12:06Z | 신세계 VMD 포트폴리오 커버 컨셉 이미지: 프롬프트는 Claude, 생성은 미드저니 | 사용자 | — |
| W2-D4 | 2026-10-15T12:16Z | 젠틀몬스터 스토리라인 무시, 새 스토리라인 (v1 WINDOWS OF TIME) | 사용자 | — |
| W2-D5 | 2026-10-15T12:25Z | A4 가로, 쇼윈도에 나를 설명하는 요소 3가지, 상품연출 · 착장 VMD 방향 → v2 'ON DISPLAY(나를 진열한 매장)' | 사용자 | W2-D4 |
| W2-D6 | 2026-10-15T12:50Z | 보다 · 집다 · 챙기다 세 행위 컨셉 | 사용자 | — |
| W2-D7 | 2026-10-15T12:55Z | 컨셉 이미지를 청사진으로 보이기 → 표지 1-D(SEE · PICK · KEEP 쇼윈도) A3 청사진 | 사용자 | — |
| W2-D8 | 2026-10-15T13:19Z | 사용자 관찰(주체는 가만히, 내가 움직인다)로 이야기 첫 문장을 다시 세움 → v3 (v2 뼈대 유지) | 사용자 | W2-D5 |
| W2-D9 | 2026-10-15T13:23Z | 이미지 전에 스토리를 문장으로 → ON DISPLAY 원고 | 사용자 | — |
| W2-D10 | 2026-10-15T13:27Z | 스토리 전체를 하나의 청사진으로 | 사용자 | — |
| W2-D11 | 2026-10-15 | 이미지 생성 경로를 미드저니에서 Codex(VM relay)로 — main CLAUDE.md '이미지는 모두 Codex' (사용자 결정) | 사용자 | W2-D3 |
| W2-D12 | 2026-10-15T15:05Z | 하나의 장면을 묘사하는 '이미지적 표현'의 청사진을 만든다 (13:38 요청이 중단된 뒤 재요청) → THE STILL RUNWAY | 사용자 | — |

## 산출물

| 상태 | 종류 | 위치 |
|---|---|---|
| draft | doc | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/story_text.md` 8636a83 |
| draft | doc | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/storyline_v3.md` 1d0ef4c |
| superseded | doc | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/storyline.md` ebec462 |
| draft | doc | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/see_pick_keep.md` f350ed8 |
| draft | doc | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/concepts_beyond_window.md` 6cd8d30 |
| superseded | doc | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/image_prompts.md` e1f8b82 |
| draft | pdf | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/blueprint/still_runway_blueprint.pdf` 8106369 |
| draft | render | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/blueprint/still_runway_render.jpg` 8106369 |
| draft | image | `gentleMonster@claude/friendly-gates-0u80ge:.relay/tasks/002-still-runway/image.png` 467a309 |
| draft | pdf | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/blueprint/story_blueprint.pdf` c852c71 |
| draft | pdf | `gentleMonster@claude/friendly-gates-0u80ge:docs/shinsegae_vmd/blueprint/cover_blueprint.pdf` b10b245 |
| final | code | `gentleMonster@claude/friendly-gates-0u80ge:tools/scene_blueprint/` 8106369 |
| final | code | `gentleMonster@claude/friendly-gates-0u80ge:tools/window_blueprint/` b10b245 |
| final | code | `gentleMonster@claude/friendly-gates-0u80ge:tools/story_blueprint/build.mjs` c852c71 |
| final | code | `gentleMonster@claude/friendly-gates-0u80ge:tools/contest_jpeg.py` 6b02cd3 |
| final | doc | `gentleMonster@claude/friendly-gates-0u80ge:docs/contests.md` 16b89d9 |
| draft | doc | `claude.ai@artifact:https://claude.ai/artifact/UcSTSA7Bxd2BxNPALedxSM`  |
| draft | doc | `claude.ai@artifact:https://claude.ai/artifact/H7V166vea7LHa6r5SqU2Hu`  |

## 미검증 (다른 세션 모델의 말, 결론으로 쓰지 않음)

- 장면 THE STILL RUNWAY(흰 큐브에 앉은 사람 + 흐리게 지나가는 사람들, 걷다 · 꺾이다 · 집다 · 챙기다)를 표지로 — session_01PEVQJv8SCpLFv14iXTm9Ek / storyline_v3.md:108
- 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' · 책 제목 ON DISPLAY — storyline_v3.md:11, storyline.md
- 도면 수치(스튜디오 8×8.2 m, 카메라 1.2 m 등) — tools/scene_blueprint/dims.mjs:5-6
- 카드의 tools/scene_blueprint/{build,dims,scene,sheet}.mjs 표기 — session_01PEVQJv8SCpLFv14iXTm9Ek 카드
- 패션 공간 직군 공고 현황(유니클로 10/19, 무신사 마감, 해외 COS VMD 마감일 등) — session_01Ctu8Xc8KMJPnwqyzGUHcmY
- REREAD 는 안경을 만들지 않음 · A/B 단계 추가 필요, 추천 A — session_011RbA1e4nPywwwdsq2ZNe4N
