# W4 혁주 CV · 인물 사진 (CV 청사진 → .ai, RELIEF 지면 엔진, CV 히어로 실사 인물)
기준 2026-10-16T07:45Z · 체크포인트 main@bdee7d6, claude/cv-blueprint@6a1d95c, claude/hyeokju-cv@84980aa

## 지금
2026-10-10 10:10 '그레이로 채택, 01과 02 상하 교체' (6a1d95c, CV_PAGE2_B_SIDENOTE_GRAY.ai). 이후 2026-10-15 CLAUDE.md 로 인물 사진 생성 경로가 Codex(W5)로 바뀜.

## 이어 할 일: `cv_layout`
초안 docs/cv/CV_2PAGE_DRAFT.pdf (bfdf3f2) 다음: 사용자가 (1) 1쪽 원본(TYPE1 .ai / RELIEF 렌더) (2) CV 빈칸 사실 (3) 히어로 사진을 portrait→W5.image 로 요청할지 정하면 최종본
- 조건: 사용자 확인 필요

## 사용자에게 물을 것
- W4-O2 1페이지 출처 선택: cv-blueprint 의 CV_TYPE1_CARD_GRID.ai(W4 헤드라인) vs hyeokju-cv 의 RELIEF CV_HOME.pdf(같은 TYPE 1 레이아웃의 3D 렌더) — 사용자 명시 선택 기록 없음
- W4-O4 CV 빈칸(학교명 · 기간 · 사무소명 · 연락처 · 어학 등) 사실 입력

## 지금 유효한 결정 (최근순)
- W4-D10 모든 새 이미지는 Codex(codex-image) — 인물 사진 A–D 의 Gemini(relief photo) · VM 오픈 모델(CMD-REL1) 경로 대체
- W4-D9 검은 · 회색 바탕 버전 제작 → 회색(#2E2E2E) 채택, 01/02 상하 교체 — W4 의 가장 최근 디자인 확정
- W4-D8 2페이지에 문항 1 원고(861자) 추가
- W4-D7 인물은 일러스트 말고 실제 사람; 'Gemini 대신 너가' → 'baseline 통해 VM 에 전달'
- W4-D6 2페이지 B안, 배경은 당시 PDF 색(#E6E2DA)으로 .ai
- W4-D5 CV 는 '우리의 엔진'(RELIEF)으로 생성, 엔진 이름 RELIEF
- 외 4개 → state.json decisions

## 작업 중인 파일
- docs/cv/CV_2PAGE_DRAFT.pdf @bfdf3f2
- docs/cv/blueprint/{cv_blueprint,cv_types,hero_options,hero_words,page2_options}.pdf, types/* @6a1d95c
- gentle_monster/relief/* (RELIEF 0.1), layouts/type1_card_grid.svg @84980aa
- docs/portfolio/cv.html @7deade0
- docs/cv/photos/{A,B,C,D}.prompt.txt @84980aa

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W4-hyeokju-cv-portrait/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 7개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
