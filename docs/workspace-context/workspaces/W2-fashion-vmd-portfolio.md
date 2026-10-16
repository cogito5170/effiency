# W2. 패션 · VMD 지원 포트폴리오

작업 공간 태그 `ws:w2-fashion-vmd-portfolio` · 상위 워크스페이스 `workspace:gentlemonster-effiency` · 도메인 fashion

신세계 VMD 'ON DISPLAY' 스토리 · 표지 · 청사진, 패션 공간 직군 공고 조사, AI×패션 시안. W1 의 지원처 전환과 같은 시기다. [요약]

이 파일은 2026-10-15 세션 카드에서 뽑은 스냅숏이다. 확정 여부는 저장소 파일로 다시 확인한다 (workspace.md P3).
`[추론·미검증]` 줄은 다른 세션의 모델이 한 말이라 결론으로 옮기지 않는다 (P2).

## 구성원

| 세션 | 세션 ID | 갱신 | 상태 | 브랜치 | 카드 |
|---|---|---|---|---|---|
| 혁주 컨셉 이미지 | `session_01PEVQJv8SCpLFv14iXTm9Ek` | 2026-10-15 15:11 | COMPLETED | `cogito5170/gentleMonster@claude/friendly-gates-0u80ge` | [카드](../sessions/session_01PEVQJv8SCpLFv14iXTm9Ek.md) |
| 의류/패션 공간 직군 채용공고 | `session_01Ctu8Xc8KMJPnwqyzGUHcmY` | 2026-10-13 08:06 | REVIEW_READY | `cogito5170/gentleMonster@claude/magical-bell-u02os9` | [카드](../sessions/session_01Ctu8Xc8KMJPnwqyzGUHcmY.md) |
| AI와 패션 디자인 아이디어 시안 | `session_011RbA1e4nPywwwdsq2ZNe4N` | 2026-10-09 17:52 | COMPLETED | `cogito5170/gentleMonster@claude/blissful-cori-hookcx`<br>`cogito5170/se_new@claude/blissful-cori-hookcx` | [카드](../sessions/session_011RbA1e4nPywwwdsq2ZNe4N.md) |

## 확정 · 정정 (사용자 말)

**혁주 컨셉 이미지**
- 이미지 생성 도구: 프롬프트는 Claude, 생성은 미드저니 (10-15 12:06) → 이후 main 의 "이미지는 모두 Codex" 규칙을 받아 Codex 로 생성 [사용자]/[추론·미검증] (event: f185f23b…)
- 젠틀몬스터 포트폴리오 스토리라인은 무시, 참고만 [사용자] (event: a6d2b690…)
- 판형 A4 가로 확정 [사용자] (event: 68dcd009…)
- 직무 방향: "상품연출 · 마네킹 착장 스타일링을 하는 VMD … '소비'하도록" [사용자] (event: 68dcd009…)
- 이미지 안 제작 전 스토리 문장 먼저 [사용자] (event: 0d235792…)

**의류/패션 공간 직군 채용공고**
- 없음 [요약]

**AI와 패션 디자인 아이디어 시안**
- 3D 렌더링 필요한 시안은 제외, RELIEF(부조) 사용 [사용자] (event: 36eafa9b-efc1-4813-9989-30736a96dca9)
- 표현 방식을 "조형적으로", "트리거 → 조형물이 움직이는 원리"로 좁힘 [사용자] (event: 06428777-…, 7ae1337e-…)
- drift 소설 요청은 사용자가 중단함 [사용자] (event: 077b80a1-…)


## 결과 · 산출물

**혁주 컨셉 이미지**
- docs/contests.md, docs/contests_winners.md — 공모전 목록 · 우승작 분석 [도구출력]
- tools/contest_jpeg.py — 공모전 제출용 JPG(1–5MB · sRGB · EXIF 유지) (커밋 6b02cd3, 10-13) [도구출력]
- docs/shinsegae_vmd/{storyline.md, storyline_v3.md, see_pick_keep.md, concepts_beyond_window.md, story_text.md, image_prompts.md} — 스토리 v1~v3 · 원고 · 미드저니 프롬프트 [도구출력]
- tools/window_blueprint/ → blueprint/cover_blueprint.pdf · _preview.jpg · cover_concept_render.jpg (표지 ①-D 청사진, b10b245) [도구출력]
- tools/story_blueprint/build.mjs → blueprint/story_blueprint.pdf (이야기 전체 청사진, c852c71) [도구출력]
- tools/scene_blueprint/{build,dims,scene,sheet}.mjs → still_runway_blueprint.pdf · _preview.jpg · still_runway_render.jpg (8106369) [도구출력]
- .relay/tasks/002-still-runway: response.json status=done, exit_code=0, image.png 생성 (15:06~15:08) [도구출력]
- 장면 THE STILL RUNWAY(흰 큐브에 앉은 사람 + 흐리게 지나가는 사람들, 걷다·꺾이다·집다·챙기다)로 정리, 컨셉 이미지는 Codex 가상 인물 [추론·미검증]
- 한 줄 "패션쇼에서는 옷이 걷는다. 매장에서는 내가 걷는다." 및 책 제목 ON DISPLAY 제안 [추론·미검증]
- 도면 수치(스튜디오 8×8.2m 등)는 가정값, dims.mjs 로 수정 [추론·미검증]

