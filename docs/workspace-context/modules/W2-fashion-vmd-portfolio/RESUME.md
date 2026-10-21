# W2 패션 · VMD 지원 포트폴리오 (JAJU 라운딩 VMD · 이전 신세계 FROM THE INSIDE)
기준 2026-10-21T10:42Z · 체크포인트 claude/friendly-gates-0u80ge@0be22a5, claude/project-thread-n4rxnf@cd4f4d2, main@bdee7d6

## 지금
JAJU 포트폴리오: 사용자가 B2 로 정했고(10-21), '부족한 점대로 임의 수정' 지시로 B3 15쪽(a180d57)이 현재본이다. 다시 낸 부족한 점 분석(0ab955e)에서 표지 사진 출처와 자기 소개 쪽 정보가 사용자 답을 기다린다.

## 이어 할 일: `storyline`
b3_gap_analysis.md 의 고칠 순서대로 B3 를 다듬는다. 먼저 W2-O22(표지 사진이 직접 찍은 것인지)와 W2-O23(자기 소개 쪽 정보)을 사용자에게 묻는다. 그 뒤 process.md 6~8단계(묶기 · InDesign · 10MB 이내 제출본).
- 조건: 사용자 확인 필요.

## 사용자에게 물을 것
- W2-O1 storyline_v3 '정해야 할 것' 5가지: ① 한 줄 '패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다.' ② 표지를 쇼윈도(①-D)에서 THE STILL RUNWAY 로 바꿀지 ③ 기획안 P1 WINDOWS OF TIME / P2 REVE…
- W2-O2 원고 빈칸 ____: LOOK 착장 세부 · '오늘 ____ 에 간다', 설치 시간 · 인원 · 예산 · 재사용 비율, 연락처
- W2-O9 안의 시선 스토리라인 두 안 중 뼈대 선택: storyline_inside.md(v4, 하루의 순서 · 얼굴) / storyline_glass.md(유리 안쪽 · 겹침 · FITTING WINDOW) / 섞기
- 외 2개 → state.json open

## 지금 유효한 결정 (최근순)
- W2-D27 JAJU 포트폴리오는 B2 로 간다(경이 안 E · D · C 는 보존). 사용자 '부족한 점을 바탕으로 임의 판단하에 수정' 지시로 B3(15쪽) 작성
- W2-D25 JAJU 포트폴리오 장 순서: 표지 → 사진(관찰하다 · 뷰파인더) → 건축(담다 · 마당) → 패션(채우다 · 작은 따옴표). 재료는 지원자의 사진 · 패션 · 건축만, JAJU 로고 · 사진은 쓰지 않음. 장마…
- W2-D24 포트폴리오 대상을 JAJU 라운딩 VMD 로 전환. 기존 P1(FROM THE INSIDE) · v5 는 보존, 표지 · 1쪽은 B안을 그대로 쓴다
- W2-D23 P1 표지 + 1쪽은 B안(Galatasaray 방식: 사진 띠 + 검정 · 메시지 한 문장)으로. 표지 이미지는 사용자 제공. cover_b.* (InDesign IDML · JSX · zip)가 현재본
- 외 15개 → state.json decisions

## 작업 중인 파일
- docs/jaju_rounding_vmd/layout/cover_clean.pdf @ec39df7
- docs/jaju_rounding_vmd/layout/plan_b3.pdf @a180d57
- docs/jaju_rounding_vmd/b3_gap_analysis.md @0ab955e
- docs/jaju_rounding_vmd/layout/plan_e.pdf @940e96a
- 외 29개 → state.json artifacts

## 읽는 법
- 이 파일만 읽고 시작한다. 더 필요하면 `W2-fashion-vmd-portfolio/state.json` 의 해당 id 만 연다. 지난 이력은 `history.jsonl`.
- 미확인 7개는 결론으로 쓰지 않는다. 확정은 저장소 파일로 다시 확인한다.
- 결정 · 산출물은 저장소에 커밋해 둔다. 백엔드가 커밋에서 다음 요약을 만든다.
