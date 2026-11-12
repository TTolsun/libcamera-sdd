# #297 Q1 요청과 버퍼 재사용

- [재사용 버퍼의 요청 연결](https://ttolsun.github.io/libcamera-sdd/camera-requests.html#재사용-버퍼의-요청-연결)에 기본 reuse()가 버퍼 연결을 비우므로 addBuffer()로 다시 붙인 뒤 제출해야 한다고 설명했습니다. [버퍼 맵을 비우는 코드](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/request.cpp#L397)
- [버퍼 재사용과 펜스 권고](https://ttolsun.github.io/libcamera-sdd/camera-requests.html#버퍼-재사용과-펜스-권고)에 같은 요청을 ReuseBuffers로 재사용해도 타임아웃으로 펜스가 남았다면 releaseFence()로 회수한 뒤 제출해야 한다고 설명했습니다. [ReuseBuffers 분기](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/request.cpp#L391) · [타임아웃 펜스 회수 계약](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/request.cpp#L464)

직전 빌드 `c309e7f32999056fa193bcf74ebccea0f02b6153ed7b40b919d6e86a5dd2fe51`에서 `88085a48ac9044679dacde915b41f220c8db014ce5db1c7b3e2a0a02b7ed5040`로 갱신했습니다. 시각화 812개는 기존 판정을 유지했고, 영향을 받은 한영 8개만 다시 검토했습니다. 한영 HTML 62개와 내부 링크를 검증했습니다. 사람 검토는 대기 상태입니다.

[검토 장부](visual-review-ledger.json.gz)를 압축 해제한 바이트의 SHA-256은 `ec10a80989af9de409bc389128261442941a7804bb64283b39d2c6f71032644f`입니다.
