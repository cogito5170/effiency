# W2 패션 · VMD 지원 포트폴리오 (신세계 VMD 'ON DISPLAY', 패션 공간 직군 조사, AI×패션 시안)
기준 2026-10-21T05:41Z · 체크포인트 claude/friendly-gates-0u80ge@0be22a5, claude/project-thread-n4rxnf@cd4f4d2, main@bdee7d6

## 지금
P1(FROM THE INSIDE, ETÉREO 흐름)의 표지 + 1쪽을 사용자가 B안(Galatasaray 방식)으로 정했고 InDesign 파일까지 나왔다(4db537a, 10-21 05:00). 재료 조건은 사진 · 패션 · 건축 세 가지. 같은 날 v5 THE FACE IS YOURS 도 나와 있어 두 갈래 중 하나를 정해야 한다.

## 이어 할 일: `storyline`
W2-O17(v5 / FROM THE INSIDE P1)을 사용자에게 확인한다. P1 은 표지 · 1쪽이 B안으로 정해졌으니 다음 쪽과 W2-O15(목차 교체 · 제안 쪽 · 세 재료 이미지)를 이어 간다.
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 3개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D23 P1 표지 + 1쪽은 B안(Galatasaray 방식: 사진 띠 + 검정 · 메시지 한 문장)으로. 표지 이미지는 사용자 제공. cover_b.* (InDesign IDML · JSX · zip)가 현재본
- W2-D22 P1(포트폴리오 1안) = flow_etereo.md 의 목차 · 흐름(ETÉREO 펼침면 문법, v4 뼈대 기준). 펼침면 종류와 목차는 ETÉREO 11장 원본으로 다시 짠 p1_types.md(타입 10가지)…
- W2-D21 표지의 웃는 사람은 특정 인물이 아니라 '누군가': 거꾸로 된 이름이 눈을 가리고(A), 행인만 얼굴 없이(B), 성별 · 나이를 흐리게(C). 미소는 남긴다
- W2-D20 표지 이미지 방향 재설정: '극장 · 강물 · 돌 · 신호' 비유 철회, 스토리 문장에 있는 것만 그린다(유리 위 두 시선, 초점은 얼굴, 진열은 등, 이름은 거꾸로, 빨강은 진열품 하나). 생성 도구는 미드저니로…
- 외 12개 → state.json decisions

## 작업 중인 파일
- .relay/tasks/010-the-face-is-yours-cues/image.png @e0b5276
- docs/shinsegae_vmd/p1_text.md @7af3dae
- docs/shinsegae_vmd/p1_layout/page09_layout.pdf @01c962e
- docs/shinsegae_vmd/p1_layout/cover_b_indesign.zip @4db537a
- 외 22개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 7개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
