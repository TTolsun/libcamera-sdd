# R-Car Gen4 빌드와 지원 조건

기존 [장치 연동 가이드](https://ttolsun.github.io/libcamera-sdd/device-integration.html#build-support)에 R-Car Gen4 파이프라인과 대응 RPPX1 IPA를 빌드하는 조건을 추가한다. [English](https://ttolsun.github.io/libcamera-sdd/en/device-integration.html#build-support)

| 확인한 항목 | 확인 범위 |
| --- | --- |
| 소스 버전 | 사이트의 구조 분석과 기존 원고는 `adfa719f`를 기준으로 한다. 이 절의 빌드·지원 자료는 `7ae183f5`에 고정했다. |
| 전체 구성 | Ubuntu WSL2 x86_64에서 Clang으로 모든 파이프라인과 RPPX1을 포함한 IPA 구성을 빌드했다. Ninja 412단계가 완료됐다. |
| R-Car 전용 구성 | 같은 소스에서 `-Dpipelines=rcar-gen4 -Dipas=rppx1`로 별도 빌드했다. Ninja 186단계가 완료됐고 링크한 `ipa_rppx1.so`를 확인했다. |
| 실기기 | 대상 보드의 커널·센서 조합에서 장치 탐색, 첫 촬영과 보정 품질은 확인하지 않았다. |

빌드 절을 기존 가이드에 추가하는 범위로 제한했다. upstream 동기화에서는 28커밋이 반영됐으며 전체 신규 버전에 대한 문서 범위 판단과 실기기 지원 판정은 미결이다. [공식 미러 동기화](https://github.com/TTolsun/libcamera-sdd/actions/runs/45845691019) · [고정 소스](https://github.com/TTolsun/libcamera-sdd/tree/7ae183f58d7c2ee8643f002560d3a616e2a77726) · [생성 설정과 근거](https://github.com/TTolsun/camera-hal-sdd-generator/pull/376)

독립 검토에서 빌드 성공과 보드에서의 초기화·촬영을 구분할 그림이 필요하다고 판정했다. 다섯 노드로 이 경계를 표시하고, 한국어와 영어에서 데스크톱 1366px와 모바일 390px 너비로 그림 렌더링·확대 및 본문 가로 넘침을 확인했다. [그림 설정](https://github.com/TTolsun/camera-hal-sdd-generator/pull/378)

원고 단계의 근거 검토와 독자판의 최종 그림 판정은 별도로 기록했다. 최종 한영 독자판 214개 항목 중 162개 지문이 동일했고 12개는 위치 이동만 확인했다. 달라진 40개는 독립 CLI로 다시 검토했다. 최종 자동 검사에서 미해결 항목은 0개다. [검증 기록](verification.json)
