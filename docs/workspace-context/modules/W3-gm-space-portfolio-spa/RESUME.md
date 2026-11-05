# W3 젠틀몬스터 공간 포트폴리오 SPA (원고 · 잡지 · 띠 이미지 · 03 ARCHITECTURE 설치작품)
기준 2026-10-16T07:45Z · 체크포인트 main@bdee7d6, claude/midjourney-574x172-image-sy9gq3@b3f3eda, claude/youthful-ride-kehgoo@cd6d457

## 지금
2026-10-15 CLAUDE.md(12ecdbd): 이미지는 모두 Codex. 그 직전 W3 작업 결정은 2026-10-10 10:16 띠 이미지 '방향성 프롬프트 3종, 오브제 · 물성은 나중에' (b3f3eda). 설치작품은 10-10 09:00 흉상 지시가 마지막이나 구현은 커밋되지 않음.

## 이어 할 일: `band_image`
섹션(01 STYLE · 02 PICTURE · 03 ARCHITECTURE) + 01_style_image.md:37-39 방향성 문장 + 사용자가 정할 오브제 · 물성 → W5.image 스펙(size 1536x1024 생성 후 574×172 로 크롭, 또는 notes 에 10:3 비율). 병행 결정: 03 ARCHITECTURE 원고 3안(215e2a0 / 64e5497 / 5ce2674) 중 채택
- 조건: 사용자 확인 필요 — 오브제 · 물성은 사용자가 '나중에 정한다'고 보류했으므로, 이를 받거나 '방향성만으로 생성'을 허락받아야 W5.image 호출 가능. 확인 없이 할 수 있는 것은 세 03 원고 비교표 작성(manuscript, 읽기 전용)까지.

## 사용자에게 물을 것
- W3-O1 띠 이미지의 오브제 프롬프트 · 물성 프롬프트 정의 (사용자가 '나중에 정한다'고 보류) — 정해지기 전에는 이미지 스펙을 쓸 근거가 없음
- W3-O2 03 ARCHITECTURE 원고: 카드에 없는 세 초안이 경쟁 — gracious-knuth 64e5497(21-24쪽), determined-thompson 5ce2674(25-28쪽), project-thread-j7zduo 215e2a0(10…

## 지금 유효한 결정 (최근순)
- W3-D15 모든 새 이미지는 Codex(codex-image) 경로 — 띠 이미지의 Midjourney 경로와 설치작품 실사 이미지는 이제 W5.image 로만
- W3-D14 오브제는 나중에, 사용자 방향성만 (방향성 프롬프트 3종) — 띠 이미지의 가장 최근 확정
- W3-D12 로봇팔이 만드는 것 = 한 인물의 흉상을 2D로 쌓음, 질감은 플라스틱 말고 메탈릭; 프롬프트 먼저 → '구현하여라'
- W3-D11 오브제가 너무 추상적 → 명확한 대상을 만드는 장면 (eyewear form)
- 외 10개 → state.json decisions

## 작업 중인 파일
- docs/portfolio/03_architecture.md (방향 제안) @215e2a0
- docs/portfolio/03_architecture.md (21-24 지면) @64e5497
- docs/portfolio/03_architecture.md (25-28 지면) @5ce2674
- docs/portfolio/idml/*.idml, docs/portfolio/scripts/*.{py,jsx}, v2_*.md (InDesign 지면 반영) @e1c49e7 · f5bd432 · 33f558b · ba10ae6 · 396cd8c
- 외 7개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W3-gm-space-portfolio-spa/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 9개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
