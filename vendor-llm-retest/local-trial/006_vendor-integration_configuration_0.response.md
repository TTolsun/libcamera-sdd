{
  "statements": [
    {
      "text": "`generateConfiguration()` 함수는 호출자가 제공한 스트림 역할 목록을 입력으로 받아 해당 카메라에 대한 기본 설정을 생성합니다.",
      "quote_id": "configuration:0",
      "covers": ["configuration"],
      "kind": "behavior"
    },
    {
      "text": "이 함수는 요청된 역할들을 모두 충족시킬 수 있으면 유효한 `CameraConfiguration` 객체를 반환하고, 그렇지 않으면 널 포인터를 반환합니다.",
      "quote_id": "configuration:0",
      "covers": ["configuration"],
      "kind": "behavior"
    },
    {
      "text": "`configure()` 함수는 호출자가 적용할 설정을 담은 `CameraConfiguration` 객체를 입력으로 받아 지정된 카메라의 스트림 그룹을 구성합니다.",
      "quote_id": "configuration:1",
      "covers": ["configuration"],
      "kind": "behavior"
    },
    {
      "text": "구현자는 `configure()` 호출 시 설정 내의 각 `StreamConfiguration` 항목에 대해 `setStream()` 함수를 사용하여 실제 스트림 인스턴스를 연결해야 합니다.",
      "quote_id": "configuration:1",
      "covers": ["configuration"],
      "kind": "behavior"
    },
    {
      "text": "`configure()` 함수는 성공하면 0을 반환하고, 실패할 경우 음수 오류 코드를 반환합니다.",
      "quote_id": "configuration:1",
      "covers": ["configuration"],
      "kind": "behavior"
    },
    {
      "text": "`generateConfiguration()` 함수는 어떤 스레드에서든 호출될 수 있으며, 파이프라인 핸들러의 카메라 상태를 변경하지 않아야 합니다.",
      "quote_id": "configuration:0",
      "covers": ["configuration"],
      "kind": "behavior"
    },
    {
      "text": "`configure()` 함수는 `CameraManager` 스레드에서 호출되며, 설정은 이미 `validate()`를 거친 유효한 것으로 간주됩니다.",
      "quote_id": "configuration:1",
      "covers": ["configuration"],
      "kind": "behavior"
    }
  ]
}
