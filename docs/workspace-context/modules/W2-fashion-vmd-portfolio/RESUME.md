# W2 패션 · VMD 지원 포트폴리오 (JAJU 라운딩 VMD · 이전 신세계 FROM THE INSIDE)
기준 2026-10-23T10:42Z · 체크포인트 claude/friendly-gates-0u80ge@af2fb56, claude/project-thread-n4rxnf@cd4f4d2, main@bdee7d6

## 지금
JAJU 포트폴리오 흐름은 /01 Observe → /02 Match. → /03 Fill. 파트 2 8–11쪽 InDesign(88a501f)에 더해 11쪽 진(zine) 판이 PDF · InDesign · 포토샵으로 나왔다(98e28f5). 표지 이미지 파일은 사용자에게서 받아야 하고, 5쪽 판 · 6쪽 글은 선택 대기.

## 이어 할 일: `storyline`
11쪽은 진 판(W2-D40)과 기존 Four places 판 중 어느 쪽을 쓸지 사용자 확인. 파트 3 Fill 쪽을 파트 2 뒤로 옮겨 B21 을 만든다. W2-O40(Match 표지 이미지) · W2-O36(5쪽 판) · W2-O37(6쪽 글) · W2-O32 를 사용자에게. 그 밖에 W2-O30 · O27 · O29 · O25 · O23.
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 1개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D40 11쪽 Four places 를 스케이트 진(PEACE. LOVE. SKATE.)의 레이아웃 · 배치 · 폰트를 참고해 진(zine) 판으로 재가공하고 PDF 로 받기
- W2-D39 파트 2 이름은 /02 Match.(맞추다): 한 벌 안에서 → 아이템끼리 → 장소에. 2-2 rev3 스토리가 확정본으로 2-1 에 넘어가 8–11쪽(표지 · Front, or back? · Selection—0…
- W2-D37 6쪽 레이아웃은 안 D(왼쪽 위 큰 사진 + 오른쪽 아래 작은 사진 둘)로 다듬는다. rev5: 큰 사진을 빨간 신호 점의 세로선까지 키우고 오른쪽 단 · 아래 글 재배치
- W2-D36 6쪽 글은 '내가 옷을 입을 때' 기준(전체를 맞추고 한 가지만 다르게), 베이글 · 지인 스타일링 이야기는 뺀다 → rev5 가 기준
- 외 25개 → state.json decisions

## 작업 중인 파일
- docs/jaju_rounding_vmd/part2_contain_story.md @9926d51
- docs/jaju_rounding_vmd/gemini_outfit_swap.md @af2fb56
- docs/jaju_rounding_vmd/indesign/part2_match/part2_match.idml @88a501f
- docs/jaju_rounding_vmd/layout/p11_zine.pdf @98e28f5
- 외 50개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 9개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
