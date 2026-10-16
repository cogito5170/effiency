# 작업 공간 모듈 W1~W6

W0~W6 묶음(구성은 유지)을 블랙박스 모듈로 바꾼 것이다. 공통 규칙은 [CONTRACT.md](CONTRACT.md).
상태 기준 2026-10-16. 10-15 스냅숏 뒤로 세션 활동과 브랜치 이동이 없음을 확인했고, 확정 사항은 저장소 파일에서 다시 찾았다.

| 모듈 | 내놓는 op | 부르는 것 | 마지막 확정 | 이어 할 곳 | 사용자 확인 |
|---|---|---|---|---|---|
| [W1 혁주 자기소개서](W1-hyeokju-cover-letter/README.md) | `analyze_posting`, `diagnose`, `draft_paragraph`, `finalize` | — | Q1 자기소개 첫 단락 = R2 (사용자 채택, 10-15 12:16) | `finalize` | 필요 |
| [W2 패션 · VMD 지원 포트폴리오](W2-fashion-vmd-portfolio/README.md) | `storyline`, `scene_blueprint`, `cover_image`, `job_scan`, `submission_jpeg` | W5.image | ON DISPLAY 스토리 v3(사용자 관찰 '주체는 가만히, 내가 움직인다') 원고와 한 장면 청사진 THE STILL RUNWAY(Codex 컨셉 이미지 + three.js 장노출 렌더, A3) | `storyline` | 필요 |
| [W3 젠틀몬스터 공간 포트폴리오 SPA](W3-gm-space-portfolio-spa/README.md) | `manuscript`, `magazine_layout`, `band_image`, `install_scene` | W5.image | 2026-10-15 CLAUDE.md(12ecdbd): 이미지는 모두 Codex | `band_image` | 필요 |
| [W4 혁주 CV · 인물 사진](W4-hyeokju-cv-portrait/README.md) | `cv_layout`, `portrait`, `fill_blanks` | W5.image | 2026-10-10 10:10 '그레이로 채택, 01과 02 상하 교체' (6a1d95c, CV_PAGE2_B_SIDENOTE_GRAY.ai) | `cv_layout` | 필요 |
| [W5 이미지 경로 (Codex)](W5-image-pipeline/README.md) | `image`, `status` | — | W5-D8: gentleMonster CLAUDE.md '이미지는 모두 Codex 로 만든다 (2026-10-15 사용자 결정)' — 사용자가 PR #14 를 머지(6acff99, 2026-10-1 | `image` | 불필요 |
| [W6 도구 · 인프라](W6-tools-infra/README.md) | `relay_run`, `relay_ask`, `relay_request`, `archive_recall`, `memory_context`, `frontend_render`, `cover` | W5.image | 2026-10-15 사용자가 gentleMonster PR #9(기억·맥락 0eeccc8) · #10(정정 슬롯 386f7ae) · #11(relay 보관소 hook b688f77) 과 effien | `relay_ask` | 필요 |
