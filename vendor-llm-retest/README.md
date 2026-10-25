# 공개 입력을 사용한 로컬 9B 재시험

이 폴더는 시험 근거이며 제품 설명 원고가 아닙니다. 채택하지 않은 9B 응답을 포함합니다.
`evaluation.json`은 자동 검사 결과이고 `author-review.json`은 작성 세션의 소스 대조입니다.
자동 통과를 의미 정확성·사람 승인으로 취급하지 않습니다. 사내 데이터는 포함하지 않습니다.

`calls/`의 요청·응답·영수증에는 실제 HTTP 호출 여부, 모델 설정과 해시가 있습니다.
추론 토큰 한도로 최종 답변이 없었던 호출에는 성공 응답 영수증이 없고 평가 보고서에 실패가 남습니다.
`sections.yaml`은 해당 시험 시점의 질문 사본입니다. 초기 시험에는 사본이 없으며 보고서의 해시를 보존합니다.
공개 문서의 세 Vendor 페이지는 별도로 소스 대조한 Codex-session 원고이며 9B 성공으로 표시하지 않습니다.

[분석·재시험 기록](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/docs/libcamera/records/vendor-9b-retest.md)을 참고하세요.
