{
  "statements": [
    {
      "text": "`CameraConfiguration::validate()` 함수는 카메라 설정을 가장 가까운 유효한 상태로 조정하고 상태를 반환하며, 호출자는 `Adjusted` 상태가 되면 스트림 파라미터 변경이나 스트림 삭제가 발생했으므로 설정을 다시 확인해야 합니다.",
      "quote_id": "validate:0",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::generateConfiguration()` 함수는 호출자가 지정한 `roles` 목록에 따라 기본 설정을 생성하며, 하드웨어 지원 한계나 특정 해상도·동시 스트림 수·성능은 보장하지 않습니다.",
      "quote_id": "configuration:0",
      "covers": [
        "constraints"
      ],
      "kind": "limitation"
    },
    {
      "text": "`PipelineHandler::configure()` 함수는 `CameraConfiguration::validate()`로 검증된 입력을 받으며, 실패 시 음수 오류 코드를 반환하고 호출자는 성공 여부를 확인해야 합니다.",
      "quote_id": "configuration:1",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::configure()` 함수는 `CameraManager` 스레드에서 호출되며, 파이프라인 핸들러 구현체는 추가 검증을 수행하지 않고 커스텀 필드를 사용할 수 있습니다.",
      "quote_id": "configuration:1",
      "covers": [
        "constraints"
      ],
      "kind": "behavior"
    }
  ]
}
