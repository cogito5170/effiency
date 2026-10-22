# W2 패션 · VMD 지원 포트폴리오 (JAJU 라운딩 VMD · 이전 신세계 FROM THE INSIDE)
기준 2026-10-22T06:42Z · 체크포인트 claude/friendly-gates-0u80ge@fcf62dd, claude/project-thread-n4rxnf@cd4f4d2, main@bdee7d6

## 지금
JAJU 포트폴리오 현재본은 B18 18쪽 315 × 195(cc0d222): 사용자가 InDesign 에서 고친 4쪽 값을 모든 쪽에 반영했고 5–18쪽 InDesign 이 나왔다. 2쪽 메시지는 1안 · 3안 · 리포타주 판 중 선택 대기, 사진 벽은 안 A 로 보류.

## 이어 할 일: `storyline`
layout_315x195.md 의 값이 기준. W2-O27(2쪽 메시지 고르기) 뒤 2 · 3쪽을 315 × 195 로(W2-O29). 사진 벽 자리 · W2-O25 · W2-O23 이 남아 있다. 마지막에 10MB 이내 제출본.
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 1개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D34 사용자가 InDesign 에서 고친 4쪽 값(기준선 0.9pt · 십자 · 모서리 표시 · 바닥 줄 7pt · 파트 제목 210 타임라인 Bold 100pt · 한 줄 '일상 속, 스쳐 지나가는 사람들을 관찰하다.…
- W2-D33 판형은 앞으로 315 × 195 mm(재단 여유 3mm)로 맞춘다. 4쪽 /01 Observe. InDesign 을 이 판형으로 다시 만듦
- W2-D32 사진 벽 단일 쪽은 안 A(색과 시간)로 보류, 들어갈 자리 · 다듬기는 나중에
- W2-D31 쪽 번호는 표지부터 센다(표지 1 · 책 사진 2 · Prologue 3 … 뒤표지 18) → B17. 3쪽 Prologue 를 InDesign 파일로
- 외 20개 → state.json decisions

## 작업 중인 파일
- docs/jaju_rounding_vmd/indesign/p02_reportage/p02_reportage.idml @4079787
- docs/jaju_rounding_vmd/indesign/p04_observe/p04_observe.idml @64ea10c
- docs/jaju_rounding_vmd/layout/plan_b18.pdf @cc0d222
- docs/jaju_rounding_vmd/indesign/p05-18_315x195/p05-18_315x195.idml @cc0d222
- 외 38개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 7개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
