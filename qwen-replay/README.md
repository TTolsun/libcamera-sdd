# 로컬 Qwen 자동 갱신 기록

**`python qwen-replay/verify.py`로 호출 기록과 변경 전후 원고의 연결을 확인하세요.** 별도 Python 패키지는 필요하지 않습니다.

실제 libcamera 부모 커밋 `7278a59eba64`에서 `2c4b67c0792f`로 `sdd update`를 실행했습니다. 양쪽 모두 300개 번역 단위를 다시 추출했고 파싱 오류는 0개였습니다. Windows의 로컬 Ollama `qwen3.5:9b`를 직접 호출했으며, WSL에서 빌드·추출했습니다.

[전체 기록](../qwen-update-proof.json)에는 소스 diff, 모델 digest, 전후 원고 해시, 실제 HTTP 요청·응답이 들어 있습니다. [변경 전 원고](before-ipa.md)의 `GL_RG → DRM_FORMAT_RG88` 설명이 [변경 후 원고](after-ipa.md)의 `GL_RG → DRM_FORMAT_GR88`로 갱신됐습니다. 새 EGL 답변에 사용한 호출은 변경 전 5회, 변경 후 5회입니다.

변경되지 않은 IPA 주제 7개는 근거를 재검증해 유지했으며 기존 작성자를 기록했습니다. 새 EGL 설명에는 Codex가 작성한 응답 묶음을 넣지 않았습니다. 기록은 생성기 PR #81의 개발 작업 트리에서 실행한 결과이며, 배포에 사용한 최종 생성기 커밋은 [run.json](../run.json)에 있습니다.

이 검증은 기록과 소스·문서의 일치를 확인합니다. 모델이 어떤 코드에서도 정확한 설명을 만든다는 보장이나 사람 승인, 실제 카메라·사내 HAL 검증은 아닙니다.

다음 단계: [배포된 IPA 문서](https://ttolsun.github.io/libcamera-sdd/ipa.html)에서 새 설명과 코드 발췌를 확인하세요.
