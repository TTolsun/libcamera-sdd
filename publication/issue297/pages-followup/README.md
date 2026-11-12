# #297 요청 진단과 정지 경계

[요청 수명 문서](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html)의 해당 그림 바로 아래에 요청 준비 300ms, 마지막 버퍼 뒤 명시적 요청 완료, FIFO 앱 반환, 공개 stop 계약을 표시했습니다. [정지 시나리오](https://ttolsun.github.io/libcamera-sdd/scenarios/camera_stop.html)에는 공통 stop의 큐 검사와 순번 초기화를 표시했습니다. 한국어와 영어 캡션은 해당 코드 행에 연결됩니다.

- 공식 libcamera 소스 `da6a6ed33ed0ab305f10b6f8b44736150d39cef4`의 기존 facts와 원고를 검증했습니다. [생성기 PR #310](https://github.com/TTolsun/camera-hal-sdd-generator/pull/310)의 예제 설정을 적용했습니다.
- 배포 기준은 `1055eaef9ed6fb70ece4279746e55a4bb1bff03b981b8b1c9c71eaf849410272`이고 후보 빌드는 `48c4f23e4b9c3246b3d365d07ddbf032944450cf5a133e3dcec1824b248055d3`입니다. 한영 HTML 62개, 내부 링크, 루트 산출물 487개와 ColourTemperature 하위 사이트를 검증했습니다.
- 변경된 시각화 20개를 별도로 대조했고 800개는 기존 판정을 재사용했습니다. 사람 검토 상태는 대기 중입니다. [검토 장부](visual-review-ledger.json.gz)를 압축 해제한 SHA-256은 `5db550f1e26ca33261d88cfd4f2fb57e4dc58b43a29155f0753612803ffac667`입니다.
- 기존 계약 보고서의 원본 CLI 영수증을 검증할 수 있는 `13facb30acde25ba0151af1474a4f683dee64b03` 렌더러로 조립했습니다. 병합된 생성기의 사이트 검증 명령으로 출력을 검사합니다.

[이슈 #297](https://github.com/TTolsun/camera-hal-sdd-generator/issues/297) · [이슈 #252](https://github.com/TTolsun/camera-hal-sdd-generator/issues/252)
