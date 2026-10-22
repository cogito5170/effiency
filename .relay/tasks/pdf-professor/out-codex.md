구현 완료했습니다.

- `relay/reader.py:1-167`: PDF 리더, 선택 버튼, 해설 패널, 로컬 서버.
- `relay/ask.py:54-78`, `relay/ask.py:230-279`: 교수 모드, 검색 링크, 기존 라우팅·저장 재사용.
- `relay/cli.py:413-418`, `relay/cli.py:594-599`: `relay read` 명령.
- `tests/test_reader.py:1-124`: HTTP 핸들러·저장·프롬프트·경로 제한 테스트.
- `docs/ask.md:43-56`: 사용법 추가.
- `.relay/tasks/pdf-professor/`에 상태와 결과 기록.

검증: 전체 113개 테스트, JavaScript 구문 검사, `git diff --check` 통과.

남은 확인: 샌드박스가 포트 바인딩을 거부했습니다. HTTP 핸들러는 메모리 요청으로 검증했으며, 실제 브라우저의 PDF 렌더링·드래그 동작은 수동 확인이 필요합니다.
