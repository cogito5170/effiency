구현 완료했습니다.

- 변경: `relay/config.py:44` — implement 러너를 `codex exec --sandbox workspace-write {prompt}`로 수정
- 테스트: `tests/test_pipeline.py:114-118` — 기본 러너 배열 검증 추가
- 문서: `docs/pipeline.md:41`, `docs/HANDOFF.md:80` — 이전 플래그 교체
- 릴레이 기록: `.relay/tasks/001-…/state.md:1`, `out-codex.md:1`
- 검사: `python3 -m unittest discover -s tests` — 49개 통과
- 검사: 코드·문서에서 `--full-auto` 미검출
- 열린 이슈: 없음
