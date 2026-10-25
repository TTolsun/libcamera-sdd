{
  "statements": [
    {
      "text": "`PipelineHandler::queueRequestDevice` 함수는 카메라 장치에 캡처 요청을 대기열에 추가하며, 해당 요청이 포함된 버퍼와 파라미터가 프레임에 적용되도록 장치를 프로그래밍해야 합니다.",
      "quote_id": "queue:0",
      "covers": [
        "request"
      ],
      "kind": "behavior"
    },
    {
      "text": "이 함수는 `CameraManager` 스레드에서 호출되며, 성공 시 0을 반환하고 실패 시 음수 오류 코드를 반환합니다.",
      "quote_id": "queue:0",
      "covers": [
        "request"
      ],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::completeBuffer` 함수는 요청의 버퍼 부분이 완료되었음을 신호하기 위해 파이프라인 핸들러가 호출해야 하며, 애플리케이션에 버퍼 완료 상태를 알리고 요청 내부의 버퍼 추적을 업데이트합니다.",
      "quote_id": "completion:0",
      "covers": [
        "request"
      ],
      "kind": "behavior"
    },
    {
      "text": "최종 버퍼가 완료되더라도 요청이 자동으로 완료되지 않으며, 파이프라인 핸들러가 추가로 수행해야 할 작업을 처리할 기회를 주기 위해 명시적으로 `completeRequest` 함수를 호출하여 요청을 완료해야 합니다.",
      "quote_id": "completion:0",
      "covers": [
        "request"
      ],
      "kind": "behavior"
    },
    {
      "text": "`completeBuffer` 함수는 요청에 포함된 모든 버퍼가 완료되었는지 여부를 나타내는 참 또는 거짓 값을 반환합니다.",
      "quote_id": "completion:0",
      "covers": [
        "request"
      ],
      "kind": "behavior"
    },
    {
      "text": "`completeBuffer` 함수는 반드시 `CameraManager` 스레드에서 호출되어야 하며, 이는 요청 처리의 순서와 스레드 안전성을 보장합니다.",
      "quote_id": "completion:0",
      "covers": [
        "request"
      ],
      "kind": "behavior"
    },
    {
      "text": "`queueRequestDevice` 함수는 요청을 장치에 프로그래밍하여 파라미터를 적용하고, `completeBuffer` 함수는 개별 버퍼 완료 상태를 보고하며, 최종 요청 완료는 별도의 명시적 호출로 처리됩니다.",
      "quote_id": "queue:0",
      "covers": [
        "request"
      ],
      "kind": "behavior"
    }
  ]
}
