{
  "statements": [
    {
      "text": "`PipelineHandler::stop` 함수는 모든 스트림의 캡처를 즉시 중단하고 대기 중인 요청을 취소합니다.",
      "quote_id": "stop:0",
      "covers": ["shutdown"],
      "kind": "behavior"
    },
    {
      "text": "이 함수는 먼저 `Camera::Private` 구조체에서 대기 중인 요청들을 임시로 가져와서 재큐잉을 방지합니다.",
      "quote_id": "stop:0",
      "covers": ["shutdown"],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::stopDevice` 함수는 캡처를 즉시 중단하고 처리 중인 요청들을 완료 상태로 만듭니다.",
      "quote_id": "stop:6",
      "covers": ["shutdown"],
      "kind": "behavior"
    },
    {
      "text": "공통 코드인 `PipelineHandler::stop` 는 하드웨어 구현에 의존하지 않고 대기 요청을 취소하고 시퀀스 번호를 초기화합니다.",
      "quote_id": "stop:5",
      "covers": ["shutdown"],
      "kind": "behavior"
    },
    {
      "text": "하드웨어별 `stopDevice` 구현은 캡처를 중단하고 대기 중인 요청을 완료 상태로 전환하는 구체적인 동작을 수행합니다.",
      "quote_id": "stop:1",
      "covers": ["shutdown"],
      "kind": "behavior"
    },
    {
      "text": "모든 요청이 취소되고 큐가 비어지면 `requestSequence_` 가 0 으로 초기화되어 새로운 캡처를 준비합니다.",
      "quote_id": "stop:5",
      "covers": ["shutdown"],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::stop` 은 `CameraManager` 스레드에서 호출되며, 모든 대기 요청을 즉시 취소하고 오류 상태로 완료합니다.",
      "quote_id": "stop:0",
      "covers": ["shutdown"],
      "kind": "behavior"
    }
  ]
}
