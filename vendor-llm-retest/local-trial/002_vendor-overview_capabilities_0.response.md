{
  "statements": [
    {
      "text": "`Camera` 클래스는 단일 이미지 소스에서 하나 이상의 이미지 스트림을 생성할 수 있는 카메라 장치를 모델링합니다.",
      "quote_id": "camera:0",
      "covers": ["capabilities"],
      "kind": "behavior"
    },
    {
      "text": "이 `Camera` 클래스는 장치를 구성하고 제어하며 이미지 스트림을 캡처하는 데 사용되는 주요 인터페이스 역할을 합니다.",
      "quote_id": "camera:0",
      "covers": ["capabilities"],
      "kind": "behavior"
    },
    {
      "text": "`libcamera` 가 제공하는 중앙 객체인 `Camera` 인스턴스는 `create()` 함수를 사용하여 반환되는 `std::shared_ptr` 로 관리됩니다.",
      "quote_id": "camera:0",
      "covers": ["capabilities"],
      "kind": "behavior"
    },
    {
      "text": "`libcamera` 가 지원하는 각 파이프라인은 미디어 장치 집합에서 작동하는 파이프라인 핸들러 구현에 의해 뒷받침되어야 합니다.",
      "quote_id": "handler:0",
      "covers": ["capabilities"],
      "kind": "behavior"
    },
    {
      "text": "파이프라인 핸들러는 필요한 미디어 장치를 시스템에 존재하는 장치와 매칭하고, 모든 장치가 획득되면 해당하는 `Camera` 인스턴스를 생성합니다.",
      "quote_id": "handler:0",
      "covers": ["capabilities"],
      "kind": "behavior"
    },
    {
      "text": "각 파이프라인 핸들러의 하위 클래스는 `REGISTER_PIPELINE_HANDLER()` 매크로를 사용하여 `libcamera` 에 등록되어야 합니다.",
      "quote_id": "handler:0",
      "covers": ["capabilities"],
      "kind": "behavior"
    },
    {
      "text": "지원되는 하드웨어 범위는 특정 장치별 파이프라인 핸들러 구현의 존재 여부에 달려 있으며, 성능 수치나 지원 기종은 추정이 불가능합니다.",
      "quote_id": "handler:0",
      "covers": ["capabilities"],
      "kind": "limitation"
    },
    {
      "text": "`Camera` 인스턴스는 수동으로 생성되거나 파괴되지 않도록 `private` 로 된 생성자와 소멸자를 가지며, 이는 라이브러리가 관리하는 수명 주기의 일부입니다.",
      "quote_id": "camera:0",
      "covers": ["capabilities"],
      "kind": "behavior"
    }
  ]
}
