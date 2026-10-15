# pdf-professor — PDF 옆에서 해설해 주는 "교수" 리더

## Goal
`relay read <pdf>` 하나로 브라우저에 PDF 리더가 열리고, 문장·수식을 드래그하면 **오른쪽 패널**에 교수처럼 해설이 붙는다.
Claude 토큰을 아끼기 위해 기본 해설은 agy → codex, 깊은 질문만 Claude 1턴 (기존 `relay/ask.py` 라우팅 재사용).

## 화면
- 왼쪽: PDF.js 로 렌더링한 페이지 + 텍스트 레이어(드래그 가능). 오른쪽: 해설 패널(넓이 조절 불필요, 고정 40%).
- 드래그하면 선택 영역 옆에 작은 버튼 4개: **해설** · **관련 연구** · **더 알아보기** · **깊게**. 자유 질문 입력칸 1개.
- 패널에는 질문 카드가 시간순으로 쌓인다 (선택 인용 + 답 + 답한 러너 표시 + 쪽 번호). 카드 클릭 시 해당 쪽으로 스크롤.
- 답 렌더링: marked + KaTeX(수식) + mermaid(그림). 기존 `ask.render_html` 의 수식 보호 로직 재사용.
- 응답 대기 중 스피너. 실패 시 어떤 러너가 왜 실패했는지 카드에 표시.

## 교수 모드 답변 형식 (`relay/ask.py` 에 mode 인자로 추가)
- 해설: 한 줄 요약 → 직관/비유 → 정확한 의미 → (필요시) 수식과 기호 표 → (필요시) mermaid 그림 1개 → 확인 질문 1개
- 관련 연구: 이 개념이 나온 맥락, 대표 연구 흐름 2~4개를 **"분야/방법/핵심 아이디어"** 로 설명. 논문 제목·저자·연도는 **확실할 때만** 쓰고 아니면 "확인 필요"로 표시.
  DOI·링크를 지어내지 않는다. 대신 각 항목에 **검색어**를 주고, 서버가 Google Scholar · Semantic Scholar 검색 링크를 로컬에서 만들어 붙인다 (토큰 0).
- 더 알아보기: 선수 지식 1~3개, 다음에 공부할 것 1~3개, 흔한 오해 1개.
- 깊게: 기존 deep 경로 (Claude 1턴, 도구 없음). 유도·증명은 단계별로.

## 구현 범위
- 새 모듈 `relay/reader.py`: 표준 라이브러리 `http.server` 로 127.0.0.1 의 빈 포트에서 서빙. 엔드포인트:
  `GET /` 뷰어 HTML, `GET /pdf` PDF 바이트, `POST /ask` {selection, page, question, mode} → {markdown, runner, failures, links}.
  외부 의존성 추가 금지 (PDF.js·marked·KaTeX·mermaid 는 버전 고정 CDN: pdfjs-dist@3.11.174 등).
- `/ask` 는 `relay/ask.py` 의 맥락 추출(쪽 번호는 뷰어가 알려 주므로 그 쪽 텍스트 사용)·러너 폴백·`notes/papers/<문서>/qa.md` 저장을 그대로 쓴다.
- CLI: `relay read <pdf> [--port N] [--no-open]`. 실행하면 브라우저를 연다. Ctrl+C 로 종료.
- 원격 PDF(URL)도 `ask.resolve_source` 로 받아 연다.

## Done when
- `relay read 샘플.pdf` → 페이지 표시, 드래그 → 버튼 → 패널에 답 카드 (러너 표시) 가 뜬다.
- 4개 모드 각각 프롬프트가 위 형식을 요구하고, 관련 연구 카드에는 검색 링크가 붙는다.
- `python3 -m unittest discover -s tests` 통과. 새 테스트: 서버 `/ask` 를 스텁 러너로 호출해 JSON 응답·qa.md 저장 확인, 모드별 프롬프트 문구 확인, 검색 링크 생성 확인, `/pdf` 가 파일 밖 경로를 서빙하지 않음.
- `docs/ask.md` 에 `relay read` 사용법 추가.

## Out of scope
- 로그인·다중 사용자·원격 접속 (127.0.0.1 전용). 하이라이트 영구 저장. PDF 편집.
- 새 AI 러너 추가, 권한 설정 변경.
