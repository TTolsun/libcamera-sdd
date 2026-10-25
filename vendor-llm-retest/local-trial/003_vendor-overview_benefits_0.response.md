{
  "statements": [
    {
      "text": "`PipelineHandler::queueRequest` 함수는 캡처 요청을 파이프라인 핸들러에 대기열로 추가하여 처리를 준비합니다.",
      "quote_id": "queue:0",
      "covers": ["benefits"],
      "kind": "behavior"
    },
    {
      "text": "요청은 내부 대기 목록에 먼저 추가되며, 파이프라인 핸들러가 제출될 수 있도록 준비 상태를 확인합니다.",
      "quote_id": "queue:0",
      "covers": ["benefits"],
      "kind": "behavior"
    },
    {
      "text": "대기 중인 요청 목록은 순차적으로 반복되며, `maxQueuedRequestsDevice_` 제한 내에서 동일한 제출 순서대로 파이프라인 핸들러로 전달됩니다.",
      "quote_id": "queue:0",
      "covers": ["benefits"],
      "kind": "behavior"
    },
    {
      "text": "요청 준비 단계 중 실패하거나 파이프라인 핸들러가 하드웨어에 제출을 실패하면 해당 요청은 자동으로 취소됩니다.",
      "quote_id": "queue:0",
      "covers": ["benefits"],
      "kind": "behavior"
    },
    {
      "text": "대기 중인 요청을 추적함으로써 `stop()` 호출 시 파이프라인 핸들러가 중지되더라도 모든 요청이 자동으로 완료됩니다.",
      "quote_id": "queue:0",
      "covers": ["benefits"],
      "kind": "behavior"
    },
    {
      "text": "요청 완료는 파이프라인 핸들러가 `completeRequest()` 함수를 사용하여 명시적으로 신호로 전달해야 합니다.",
      "quote_id": "queue:0",
      "covers": ["benefits"],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::queueRequest` 는 카메라 관리자 스레드에서 호출됩니다.",
      "quote_id": "queue:0",
      "covers": ["benefits"],
      "kind": "behavior"
    }
  ]
}
