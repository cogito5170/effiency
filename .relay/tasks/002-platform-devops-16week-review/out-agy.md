## 1. 종합 판단

현재 제시된 16주 로드맵은 **"방향성은 우수하나, 비전공·실무 무경험 초심자의 가용 시간 대비 과도하게 많은 기술 스택과 메타 태스크가 포함되어 있어 실행 불가능에 가까운 과부하(Over-scoped) 상태"**입니다.

- **[근거 (Evidence)]**:
  - 후보자는 전자공학 학사로 Python/C++ 사용 경험은 있으나 Linux, 네트워크, 클라우드 실무 경험이 전무합니다.
  - 가용 기간은 16주이며, 하루 학습 시간이 제한적입니다.
  - 16주 동안 소화하려는 스택: Linux 커널/네트워크 기초, FastAPI, PostgreSQL 심화(트랜잭션 격리/락/원자성), 분산 워커 메커니즘(heartbeat/lease/orphan 회수), Docker, AWS(VPC/IAM/컴퓨팅/스토리지/RDS), Terraform, GitHub Actions, 관측성(Prometheus/Grafana/Alertmanager), Kubernetes, EDA 툴(Yosys/OpenROAD), 자격증 2~3개(AWS SAA, LFCS/RHCSA, Terraform), 주당 2~4개 마이크로 교안 자체 제작.
- **[추론 (Inference)]**:
  - 프로젝트 60%, 기초 25%, 자격증 15%의 시간 배분에서 15%(약 2.4주치 시간)로 객관식(SAA)과 실기형 터미널 시험(LFCS/RHCSA)을 모두 준비하는 것은 물리적으로 불가능합니다.
  - 백엔드 분산 큐/워커의 복잡한 엣지 케이스를 바닥부터 구현하는 데 너무 많은 시간(5~8주차)이 소모되어, 정작 DevOps/플랫폼 엔지니어링의 본질인 인프라 프로비저닝, 배포 파이프라인, 클라우드 네트워킹, 시스템 트러블슈팅 역량을 깊이 있게 다질 시간이 부족해집니다.
- **[트레이드오프 (Trade-off)]**:
  - 넓은 기술 나열(K8s, EDA, 자격증 3종)을 유지하면 "튜토리얼 따라하기식 얕은 복붙"으로 끝나 기술 면접에서 검증을 통과하기 어렵습니다.
  - 스택을 좁히고 핵심(FastAPI + PostgreSQL + Docker + AWS ECS/RDS + Terraform + CI/CD + 로깅/메트릭)에 집중하면 스택의 화려함은 줄어들지만, 실제 장애 대응 경험과 깊이 있는 시스템 이해도를 증명할 수 있습니다.

---

## 2. 16주 과부하 위험

1. **자격증 병행으로 인한 인지 과부하 (Cognitive Overload)**
   - [근거]: 필수 1(AWS SAA)과 필수 2(LFCS/RHCSA 실기)가 포함되어 있습니다.
   - [추론]: LFCS/RHCSA는 2~3시간 동안 CLI 환경에서 스토리지(LVM), systemd, SELinux, 네트워크 설정을 직접 수행해야 하는 실기 시험입니다. 리눅스 실무 경험이 없는 상태에서 이를 준비하려면 매일 2시간 이상의 터미널 실습이 필요한데, 이는 프로젝트 진행을 완전히 멈추게 만듭니다.
2. **5~8주차 분산 워커/동시성/장애복구의 지나친 구현 난이도**
   - [근거]: PostgreSQL 트랜잭션 기반 atomic claim, idempotency key, bounded retry, lease/heartbeat, worker crash 후 orphan job 회수, fault injection을 직접 구현하도록 설계되어 있습니다.
   - [추론]: 이는 Celery나 Kafka 같은 검증된 도구를 쓰지 않고 RDBMS 상에서 분산 작업 큐를 자체 제작하는 고난도 백엔드 과제입니다. 커넥션 풀 고갈, 고스트 워커, 데드락 등 미묘한 버그 디버깅에 갇혀 9주차 이후의 인프라 일정이 대규모로 지연될 위험이 큽니다.
