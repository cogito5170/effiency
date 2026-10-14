# 1. 최종 결정

- 자격증: **AWS SAA 단 1개만 필수**. LFCS/RHCSA, Terraform Associate 전부 삭제. 이유: 프로젝트 자체(Docker/Terraform/Linux 운용)가 실기 증거로 더 강함. 중복 투자 금지.
- Kubernetes, EDA(Yosys/OpenROAD) workload: 메인 일정에서 완전 제거. 12주 feature freeze 통과하고 13주차 이전 전부 끝났을 때만 **stretch**로 건드림. 기본값은 "안 한다".
- 워커 메커니즘: heartbeat 스레드 합의 모델 버림. `SELECT FOR UPDATE SKIP LOCKED` + `lease_expires_at` 타임아웃 회수로 단순화. 분산 합의 난이도 피하고 핵심 개념(원자적 claim, 멱등성)에 집중.
- 교안: Claude/Codex가 구현 직전 10–20분 교안 제공, **주당 최대 2개**로 제한. 사용자 자체 교안 집필은 안 한다(브리프 명시). 대신 사용자는 매주 장애 재현/디버깅 리포트 1건을 자기 손으로 쓴다 — 이게 "AI 없이 하는 핵심 작업".
- 문서 산출물(ADR, failure matrix, runbook, incident report)은 매주 명시적 시간 배정. "구현 다 하고 남는 시간에 쓰기" 금지.
- 12주 feature freeze 확정. 13–16주는 부하테스트/SAA시험/데모/지원 전용.
- 지원 준비는 6주차부터 저강도로 시작, 14주차부터 본격 지원.

# 2. 프로젝트 MVP vs 제외·Stretch

**MVP (12주까지 반드시 완성)**
- FastAPI job CRUD, 상태 전이(queued/running/succeeded/failed/dead)
- PostgreSQL `SKIP LOCKED` 원자적 claim, idempotency key, 다중 worker
- timeout, bounded retry, exponential backoff
- `lease_expires_at` 기반 orphan job 회수 (heartbeat 스레드 없음)
- structured log + correlation ID
- 기본 metrics(throughput/error rate/latency/queue depth) + alert 1–2개
- Docker Compose 로컬 환경
- Terraform: VPC(단일 NAT), IAM 최소권한, ECS Fargate + RDS PostgreSQL
- GitHub Actions test/build/deploy + rollback(수동 1클릭 가능 수준)
- Secrets: AWS Secrets Manager/SSM, 하드코딩 금지

**제외 (16주 로드맵에 아예 안 넣음)**
- Kafka/Redis/microservice/service mesh/multi-cloud (원본에서도 비목표, 재확인)
- LFCS/RHCSA/Terraform Associate
- 사용자 자체 교안 집필

**Stretch (gate 통과시에만, 완전 분리)**
- 조건: 12주 feature freeze 성공 + 13주차 시작 시점 부하테스트/SAA 공부 여유 확인됨
- K8s: 로컬 minikube, probes/resources/rollout, 장애 3개 진단 — 단 ECS 대비 ADR 비교문서로 대체 가능(권장)
- EDA batch workload 1개 연결 — 일반 DevOps 채용엔 신호 약함, 가장 먼저 버릴 stretch

# 3. 자격증 결정

| 자격증 | 결정 | 이유 |
|---|---|---|
| AWS SAA | **필수** | 서류 필터링 통과용 최소 안전장치. 14주차 집중 공부, 15주차 응시. |
| LFCS/RHCSA | **삭제** | 실기 준비 시간 과다, 국내 DevOps 가산점 낮음. Linux 역량은 프로젝트+면접 구두질문으로 증명. |
| Terraform Associate | **삭제** | 객관식 문법 시험. 동작하는 Terraform 레포 + CI/CD가 100배 강한 증거. |
| CKA, SQLD, 기타 | **제외** (원본과 동일) | |

# 4. 주 20시간 기준 16주 일정

시간배분 표기: 학습/구현/문서/자격증/지원 (합 20h)

