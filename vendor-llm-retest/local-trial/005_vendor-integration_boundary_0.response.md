{
  "statements": [
    {
      "text": "`PipelineHandler::match()` 함수는 시스템에서 발견된 모든 미디어 장치를 제공받는 `DeviceEnumerator`를 통해 해당 파이프라인에 필요한 장치를 모두 확보해야 합니다.",
      "quote_id": "handler:0",
      "covers": ["boundary"],
      "kind": "behavior"
    },
    {
      "text": "모든 필요한 미디어 장치가 `MediaDevice::acquire()` 호출을 통해 확보되면, 해당 함수는 내부적으로 대응하는 카메라 인스턴스를 생성하고 이를 카메라 매니저에 등록한 뒤 참 값을 반환해야 합니다.",
      "quote_id": "handler:0",
      "covers": ["boundary"],
      "kind": "behavior"
    },
    {
      "text": "반면, 파이프라인 처리에 필요한 모든 미디어 장치를 찾지 못하면 해당 함수는 어떤 미디어 장치도 확보하지 않거나 이미 확보한 장치를 `MediaDevice::release()`로 모두 해제해야 합니다.",
      "quote_id": "handler:0",
      "covers": ["boundary"],
      "kind": "behavior"
    },
    {
      "text": "장치 매칭이 실패한 경우 `PipelineHandler::match()` 함수는 거짓 값을 반환하며, 카메라 인스턴스 생성이나 등록 작업은 수행하지 않습니다.",
      "quote_id": "handler:0",
      "covers": ["boundary"],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::match()` 함수는 카메라 매니저 스레드에서 호출되며, 각 파이프라인 인스턴스마다 한 번씩 생성되어 매칭 작업을 수행합니다.",
      "quote_id": "handler:0",
      "covers": ["boundary"],
      "kind": "behavior"
    }
  ]
}
