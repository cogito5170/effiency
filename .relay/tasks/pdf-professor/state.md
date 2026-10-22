# pdf-professor state

완료: loopback PDF 리더, 교수 모드 4개, 기존 ask 라우팅/맥락/노트 재사용, 검색 링크, CLI와 문서.
- relay/reader.py:1-167: PDF.js 텍스트 레이어, 40% 패널, HTTP 핸들러와 서버.
- relay/ask.py:54-78: 교수 프롬프트와 로컬 검색 링크.
- relay/ask.py:230-279: 명시적 모드/쪽/캐시된 페이지와 저장 결과 재사용.
- relay/cli.py:413-418: read 실행; relay/cli.py:594-599: 인자.
- tests/test_reader.py:1-124: 스텁 러너와 메모리 HTTP 요청 검증.
- docs/ask.md:43-56: 사용법.

검증: unittest discover 113개 통과. 생성된 JavaScript node --check 및 git diff --check 통과.
제약: 샌드박스에서 socket.bind가 PermissionError로 거부됨. HTTP 핸들러는 메모리 요청으로 검증. 실제 브라우저/CDN/PDF 렌더링은 허용된 환경에서 수동 확인 필요.