| 주 | 시간배분 | 학습 | 직접구현 | AI교안(≤2개) | 검증 | 주간 산출물 | 완료조건 | 단독 핵심작업 |
|---|---|---|---|---|---|---|---|---|
|1|8/9/2/0/1|Linux 파일시스템/권한/프로세스/시그널, Git 흐름, 기존 runner 코드 읽기|Graceful shutdown 데몬 스크립트(Python), zombie/orphan 재현|시그널 처리 그림+TODO 1개|코드 리뷰(AI)|공개 repo, graceful shutdown 스크립트, 실습 로그 markdown|repo 존재, 스크립트 SIGTERM 처리 확인됨|시그널 재현 코드 직접 작성 (AI 없이)|
|2|8/9/2/0/1|DNS/TCP/TLS/HTTP, 보안그룹 개념, `ss`/`curl`/`dig`/`tcpdump` 진단 체인|raw socket 서버 띄우고 진단 도구로 직접 관찰|네트워크 진단 흐름도 1개|진단 로그 캡처|네트워크 디버깅 리포트 1편|5개 명령어로 핸드셰이크 설명 가능|포트 열고 ss/tcpdump로 직접 확인|
|3|7/10/2/0/1|FastAPI validation, pytest|job CRUD API, 기본 상태 모델|FastAPI 라우팅 교안 1개|pytest green|API repo, 테스트 커버리지 기록|CRUD 엔드포인트 테스트 통과|엔드포인트 하나 AI 없이 직접 설계|
|4 (Gate)|6/11/2/0/1|Docker/Compose 네트워킹|Compose로 API+DB+worker 로컬 통합|Dockerfile 최소구성 교안 1개|docker compose up 전체 기동|Compose 레포, README 실행법|**Gate4: 로컬 전체 스택 1커맨드 기동 성공**|compose.yml 직접 디버깅|
|5|6/11/3/0/0|PostgreSQL transaction/isolation/lock|SKIP LOCKED 기반 atomic claim 구현|isolation level 비교 교안 1개|동시 claim 경쟁 테스트|claim 로직 + 테스트코드|동시 워커 2개로 중복 claim 0건 확인|경쟁조건 재현 테스트 직접 작성|
|6|5/10/3/0/2|idempotency 패턴, lease timeout 설계|idempotency key + lease_expires_at 회수 로직|lease 타임아웃 시퀀스 교안 1개|worker kill 후 회수 확인|지원 준비: 이력서 초안, 타깃기업 30곳 리스트|idempotent 재시도 중복 실행 0건|lease 회수 시나리오 직접 재현|
|7|5/10/3/0/2|retry/backoff 패턴, fault injection|bounded retry+backoff, fault injection 테스트|backoff 곡선 그림 교안 1개|장애 주입 후 복구 확인|Incident Report #1|장애 주입 시나리오 1개 end-to-end 복구 확인|장애 재현 후 원인분석 직접 작성|
|8 (Gate)|5/10/3/0/2|structured logging, correlation ID, 기본 metrics|JSON 로그+correlation ID, throughput/error/latency/queue depth 수집|로그 상관관계 교안 1개|로그로 특정 job 추적 가능 확인|metrics 수집 코드, 지원: 포트폴리오 README v1|**Gate8: MVP 핵심 로직(claim/idempotency/retry/lease/log/metrics) 전부 동작**|특정 job 실패 로그 추적 직접 수행|
|9|6/10/3/0/1|AWS IAM/VPC/보안그룹/ECS Fargate/RDS (콘솔로 1차 체험)|콘솔로 최소 구성 1회 수동 배포|VPC 구조 그림 교안 1개|수동 배포 성공 확인|AWS 아키텍처 다이어그램 1차안|수동으로 ECS+RDS 뜨고 API 응답 확인됨|보안그룹 규칙 직접 설정하고 설명|
|10|6/9/3/0/2|Terraform 모듈화, 단일 NAT 비용구조|콘솔 구성을 Terraform으로 전환|Terraform state/모듈 교안 1개|terraform plan/apply 무오류|Terraform repo, 비용 추정 문서, ADR#1(ECS vs K8s)|terraform apply로 전체 인프라 재현 가능|비용 추정 직접 계산 (NAT/RDS/Fargate)|
|11|6/9/3/0/2|GitHub Actions, Secrets Manager/SSM|CI/CD test→build→deploy, secret 주입, rollback 절차|CI/CD 파이프라인 교안 1개|파이프라인 green, rollback 1회 리허설|CI/CD workflow, rollback runbook|main 머지 시 자동배포, rollback 1회 성공|rollback 직접 1회 수행하고 기록|
|12 (Gate/Freeze)|4/9/5/0/2|-|버그 수습, 통합, Prometheus/Grafana 알림+runbook|없음(통합주)|alert 발생 후 runbook대로 대응 확인|Incident Report #2, runbook, ADR 2개 추가(총 3+)|**Gate12: feature freeze 선언, 신규 기능 추가 중단**|alert 대응 직접 수행|
|13|2/10/5/0/3|k6/locust 기초|부하테스트 전/후 수치 확보, 버그 수정만|없음|부하테스트 결과 재현 가능|load-test 리포트(전/후 수치), Incident Report #3|부하테스트 before/after 수치 확보됨|병목 1개 직접 프로파일링|
|14|10/2/4/0/4|AWS SAA 집중 공부|ADR 5개 이상 정리, 아키텍처 다이어그램 최종화|없음|모의시험 70%+|ADR 세트 완성, SAA 모의고사 기록|ADR 5개+ 완성, 지원 wave1 시작(10곳)|모의시험 직접 풀고 오답 분석|
|15|4/0/4/4/8|SAA 막판 정리|데모 영상 스크립트|없음|데모 리허설|**SAA 응시**, 3–5분 데모 영상|SAA 응시 완료(합불 무관), 데모 영상 완성|시험 직접 응시|
|16 (Gate)|0/0/2/0/18|-|포트폴리오 최종 다듬기만|없음|지원 서류 체크리스트|지원서 20곳+ 제출, 이력서/레포 최종본|**Gate16: 지원 20곳+ 제출, 면접 1개+ 확보 목표**|이력서/자소서 직접 작성|

