# AI 쇼핑 통합 서비스 (가칭) — 자료조사

여러 쇼핑몰에 흩어진 상품을 조건과 대화로 좁히고 시각적으로 탐색하는 AI 서비스를 만들기 위한 프로젝트다.
왜 하는지, 무엇을 답해야 하는지, 무엇을 하지 않는지는 [intent.md](intent.md)에 있다.

현재 단계: **0. 자료조사** (2026-10-27 시작). 코드는 아직 없다.

## 파일 구성

```
notes/ai-shopping/
├── intent.md             목적·핵심 질문(Q1~Q4)·원칙·결정 기록
├── README.md             이 파일: 조사 계획과 진행 상황
└── research/
    ├── R1-bibliography.md     서지 검증 결과
    ├── R2-landscape.md        경쟁 지형
    ├── R3-data-legal.md       데이터 확보 경로와 법적 검토
    ├── R4-tech.md             기술 수준
    ├── R5-demand.md           수요·지불의사 조사 설계와 결과
    └── R6-decision.md         방향 결정 매트릭스
```

## 조사 계획

각 항목은 산출물 파일 하나와 완료 조건을 가진다. R1~R4는 책상 조사, R5는 사람을 만나는 조사, R6은 결정이다.

| ID | 주제 | 답하는 질문 | 방법과 이론 축 | 완료 조건 | 상태 |
|---|---|---|---|---|---|
| R1 | 서지 검증 | 전체 | 검토 문서의 논문 26편을 출판사·DOI와 대조 | 26편 모두 `확인/수정/삭제` 판정 | 1차 완료: 26편 실재, 6편 부제 보완, 8편 권·호 재확인 필요 |
| R2 | 경쟁 지형 | Q1 | 국내외 AI 쇼핑 에이전트와 버티컬 서비스의 기능 매트릭스. 플랫폼 포위(Eisenmann 외, 2011), 롱테일(Brynjolfsson 외, 2011) | 서비스 15개 이상, 각 기능 칸에 확인 출처 | 다음 |
| R3 | 데이터·법 | Q2 | 제휴 피드·공개 API 목록, 크롤링 판례와 법조문(부정경쟁방지법 데이터 조항, 저작권법 DB 보호, 국내외 크롤링 판례) | 방향별 합법 데이터 경로 1개 이상 또는 "없음" 판정 | 대기 |
| R4 | 기술 | Q4 | 합성 이미지 검색(FashionIQ, CIRR) 최신 성능, 패션 특화 비전-언어 모델, 추론 비용 | 공개 모델 기준 성능·비용 표 | 대기 |
| R5 | 수요·지불의사 | Q3 | 반구조화 인터뷰(Jobs-to-be-done), Van Westendorp 가격 민감도, 선택 기반 컨조인트 | 인터뷰 설계안 → 혁주·윤경 검토 → 실시 | 대기 |
| R6 | 방향 결정 | 전체 | R1~R5를 세 방향 × 네 질문 매트릭스로 정리, 반증 조건 적용 | 방향 하나 선택 또는 전부 기각 | 대기 |

## GPT 교차 조사

R2~R4는 GPT(Codex)에게도 같은 질문을 Claude 결과를 보여 주지 않고 맡긴 뒤 비교한다.
요청 파일은 effiency의 `.relay/tasks/` 아래에 두고, VM 워커가 멈춰 있으면 Mac에서 직접 실행한다.

```
cd ~/effiency
git pull
codex exec --search --sandbox workspace-write -c sandbox_workspace_write.network_access=true "Read .relay/tasks/<task>/prompt.md and do exactly what it asks. Write the result in Korean to .relay/tasks/<task>/out-codex.md."
git add -f .relay/tasks/<task>/out-codex.md
git commit -m "codex: <task> result"
git push
```

## 근거 표기

모든 조사 파일은 주장마다 근거 등급을 붙인다.

- `[확인]` 이번 조사에서 원문 또는 웹 페이지를 열어 확인함 (URL과 확인 날짜)
- `[서지]` 학술 문헌 인용 (DOI 대조 여부를 함께 표기)
- `[판단]` 작성자의 해석

## 관련 문서

- [AI 쇼핑 통합 서비스: 이론 기반 검토](https://claude.ai/artifact/VwqhX7QXNhYj5Z1pMGdUMo)
- [AI 서비스 아이디어 브레인스토밍](https://claude.ai/artifact/DPmcxhexN1d4t6PHmBpjHK)
