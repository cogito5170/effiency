# codex 이미지 파이프라인 첫 생성

- id: `005-codex-이미지-파이프라인-첫-생성`
- 생성: 2026-10-15

## Goal
`relay image` 파이프라인을 실제로 한 번 돌린다. Claude 는 `image-spec.json` (의미 스펙)만 썼다.
Codex 가 스펙을 상세 영어 프롬프트(`image-prompt.md`)로 펼치고, 내장 이미지 도구로 `image.png` 를 만든다.

## Run (Codex 로그인된 VM)
```bash
git pull && relay image 005
git add .relay/tasks/005-* && git commit -m "relay image 005: 생성 결과" && git push
```

## Done when
- `image.png`, `image-prompt.md`, `image.json`(status=ok) 가 이 폴더에 커밋되어 있다.

## VM 인박스로 실행 (VM 접근 없이)
`request.json` (action=image) 이 커밋되어 있다. VM 인박스 워커(docs/vm-inbox.md)가 켜져 있으면 자동으로 처리해
결과와 `response.json` 을 이 브랜치에 푸시한다.