3. **9~14주차 인프라·클라우드·IaC·K8s의 급격한 스택 점프**
   - [근거]: 9-10주 AWS/Terraform → 11-12주 CI/CD/Prometheus/Grafana → 13-14주 Kubernetes.
   - [추론]: 클라우드 무경험자가 2주 만에 AWS VPC, 서브넷, IAM, RDS를 Terraform으로 모듈화하고 배포하는 것만으로도 한계에 도달합니다. 그 직후 관측성 스택과 K8s까지 얹는 것은 피상적인 YAML 복사로 귀결됩니다.
4. **마이크로 교안 작성의 메타 오버헤드**
   - [근거]: 매주 구현 전 10~20분짜리 교안을 2~4개 직접 작성(질문, 다이어그램, 코드, TODO, 회상 질문 포함).
   - [추론]: 학습자가 본인의 학습보다 "교육 자료 제작"이라는 메타 업무에 더 많은 인지 에너지를 소모하게 됩니다.
5. **완충 기간(Buffer)의 완전한 부재**
   - [근거]: 15주 EDA 워크로드 연결, 16주 SAA 시험 및 이력서/지원.
   - [추론]: 앞선 단계에서 단 1주일만 지연되어도 16주차에 프로젝트 미완성, 자격증 미취득, 서류 미작성 상태로 마감됩니다.

---

## 3. 유지 / 연기 / 삭제

### 반드시 유지 (Must Keep)
- **Reliable Job Platform의 핵심 로직**:
  - FastAPI + PostgreSQL (`FOR UPDATE SKIP LOCKED` 기반 원자적 작업 할당) + 단일/다중 Python 워커.
  - [이유]: 단순 CRUD API가 아니라 프로세스 라이프사이클, DB 동시성 제어, 멱등성(Idempotency)을 다뤄본 경험은 플랫폼 엔지니어로서 강력한 기본기를 보여줍니다.
- **Docker & Docker Compose 로컬 재현 환경**:
  - [이유]: 애플리케이션, DB, 로컬 워커를 컨테이너화하여 원클릭으로 띄우는 환경 구성은 주니어의 필수 소양입니다.
- **AWS 단일 컴퓨팅 환경 배포 (Terraform)**:
  - VPC(Public/Private 서브넷 격리), IAM 최소 권한, ECS Fargate(또는 EC2), RDS PostgreSQL.
  - [이유]: 콘솔 클릭이 아닌 IaC 기반의 안전한 네트워크 및 리소스 프로비저닝은 클라우드 주니어의 핵심 증거입니다.
- **GitHub Actions CI/CD**:
  - Test, Docker Build & Push, Terraform 연동 자동 배포.
- **관측성 및 트러블슈팅 산출물**:
  - JSON 구조화 로그, Correlation ID, 기본 메트릭(작업 처리량, 에러율, 대기열 깊이), **Incident Report 2~3건**.

### 연기 (Defer - 서류 지원 후 또는 취업 후)
- **Kubernetes (13–14주차)**:
  - [트레이드오프]: K8s는 채용 공고에 자주 등장하지만, 2주 만에 로컬 minikube를 만지는 것은 얕은 지식만 남깁니다. ECS Fargate 인프라를 견고하게 완성한 뒤, "왜 우리 워크로드에 ECS를 선택했고 K8s와 어떤 차이가 있는가"를 비교 분석한 **아키텍처 결정 기록(ADR)**으로 대체하는 것이 훨씬 효율적입니다.
- **Terraform Associate 자격증**:
  - [이유]: 깃허브에 실제로 동작하는 Terraform 코드와 GitHub Actions 자동 배포 파이프라인이 있으면 자격증 유무는 채용에 아무런 영향을 주지 않습니다.
