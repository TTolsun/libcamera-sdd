# #297 Q1 요청 소유권과 객체 수명

[요청과 버퍼를 유지할 기간](https://ttolsun.github.io/libcamera-sdd/camera-requests.html#요청과-버퍼를-유지할-기간)에서 앱의 요청 소유권과 버퍼 참조·큐 인자의 수명 조건을 설명합니다. [요청 소유권](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/camera.cpp#L1254) · [버퍼 유지 책임](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/request.cpp#L447) · [큐에 포인터 전달](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/camera.cpp#L1377) · [포인터 인자 계약](https://github.com/TTolsun/libcamera-sdd/blob/c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78/src/libcamera/base/object.cpp#L269)

직전 빌드 `88085a48ac9044679dacde915b41f220c8db014ce5db1c7b3e2a0a02b7ed5040`에서 `536c8d5d6919b6bff1315e211caf7a576d93f97c692a29250e348790990e3fa9`로 갱신했습니다. 시각화 814개는 기존 판정을 유지했고, 영향을 받은 한영 6개만 다시 검토했습니다. 한영 HTML 62개와 내부 링크를 검증했습니다. 사람 검토는 대기 상태입니다.

[검토 장부](visual-review-ledger.json.gz)를 압축 해제한 바이트의 SHA-256은 `921b45edad24c24ddbd7d93e90795bb6951222c1b89e7c511b3e63a16028d0e9`입니다.
