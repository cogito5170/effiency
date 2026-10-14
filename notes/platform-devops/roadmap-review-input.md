# 16주 플랫폼·DevOps 로드맵 — 독립 검토 입력

## 후보자와 목표

- 전자공학 학사, Python/C++ 사용 경험
- Linux, 네트워크, 클라우드 실무 경험 부족
- 가용 기간 약 16주
- 목표: 국내 주니어 Platform/DevOps, Cloud, Developer Productivity, Workflow Automation, 장기적으로 EDA/CAD infrastructure
- 시간 배분안: 프로젝트 60%, 기초 25%, 자격증 15%

## 자격증 계획

- 필수 1: AWS Solutions Architect Associate
- 필수 2: LFCS 또는 RHCSA 중 하나. 기본은 vendor-neutral 실기형 LFCS, RHEL·공공·SI 목표면 RHCSA
- 선택 3: 12주차까지 프로젝트와 AWS 배포가 완료된 경우에만 Terraform Associate
- 제외: CKA, SQLD, Python/C++ 민간 자격증, LFCS와 RHCSA 동시 취득

## 프로젝트

Reliable Job Platform: FastAPI로 작업을 접수하고 PostgreSQL에 저장한 뒤 여러 Python worker가 subprocess/container 작업을 실행한다.

핵심 기능:

- job CRUD와 상태 전이 queued/running/succeeded/failed/dead
- transaction 기반 atomic claim, idempotency key, 다중 worker
- timeout, bounded retry, exponential backoff
- lease/heartbeat와 worker crash 후 orphan job 회수
- structured log, job correlation ID
- throughput, error rate, latency, queue depth metrics와 alert/runbook
- Docker Compose 로컬 환경
- Terraform 기반 AWS 배포, IAM 최소 권한, secret/TLS
- GitHub Actions test/build/deploy와 rollback

후반 선택 기능:

- 13–14주 Kubernetes 로컬 배포, probes/resources/rollout 및 장애 3개 진단
- 15주 Yosys/OpenROAD batch workload 한 개 연결. PD/signoff 전문성은 주장하지 않고 EDA workload 운영만 증명

초기 비목표: Redis, Kafka, microservices, service mesh, multi-cloud.

## 학습과 구현 순서

1–2주: Linux process/signal/permission/log, DNS/TCP/TLS/HTTP, Git, 기존 runner 분석
3–4주: FastAPI, validation, pytest, subprocess, Docker/Compose
5–6주: PostgreSQL schema/constraint/index/transaction/isolation/lock, idempotency와 atomic claim
7–8주: retry/backoff/lease/heartbeat, fault injection, incident report
9–10주: AWS IAM/VPC/compute/storage/database, Terraform, cost와 architecture ADR
11–12주: CI/CD, structured logs, Prometheus/Grafana, alert와 runbook
13–14주: Kubernetes 기본과 ECS/VM/Kubernetes 비교 ADR
15주: 선택 EDA workload
16주: SAA 응시, 문서·데모·이력서·지원

## 마이크로 교안

매주 구현 전에 10–20분짜리 교안을 2–4개 작성한다. 한 교안은 질문 하나, Mermaid/ASCII 그림 하나, 핵심 문장 3–5개, 실행 가능한 10–30줄 코드, 실패 예제, 사용자가 AI 없이 푸는 TODO, 프로젝트 연결, 회상 질문 3개, 실행 증거로 구성한다. 사용자는 매주 한 번 60–90분 AI 없이 구현 또는 장애 해결을 수행한다.

## 계획된 증거물

- 공개 저장소, 자동 테스트와 CI
- Docker/Terraform, 선택 Kubernetes manifests
- architecture diagram, ADR 5개 이상
- failure matrix, runbook, incident report
- load-test 전후 수치, 비용 추정, 3–5분 데모
- 사용자의 교안 실습과 회상 답변

## Claude가 답할 질문

1. 이 계획이 초심자에게 16주 안에 현실적인가?
2. 반드시 유지, 연기, 삭제할 항목은 무엇인가?
3. 자격증 조합은 시간 대비 타당한가?
4. 국내 주니어 채용에서 강한 증거와 약한 증거는 무엇인가?
5. 빠진 기초는 무엇인가?
6. 첫 주에 실제로 끝낼 범위는 어디까지인가?
7. 가장 우선할 수정 5개는 무엇인가?
