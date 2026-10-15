# Physical Design 포트폴리오 프로젝트 제안서

## 한 줄 제안

**Ibex 32-bit RISC-V 코어를 Sky130HD에서 ORFS로 RTL-to-GDS 구현하고, 코어 이용률과 목표 클록 주기를 한 번에 하나씩 바꾸어 PPA·타이밍·혼잡·배선 가능성의 상충 관계를 설명하는 16주 프로젝트**를 수행한다.

이 프로젝트의 목표는 가장 높은 주파수나 가장 작은 면적을 과시하는 것이 아니다. 동일한 RTL·플랫폼·플로에서 제약이 물리 구현 결과에 미치는 영향을 재현하고, 실패한 조건을 보고서로 진단하며, 선택한 최종 구현점을 근거로 방어하는 것이 목표다.

## 1. 채용 관점에서의 가치

Ibex + Sky130HD + ORFS 조합은 신입 Physical Design/PnR 지원자에게 다음 능력을 한 프로젝트 안에서 보여 준다.

- **전체 흐름 이해:** Yosys 합성부터 floorplan, placement, CTS, routing, GDS 생성까지 단계별 입력·출력과 제약의 연결을 설명할 수 있다.
- **PD 핵심 판단:** 이용률이 높아질 때 면적은 줄 수 있지만 혼잡·우회 배선·타이밍 위반이 늘 수 있고, 클록 요구가 빡빡해질수록 버퍼링·셀 크기·전력·배선 난도가 변한다는 사실을 실제 리포트로 입증한다.
- **디버깅 역량:** 단순히 성공한 마지막 결과만 제시하지 않고, 위반 경로·혼잡 구역·DRC 유형을 찾아 한 가지 실패 조건을 원인-조치-결과로 기록한다.
- **재현성:** 공개 RTL, 공개 PDK 기반 플랫폼, 공식 ORFS Docker 실행법, 고정한 소스 리비전과 설정을 사용하므로 면접관이 작업 범위와 결과의 출처를 확인할 수 있다.
- **신입에게 맞는 깊이:** CPU 마이크로아키텍처를 새로 설계하지 않고 검증된 소형 코어를 사용해, 제한된 16주를 물리 구현과 결과 해석에 집중한다.

Sky130HD와 OpenROAD의 결과는 학습 및 포트폴리오 목적의 오픈소스 구현 증거다. 여기서 수행하는 timing/DRC 검사는 사용한 공개 모델과 도구 범위의 교육용 확인이며, 상용 signoff, 실리콘 검증, tapeout readiness를 의미하지 않는다.

## 2. 대안 검토

**최종안보다 진정으로 나은 대안은 현재 없다.** 더 큰 SoC는 메모리·매크로·주변장치 통합과 긴 런타임 때문에 16주 내 분석 깊이를 해치며, 더 작은 장난감 RTL은 실행은 쉽지만 실제 코어의 클록·혼잡·타이밍 상충 관계를 보여 주는 채용 증거가 약하다. 따라서 별도 대안 프로젝트를 병행하지 않는다.

## 3. 최종 추천 프로젝트와 선택 이유

### 프로젝트 제목

**Constraint-Driven Physical Design of Ibex on Sky130HD**

### 고정 범위

- 디자인: 공개 Ibex 32-bit RISC-V 코어의 ORFS에서 지원되는 고정 구성
- 플랫폼: Sky130HD
- 실행 환경: Apple Silicon macOS의 공식 ORFS Docker 흐름
- 합성/구현: Yosys + OpenROAD, ORFS 기본 단계 사용
- 실험 변수: 코어 이용률과 목표 클록 주기만 사용
- 결과: 재현 가능한 baseline, 두 개의 독립된 소규모 sweep, 최종 구현점 선정, 실패 사례 1건 분석

이 안을 추천하는 이유는 입문자가 완주할 수 있을 만큼 작으면서도 합성 결과, floorplan 밀도, CTS, setup/hold, congestion, routing DRC를 하나의 인과관계로 설명할 만큼 실제적이기 때문이다. 실험 변수를 두 개로 제한하면 넓은 자동 탐색 대신 각 결과를 직접 검토하고 면접에서 수치와 판단을 방어할 수 있다.

