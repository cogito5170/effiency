# W2 패션 · VMD 지원 포트폴리오 (JAJU 라운딩 VMD · 이전 신세계 FROM THE INSIDE)
기준 2026-10-22T05:42Z · 체크포인트 claude/friendly-gates-0u80ge@fcf62dd, claude/project-thread-n4rxnf@cd4f4d2, main@bdee7d6

## 지금
JAJU 포트폴리오 판형은 315 × 195 mm 로 정해졌다(10-22 사용자). 4쪽 Observe InDesign 은 새 판형, B17 PDF · 2 · 3쪽 InDesign 은 아직 A4. 2쪽 메시지는 1안 · 3안 · 리포타주 판 중 선택 대기, 사진 벽은 안 A 로 보류.

## 이어 할 일: `storyline`
plan_b13.md 의 판형 315 × 195 규칙대로 남은 쪽을 옮기고(W2-O28) 쪽마다 InDesign 을 만든다. W2-O27(2쪽 메시지 고르기) · 사진 벽 자리 · W2-O25 · W2-O23 이 남아 있다. 마지막에 10MB 이내 제출본.
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 1개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D33 판형은 앞으로 315 × 195 mm(재단 여유 3mm)로 맞춘다. 4쪽 /01 Observe. InDesign 을 이 판형으로 다시 만듦
- W2-D32 사진 벽 단일 쪽은 안 A(색과 시간)로 보류, 들어갈 자리 · 다듬기는 나중에
- W2-D31 쪽 번호는 표지부터 센다(표지 1 · 책 사진 2 · Prologue 3 … 뒤표지 18) → B17. 3쪽 Prologue 를 InDesign 파일로
- W2-D30 B13~B15: 2-2 확정 스토리를 B10 흐름에 반영(03 사진 6장, 04 d) PH-10), 첫 표지는 사용자가 준 흑백 사진 한 장만(글 · 띠 없음), 03 왼쪽 단은 안 A 시안 배치. 자주 스타일 안…
- 외 19개 → state.json decisions

## 작업 중인 파일
- docs/jaju_rounding_vmd/indesign/p02_photo_desjobert/p02_photo_desjobert.idml @8f000d4
- docs/jaju_rounding_vmd/photo_wall.md @fe98c7d
- docs/jaju_rounding_vmd/indesign/p02_reportage/p02_reportage.idml @4079787
- docs/jaju_rounding_vmd/indesign/p04_observe/p04_observe.idml @64ea10c
- 외 37개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 7개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
