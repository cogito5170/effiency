# W4 · 혁주 CV · 인물 사진

> 새 세션은 이 문서 대신 [RESUME.md](RESUME.md)(2000자 이하)부터 읽는다. 지금 유효한 상태는 `state.json`, 지난 이력은 `history.jsonl`. 이 문서는 모듈 설명이고 상태 서술은 만든 시점(10-16 03:30) 기준이다.

`ws:w4-hyeokju-cv-portrait` · 도메인 interior + fashion · 계약 [ws-module/1](../CONTRACT.md) · 상태 기준 2026-10-16T03:30Z

사실 · 레이아웃 유형을 받아 CV 지면(.ai/PDF)과 인물 사진 요청을 낸다.

## 인터페이스 (ops.json)

| op | 하는 일 | 입력 | 출력 | 실행 | 부수 효과 | 부르는 모듈 |
|---|---|---|---|---|---|---|
| `cv_layout` | 확정된 CV 사실과 유형으로 A4 CV 지면을 청사진 → 유형안 → .ai/PDF 로 만들고, 최종본은 1페이지(CV) + 2페이지(자기소개서)를 한 PDF 로 합친다 | type, facts, page1, page2, hero_png | ai, pdf, commit | 허브 | git commit + push (claude/* 브랜치); RELIEF 산출물은 out/ (git 미포함) | — |
| `portrait` | CV 히어로(PHOTO 01)용 실사 인물 사진 — 중앙에 멈춰 선 사람, 슬로 셔터로 흐르는 군중 — 을 요청한다. 이미지는 W5 만 만든다 | scene, brief, face_ref | png, response, graded | 허브 (스펙) → VM (생성, W5) | W5.image 를 통한 git push (.relay/tasks) | W5.image |
| `fill_blanks` | CV 의 빈칸(학교명 · 기간 · 사무소명 · 연락처 · 어학 등)을 사용자가 준 사실로만 채우고, 남은 빈칸 목록을 돌려준다 (지어내지 않음) | facts, source_files | cv, remaining_blanks, changed_files | 허브 | git commit + push (claude/* 브랜치) | — |

입력 · 출력 필드의 타입과 설명은 [ops.json](ops.json). 내부 구현(`impl`)은 참고용이며 호출자는 기대지 않는다.

## 마지막 확정 상태

2026-10-10 10:10 '그레이로 채택, 01과 02 상하 교체' (6a1d95c, CV_PAGE2_B_SIDENOTE_GRAY.ai). 이후 2026-10-15 CLAUDE.md 로 인물 사진 생성 경로가 Codex(W5)로 바뀜.

## 이어 할 곳 (resume_point)

- op: `cv_layout`
- 입력: 초안 docs/cv/CV_2PAGE_DRAFT.pdf (bfdf3f2) 다음: 사용자가 (1) 1쪽 원본(TYPE1 .ai / RELIEF 렌더) (2) CV 빈칸 사실 (3) 히어로 사진을 portrait→W5.image 로 요청할지 정하면 최종본
- 조건: 사용자 확인 필요

## 열린 일

| id | 일 | 기다리는 것 | 막힘 | 출처 |
|---|---|---|---|---|
| W4-O1 | 1페이지 + 2페이지를 하나의 PDF 로 합친 최종본 없음 (W4-D1 미실행) (→ 초안 docs/cv/CV_2PAGE_DRAFT.pdf (gentleMonster@claude/project-thread-o0m9e5 bfdf3f2), 최종본은 사용자 결정 뒤) | 허브 (W4.cv_layout) | 아니오 | 도구출력 |
| W4-O2 | 1페이지 출처 선택: cv-blueprint 의 CV_TYPE1_CARD_GRID.ai(W4 헤드라인) vs hyeokju-cv 의 RELIEF CV_HOME.pdf(같은 TYPE 1 레이아웃의 3D 렌더) — 사용자 명시 선택 기록 없음 | 사용자 | 예 | 추론·미검증 |
| W4-O3 | CV 히어로 실사 인물 사진 A–D 0장 — 프롬프트 A–D 는 docs/cv/photos/*.prompt.txt 에 있음, 이제 W5.image 로 요청해야 함 | 다른 모듈 W5 | 아니오 | 도구출력 |
| W4-O4 | CV 빈칸(학교명 · 기간 · 사무소명 · 연락처 · 어학 등) 사실 입력 | 사용자 | 예 | 추론·미검증 |
| W4-O5 | RELIEF 가 쓰는 머리 스캔(LeePerrySmith, CC BY 3.0) 출처 표기 미반영 | 허브 | 아니오 | 추론·미검증 |
| W4-O6 | 12:45 '오픈소스로 잡지를 만들어라'(Penpot·Inkscape 등) 요청 결과가 브랜치에 없음 — 처리 여부 불명 | 사용자 | 아니오 | 추론·미검증 |
| W4-O7 | cv-blueprint · hyeokju-cv PR · main 머지 없음 | 사용자 | 아니오 | 도구출력 |

## 확정 사항 (저장소 파일로 확인)

| id | 내용 | 출처 | 근거 | 파일 확인 |
|---|---|---|---|---|
| W4-C1 | 제출 문서 구성: CV 1장 + 자기소개서 1장 = 한 PDF, 포트폴리오와 별도 | 사용자 | `claude/cv-blueprint:docs/cv/blueprint/page2.py:1` 70c1a58 | ✓ |
| W4-C2 | 1페이지는 TYPE 1(카드 그리드) 채택, 헤드라인은 문장 아닌 두 단어 — W4 'FRAME & INTERIOR' 선정, CV_TYPE1_CARD_GRID.ai 에 반영 | 사용자 | `claude/cv-blueprint:docs/cv/blueprint/hero_words.py:28` c5b355d | ✓ |
| W4-C3 | CV 는 '우리의 엔진'으로 생성 → 페이지 엔진 이름 RELIEF (구 cv3d), TYPE 1 레이아웃 SVG 를 3D 세트로 렌더 | 사용자 | `claude/hyeokju-cv:gentle_monster/relief/__init__.py:1` 74476c2 | ✓ |
| W4-C4 | 2페이지는 B안(여백 표시 1단 사이드노트)을 .ai 로 | 사용자 | `claude/cv-blueprint:docs/cv/ai/CV_PAGE2_B_SIDENOTE.ai` 63ee8fe | ✓ |
| W4-C5 | CV 히어로 인물은 일러스트가 아니라 실제 사람처럼 (실사 사진) | 사용자 | `claude/hyeokju-cv:gentle_monster/relief/photo.py:58` ec5163a | ✓ |
| W4-C6 | 2페이지에 문항 1 원고 〈계단을 통로가 아닌 전시로 만든 곳〉(861자) 추가 | 사용자 | `claude/cv-blueprint:docs/cv/blueprint/page2.py` 9c33997 | ✓ |
| W4-C7 | 2페이지 회색 바탕(#2E2E2E) 채택, 01/02 상하 순서 교체(본인 소개 위 · 지원 이유 아래) — CV_PAGE2_B_SIDENOTE_GRAY.ai | 사용자 | `claude/cv-blueprint:docs/cv/blueprint/page2.py:392` 6a1d95c | ✓ |
| W4-C8 | 새 이미지(인물 포함)는 Codex(codex-image, image-spec.json → VM)로만; Gemini 직접 호출 금지 | 사용자 | `main:CLAUDE.md:3` 12ecdbd | ✓ |
| W4-C9 | Gemini 이미지 생성 시도는 HTTP 429(free tier limit 0)로 실패, 이미지 0장; claude/relief-photos 브랜치는 원격에 없음 | 도구출력 | `claude/hyeokju-cv:docs/relief/requests/CMD-REL1.md:4` 84980aa | ✓ |

## 의사결정 이력 (오래된 것 → 최신)

| id | 날짜 | 결정 | 누가 | 대체한 것 |
|---|---|---|---|---|
| W4-D1 | 2026-10-09 | CV 1장 + 자기소개서 1장 = 한 PDF, 포트폴리오와 별도 | 사용자 | — |
| W4-D2 | 2026-10-09 | 1페이지 TYPE 1(카드 그리드) 채택 (TYPE 2 사이드바 탈락) | 사용자 | — |
| W4-D3 | 2026-10-09 | 헤드라인은 문장이 아닌 두 단어, 9안 중 W4 FRAME & INTERIOR | 사용자 | C-01 헤드라인 6안(84460dc, 문장형) |
| W4-D4 | 2026-10-09 | Remarque Atelier 디자인 시스템 → 혁주 CV(젠틀몬스터 매거진풍)로 전환, 글은 줄이고 이미지·무드로 | 사용자 | 디자인 시스템 요청(a738945e) |
| W4-D5 | 2026-10-09 | CV 는 '우리의 엔진'(RELIEF)으로 생성, 엔진 이름 RELIEF | 사용자 | — |
| W4-D6 | 2026-10-10 | 2페이지 B안, 배경은 당시 PDF 색(#E6E2DA)으로 .ai | 사용자 | — |
| W4-D7 | 2026-10-10 | 인물은 일러스트 말고 실제 사람; 'Gemini 대신 너가' → 'baseline 통해 VM 에 전달' | 사용자 | — |
| W4-D8 | 2026-10-10 | 2페이지에 문항 1 원고(861자) 추가 | 사용자 | — |
| W4-D9 | 2026-10-10 | 검은 · 회색 바탕 버전 제작 → 회색(#2E2E2E) 채택, 01/02 상하 교체 — W4 의 가장 최근 디자인 확정 | 사용자 | W4-D6 의 #E6E2DA 바탕 |
| W4-D10 | 2026-10-15 | 모든 새 이미지는 Codex(codex-image) — 인물 사진 A–D 의 Gemini(relief photo) · VM 오픈 모델(CMD-REL1) 경로 대체 | 사용자 | W4-D7 의 생성 경로 (실사 인물이라는 내용 결정은 유지) |

## 산출물

| 상태 | 종류 | 위치 |
|---|---|---|
| draft | pdf | `gentleMonster@claude/project-thread-o0m9e5:docs/cv/CV_2PAGE_DRAFT.pdf` bfdf3f2 |
| final | ai | `gentleMonster@claude/cv-blueprint:docs/cv/ai/CV_TYPE1_CARD_GRID.ai (+ __T1_03_HERO.ai, .svg)` c5b355d |
| final | ai | `gentleMonster@claude/cv-blueprint:docs/cv/ai/CV_PAGE2_B_SIDENOTE_GRAY.ai (+ .svg)` 6a1d95c |
| superseded | ai | `gentleMonster@claude/cv-blueprint:docs/cv/ai/CV_PAGE2_B_SIDENOTE.ai, CV_PAGE2_B_SIDENOTE_BLACK.ai` 6a1d95c |
| superseded | ai | `gentleMonster@claude/cv-blueprint:docs/cv/ai/CV_TYPE2_SIDEBAR.ai` ba4efa2 |
| draft | pdf | `gentleMonster@claude/cv-blueprint:docs/cv/blueprint/{cv_blueprint,cv_types,hero_options,hero_words,page2_options}.pdf, types/*` 6a1d95c |
| final | code | `gentleMonster@claude/cv-blueprint:docs/cv/blueprint/{bp,cv_blueprint,cv_types,hero_options,hero_words,page2,export_ai}.py` 6a1d95c |
| draft | code | `gentleMonster@claude/hyeokju-cv:gentle_monster/relief/* (RELIEF 0.1), layouts/type1_card_grid.svg` 84980aa |
| draft | doc | `gentleMonster@claude/hyeokju-cv:docs/portfolio/cv.html` 7deade0 |
| draft | doc | `gentleMonster@claude/hyeokju-cv:docs/cv/photos/{A,B,C,D}.prompt.txt` 84980aa |
| superseded | doc | `gentleMonster@claude/hyeokju-cv:docs/relief/requests/CMD-REL1.md (VM 오픈 모델 지시 초안)` 84980aa |
| superseded | code | `gentleMonster@claude/hyeokju-cv:gentle_monster/relief/photo.py (Gemini 이미지 경로)` 9a62f70 |

## 미검증 (다른 세션 모델의 말, 결론으로 쓰지 않음)

- 최종 전달물은 CV_PAGE2_B_SIDENOTE_GRAY.ai (2페이지) — 파일과 커밋은 확인, '최종'이라는 판단은 모델 보고 — session_011o2Zk5R9TTMbgacGgwBcjp
- JEONG_HYEOKJU_SPA_CV.pdf(A4 5쪽) · CV_HOME.pdf 렌더 — out/ 산출물, git 에 없음 — session_01EwZvjiXu5ppJiaJniHRYoT
- Monochrome Résumé 아티팩트 K7WAqyzQ1CY5BNMd9D45ZK (split · bleed · poster) — session_01EwZvjiXu5ppJiaJniHRYoT
- VM(agy) 로그인 만료로 baseline 이슈 #83 declined — session_01EwZvjiXu5ppJiaJniHRYoT
- relief-photos 세션이 A.prompt.txt 만 로컬에 썼다는 보고 — 단, hyeokju-cv(84980aa)에는 A–D 프롬프트 4개가 모두 커밋되어 있음 (카드/W4 파일의 '커밋 안 함'은 relief-photos 세션 로컬 한정) — session_017EVHBofkdPhvYSUBCeRAH4 vs gentleMonster@claude/hyeokju-cv
- page2.py 머리말은 'Q1 still being written, reserved as grey bars' 라고 적혀 있으나 이후 9c33997 에서 문항 1 원고(861자)가 반영됨 — 독스트링이 오래됨 — docs/cv/blueprint/page2.py:5
- 2페이지 원고는 W1(혁주 자소서 session_01FYwvzhDCTYAAM1u37s5yGE)와 맞물림 — session_011o2Zk5R9TTMbgacGgwBcjp 카드
