# 실제 Qwen Vendor 연동·지원 문서 작성 시험

최종 두 원고의 47개 답변은 실제 로컬 Qwen HTTP 응답에서 왔습니다. 문장을 수동으로 고쳐서 모델 작성 성공으로 세지 않았습니다. 최종 실행 방식은 verified-http-replay-and-live-repair입니다. 원응답 55회를 재사용하고 실제 HTTP 1회를 새로 호출한 보완 실행이며, 전체 신규 생성 시험과 구분합니다. `final/`은 채택한 시험이며 나머지 폴더는 실패·비교 기록입니다. 자동 통과와 작성 세션의 소스 대조는 사람 승인이나 사내 HAL 검증이 아닙니다.

[원인과 질문·근거·프롬프트 개선](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/docs/libcamera/records/vendor-9b-focused.md), [작성자의 소스 대조](author-review.json), [최종 평가](final/evaluation.json), [모델 실행 정보](final/runtime.json)를 확인하세요. 모든 입력은 공개 libcamera 소스입니다. PR #84의 두 개요와 소스 변경 시험은 ../qwen-overviews/에 그대로 보존했습니다.

생성기 저장소에서 `python examples/libcamera/verify_vendor_trial.py <공개 SDD 복제본>/qwen-vendor-guides/final`을 실행하면 요청·응답·질문·원고 해시와 인용 연결을 대조합니다. 검증기가 자연어 의미를 승인하지는 않습니다. 파일 이름의 final은 실행 당시의 이름일 수 있으므로 채택 여부는 이 문서와 배포 기록으로 구분하세요.
