# 1. 종합 판단

과욕 계획. 범위 좋음(핵심 기능 선정 타당), 양 많음. 16주 × 초보자 Linux/네트워크/클라우드 제로 베이스 조건 무시한 분량. 자격증 2개+프로젝트 전체 스택 동시 진행은 전일제 학습자도 빡빡. 현재 안은 "완료"보다 "번아웃" 리스크 높음. 구조(순서, ADR, failure matrix, runbook)는 채용 담당자 설득력 있게 잘 짜였으나, 분량 20–30% 쳐내야 생존 가능.

# 2. 16주 과부하 위험

- 1–2주에 Linux process/signal/permission/log + DNS/TCP/TLS/HTTP + Git + 기존 runner 분석까지 몰림. 초보자에겐 이것만으로 3–4주 분량.
- 5–8주(PostgreSQL 트랜잭션/isolation/lock + idempotency + retry/backoff/lease/heartbeat + fault injection)는 분산시스템 핵심 난제 집합. 경험자도 각 항목에 1–2주 쓰는 영역을 2주에 합침.
- 9–10주 AWS IAM/VPC/compute/storage/database + Terraform + cost/ADR까지 2주. AWS 자체도 입문자에겐 4주 과정 분량.
- 매주 마이크로 교안 2–4개 + 60–90분 AI-없이 구현/장애해결 챌린지는 "구현 주차"에 추가 부담. 메인 학습과 별도 시간 요구 — 하루 학습시간 제한 조건과 충돌.
- 13–14주 Kubernetes는 "후반 선택"이라 했으나 순서표에 고정 배치돼 사실상 필수처럼 보임. ADR 작성까지 포함되어 가볍지 않음.
- 16주 1주에 SAA 응시 + 문서 + 데모 + 이력서 + 지원을 몰아넣음. 시험 준비(공식적으로 보통 수주)와 취업 서류 작업을 같은 주에 배치 — 비현실적.
- ADR 5개 이상 + failure matrix + runbook + incident report + load-test 전후 수치 + 비용 추정 + 데모, 전부 작성 산출물. 구현 분량과 별개로 "쓰는 시간"이 상당하나 일정에 명시적 배정 없음.

# 3. 유지 / 연기 / 삭제

**유지 (반드시)**
- job CRUD, 상태 전이, atomic claim, idempotency key, 다중 worker
- timeout/bounded retry/backoff (분산 신뢰성 핵심 — 이 프로젝트 차별점)
- lease/heartbeat + orphan 회수 (실무형 디테일, 강한 신호)
- structured log + correlation ID
- 기본 metrics(throughput/error rate/latency/queue depth) + alert 1–2개
- Docker Compose
- Terraform 기반 AWS 배포(최소 구성), IAM 최소권한
- GitHub Actions test/build/deploy

**연기 (16주 밖, 선택으로 완전 분리)**
- Kubernetes 전체 블록 (13–14주) — "선택"이라면서 메인 순서표에 넣는 것 자체가 모순. 완전히 분리된 stretch goal로 두고 11주차 평가 후 여유 있을 때만.
- Yosys/OpenROAD EDA workload (15주) — 장기 목표(EDA infrastructure)와 연결되나 16주 핵심 평가에는 불필요. 연기.
- cost 추정 상세화, rollback 고도화 등은 MVP 수준으로 축소.

**삭제**
- Terraform Associate 자격증 응시 자체 (아래 4번 참고, 실기 Terraform 구현으로 대체 충분)
- "매주 60–90분 AI 없이 구현/장애 해결" 별도 세션 — 좋은 의도지만 이미 빡빡한 일정에 추가 레이어. 핵심 주차(5–8, 9–10) 작업에 통합시키고 독립 일정으로 안 뺀다.
- RHCSA/LFCS 동시 비교 검토 자체 시간 — 이미 "동시취득 제외"로 잘 정리됨, 유지.

# 4. AWS SAA + LFCS/RHCSA + Terraform Associate 평가