- **복잡한 분산 Heartbeat/Lease 합의 스레드**:
  - [이유]: 워커 내 백그라운드 하트비트 스레드 대신, DB 레코드의 `lease_expires_at` 타임스탬프와 단순 타임아웃 회수 로직으로 1차 버전을 단순화합니다.

### 삭제 (Cut - 16주 로드맵에서 제외)
- **LFCS 또는 RHCSA 자격증 취득**:
  - [이유]: 실기 자격증 준비에 들어가는 막대한 시간을 프로젝트 완성도와 트러블슈팅에 투자해야 합니다. 리눅스 역량은 프로젝트 내 Dockerfile 최적화, 프로세스 시그널 처리, Linux CLI 디버깅 기록으로 충분히 증명됩니다.
- **Yosys/OpenROAD EDA batch workload (15주차)**:
  - [이유]: EDA 툴은 특정 반도체 팹리스/인프라 팀을 제외한 대다수 국내 일반 플랫폼/DevOps 채용 담당자에게 생소합니다. 컴파일 및 툴 설치 오류에 시간을 낭비하는 대신, CPU 집약적 연산이나 이미지/데이터 배치 등 범용적 워크로드로 대체하는 것이 취업 범용성에 훨씬 유리합니다.
- **자체 마이크로 교안 집필 시스템**:
  - [이유]: 본인이 학습할 교안을 본인이 집필하는 모순을 없애고, 실패 기록과 기술 블로그 형태의 트러블슈팅 노트로 단순화합니다.

---

## 4. AWS SAA + LFCS/RHCSA + optional Terraform Associate 평가

| 자격증 | 추천 여부 | 시간 대비 가치 | 채용 시장 증거력 | 평가 및 전략 |
|---|---|---|---|---|
| **AWS SAA** | **유지 (필수 1개로 단일화)** | 높음 (2~3주 집중 투자) | 중간 (서류 필터링 통과용) | 비전공/신입 지원자에게 "클라우드 전반(VPC, IAM, 컴퓨팅, 스토리지)의 기본 개념을 갖추었다"는 서류 전형 통과용 최소 안전장치 역할을 합니다. 프로젝트 AWS 배포 후 14~15주차에 집중 학습하여 취득하는 것을 권장합니다. |
| **LFCS / RHCSA** | **삭제 (비추천)** | 매우 낮음 (실기 준비에 과다한 시간 소모) | 낮음~중간 (국내 DevOps 기준) | 국내 스타트업/빅테크 DevOps 채용에서 실기 리눅스 자격증의 가산점은 크지 않습니다(공공/금융/SI의 RHEL 환경 제외). 리눅스 역량은 기술 면접 구두 질문(프로세스, 소켓, 파일시스템)과 프로젝트 코드로 검증됩니다. |
| **Terraform Associate** | **삭제 (선택에서도 제외)** | 낮음 | 매우 낮음 | 문법 객관식 시험에 불과합니다. 잘 모듈화된 Terraform 저장소와 `terraform plan/apply`가 연동된 CI/CD PR(Pull Request)이 자격증보다 100배 더 강력한 증거입니다. |

**결론**: 자격증은 **AWS SAA 단 1개**만 남기고, 나머지 시간은 인프라 코드 품질과 장애 시나리오 해결 기록에 집중해야 합니다.

---

## 5. 누락된 기초

현재 로드맵은 응용 프레임워크(FastAPI)와 인프라 키워드에 집중되어 있어, 주니어 면접에서 당락을 결정짓는 **운영 기본기와 시스템 밑바닥 기초**가 누락되어 있습니다.

1. **Linux OS 및 프로세스 라이프사이클 심화**:
   - 파일 디스크립터(File Descriptor)와 표준 입출력/파이프 리다이렉션.
   - `SIGTERM`, `SIGINT`, `SIGKILL` 시그널 전파 방식과 애플리케이션의 **Graceful Shutdown** 구현.
   - Zombie 프로세스와 Orphan 프로세스의 실제 발생 원인 및 커널의 회수(reaping) 메커니즘.
   - `/proc` 파일시스템(CPU, 메모리, FD 모니터링) 활용법.
