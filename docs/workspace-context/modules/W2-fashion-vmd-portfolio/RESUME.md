# W2 패션 · VMD 지원 포트폴리오 (신세계 VMD 'ON DISPLAY', 패션 공간 직군 조사, AI×패션 시안)
기준 2026-10-16T06:50Z · 체크포인트 claude/friendly-gates-0u80ge@47b5377, claude/project-thread-n4rxnf@cd4f4d2, main@6acff99

## 지금
v4 FROM THE INSIDE: 이야기 단락 A 확정(05:49). 진열은 VMD 의 일 세 요소 입히다 · 비추다 · 짓다로 옮겼고(짓다 확정, 167b482), 그 한 장면 이미지 008 이 나왔다(47b5377). '얼굴 없는 사람들'은 보류.

## 이어 할 일: `cover_image`
008 이미지를 사용자에게 보여 표지로 쓸지 묻고, 정해지면 tools/inside_blueprint 를 008 기준으로 다시 빌드한다. 함께 v4 '정해야 할 것'(W2-O11)과 v4 · glass 뼈대 선택(W2-O9)을 묻는다.
- 조건: 사용자 확인 필요. 확인 없이 할 수 있는 것: 008 기준 spots 파일 준비.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 2개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D18 새 컨셉 '얼굴 없는 사람들'(지나가는 사람은 얼굴이 없고 멈추면 생긴다, WINDOW LOG 3×3 격자)은 보류
- W2-D17 제작자 세 사물(코트 · 카메라 · 모형)은 VMD 로 읽히지 않는다는 판단 → VMD 의 일 세 요소로: 입히다(조합해 입히는 마네킹) · 비추다(스폿 조명) · 짓다(1:10 진열 목업, 확정)
- W2-D14 v4 이야기 단락 A(다짐형) 확정
- W2-D13 안에서 바라보는 시선으로 스토리라인을 다시 짬 → v4 storyline_inside.md(의뢰인 세션)와 storyline_glass.md(프로젝트 스레드) 두 안
- 외 8개 → state.json decisions

## 작업 중인 파일
- docs/shinsegae_vmd/storyline_inside.md @167b482
- docs/shinsegae_vmd/storyline_glass.md @cd4f4d2
- docs/shinsegae_vmd/blueprint/from_the_inside_blueprint.pdf @67dfff0
- .relay/tasks/008-combine-light-build/image.png @47b5377
- 외 11개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 6개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