**의류/패션 공간 직군 채용공고**
- 파일·커밋 없음. 브랜치 claude/magical-bell-u02os9 는 origin 에 없음 [도구출력]
- 채용 사이트 원문을 직접 열지 못했고 검색 요약 기반이라고 스스로 밝힘 [추론·미검증]
- 10/13 기준 지원 가능해 보이는 국내 공고는 유니클로(에프알엘코리아) VMD Designer(In-Store Merchandising팀, 마감 10/19, 경력 3년+) 1건 [추론·미검증]
- 무신사 스탠다드 머천다이징 VMD 는 진행 여부 불명, 다른 무신사 VMD 공고들은 마감; 자라·COS 국내 공간 공고는 만료 가능성 높음 [추론·미검증]
- 국내에는 "공간 설계(인테리어 건축)" 직무가 거의 없고 대부분 VMD; 해외 COS VMD(런던 11/5, 암스테르담 10/28, 홍콩 10/29, 브로츠와프 11/11) 열림 [추론·미검증]
- COSRX VMD 공고는 H&M COS 와 무관하다는 주의 [추론·미검증]

**AI와 패션 디자인 아이디어 시안**
- Artifact "선글라스를 만들어라" https://claude.ai/artifact/UcSTSA7Bxd2BxNPALedxSM (V1, 원본 그 세션 scratchpad sun/site/index.html) [도구출력]
- Artifact "REREAD 다시 읽는 기계" https://claude.ai/artifact/H7V166vea7LHa6r5SqU2Hu (V1, sun/machine/index.html) [도구출력]
- 그 세션 scratchpad 에 sunglasses.svg(run1~3), strip/obj *_rake/_flat.png, raster*.png 등 부조 렌더 파일 (컨테이너 휘발, git 아님) [도구출력]
- origin 에 gentleMonster@claude/blissful-cori-hookcx 브랜치 없음 — 커밋 산출물 없음으로 보임 (se_new 는 클론 없어 미확인) [도구출력]
- 마지막 답: "REREAD 는 안경을 만들지 않고 LLM 그림의 부조와 과정 띠만 새긴다; 실착용 안경은 A(시착 검증) 또는 B(얼굴 치수 입력) 단계 추가 필요, 추천 A" [추론·미검증]


## 열린 일

**혁주 컨셉 이미지**
- 모델이 묻고 답 없음: 한 줄 문구 확정, 표지(쇼윈도 vs 앉은 나+흐린 사람들), 기획안(WINDOWS OF TIME / REVERSE RUNWAY / 둘 다), 빨강 한 점, 표지 직접 촬영 가능 여부 [추론·미검증]
- 원고 빈칸(____: 착장 세부 · 예산 · 연락처), 향수 브랜드명 노출, 신세계 사실관계 재확인 [추론·미검증]
- 마지막 제안: 이 장면으로 표지 확정 시 촬영 준비 목록 작성 [추론·미검증]
- 브랜치는 PR 없이 원격에만 존재(main 미병합) [도구출력]

**의류/패션 공간 직군 채용공고**
- 유니클로 공고 원문에서 마감·조건 확인 필요(조건 일부가 2022년 공고일 수 있음) [추론·미검증]
- 후속 사용자 요청 없음, REVIEW_READY 상태 [도구출력]

**AI와 패션 디자인 아이디어 시안**
- "안경을 만들어주는가?"에 대한 A/B 안 중 선택 없음; 포트폴리오 문항 답(AI 기술 1개 서술) 작성 여부 불명 [요약]
- 이미지 생성 규칙(CLAUDE.md: 이미지는 Codex) 이전 세션 — 부조 PNG/SVG 는 코드 렌더로 만든 것으로 보임 [추론·미검증]

## 이어받는 법

1. 이 프로젝트 채팅에 "W2 이어서 …" 처럼 요청하면 새 스레드가 이 파일을 근거로 시작한다. 새 세션에는 `workspace:gentlemonster-effiency` 와 `ws:w2-fashion-vmd-portfolio` 태그를 붙인다.
2. 원본이 필요하면 위 세션 ID 로 `list_events(kinds=["user"])` 를 읽고, 카드의 event ID 만 `get_event` 한다. 대화를 통째로 옮기지 않는다 (P1).
3. 브랜치는 `git log origin/<branch> ^origin/main` 으로 확인한다.
4. 다른 워크스페이스에서 일을 넘겨받을 때 도메인이 다르면 첫 줄에 붙인다: `주제 전환: <앞> → 패션 · VMD 지원 포트폴리오. 앞 작업에서 정한 재료 · 브랜드 · 치수 · 결정은 이 요청에 적용하지 마세요.` (P4)
