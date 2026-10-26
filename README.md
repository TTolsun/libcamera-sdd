# libcamera 설계 문서 검증

[Vendor 연동 가이드](https://ttolsun.github.io/libcamera-sdd/vendor-integration.html)에 IPA 모듈 이름과 최소·최대 버전의 호환 조건을 보완했습니다. 실제 로컬 Qwen 9B가 실패 진단, 근거 확장과 세부 질문 생성을 거쳐 답변을 다시 작성했습니다. [자동 보완 시험 기록](qwen-reader-loop/README.md)에서 성공·실패와 재사용 범위를 구분합니다.

공식 source는 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `f2b3360d5f95055c01cd81c6145e2142495e7ed2`입니다. upstream 변경이 없어 300 TU·클래스 1,513개의 전체 빌드 facts를 재사용하고 공개 발췌를 다시 수집했습니다. 다른 원고 18편과 [이전 Vendor 시험](qwen-vendor-guides/README.md), [PR84 개요·소스 변경 시험](qwen-overviews/README.md)은 보존했습니다. 정기 예약은 설치하지 않았습니다.

한영 42페이지와 반복 빌드 138개 산출물을 검증했습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/vendor-integration.html)의 새 문장도 실제 Qwen으로 번역했습니다. 작성 세션의 소스 대조와 자동 검사만 수행했으며, 사람 승인·사내 HAL·실기기 검증은 남아 있습니다.

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 libcamera 입력만 게시하며 HTML은 생성기에서 만듭니다. [배포 기록](run.json), [산출물 해시](docs/site-manifest.json), [문장별 출처](generation-receipts.json)를 확인하세요.
