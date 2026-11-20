# 마지막 버퍼 이후 요청 완료 통지 진단

기준 Pages 빌드는 `d1069be92ef26b1085c3dad1dfebc3b9721325d5b78f57e9eb9cf258d82d7ca0`입니다. 기준과 변경 후보는 모두 libcamera `da6a6ed33ed0ab305f10b6f8b44736150d39cef4`를 분석합니다. 공식 upstream은 `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`까지 미러에 반영했습니다. 두 커밋 사이에 아래 요청 구현과 UVC·신호 전달 코드의 변경이 없음을 확인했습니다. 이 발행의 분석 전체는 기존 고정 커밋으로 유지합니다. [기준 배포](https://github.com/TTolsun/libcamera-sdd/actions/runs/44756509874) · [공식 미러 동기화](https://github.com/TTolsun/libcamera-sdd/actions/runs/44761768596)

| 조사 경계 | 확인한 위치와 값 |
| --- | --- |
| 같은 요청 | `doQueueRequest()`의 큐 등록 및 요청 시퀀스 할당을 카메라·실행·제출 세대와 연결합니다. `Request::reuse()`를 거치면 같은 객체 주소와 cookie를 다시 볼 수 있습니다. |
| 마지막 버퍼 | `PipelineHandler::completeBuffer()`가 버퍼 신호를 발생시킨 뒤 내부 추적을 갱신합니다. 반환값 `true`에서 모든 버퍼가 끝났음을 확인합니다. |
| 사례 A | 관측 구간·경로가 충분한데 같은 제출의 `completeRequest()` 진입이 없습니다. 처리한 핸들러의 콜백과 이후 완료 호출 조건을 확인합니다. |
| 사례 B | `complete()` 뒤 대상은 `RequestComplete`입니다. 앞선 선두가 `RequestPending`이고 같은 큐 처리에서 `break`가 실행됩니다. 선두의 남은 버퍼와 완료 경로를 확인합니다. |
| 앱 통지 | 대상의 `Camera::requestComplete(req)` 전달을 확인한 뒤 `requestCompleted.emit(request)`와 앱 슬롯 진입을 별도 기록합니다. |

이 값은 소스에서 구성한 조사 사례입니다. 앱과 실기기에서 두 사례를 재현하는 실행은 수행하지 않았습니다. 기존 실험 기록과 사람 검토 상태는 그대로 유지했습니다.

- [큐 등록, 마지막 버퍼 및 FIFO 반환](https://github.com/TTolsun/libcamera-sdd/blob/da6a6ed33ed0ab305f10b6f8b44736150d39cef4/src/libcamera/pipeline_handler.cpp#L483-L605)
- [버퍼 추적과 요청 상태 갱신](https://github.com/TTolsun/libcamera-sdd/blob/da6a6ed33ed0ab305f10b6f8b44736150d39cef4/src/libcamera/request.cpp#L103-L136)
- [재사용](https://github.com/TTolsun/libcamera-sdd/blob/da6a6ed33ed0ab305f10b6f8b44736150d39cef4/src/libcamera/request.cpp#L375-L402) · [요청 시퀀스](https://github.com/TTolsun/libcamera-sdd/blob/da6a6ed33ed0ab305f10b6f8b44736150d39cef4/src/libcamera/request.cpp#L533-L554)
- [카메라 요청 완료 신호](https://github.com/TTolsun/libcamera-sdd/blob/da6a6ed33ed0ab305f10b6f8b44736150d39cef4/src/libcamera/camera.cpp#L1475-L1489) · [Signal 연결 방식](https://github.com/TTolsun/libcamera-sdd/blob/da6a6ed33ed0ab305f10b6f8b44736150d39cef4/src/libcamera/base/bound_method.cpp#L22-L110)

진단 절의 맨 앞에 소스 발췌와 연결한 결정도 및 분기표를 배치했습니다. 벤더 연동과 파이프라인의 기존 요청 완료 절에는 증상을 그대로 보여 주는 링크를 추가했습니다. 두 원인이 성립하는 최소 관측값을 새 그림에서 비교하고, 이어지는 기존 그림에서 완료 호출과 반환 순서의 상세를 확인할 수 있습니다.

한국어와 영어 진단 원고에 Codex CLI `gpt-6.1-terra` / `high`를 사용했습니다. 별도 검토가 지적한 FIFO 분기 조건을 반영했습니다. 기준본 과업과 독립 근거 대조 기록을 동봉합니다. 일반적인 큐 순서, 완료·취소 상태와 앱 신호 전달에 해당하는 고정 소스 창을 검토했습니다. 다른 파이프라인과 사내 HAL의 구현 및 실행 검증은 이 기록의 범위 밖입니다.
