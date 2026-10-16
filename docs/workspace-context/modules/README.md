# 작업 공간 모듈 W1~W6

W0~W6 묶음(구성은 유지)을 블랙박스 모듈로 바꾼 것이다. 공통 규칙은 [CONTRACT.md](CONTRACT.md).
상태 기준 2026-10-16 06:30Z (W1 · W2 증분 동기화, W3~W6 은 체크포인트 뒤 커밋 없음 확인).
새 의뢰인 세션은 모듈의 `RESUME.md`(2000자 이하) 하나만 읽고 시작한다. 동기화 · 세션 교대 규칙은 [CONTRACT.md](CONTRACT.md#백엔드-동기화--세션-교대).

| 모듈 | 내놓는 op | 부르는 것 | 마지막 확정 | 이어 할 곳 | 사용자 확인 |
|---|---|---|---|---|---|
| [W1 혁주 자기소개서](W1-hyeokju-cover-letter/README.md) | `analyze_posting`, `diagnose`, `draft_paragraph`, `finalize` | — | Q1 구성 R2 + 왜 해외 브랜드 VMD + 역량 답변 (사용자, 10-16 06:09) · 현재본 qa-fix 998자 | `finalize` | 필요 |
| [W2 패션 · VMD 지원 포트폴리오](W2-fashion-vmd-portfolio/README.md) | `storyline`, `scene_blueprint`, `cover_image`, `job_scan`, `submission_jpeg` | W5.image | v4 FROM THE INSIDE 이야기 단락 A 확정(10-16 05:49) · 제작자 진열 청사진(67dfff0) | `cover_image` | 필요 |
| [W3 젠틀몬스터 공간 포트폴리오 SPA](W3-gm-space-portfolio-spa/README.md) | `manuscript`, `magazine_layout`, `band_image`, `install_scene` | W5.image | 2026-10-15 CLAUDE.md(12ecdbd): 이미지는 모두 Codex | `band_image` | 필요 |
| [W4 혁주 CV · 인물 사진](W4-hyeokju-cv-portrait/README.md) | `cv_layout`, `portrait`, `fill_blanks` | W5.image | 2026-10-10 10:10 '그레이로 채택, 01과 02 상하 교체' (6a1d95c, CV_PAGE2_B_SIDENOTE_GRAY.ai) | `cv_layout` | 필요 |
| [W5 이미지 경로 (Codex)](W5-image-pipeline/README.md) | `image`, `status` | — | W5-D8: gentleMonster CLAUDE.md '이미지는 모두 Codex 로 만든다 (2026-10-15 사용자 결정)' — 사용자가 PR #14 를 머지(6acff99, 2026-10-1 | `image` | 불필요 |
| [W6 도구 · 인프라](W6-tools-infra/README.md) | `relay_run`, `relay_ask`, `relay_request`, `archive_recall`, `memory_context`, `frontend_render`, `cover` | W5.image | 2026-10-15 사용자가 gentleMonster PR #9(기억·맥락 0eeccc8) · #10(정정 슬롯 386f7ae) · #11(relay 보관소 hook b688f77) 과 effien | `relay_ask` | 필요 |
