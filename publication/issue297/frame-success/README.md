# #297 Q1 프레임 데이터 사용 조건

[펜스 그림](https://ttolsun.github.io/libcamera-sdd/camera-requests.html#타임아웃-뒤-펜스-회수) 바로 아래에 버퍼 상태가 FrameSuccess일 때만 프레임 데이터를 사용하라는 문장을 추가했습니다. [고정 libcamera 소스](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/framebuffer.cpp#L42)의 42행에서 FrameSuccess의 데이터 유효성 계약을 확인할 수 있습니다.

직전 빌드 `abda2952c9e3e42f602aea0ca706f94172513efc863fdd1c8c61037aee673630`에서 `c309e7f32999056fa193bcf74ebccea0f02b6153ed7b40b919d6e86a5dd2fe51`로 갱신했습니다. 시각화 814개는 기존 판정을 유지했고 한영 변경 영향 항목 6개만 독립적으로 다시 검토했습니다. 한영 HTML 62개와 내부 링크를 검증했습니다. 사람 검토는 대기 상태입니다.

[검토 장부](visual-review-ledger.json.gz)를 압축 해제한 SHA-256은 `e7e4914e123cccbee9f4c8cfbb0059cd3fc723531f5a982f415412d50bcc3307`입니다.
