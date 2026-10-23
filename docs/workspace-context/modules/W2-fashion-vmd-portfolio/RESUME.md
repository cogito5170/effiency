# W2 패션 · VMD 지원 포트폴리오 (JAJU 라운딩 VMD · 이전 신세계 FROM THE INSIDE)
기준 2026-10-23T04:41Z · 체크포인트 claude/friendly-gates-0u80ge@edf19dd, claude/project-thread-n4rxnf@cd4f4d2, main@bdee7d6

## 지금
JAJU 포트폴리오 현재본은 B20 18쪽 315 × 195(84b281a). 5쪽은 일정표 격자 꼴(4d9b7aa, InDesign 있음)이 새로 나왔고, 6쪽은 레이아웃 안 D rev5 위에 글 rev5 · rev6 · rev7(cb930ad, '하나의 장면 속 배치의 조화') 중 사용자 선택을 기다린다.

## 이어 할 일: `storyline`
W2-O36(5쪽 B19 판 vs 격자 꼴) · W2-O37(6쪽 글 rev5/6/7) · W2-O32(견본 값)를 정하면 B21 을 만든다. 그 밖에 W2-O30 · W2-O27 · W2-O29 · W2-O25 · W2-O23. 마지막에 10MB 이내 제출본.
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 1개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D37 6쪽 레이아웃은 안 D(왼쪽 위 큰 사진 + 오른쪽 아래 작은 사진 둘)로 다듬는다. rev5: 큰 사진을 빨간 신호 점의 세로선까지 키우고 오른쪽 단 · 아래 글 재배치
- W2-D36 6쪽 글은 '내가 옷을 입을 때' 기준(전체를 맞추고 한 가지만 다르게), 베이글 · 지인 스타일링 이야기는 뺀다 → rev5 가 기준
- W2-D35 5쪽 'Where people stop?' 왼쪽 단에 A안(질문 + 01–03 쉼 / 04–06 행위 표)을 위에, B안(서술)을 아래에 둘 다 싣는다 → B19. 가장자리에서는 머물고 가운데에서는 모인다는 '가운…
- W2-D34 사용자가 InDesign 에서 고친 4쪽 값(기준선 0.9pt · 십자 · 모서리 표시 · 바닥 줄 7pt · 파트 제목 210 타임라인 Bold 100pt · 한 줄 '일상 속, 스쳐 지나가는 사람들을 관찰하다.…
- 외 23개 → state.json decisions

## 작업 중인 파일
- docs/jaju_rounding_vmd/layout/p06_layout_d.pdf @90c8f06
- docs/jaju_rounding_vmd/indesign/p06_layout_d/p06_layout_d.idml @666afb8
- docs/jaju_rounding_vmd/indesign/p05_itinerary/p05_itinerary.idml @4d9b7aa
- docs/jaju_rounding_vmd/midjourney_room_spread.md @edf19dd
- 외 45개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 9개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
