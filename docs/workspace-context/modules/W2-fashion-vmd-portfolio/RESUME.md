# W2 패션 · VMD 지원 포트폴리오 (JAJU 라운딩 VMD · 이전 신세계 FROM THE INSIDE)
기준 2026-10-21T06:41Z · 체크포인트 claude/friendly-gates-0u80ge@0be22a5, claude/project-thread-n4rxnf@cd4f4d2, main@bdee7d6

## 지금
10-21 대상을 JAJU 라운딩 VMD 로 바꿨다. 표지 · 1쪽은 B안(사진 띠 + 검정)을 이어 쓰고, 장 순서는 사진 → 건축 → 패션(사용자 결정). 장 1 사진은 재료 17장 중 15장 파일을 받아 2~4쪽 시안(3bdb976)까지 왔다.

## 이어 할 일: `storyline`
docs/jaju_rounding_vmd/process.md 의 단계대로 이어 간다. 지금은 장 1 사진: assets.md 의 고르기 제안(W2-O20)과 ch1_photo.pdf 시안을 사용자가 확인하고, 사진마다 장소 · 때를 받는다. 그 다음 장 2 건축 재료.
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 2개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D25 JAJU 포트폴리오 장 순서: 표지 → 사진(관찰하다 · 뷰파인더) → 건축(담다 · 마당) → 패션(채우다 · 작은 따옴표). 재료는 지원자의 사진 · 패션 · 건축만, JAJU 로고 · 사진은 쓰지 않음. 장마…
- W2-D24 포트폴리오 대상을 JAJU 라운딩 VMD 로 전환. 기존 P1(FROM THE INSIDE) · v5 는 보존, 표지 · 1쪽은 B안을 그대로 쓴다
- W2-D23 P1 표지 + 1쪽은 B안(Galatasaray 방식: 사진 띠 + 검정 · 메시지 한 문장)으로. 표지 이미지는 사용자 제공. cover_b.* (InDesign IDML · JSX · zip)가 현재본
- W2-D22 P1(포트폴리오 1안) = flow_etereo.md 의 목차 · 흐름(ETÉREO 펼침면 문법, v4 뼈대 기준). 펼침면 종류와 목차는 ETÉREO 11장 원본으로 다시 짠 p1_types.md(타입 10가지)…
- 외 14개 → state.json decisions

## 작업 중인 파일
- docs/shinsegae_vmd/p1_layout/cover_b_indesign.zip @4db537a
- docs/jaju_rounding_vmd/process.md @62ae319
- docs/jaju_rounding_vmd/assets.md @3bdb976
- docs/jaju_rounding_vmd/layout/ch1_photo.pdf @3bdb976
- 외 25개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 7개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