2. **실전 네트워크 디버깅 역량**:
   - 도메인 질의 흐름(`resolv.conf`, Local DNS 캐시, CNAME/A 레코드).
   - TCP 3-way Handshake 및 소켓 상태(`ESTABLISHED`, `TIME_WAIT`, `CLOSE_WAIT`)의 이해.
   - "서버 간 통신이 안 될 때" 순차적 진단 절차: `ping` → `dig`/`nslookup` → `traceroute` → `nc`/`curl` → `ss -tulpn` / `netstat` → `tcpdump`.
   - AWS 보안 그룹(Stateful)과 서브넷 NACL(Stateless)의 패킷 흐름 차이.
3. **비밀값 관리(Secret Management) 및 보안 기본기**:
   - DB 패스워드와 API 키를 Git에 올리지 않고 안전하게 주입하는 패턴(AWS Secrets Manager, SSM Parameter Store, 환경변수 주입).
   - 하드코딩된 자격증명 대신 IAM Role 및 Instance Profile을 통한 최소 권한(Least Privilege) 부여 원칙.
4. **Git 협업 및 릴리스 워크플로우**:
   - 단순히 코드를 올리는 것을 넘어 Feature Branch 전략, PR 리뷰 템플릿, Conflict 해결, Semantic Versioning(태깅).
5. **FinOps (클라우드 비용 감각)**:
   - NAT Gateway 요금(시간당 + 트래픽당), RDS 인스턴스 비용 등 AWS 프리티어 한도 초과 방지 및 비용 최적화 감각(단일 NAT GW 구성, 불필요 리소스 자동 정리).

---

## 6. 현실적인 1주차 범위

기존 계획의 1–2주차("Linux process/signal/permission/log, DNS/TCP/TLS/HTTP, Git, 기존 runner 분석")는 너무 광범위하여 이론서만 읽다가 시간이 지나갈 위험이 큽니다. 1주차는 **"로컬 Linux 환경 구축 + 프로세스 시그널 제어 데몬 구현 + 네트워크 진단 도구 체화"**로 범위를 좁히고 명확한 산출물을 남겨야 합니다.

### 1주차 Day-by-Day 실행 계획
- **Day 1: 환경 구축 및 Git 표준화**
  - 로컬 Ubuntu 환경(WSL2 또는 Docker 기반 Ubuntu) 세팅.
  - Git 환경 설정(SSH Key, 커밋 서명, `.gitignore`), 저장소 생성.
- **Day 2: 프로세스 & 시그널 제어 실습 (Python/C++)**
  - `SIGTERM`과 `SIGINT`를 가로채서(trap) 진행 중인 작업을 5초간 마무리하고 안전하게 종료되는 Graceful Shutdown 스크립트 작성.
  - 백그라운드 실행(`nohup`, `&`), 프로세스 상태 조회(`ps aux`, `pstree`, `top`), 강제 종료(`kill -9` vs `kill -15`) 차이 관찰.
- **Day 3: Zombie & Orphan 프로세스 재현**
  - 부모 프로세스가 `wait()`하지 않고 종료되거나 방치될 때 발생하는 좀비/고아 프로세스 재현 코드(20줄 내외) 작성.
  - `ps` 및 `/proc/<pid>/status`에서 상태 플래그(`Z` 상태) 확인 및 init/systemd의 회수 과정 로그 확인.
- **Day 4: 네트워크 디버깅 도구 체화**
  - Python 표준 `http.server` 또는 raw socket으로 8080 포트를 열고, 다른 터미널에서 `ss -tulpn`, `lsof -i :8080`으로 바인딩 확인.
  - `curl -v`, `dig +trace`, `tcpdump -i lo port 8080`을 실행하여 HTTP 헤더와 패킷 핸드셰이크 흐름 직접 캡처.
