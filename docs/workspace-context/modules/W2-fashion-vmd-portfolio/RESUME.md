# W2 패션 · VMD 지원 포트폴리오 (신세계 VMD 'ON DISPLAY', 패션 공간 직군 조사, AI×패션 시안)
기준 2026-10-16T06:30Z · 체크포인트 claude/friendly-gates-0u80ge@a95c85d, claude/project-thread-n4rxnf@cd4f4d2, main@6acff99

## 지금
안에서 바라보는 시선(사용자 관점, 10-16 03:12)으로 v4 FROM THE INSIDE 를 진행 중: 이야기 단락 A(다짐형) 확정(05:49), 무대는 백화점 실내, 진열은 제작자 세 요소(WEAR · SEE · BUILD)로 청사진(67dfff0). 006 · 007 이미지 요청이 VM 에 걸려 있다.

## 이어 할 일: `cover_image`
relay 006 · 007 의 response.json 을 확인하고 005 · 006 · 007 세 장을 사용자에게 보여 표지 진열안을 고르게 한다. 함께 v4 '정해야 할 것' 4가지(W2-O11)와 v4 · glass 뼈대 선택(W2-O9)을 묻는다.
- 조건: 사용자 확인 필요. 확인 없이 할 수 있는 것: 006 · 007 결과 확인, 고른 이미지로 inside_blueprint 다시 빌드.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 1개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D16 쇼윈도에 상품 대신 제작자를 진열: WEAR(롱코트 마네킹) · SEE(필름 카메라) · BUILD(쇼윈도 모형)
- W2-D14 v4 이야기 단락 A(다짐형) 확정
- W2-D13 안에서 바라보는 시선으로 스토리라인을 다시 짬 → v4 storyline_inside.md(의뢰인 세션)와 storyline_glass.md(프로젝트 스레드) 두 안
- W2-D12 하나의 장면을 묘사하는 '이미지적 표현'의 청사진을 만든다 (13:38 요청이 중단된 뒤 재요청) → THE STILL RUNWAY
- 외 7개 → state.json decisions

## 작업 중인 파일
- docs/shinsegae_vmd/storyline_inside.md @67dfff0
- docs/shinsegae_vmd/storyline_glass.md @cd4f4d2
- docs/shinsegae_vmd/blueprint/from_the_inside_blueprint.pdf @67dfff0
- .relay/tasks/005-selling-the-maker/image.png @93f9a25
- 외 11개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 6개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
