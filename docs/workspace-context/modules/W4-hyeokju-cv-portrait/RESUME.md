# W4 혁주 CV · 인물 사진 (CV 청사진 → .ai, RELIEF 지면 엔진, CV 히어로 실사 인물)
기준 2026-10-25T13:42Z · 체크포인트 main@bdee7d6, claude/cv-blueprint@1944b21, claude/hyeokju-cv@84980aa

## 지금
1쪽 TYPE 1 · 2쪽 그레이 사이드노트(6a1d95c) 위에, 2026-10-25 자주(JAJU) 지원용 CV 를 따로 짬. 지금 판은 v4: 사용자 폼 클로드.idml(TYPE 2C 흰 바탕, 사이드바 1/3) 위 재배치(D13), 사진 S(D12), 글은 자기소개서 확정본 + 젠틀몬스터 CV 사실과 사용자 수정(C12). TYPE 1 v3 안(D11)도 남아 있음. 인물 사진은 Codex(W5) 경로(D10).

## 이어 할 일: `cv_layout`
자주 CV v4(CV_JAJU_V4.idml)를 사용자가 InDesign 에서 확인한 고칠 점을 cv_jaju_v4.py 로 반영. TYPE 1 v3(W4-O8)를 쓸지, 2쪽과 합친 PDF(W4-O1), 빈칸 사실(W4-O4)은 그대로 남음.
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W4-O2 1페이지 출처 선택: cv-blueprint 의 CV_TYPE1_CARD_GRID.ai(W4 헤드라인) vs hyeokju-cv 의 RELIEF CV_HOME.pdf(같은 TYPE 1 레이아웃의 3D 렌더) — 사용자 명시 선택 기록 없음
- W4-O4 CV 빈칸(학교명 · 기간 · 사무소명 · 연락처 · 어학 등) 사실 입력

## 지금 유효한 결정 (최근순)
- W4-D13 자주 CV 는 사용자가 InDesign 에서 만든 폼 '클로드.idml'(TYPE 2C, 흰 바탕, 사이드바 1/3) 위에 v4 로 재배치: 폼의 마스터 · 스타일 · 레이어 · 사진 틀(IMG_5685.psd)은…
- W4-D12 TYPE 2 사이드바 사진은 S(48×64) 로, 그에 맞춰 전체 재배치(CV_TYPE2B_SIDEBAR)
- W4-D11 자주(JAJU)용 1페이지는 v3 배치: 첫 화면(FRAME & INTERIOR) 빼고 위 프로필 블록을 62→38 로 줄이고 강점 카드 3개를 크게
- W4-D10 모든 새 이미지는 Codex(codex-image) — 인물 사진 A–D 의 Gemini(relief photo) · VM 오픈 모델(CMD-REL1) 경로 대체
- W4-D9 검은 · 회색 바탕 버전 제작 → 회색(#2E2E2E) 채택, 01/02 상하 교체 — W4 의 가장 최근 디자인 확정
- W4-D8 2페이지에 문항 1 원고(861자) 추가
- 외 7개 → state.json decisions

## 작업 중인 파일
- docs/cv/ai/CV_JAJU_V3_J{1_HEMP,2_PORCELAIN,3_CHARCOAL}.ai @b7ec8f6
- docs/cv/ai/CV_TYPE2_SIDEBAR_PHOTO_{S,XS}.ai @94d3af5
- docs/cv/ai/CV_TYPE2C_JAJU.ai @c18b8ba
- docs/cv/indesign/CV_TYPE2C_JAJU{,_WHITE,_GRAY,_IVORY}.idml @e68edc5
- docs/cv/indesign/CV_JAJU_V4.idml @1944b21
- 외 6개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W4-hyeokju-cv-portrait/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 9개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