- **Day 5: 1주차 종합 산출물 정리**
  - 작성한 코드와 실행 로그를 GitHub 저장소에 커밋/푸시.
  - "프로세스 시그널 처리 및 소켓 디버깅 실습 리포트" 1편 작성.

### 1주차 완료 시 남아야 하는 구체적 증거물
1. GitHub 공개 저장소 (표준 브랜치 구조 및 README).
2. Graceful shutdown을 처리하는 검증된 Python/C++ 데몬 스크립트.
3. Linux 터미널 디버깅 명령어(`ps`, `kill`, `ss`, `curl`, `dig`) 실행 로그와 원리를 설명한 Markdown 리포트 1편.

---

## 7. 우선 수정 5개

1. **기술 스택의 과감한 가지치기 (Scope Pruning)**
   - **조치**: LFCS/RHCSA, Terraform Associate, Kubernetes manifests, Yosys/OpenROAD EDA 연동을 16주 로드맵에서 공식 제외한다.
   - **이유**: 초심자에게 16주는 FastAPI + PostgreSQL + Docker + AWS + Terraform + CI/CD 1세트를 깊이 있게 완성하기에도 빠듯합니다. 군더더기를 쳐내야 완주할 수 있습니다.

2. **워커 메커니즘을 PostgreSQL `SKIP LOCKED`로 단순화 (Worker Simplification)**
   - **조치**: 복잡한 분산 하트비트 스레드 합의 모델 대신, PostgreSQL의 `SELECT ... FOR UPDATE SKIP LOCKED`와 `lease_expires_at` 타임스탬프 기반 타임아웃 회수 구조로 표준화한다.
   - **이유**: 분산 시스템의 미묘한 동시성 버그(데드락, 좀비 스레드)에 매몰되는 것을 막고, DB 트랜잭션 격리수준과 원자적 상태 전이라는 핵심 개념에 집중할 수 있습니다.

3. **산출물 중심의 전환: 교안 작성 대신 '장애 보고서' 작성 (Incident-Driven Portfolio)**
   - **조치**: 주당 2~4개 마이크로 교안 작성을 폐기하고, 프로젝트 운영 중 발생한 **Incident Report & Runbook 3건**(예: DB 커넥션 고갈 장애, 워커 OOM 강제 종료 장애, 배포 실패 시 롤백 시나리오) 작성으로 대체한다.
   - **이유**: 신입 포트폴리오에서 "내가 만든 튜토리얼"은 채용 담당자에게 어필하지 못합니다. 실제 발생한 장애 로그, 근본 원인 분석(RCA), 해결 조치, 재발 방지책을 담은 장애 보고서가 현업에서 가장 높게 평가받는 강력한 증거입니다.

4. **클라우드 인프라를 AWS ECS Fargate + RDS로 단일화 (Infrastructure Streamlining)**
   - **조치**: EC2 직접 프로비저닝이나 K8s 도입을 배제하고, **AWS ECS Fargate + RDS PostgreSQL** 조합을 Terraform으로 완벽하게 코딩하여 배포한다.
   - **이유**: Fargate는 OS 레벨의 유지보수 부담을 없애면서도 VPC 격리, IAM 태스크 역할 분리, ECR 연동, CloudWatch 로그 스트리밍 등 클라우드 네이티브의 핵심 아키텍처를 온전히 배울 수 있는 최적의 타깃입니다.

5. **12주차 기능 동결(Feature Freeze) 및 완충 기간 확보 (Schedule Re-allocation)**
   - **조치**: 모든 기능 개발과 인프라 배포를 12주차에 종료한다. 13~14주차는 부하 테스트(Locust/k6) 및 장애 복구 시나리오 실증, 15주차는 AWS SAA 시험 응시, 16주차는 데모 영상 제작 및 이력서/포트폴리오 작성으로 재배치한다.
   - **이유**: 마감 4주 전 기능 구현을 동결해야만 예상치 못한 버그를 수습하고, 수치 기반의 성능 개선 지표를 확보하며, 완성도 높은 지원 서류를 준비할 수 있습니다.
