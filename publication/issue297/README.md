# #297 펜스 회수와 제출 회차

- [Q1 펜스 회수 그림](https://ttolsun.github.io/libcamera-sdd/camera-requests.html#타임아웃-뒤-펜스-회수)에서 펜스 회수를 버퍼 재사용의 선행 조건으로 표시합니다.
- [Q2 준비 대기와 재진입](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#준비-대기와-재진입을-좁히기)에서 앱이 논리적 제출 회차 표식을 만들고 API 시작·반환, 메시지 게시, 파이프라인 진입을 이어서 기록하는 방법을 설명합니다.

직전 공개 빌드는 `c92c121a77e3756c9a10d7813fe71bb517d70c1d020b501f8c56fc54222a63ea`입니다. 이번 빌드는 `abda2952c9e3e42f602aea0ca706f94172513efc863fdd1c8c61037aee673630`이며 두 빌드의 문서 근거는 같은 [libcamera 커밋](https://github.com/TTolsun/libcamera-sdd/tree/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78)을 사용합니다. 공개 upstream 미러는 `da6a6ed33ed0ab305f10b6f8b44736150d39cef4`까지 갱신했습니다.

전체 시각화 항목 820개 중 710개는 정확히 같은 지문을 유지했습니다. 98개는 절의 절대 위치만 달라 기존 판정을 이어갔습니다. 변경된 12개는 Codex CLI `gpt-6.1-terra` high로 독립 검토했습니다. 두 호출은 각각 29.719초·99,736토큰과 37.719초·208,010토큰을 사용했습니다. 입력과 출력을 합산했습니다. 문서 간 계약 151개는 기존 영수증과 다시 대조했습니다.

[발행 manifest](../../docs/site-manifest.json)의 `inputs.item_visual_reviews`는 [검토 장부](visual-review-ledger.json.gz)를 압축 해제한 바이트의 SHA-256인 `0013c8496abb62e1eb175728a1cb1f79dce1241eab05b900cf58d2945ca53b5a`입니다. 장부에는 변경된 위치의 재사용 근거와 원 검토 기록의 해시가 있습니다. 사람 검토 상태는 대기입니다.
