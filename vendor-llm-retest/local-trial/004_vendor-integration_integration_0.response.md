{
  "statements": [
    {
      "text": "애플리케이션은 먼저 카메라를 획득하고 구성한 뒤 촬영을 준비해야 하며, 이후 카메라를 시작하면 요청을 처리할 수 있습니다. 완료되면 카메라를 중지하고 해제해야 합니다.",
      "quote_id": "camera:0",
      "covers": [
        "integration"
      ],
      "kind": "behavior"
    },
    {
      "text": "카메라는 여러 번 시작하거나 중지할 수 있지만, 해제된 상태에서는 안 됩니다. 또한 카메라를 다시 구성하는 것도 가능합니다.",
      "quote_id": "camera:0",
      "covers": [
        "integration"
      ],
      "kind": "behavior"
    },
    {
      "text": "PipelineHandler::match() 함수는 매체 장치를 확보하고 카메라 인스턴스를 생성하며 카메라 관리자에서 등록하는 책임을 가집니다.",
      "quote_id": "handler:0",
      "covers": [
        "integration"
      ],
      "kind": "behavior"
    },
    {
      "text": "match() 함수는 모든 필요한 매체 장치를 확보하고 카메라 인스턴스를 생성하면 true 를 반환하며, 그렇지 않으면 어떤 장치도 확보하지 않거나 이미 확보한 장치를 모두 해제한 뒤 false 를 반환합니다.",
      "quote_id": "handler:0",
      "covers": [
        "integration"
      ],
      "kind": "behavior"
    },
    {
      "text": "상태를 변경하는 함수들은 일반적으로 Camera 클래스에 의해 서로 동기화되지 않으므로, 호출자가 필요한 경우 자체적으로 동기화를 보장해야 합니다.",
      "quote_id": "camera:0",
      "covers": [
        "integration"
      ],
      "kind": "behavior"
    },
    {
      "text": "PipelineHandler::match() 함수는 CameraManager 스레드에서 호출됩니다.",
      "quote_id": "handler:0",
      "covers": [
        "integration"
      ],
      "kind": "behavior"
    }
  ]
}
