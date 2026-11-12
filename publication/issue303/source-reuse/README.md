# 소스 갱신과 시각화 판정 재사용

공식 libcamera 분석 기준을 `c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78`에서 `da6a6ed33ed0ab305f10b6f8b44736150d39cef4`로 갱신했습니다. IMX832 튜닝과 등록, ColourTemperature 제어 방향 변경을 포함합니다. 두 공식 커밋의 차이는 [upstream 비교](https://gitlab.freedesktop.org/camera/libcamera/-/compare/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78...da6a6ed33ed0ab305f10b6f8b44736150d39cef4)에서 확인할 수 있습니다.

- Meson 번역 단위 295개를 추출했습니다. 원고 29개의 본문과 번역 2,245개의 내용이 같았습니다. 현재 근거에 연결한 계약 대조 151개 배치는 원본 CLI 영수증을 재검증했습니다.
- 실제 이전 Pages 빌드 `536c8d5d6919b6bff1315e211caf7a576d93f97c692a29250e348790990e3fa9`의 장부와 최종 한영 HTML을 대조했습니다. 시각화 820개에서 본문·그림·근거가 같은 사실을 확인해 원래 판정과 검토 기록을 이월했습니다. 새로 검토할 항목은 0개였습니다. 회귀 시험에서는 파일·로컬 발췌·본문·Mermaid가 바뀌면 해당 항목을 보류했습니다.
- [비교 근거](comparison.json.gz)는 확인한 Git 파일과 양쪽 커밋을 기록합니다. [이월 장부](visual-review-ledger.json.gz)의 압축을 해제한 SHA-256은 `ab5b3f975e2359d5fb4da9ceade310b3c424f6a9f445ca939b1f832ee24ba6fe`입니다. [독립 Terra High 검토](independent-review.json)는 비교 구현과 확인 범위를 기록합니다. 사람 검토 상태는 대기 중입니다.
- 루트 SDD를 조립한 생성기 커밋은 `13facb30acde25ba0151af1474a4f683dee64b03`입니다. 계약 대조 원본을 검증한 이 조립 환경을 고정했습니다. 병행 PR #110의 [ColourTemperature 문서](https://ttolsun.github.io/libcamera-sdd/upstream/colour-temperature/colour-temperature.html)는 별도 manifest로 검증했습니다.
- 정식 발행 검사를 거친 build ID는 `1055eaef9ed6fb70ece4279746e55a4bb1bff03b981b8b1c9c71eaf849410272`입니다. 한영 HTML 62개와 산출물 487개의 manifest 해시, 내부 링크를 검증했습니다.

[생성기 PR #308](https://github.com/TTolsun/camera-hal-sdd-generator/pull/308) · [이슈 #303](https://github.com/TTolsun/camera-hal-sdd-generator/issues/303)