### 실행 원칙과 실험 설계

1. ORFS 공식 문서의 Apple Silicon용 Docker 절차로 환경을 구성하고 Docker 이미지 태그 또는 digest, ORFS·Ibex commit, 실행 명령, 호스트 사양을 기록한다.
2. ORFS에서 제공하거나 검증된 Ibex 설정을 먼저 그대로 실행한다. 첫 성공 전에는 RTL이나 flow Tcl을 임의로 최적화하지 않는다.
3. baseline의 클록 주기와 이용률을 기준으로 고정한다. 이후 **한 번에 한 변수만** 바꾼다.
4. 이용률 실험은 baseline을 포함해 현실적으로 완주 가능한 3개 지점(예: 40%, 50%, 60%)으로 시작한다. 한 지점이 명백히 unroutable이면 같은 실패를 반복하지 않고 원인을 기록한다.
5. 클록 실험도 baseline을 포함한 3개 지점으로 제한한다. 첫 baseline 결과를 보고 지나치게 느슨하거나 불가능하지 않은 간격을 정한다(예: 20 ns, 15 ns, 12 ns). 이용률은 baseline 값으로 고정한다.
6. 각 설정은 clean run으로 실행하고 config diff와 결과 디렉터리를 보존한다. 임의로 성공 사례만 골라내지 않는다.
7. 최종 구현점은 단순 최고 주파수가 아니라 routed 완료, 교육용 DRC 상태, setup/hold 여유, 혼잡, 면적의 균형으로 선택한다.

## 4. 16주 마일스톤

| 주차 | 작업 | 주간 완료 기준 |
|---|---|---|
| 1 | PD 흐름과 ORFS 구조 학습, 저장소·Docker 준비 | 단계별 입력/출력 1쪽 요약, 환경 정보 기록 |
| 2 | Apple Silicon 공식 Docker 흐름 확인, 버전 고정 | 컨테이너 실행과 최소 smoke test 재현 |
| 3 | Ibex/Sky130HD 설정 확인, 합성 실행 | Yosys 합성 완료, 셀 수·면적·제약 보관 |
| 4 | 첫 baseline RTL-to-GDS 실행 | GDS와 단계별 로그 생성, 실패 시 최초 원인 기록 |
| 5 | baseline 안정화 및 clean rerun | 동일 설정 재실행 성공, 핵심 지표 표 작성 |
| 6 | floorplan·placement 분석 | die/core 면적, 이용률, placement density, 혼잡 이미지 정리 |
| 7 | CTS·timing 분석 | clock tree, setup/hold, WNS/TNS, 주요 경로 설명 |
| 8 | routing·교육용 DRC 분석 | routed 결과, wirelength/via/DRC 요약과 레이아웃 이미지 |
| 9 | 이용률 sweep 3점 실행 | 동일 클록에서 3점 결과 또는 실패 근거 확보 |
| 10 | 이용률 결과 비교 | 면적·혼잡·타이밍·DRC 비교표와 인과 해석 |
| 11 | 클록 주기 sweep 3점 실행 | 동일 이용률에서 3점 결과 또는 실패 근거 확보 |
| 12 | 클록 결과 비교 | 셀/버퍼·타이밍·면적·전력 추정치 비교표 작성 |
| 13 | 실패 사례 1건 심층 분석 | 증상→근거→가설→최소 조치→재실행 결과 기록 |
| 14 | 최종 구현점 선정 및 재현 | 선택 기준 명시, clean run으로 최종 결과 재생성 |
| 15 | 포트폴리오 문서와 그림 완성 | 8~12쪽 보고서 초안, 표·그림마다 출처/조건 표기 |
| 16 | 면접 리허설과 저장소 정리 | 5분 설명, 예상 질문 답변, README 재현 절차 검증 |

4주차까지 baseline이 완료되지 않으면 sweep 지점을 늘리지 않는다. 6주차에도 막히면 새 RTL이나 새 플랫폼으로 바꾸지 않고, 공식 예제 설정과 로그를 기준으로 baseline 복구를 우선한다.

