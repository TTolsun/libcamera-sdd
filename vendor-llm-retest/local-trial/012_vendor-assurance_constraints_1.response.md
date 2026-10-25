{
  "statements": [
    {
      "text": "`CameraConfiguration::validate()` 함수는 카메라 설정을 가장 가까운 유효한 상태로 조정하고 검증 상태를 반환하며, 이 과정에서 스트림 파라미터가 변경되거나 스트림 구성이 제거될 수 있습니다.",
      "quote_id": "validate:0",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "검증 결과가 `CameraConfiguration::Adjusted`인 경우 호출자는 반드시 조정된 설정을 다시 확인해야 하며, 파라미터 변경 사항이나 제거된 스트림에 대한 주의가 필요합니다.",
      "quote_id": "validate:0",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::generateConfiguration()` 함수는 호출자가 지정한 `roles`를 기반으로 기본 카메라 설정을 생성하며, 요청된 역할이 충족될 경우 유효한 설정을 반환하고 그렇지 않으면 null 포인터를 반환합니다.",
      "quote_id": "configuration:0",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`generateConfiguration()` 함수는 어떤 스레드에서든 호출될 수 있으며, 파이프라인 핸들러의 카메라 상태를 수정하지 않는 스레드 안전성을 보장합니다.",
      "quote_id": "configuration:0",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::configure()` 함수는 `CameraConfiguration::validate()`로 검증된 설정을 사용하여 스트림 그룹을 구성하며, 파이프라인 핸들러 구현체는 추가 검증을 수행하지 않습니다.",
      "quote_id": "configuration:1",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`configure()` 함수는 성공 시 0을 반환하고 실패 시 음수 오류 코드를 반환하며, 호출자는 이 반환 값을 통해 설정 적용 결과를 확인해야 합니다.",
      "quote_id": "configuration:1",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`configure()` 함수는 `CameraManager` 스레드에서 호출되며, 설정 적용 시 각 `StreamConfiguration` 항목에 해당하는 `Stream` 인스턴스를 연결합니다.",
      "quote_id": "configuration:1",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::exportFrameBuffers()` 함수는 프레임 버퍼를 내보내는 역할을 수행하며, 구체적인 동작은 해당 함수의 구현에 따라 결정됩니다.",
      "quote_id": "configuration:2",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    }
  ]
}