- SAA 단독: 타당. 클라우드 아키텍처 개념 잡기 좋고 국내 채용에서 인지도 높음.
- LFCS/RHCSA 추가: 신중히. 실기형 자격증이라 "증명"으로는 의미 있으나, 프로젝트 자체(Linux/Docker/Terraform 다룸)가 이미 Linux 실무력을 더 직접적으로 보여줌. 자격증은 보조 신호일 뿐, 채용 담당자는 실제 레포·데모를 더 본다. 시간당비(공식 비용+준비시간)를 "필수 2"로 못박기보다 "프로젝트 끝나고 여유 있으면" 수준으로 다운그레이드 추천.
- Terraform Associate(선택): 삭제 권장. 이 프로젝트가 Terraform으로 AWS 배포하는 것 자체가 Terraform 실기 증거다. 자격증 추가는 중복 증명 — ROI 낮음. 12주차까지 프로젝트 완료라는 조건 자체가 이미 빡빡한 일정에서 달성 어려움.
- 결론: SAA 하나만 "필수", LFCS/RHCSA는 "시간 남으면", Terraform Associate는 "스킵, 프로젝트가 대체".

# 5. 누락된 기초

- 쉘 스크립팅/기본 bash 유틸 사용 능력 (find/grep/awk/sed, 프로세스 관리) — Linux 섹션에 암묵적으로만 포함, 명시 안 됨.
- 네트워크 기초 중 "포트/방화벽/보안그룹" 다루는 실습 없음 — AWS VPC/보안그룹과 연결되는 핵심인데 1–2주 "DNS/TCP/TLS/HTTP"에 security group 실습 빠짐.
- Git 기초는 명시됐으나 브랜치 전략/PR 리뷰 흐름(실무 협업 신호) 없음 — 채용 시 협업 증거로 약함.
- 로깅/모니터링 스택에서 "디스크/메모리 리소스 제약 하 운영" 경험 없음 (자원 제한 환경에서 디버깅) — 실무에서 자주 겪는 문제, 포함 고려.
- 비용 최적화/정리(AWS 리소스 삭제, 과금 방지) 습관 — "cost 추정"만 있고 실제 운영 중단/정리 루틴 없음. 실무에서 중요, 누락.
- 보안 기초(secret 관리는 있으나 의존성 스캔, 기본 OWASP 체크 등)는 전혀 없음. Platform/DevOps 채용에서 종종 물어보는 영역.

# 6. 현실적인 1주차 범위

16주 전체가 과부하이므로 1주차는 더 작게 잘라야 함. 1–2주 통째로 밀던 것 중 1주차만 분리:

- Linux 기초: 파일시스템/권한/프로세스/시그널 핵심만 (디렉터리 구조, chmod/chown, ps/kill, 백그라운드 job) — 실습 중심, 이론 최소
- Git: clone/branch/commit/PR 흐름 1회 실습
- 기존 runner 코드 읽기: 전체 이해 아니라 "job이 어떻게 접수되고 실행되는지" 흐름 하나만 추적
- 마이크로 교안 1–2개만 (2–4개는 과함, 첫 주는 적응 기간)
- DNS/TCP/TLS/HTTP는 2주차로 통째로 이동

1주차 목표: "Linux 터미널에서 불편함 없이 움직이고, 기존 코드 구조 파악" 정도. 산출물 기대 낮게.

# 7. 우선 수정 5개

1. Kubernetes/EDA 블록을 순서표에서 완전히 빼고 "16주 밖 stretch"로 재배치 — 메인 일정은 11–12주에 끝나는 구조로 재설계.
2. Terraform Associate 자격증 삭제, LFCS/RHCSA는 "필수"에서 "선택/여유시"로 강등. 자격증 15% 시간 배분을 10% 이하로.
3. 1–2주 Linux+네트워크+Git+코드분석 블록을 1–3주로 늘려 분산 (초보자 기초는 압축하면 안 됨).
4. 매주 "AI 없이 60–90분 챌린지"를 독립 일정에서 빼고 핵심 구현 주차(5–8주, 9–10주) 작업 내부 체크포인트로 흡수.
5. ADR/failure matrix/runbook/비용추정/데모 등 문서 산출물 작성 시간을 순서표에 명시적으로 배정 (현재는 "구현 순서"에만 시간 할당, 글쓰기 시간 누락 — 이게 실제 지연의 흔한 원인).
