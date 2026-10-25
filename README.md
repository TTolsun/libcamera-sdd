# libcamera 설계 문서 검증

Vendor는 [제품 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html), [지원 범위와 검증](https://ttolsun.github.io/libcamera-sdd/vendor-assurance.html), [연동 가이드](https://ttolsun.github.io/libcamera-sdd/vendor-integration.html)에서 도입·연동 조건을 확인합니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/vendor-overview.html)도 제공합니다. 작업별 탐색 메뉴를 유지하며 Developer는 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)에서 시작합니다.

공식 upstream `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기 `49b1188125a5ec3d5d67f0d5f07e277cfc11661b` 기준입니다. upstream 변경이 없어 기존 전체 빌드 facts(TU 300개, 클래스 1,513개)를 재사용하고 설명의 누락·의무 표현을 보완했습니다. 세 Vendor 페이지의 30개 답변은 소스 대조한 Codex-session 원고입니다. 나머지 원고 16편과 [기존 Qwen EGL 근거](qwen-update-proof.json)를 보존했습니다.

## 실제 모델 재시험

로컬 qwen3.5:9b의 전체 문서 시험은 3개 모두 차단됐고, 추론을 켠 비교도 출력 한도로 전체 문서를 완료하지 못했습니다. 오류별 여섯 질문의 마지막 시험은 3개가 자동 통과했으나 자연어 의미 검토가 여전히 필요합니다. 이 시험을 사내 LLM의 무인 게시 준비 완료로 해석하지 않습니다. 채택하지 않은 모델 응답은 제품 원고로 게시하지 않았습니다.

[원요청·원응답과 시험 보고서](vendor-llm-retest/README.md), [작성자의 의미 대조](vendor-llm-retest/author-review.json), [생성기 PR #86](https://github.com/TTolsun/camera-hal-sdd-generator/pull/86)에서 작성 경로와 한계를 확인할 수 있습니다.

통합 회귀 792개 통과·1개 건너뜀, 마지막 회귀 사례를 포함한 관련 검사 68개 통과. 한영 42페이지, 링크 오류 0개, 반복 빌드 98개 파일 일치를 확인했습니다. 실제 사내 HAL·장치·독립 Vendor 읽기 검증은 수행하지 않았으며 원문·번역은 사람 검토 전입니다. 구매·홍보용 보장에는 실제 제품 사양·지원 조합·측정 결과·공개 승인이 필요합니다.

## 동기화와 배포

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 정기 예약은 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·누락 보완·검증·배포를 수행합니다. HTML은 직접 수정하지 않습니다. 사내 소스와 파생 데이터는 배포하지 않습니다.

[배포 기록](run.json), [작성 응답 해시](generation-receipts.json), [산출물 해시](docs/site-manifest.json)를 확인하세요.