# 5. 주 10시간 축소 규칙

- 비율 유지, 절대시간만 절반. 배정: 학습/구현 70%, 문서 20%, 지원/자격증 10%.
- 1–4주: Day4(네트워크 심화 진단)와 Day5(리포트) 통합, 교안 주당 1개로.
- 5–12주: 문서화(ADR/runbook)는 "최소 1문단 요약"으로 축소, 전체 서술 생략.
- 지연 발생 시 즉시 "7. 지연 시 삭제 순서" 1번부터 적용. 10시간 모드는 버퍼 없다고 가정하고 매주 금요일 진도 체크, 2주 이상 밀리면 다음 삭제 항목 선제 적용.
- 지원 활동(6–13주)은 축소 금지 — 저강도(주 1시간, 타깃 리스트/이력서 다듬기)라도 유지. 지원 일정 전체가 밀리면 취업 자체가 밀림.

# 6. 4/8/12/16주 Gate

- **4주 Gate**: `docker compose up` 1커맨드로 API+DB+worker 전체 기동, README만 보고 재현 가능. 실패 시: 네트워크 심화 내용 추가 축소, 5주차로 통합 작업 일부 이월.
- **8주 Gate**: MVP 핵심 신뢰성 로직(atomic claim, idempotency, retry, lease 회수, structured log, metrics) 전부 동작 + 테스트 통과. 실패 시: fault injection 시나리오 3→1, metrics는 수집만 하고 대시보드 생략.
- **12주 Gate**: feature freeze 선언. Terraform으로 AWS 전체 재현 가능 + CI/CD green + rollback 1회 성공 + alert→runbook 대응 1회 검증. 실패 시: GitHub Actions rollback 자동화 포기하고 수동 rollback 절차서만 남김, ADR 개수 5→3으로 하향.
- **16주 Gate**: SAA 응시 완료(합불 무관), 지원서 20곳 이상 제출, 데모 영상 완성, 레포 공개 상태. 실패 시: SAA는 "공부함"으로 강등하고 응시는 취업 후로 미룸 — 지원은 반드시 한다.

