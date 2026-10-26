# 로컬 9B 자동 보완 루프 시험

최종 실행은 3회차와 실제 HTTP 10회로 완료했습니다. 변경되지 않은 기존 응답은 해시를 검증해 재사용했으며, 전체 원고를 새로 생성한 시험이 아닙니다. 진단 대상은 IPA 모듈 호환성 질문 1개이며 나머지 37개 질문은 의미 진단에서 제외했습니다. 최종 원고의 40개 답변은 실제 Qwen 응답과 연결됩니다.

현재 근거만으로 진단하고 허용된 함수 범위를 확장한 뒤, 반복되는 조건 누락은 세부 질문으로 분리했습니다. 원래 답변 계약은 유지했습니다. [원인 분석](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/docs/libcamera/records/reader-loop-9b.md), [최종 기록](final/loop.json), [호출 한도 종료](call-limit/loop.json), [출처 검증](verification.json), [작성 세션 소스 대조](author-review.json)를 확인하세요.

`history/`는 실패·개발 시험이며 배포 원고로 채택하지 않았습니다. 특히 trial-2의 완료 판정은 근거 혼동에 따른 오판으로 폐기했습니다. 모델 검토 완료는 의미 정확성 보장이나 사람 승인이 아닙니다. 사내 HAL·실기기 검증은 수행하지 않았습니다. `python examples/libcamera/verify_reader_loop.py <이 폴더>/final`로 출처를 재검사할 수 있습니다.
