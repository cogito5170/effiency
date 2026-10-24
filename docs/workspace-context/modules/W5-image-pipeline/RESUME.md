# W5 이미지 생성 경로 (로컬 확산 · Gemini · Codex)
기준 2026-10-16T07:45Z · 체크포인트 main@bdee7d6, main@8724b6c, claude/codex-all-images@12ecdbd

## 지금
W5-D8: gentleMonster CLAUDE.md '이미지는 모두 Codex 로 만든다 (2026-10-15 사용자 결정)' — 사용자가 PR #14 를 머지(6acff99, 2026-10-15T14:39Z). 로컬 확산 · Gemini · Midjourney 프롬프트 경로를 대체. 경로: image-spec.json → claude/* 푸시 → VM relay inbox → codex exec 이미지 → 같은 브랜치 커밋.

## 이어 할 일: `image`
경로 정상(status 확인 완료). 다음 이미지는 W2.cover_image · W3.band_image · W4.portrait · W6.cover 가 spec 만 넘겨 부른다.
- 조건: 요청 모듈 쪽 사용자 결정(무엇을 그릴지)이 먼저

## 지금 유효한 결정 (최근순)
- W5-D8 이미지는 모두 Codex 로 만든다 (CLAUDE.md, '2026-10-15 사용자 결정'); 렌더링은 코드 그대로; 실패 시 대체 수단 금지. 가장 최근 확정.
- W5-D7 gentleMonster 에 codex-image 스킬 (세션은 스펙만 쓰고 VM 인박스로 요청) 머지 (PR #12)
- W5-D6 effiency relay image + VM inbox 머지 (PR #2), 이후 PR #4·#5 (Codex 재시도·여러 저장소 감시)
- W5-D5 맥 램 8GB (앞선 'Ram 16' 정정)
- W5-D4 미드저니처럼 프롬프트만 넣으면 뽑아 주는 UI
- W5-D3 이미지 시스템은 확산 모델 학습이 아니라 기존 모델 + 서브에이전트(diffusion_model atelier)
- 외 2개 → state.json decisions

## 작업 중인 파일
- .relay/tasks/001-codex-test/ @cb7027b

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W5-image-pipeline/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 5개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