# 7. 지연 시 삭제 순서 (1번부터 먼저 버림)

1. Stretch: K8s, EDA workload (원래부터 기본 미포함, 재검토도 안 한다)
2. 부하테스트 시나리오 다양화 (1개만 남김)
3. Grafana 대시보드 polish (메트릭 수집/로그만 유지)
4. ADR 개수 (5개 → 3개)
5. Fault injection 시나리오 (3개 → 1개)
6. Incident Report 개수 (3건 → 2건)
7. AWS SAA 응시 (최후 수단, 공부만 하고 시험은 취업 후로)

**절대 안 자르는 항목**: job CRUD/atomic claim/idempotency/retry/lease 회수, Docker Compose, Terraform AWS 배포, GitHub Actions CI/CD, structured log, 지원 활동 자체.

# 8. 지원 일정과 포트폴리오 증거

- 6주차: 이력서 초안, 타깃기업 리스트 30곳, 포트폴리오 README 뼈대.
- 8주차: 포트폴리오 README v1 (아키텍처 다이어그램 1차).
- 10–11주차: 네트워킹(커뮤니티, 스터디, 현직자 커피챗) 시작, 저강도.
- 14주차: 지원 wave1 — 10곳 지원 (허수 지원 포함, 서류 보정용 캘리브레이션).
- 15–16주차: 본격 지원 — 누적 20곳+ 제출, 1분 자기소개/면접 모의 준비.
- 포트폴리오 증거물: 공개 repo+CI 배지, ADR 3–5개, failure matrix, runbook, incident report 2–3건, load-test 전/후 수치, 비용 추정 문서, 3–5분 데모 영상.

**AWS 비용 상한/정리 규칙**
- 월 예산 상한 $20, AWS Budget Alarm 설정 필수 (Day1에).
- 단일 NAT Gateway만 사용, RDS는 가장 작은 인스턴스(t3.micro/t4g.micro), Fargate는 최소 vCPU/메모리.
- 작업 세션 끝날 때마다(특히 9–12주) `terraform destroy` 또는 ECS 서비스 scale-to-0 습관화. 상시 기동 금지.
- 매주 금요일 AWS 콘솔 Cost Explorer 확인 후 미사용 리소스 삭제.

# 9. Day 1 체크리스트

1. GitHub repo 생성, README 뼈대, `.gitignore`, SSH key 설정
2. 로컬 개발환경: WSL2 또는 Docker 기반 Ubuntu 세팅
3. AWS 계정 생성 + Budget Alarm $20 설정 (가장 먼저, 비용 사고 방지)
4. `terraform`, `aws cli`, `docker`, `docker compose` 설치 확인
5. 기존 job runner 코드 1회 통독, "job 접수→실행" 흐름 하나만 추적해서 메모
6. 주당 20h/10h 중 본인 모드 결정, 캘린더에 학습 블록 고정
7. Day1 로그 markdown 1편 작성 (한 일, 막힌 점, 내일 계획)
8. SIGTERM/SIGINT graceful shutdown 스크립트 작성 시작 (1주차 핵심 구현)

# 10. 다음 Claude 실행 프롬프트

```
task 003 state.md 참고. 현재 N주차 시작.
이번 주 계획(학습/구현/검증/산출물)은 pack.md의 16주 표 N번째 행 기준.
구현 직전 10–20분 교안 최대 2개 생성해줘.
각 교안 구성: 질문 1개, Mermaid/ASCII 그림 1개, 핵심 문장 3–5개,
실행 가능한 10–30줄 코드, 실패 예제 1개, 사용자가 AI 없이 푸는 TODO 1개,
프로젝트 연결 설명, 회상 질문 3개.
이번 주 "AI 없이 직접 할 핵심 작업"도 표에서 확인해서 교안에 포함시키지 말고 분리 안내해줘.
끝나면 state.md 갱신 형식으로 요약해줘.
```