## 5. QoR 지표와 보존할 증거

모든 수치는 **어느 flow 단계의 어느 리포트에서 나온 값인지** 표시한다. 서로 다른 단계의 수치를 같은 의미로 비교하지 않는다.

| 영역 | 측정할 지표 | 보존할 증거 |
|---|---|---|
| 재현성 | ORFS/Ibex revision, Docker image, 호스트 CPU·RAM, 명령, runtime | `README`, version manifest, 실행 스크립트/명령, config 파일과 diff |
| 합성 | 표준셀 수, 조합/순차 셀 수, 합성 면적, 메모리/black box 유무 | Yosys log와 synthesis statistics report |
| 면적/밀도 | die/core 면적, 목표·실제 utilization, placement density | floorplan/placement report, GUI 스크린샷 |
| 타이밍 | clock period, setup WNS/TNS와 violating endpoints, hold WNS/TNS와 위반 수, 대표 critical path | post-CTS와 post-route timing report, 경로 발췌, 단계별 비교표 |
| 클록 | insertion delay/latency, skew, clock buffer 수(리포트가 제공하는 범위) | CTS report와 clock tree 이미지 |
| 혼잡/배선 | global-route overflow 또는 congestion 지표, total wirelength, via 수 | congestion report/heatmap, route statistics |
| 물리 검사 | 교육용 routing DRC 총수와 유형별 수, antenna 등 도구가 보고한 항목 | 상세 DRC report와 위반 위치 이미지 |
| 전력 | ORFS가 동일 조건에서 제공하는 추정 total/internal/switching/leakage power | power report, 분석 조건과 activity 가정; 실측 전력처럼 표현하지 않음 |
| 완주 상태 | 각 단계 성공/실패, 최종 GDS 생성 여부 | 원본 로그, 결과 디렉터리, GDS/DEF, 최종 레이아웃 이미지 |

최종 포트폴리오에는 baseline과 각 sweep의 한 행짜리 요약표, 이용률-지표 그래프, 클록 주기-지표 그래프, baseline/최종/실패 조건 레이아웃 그림을 넣는다. 로그 전체를 본문에 붙이지 않고 원본 경로와 핵심 줄을 연결한다. 전력은 동일한 activity 가정이 유지될 때만 상대 비교하며, PDK·라이브러리·코너가 달라지면 직접 비교하지 않는다.

### 최종 구현점의 최소 판정 기준

- flow가 routing과 GDS 생성까지 완료될 것
- 목표 클록에 대한 post-route setup/hold 상태를 수치로 제시할 것(위반이 남으면 숨기지 않고 이유와 영향을 명시)
- 교육용 DRC 결과를 유형별로 제시할 것(0이 아니어도 원인과 한계를 설명)
- sweep의 이웃 지점보다 왜 채용 포트폴리오에 더 균형 잡힌 선택인지 정량적으로 설명할 것
- 같은 고정 버전과 설정에서 clean run 절차가 재현될 것

## 6. 면접에서 방어해야 할 기술 질문

지원자는 아래 질문에 자신의 리포트와 그림을 가리키며 답할 수 있어야 한다.

1. RTL constraint가 합성과 placement, CTS, routing을 거쳐 최종 타이밍에 어떤 영향을 주었는가?
2. target utilization과 실제 placement density는 무엇이 다르며, 이용률을 높였을 때 어떤 지표가 먼저 악화됐는가?
3. setup과 hold 위반의 차이는 무엇이며 일반적으로 어느 단계에서 어떤 방식으로 고치는가?
4. WNS와 TNS는 각각 무엇을 말하며, 한쪽만 보고 구현점을 선택하면 왜 위험한가?
5. pre-CTS, post-CTS, post-route timing이 달라진 이유는 무엇인가?
6. clock skew와 insertion delay는 무엇이며 이 프로젝트의 CTS 결과에서 어떻게 관찰했는가?
7. congestion heatmap과 routing overflow는 무엇이며 실제 상세 배선 실패와 어떤 관계가 있었는가?
8. 클록 주기를 줄였을 때 셀 크기, 버퍼 수, 면적, 전력 추정치가 왜 변했는가?
9. 가장 나쁜 critical path의 startpoint, endpoint, 논리 깊이, 지연 구성에서 무엇을 읽었는가?
10. 실패한 run에서 증상과 근본 원인을 어떻게 구분했고, 어떤 최소 변경으로 가설을 검증했는가?
11. 결과의 비교 공정성을 위해 무엇을 고정했고, run-to-run 재현성을 어떻게 확인했는가?
12. Sky130HD/OpenROAD의 교육용 timing·DRC 결과가 상용 signoff 또는 tapeout 준비 완료를 증명하지 못하는 이유는 무엇인가?
13. 전력 수치에 어떤 switching activity와 분석 코너 가정이 있으며, 그 수치를 어디까지 해석할 수 있는가?
14. 최종 구현점을 가장 빠른 조건이 아니라 해당 조건으로 선택한 근거는 무엇인가?

