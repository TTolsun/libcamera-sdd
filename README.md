# libcamera 설계 문서 검증

**[공개 문서](https://ttolsun.github.io/libcamera-sdd/)에서 시작하세요.** For Vendor는 연동·구현 담당자, For Developer는 신입·타팀 개발자를 위한 경로입니다.

[시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)에서 구조를 확인하고, 장애를 조사할 때는 [요청 처리와 문제 진단](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html)을 읽으세요. 문단 근거의 **발췌**는 문서 안의 코드로, **전체 소스**는 분석 커밋의 저장소로 연결됩니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/)도 제공합니다.

## 로컬 Qwen 자동 갱신 검증

실제 libcamera 소스를 `7278a59eba64`에서 `2c4b67c0792f`로 변경하고 `sdd update`를 실행했습니다. 양쪽 커밋에서 각각 300개 번역 단위를 새로 추출했고, 로컬 Ollama의 `qwen3.5:9b`가 변경 전후 각각 5회 응답했습니다. [IPA 문서](https://ttolsun.github.io/libcamera-sdd/ipa.html)의 EGL 설명은 소스 변경에 따라 `GL_RG → DRM_FORMAT_RG88`에서 `GL_RG → DRM_FORMAT_GR88`로 갱신됐습니다.

새 EGL 문단 9개는 실제 HTTP 응답과 대조했습니다. 이 설명에는 Codex가 작성한 응답 묶음을 사용하지 않았습니다. IPA의 다른 주제 7개와 변경되지 않은 문서는 기존 내용과 작성자를 유지했습니다. 모든 문서를 이번에 Qwen으로 다시 생성했다는 뜻은 아닙니다.

[재현 자료와 검증 방법](qwen-replay/README.md), [호출 원문 10개와 소스 변경 기록](qwen-update-proof.json), [배포 입력·검사 기록](run.json), [산출물 해시](docs/site-manifest.json)를 확인하세요. `python qwen-replay/verify.py`는 별도 패키지 없이 호출 기록과 변경 전후 원고의 연결을 검사합니다.

## 생성과 배포

생성기 [#81](https://github.com/TTolsun/camera-hal-sdd-generator/pull/81)을 병합한 `f0389fa4b4f2a206fc0b4b4ac6f16f9320204561`로 사이트를 빌드했습니다. 최종 변경의 Ubuntu·Windows, Python 3.11·3.14 검사가 모두 통과했습니다. 한영 38페이지에서 링크 오류는 0개였고, manifest 검증과 동일 입력의 반복 빌드 비교가 통과했습니다.

2026-10-25 확인 시 공식 upstream의 새 커밋은 없었습니다. 기존의 실제 변경을 재실행하고, 문서에 없던 DMA-BUF 설명을 보완했습니다. 변경되지 않은 최신 개요와 진단 설명도 유지했습니다. 새 영어 문장은 같은 로컬 Qwen으로 번역했습니다.

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 정기 예약은 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·문서 갱신·검증·배포를 수행합니다. 생성 HTML은 직접 수정하지 않습니다.

한국어·영어 설명은 사람 검토 전입니다. 이 공개 검증은 사내 Camera HAL 적용이나 실제 카메라 시험을 포함하지 않습니다. 공개 libcamera 입력만 배포하며 사내 소스와 파생 산출물은 올리지 않습니다.

다음 단계: [IPA 문서](https://ttolsun.github.io/libcamera-sdd/ipa.html)에서 새 설명과 코드 발췌를 확인하세요.
