---
generated_at: 2026-09-20T14:07:03+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: ok
section: ipa
---

# IPA 관리와 구현 진입점

**IPA 관리자, 모듈, 프록시와 IPU3·RKISP1 구현의 근거 위치를 먼저 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 관련 클래스 절을 확인합니다. | [관련 클래스](#관련-클래스) |
| 구조 설명 절을 확인합니다. | [구조 설명](#구조-설명) |

## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::IPAManager` | `include/libcamera/internal/ipa_manager.h:29` | – | 확인 필요 |
| `libcamera::IPAModule` | `include/libcamera/internal/ipa_module.h:21` | `libcamera::Loggable` | 확인 필요 |
| `libcamera::IPAProxy` | `include/libcamera/internal/ipa_proxy.h:22` | `libcamera::IPAInterface` | 확인 필요 |
| `libcamera::ipa::ipu3::IPAIPU3` | `src/ipa/ipu3/ipu3.cpp:139` | `libcamera::ipa::ipu3::IPAIPU3Interface`, `libcamera::ipa::ipu3::Module` | The IPU3 IPA implementation |
| `libcamera::ipa::rkisp1::IPARkISP1` | `src/ipa/rkisp1/rkisp1.cpp:46` | `libcamera::ipa::rkisp1::IPARkISP1Interface`, `libcamera::ipa::rkisp1::Module` | 확인 필요 |

## 구조 설명

IPA 관리와 구현 진입점을 분석하기 위해 `libcamera::IPAManager` 클래스의 생성자 및 파싱 메서드를 먼저 확인해야 합니다. `IPAManager`는 `src/libcamera/ipa_manager.cpp:107` 에서 인스턴스가 생성되고, `src/libcamera/ipa_manager.cpp:175` 의 `parseDir()` 를 통해 공유 라이브러jeti 객체를 식별하며, `src/libcamera/ipa_manager.cpp:224` 의 `addDir()` 를 호출하여 디렉토리에서 IPA 모듈을 로드합니다. 이 과정에서 `src/libcamera/ipa_manager.cpp:254` 의 `module()` 메서드는 파이프라인 핸들러에 맞는 IPA 모듈을 검색하고, `src/libcamera/ipa_manager.cpp:289` 의 `isSignatureValid()` 는 서명 유효성을 검증합니다.

알고리즘과 프록시 간의 경계를 명확히 하기 위해 `libcamera::IPAModule` 과 `libcamera::IPAProxy` 클래스의 초기화 및 인터페이스 생성 메서드를 확인해야 합니다. `IPAModule` 은 `src/libcamera/ipa_module.cpp:406` 의 `load()` 를 통해 공유 객체에서 구현 팩토리를 로드하고, `src/libcamera/ipa_module.cpp:451` 의 `createInterface()` 를 호출하여 IPA 인터페이스를 인스턴스화합니다. 반면 `libcamera::IPAProxy` 는 `src/libcamera/ipa_proxy.cpp:217` 의 `resolvePath()` 를 통해 프로세스 워커의 유효한 전체 경로를 찾습니다. 구체적인 스레드 동기화나 콜백 전달 순서는 설계 근거가 부족하므로 확인이 필요합니다.

??? note "근거와 검토 정보"
    - 근거 파일: `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/ipa_module.h`, `include/libcamera/internal/ipa_proxy.h`, `src/ipa/ipu3/ipu3.cpp`, `src/ipa/rkisp1/rkisp1.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/ipa_module.cpp`, `src/libcamera/ipa_proxy.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 인용 검증: 통과
    - 검토: 2026-09-20 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