## 7. 제거할 과잉 범위

다음은 16주 프로젝트 범위에서 명시적으로 제외한다.

- 새 CPU/명령어/파이프라인 설계 또는 Ibex 기능 수정
- 여러 CPU 코어, 여러 PDK·표준셀 라이브러리, FPGA 결과와의 병렬 비교
- 캐시·SRAM macro 통합, pad ring, package, IO, power intent/UPF, multi-voltage 설계
- 대형 SoC, 멀티코어, full-chip 통합
- 수십~수백 조합의 광범위한 parameter search 및 자동 최적화
- AI/LLM/agent를 이용한 설정 생성, 탐색, 로그 분석 또는 PD flow 자동화
- 새로운 EDA 플러그인·대시보드·웹 UI 제작
- RTL functional verification를 별도 대형 프로젝트로 확장
- 상용 도구 결과와의 비교, foundry signoff, 실제 tapeout 또는 실리콘 성능 주장

필요한 자동화는 ORFS 자체 흐름 실행과 결과 정리에 필요한 단순 shell 명령 수준으로 제한한다. 핵심 산출물은 자동화 코드가 아니라 물리 구현 결과와 엔지니어링 판단이다.

## 8. 한국어 이력서 문장

아래 문장은 실제 결과 수치를 확보한 뒤 대괄호를 채워 사용한다. 달성하지 못한 항목은 삭제한다.

- 공개 RISC-V Ibex 코어를 Sky130HD·Yosys·OpenROAD Flow Scripts 환경에서 합성부터 배치·CTS·배선·GDS 생성까지 구현하고, Docker 기반 재현 절차와 단계별 결과를 문서화했습니다.
- 코어 이용률 [A/B/C%] 조건을 통제 비교하여 post-route WNS/TNS, 혼잡, 배선 길이, DRC 변화의 상충 관계를 분석하고 [선택 이용률]%를 최종 조건으로 선정했습니다.
- 목표 클록 주기 [X/Y/Z ns] 실험에서 셀 수·면적·타이밍·전력 추정치 변화를 비교하고, 동일 RTL·PDK·분석 조건을 유지해 결과의 비교 가능성을 확보했습니다.
- [실패 조건]에서 발생한 [timing/congestion/DRC] 문제를 리포트와 레이아웃으로 추적하고, [변경한 한 가지 조건] 조정 전후 결과를 비교해 원인과 해결 과정을 정리했습니다.

이력서와 면접에서는 이 결과를 **오픈소스 도구 기반 교육용 RTL-to-GDS 구현 및 분석**으로 표현한다. 상용 signoff 완료, tapeout 완료, 실리콘 검증, 양산 수준이라는 표현은 사용하지 않는다.

## 최종 산출물 체크리스트

- 재현 절차와 고정 버전이 있는 README
- baseline 및 실험 설정 파일과 변경 diff
- 6회 이내의 계획된 핵심 run 결과와 원본 로그
- QoR 요약 CSV/표와 2개의 통제 실험 그래프
- baseline·최종·실패 사례의 레이아웃/혼잡/경로 이미지
- 실패 사례 1건의 원인-조치-결과 기록
- 8~12쪽 최종 보고서와 5분 면접 설명 자료
- 교육용 검사와 상용 signoff의 경계를 명시한 한계 섹션
