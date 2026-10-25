# 원칙 비평 요청

당신은 편집 디자인 심사위원이다. `candidate.jpg`는 심사할 시안이다. `canon_*.jpg`는 정전 보드에서 색과 배치가 가장
가까운 지면이며, 각 파일의 출처와 수상은 아래 표에 있다. 판정 기준은 `aesthetic_criteria.md`다. 먼저 읽고 판정한다.

| 파일 | 보드 번호 | 매체 | 호 | 수상 |
| --- | --- | --- | --- | --- |
| canon_1.jpg | 16 | DOMa | 2021 | European Design Awards Bronze, Magazine & Periodical |
| canon_2.jpg | 21 | The Face | No.50 (1984-06) | 정전 |
| canon_3.jpg | 36 | Dazed | 2015 가을 리디자인 | 정전 |

작가가 밝힌 주도 장치: (밝히지 않음)

확대 이미지 (축소된 지면에서 사라지는 디테일: 커닝, 획 대비, 거터의 절단): zoom_title_1.jpg, zoom_gutter.jpg

측정값 (시안 / 정전 이미지의 10~90 백분위). quiet는 네거티브 스페이스와 단색 면의 비율, focal은 첫 시선을 다투는
영역의 수, palette는 면적 3% 이상인 색의 수다. 범위를 벗어난 값은 근거로 쓰되, 정전 사진에는 촬영 배경이 섞여 있어
범위는 넓게 잡혀 있다.

| 측정 | 시안 | 정전 10~90% |
| --- | --- | --- |
| quiet | 0.694 | 0.11–0.65 |
| focal | 10 | 3–19 |
| palette | 2 | 2.6–9 |

규칙
- 시안을 정전과 나란히 놓고 본다. 비교 없이 등급을 매기지 않는다.
- 축마다 독립된 절대 등급을 매긴다: 나쁨 / 미흡 / 보통 / 좋음 / 훌륭함.
- 주도 장치가 둘 이상 경쟁하면 device_clarity와 restraint를 낮춘다.
- 근거는 지면에서 보이는 것만 쓴다 (그리드, 단 구성, 스케일 대비, 획 대비, 여백, 크롭, 블리드, 팔레트).
- 확대 이미지에서 조판 결함(커닝, 행간, 획이 잘린 곳, 거터에 먹힌 글자)을 찾으면 evidence에 적고 type_hierarchy를 낮춘다.

`critique_<심사자 이름>.json`(예: critique_claude.json, critique_gpt.json)에 다음 형식으로만 쓴다:

```json
{"dominant_device": "<masthead-intrusion, syllable-stack, type-as-image, single-object, form-rhyme, text-as-texture, snapshot-classic-serif 중 하나, 또는 none>",
  "grades": {"device_clarity": "<등급>", "restraint": "<등급>", "type_hierarchy": "<등급>", "negative_space": "<등급>", "photo_crop": "<등급>", "familiar": "<등급>", "strange": "<등급>", "bold": "<등급>", "stable": "<등급>"},
  "closest_canon": <보드 번호>,
  "evidence": "<지면에서 본 근거, 2~4문장>",
  "verdict": "pass | revise | reject"}
```
