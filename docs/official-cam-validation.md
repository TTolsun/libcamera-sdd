---
generated_at: 2026-11-20T20:07:34+00:00
source_commit: adfa719f8ed67d18fd8a0739fc088a1f8b9e7252
status: ok
section: official-cam-validation
generation_method: facts-and-llm
evidence_fingerprint: 80180d53a547764031945df73a08c757691223132e5cd4e0375fb79f0d5c4131
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "80180d53a547764031945df73a08c757691223132e5cd4e0375fb79f0d5c4131", "answers": {"conclusion": [{"text": "이번 기준 재현에서 기본 WSL 커널은 DMA-BUF 할당기를 노출하지 않았고, 공식 cam은 버퍼를 할당하지 못했습니다.", "evidence": ["product-official-cam-reader"], "covers": ["conclusion"], "kind": "behavior", "quote": "{\r\n  \"schema\": 1,\r\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\r\n  \"camera\": \"Virtual2\",\r\n  \"applied_configuration\": \"(0) 400x300-NV12/SMPTE170M\",\r\n  \"status\": \"observed-wsl-virtual-only\",\r\n  \"kernel\": \"6.18.33.2-microsoft-standard-WSL2-issue211\",\r\n  \"results\": [\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        434,\r\n        437\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 434,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        449,\r\n        452\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 449,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        464,\r\n        467\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 464,\r\n      \"allocations\": 4\r\n    }\r\n  ],\r\n  \"source_unmodified\": true,\r\n  \"allocator\": \"udmabuf built-in, /dev/udmabuf root-only; permissions unchanged\",\r\n  \"run_threads\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"callbacks\": [\r\n        437\r\n      ],\r\n      \"processed\": [\r\n        434\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"callbacks\": [\r\n        452\r\n      ],\r\n      \"processed\": [\r\n        449\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"callbacks\": [\r\n        467\r\n      ],\r\n      \"processed\": [\r\n        464\r\n      ]\r\n    }\r\n  ],\r\n  \"inferior_exit_codes\": [\r\n    0,\r\n    0,\r\n    0\r\n  ],\r\n  \"processed_sequences\": [\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ]\r\n  ],\r\n  \"dma_probe_events\": [\r\n    {\r\n      \"event\": \"provider-open\",\r\n      \"provider\": \"/dev/udmabuf\",\r\n      \"result\": 3,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"allocate\",\r\n      \"result\": 5,\r\n      \"errno\": 0,\r\n      \"backing_fd\": 4,\r\n      \"dmabuf_fd\": 5,\r\n      \"size\": 4096\r\n    },\r\n    {\r\n      \"event\": \"mmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"sync-start\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 3,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"cpu-access\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"bytes\": 4096,\r\n      \"checksum\": 522240\r\n    },\r\n    {\r\n      \"event\": \"sync-end\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 7,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"munmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-dmabuf\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-backing\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-provider\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    }\r\n  ],\r\n  \"pretrial_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"pretrial_udmabuf\": false,\r\n  \"pretrial_dmabuf_heaps\": false,\r\n  \"pretrial_provider_devices_present\": false,\r\n  \"kernel_trial_authorized_by_user\": true,\r\n  \"restored_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"restored_wslconfig_exists\": false,\r\n  \"matching_modules_installed\": false,\r\n  \"docker_during_trial\": \"stopped\",\r\n  \"unprivileged_run\": {\r\n    \"status\": \"failed\",\r\n    \"errno\": 13\r\n  },\r\n  \"observation_limits\": [\r\n    \"GDB breakpoints affect timing\",\r\n    \"No callback-return instruction observation\",\r\n    \"Cancellation branch not dynamically exercised; observed count 0 is not forced\"\r\n  ],\r\n  \"physical_dma\": \"not-validated\",\r\n  \"physical_camera\": \"not-run\",\r\n  \"production_application\": \"not-run\",\r\n  \"internal_hal\": \"not-run\",\r\n  \"human_review\": \"pending\",\r\n  \"raw_evidence\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/main/examples/libcamera/validation/issue211/runs/20261031-wsl-cam-3\",\r\n  \"official_allocator_observations\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"bfc0215112bb3a7e30cf66e2ce016dbcc3bd1ad7f7d3ba79d14c868d29417bd2\"\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"0529146d43e1f826240fa9790545e81b69b274dca8173d9da598add516320727\"\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"38433db15aa2928b1e6fe0f54293fd3b4ee34eb1b9b9d5e5b10526c89605d46a\"\r\n    }\r\n  ],\r\n  \"baseline_capture\": {\r\n    \"inferior_exit\": {\r\n      \"exit_code\": 1,\r\n      \"observation_failures\": []\r\n    },\r\n    \"errors\": [\r\n      \"[0:07:17.247127806] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"[0:07:17.258236285] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"Can't allocate buffers\"\r\n    ],\r\n    \"stdout_sha256\": \"2432d60d69ed6e496a45df1c3edac64e9296b1c77f5054a60aa9d40a75ae5bd1\",\r\n    \"stderr_sha256\": \"cdcfbb0f7b1d46f55b30b94e7a1de119dfcfb7ab937fbb18cda4be9397e8e32a\",\r\n    \"raw_url\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/580df5156da7066a60e16ff9b656253b1c17f0c0/examples/libcamera/validation/issue211/runs/20261031-runtime-negative/official-cam-debugger-before\"\r\n  },\r\n  \"source_measurement\": {\r\n    \"sha256\": \"6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1\",\r\n    \"url\": \"https://github.com/TTolsun/libcamera-sdd/blob/d36affef9b3a741581d1c5f0f4cd68425c5dbe15/publication/issue211/config/product-evidence/official-cam-observation.json\",\r\n    \"operation\": \"Exact projection of named original fields, no new runtime execution\"\r\n  }\r\n}", "part_id": "problem"}, {"text": "승인된 UDMABUF 시험 커널의 WSL 가상 파이프라인 시뮬레이션에서 수정하지 않은 공식 cam이 Virtual2 400x300 NV12로 세 독립 프로세스에서 실행되어, 각 실행의 3프레임 정상 완료와 udmabuf 할당 성공이 관측되었습니다. 별도 DMA-BUF 프로브에서는 CPU 접근 성공이 관측되었습니다. 시험 후 기본 커널로 원복되어 현재 상태 그대로는 이 시험을 재실행할 수 없습니다.", "evidence": ["product-official-cam-reader", "product-reproduction-procedure"], "covers": ["conclusion"], "kind": "behavior", "quote": "{\r\n  \"schema\": 1,\r\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\r\n  \"camera\": \"Virtual2\",\r\n  \"applied_configuration\": \"(0) 400x300-NV12/SMPTE170M\",\r\n  \"status\": \"observed-wsl-virtual-only\",\r\n  \"kernel\": \"6.18.33.2-microsoft-standard-WSL2-issue211\",\r\n  \"results\": [\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        434,\r\n        437\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 434,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        449,\r\n        452\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 449,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        464,\r\n        467\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 464,\r\n      \"allocations\": 4\r\n    }\r\n  ],\r\n  \"source_unmodified\": true,\r\n  \"allocator\": \"udmabuf built-in, /dev/udmabuf root-only; permissions unchanged\",\r\n  \"run_threads\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"callbacks\": [\r\n        437\r\n      ],\r\n      \"processed\": [\r\n        434\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"callbacks\": [\r\n        452\r\n      ],\r\n      \"processed\": [\r\n        449\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"callbacks\": [\r\n        467\r\n      ],\r\n      \"processed\": [\r\n        464\r\n      ]\r\n    }\r\n  ],\r\n  \"inferior_exit_codes\": [\r\n    0,\r\n    0,\r\n    0\r\n  ],\r\n  \"processed_sequences\": [\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ]\r\n  ],\r\n  \"dma_probe_events\": [\r\n    {\r\n      \"event\": \"provider-open\",\r\n      \"provider\": \"/dev/udmabuf\",\r\n      \"result\": 3,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"allocate\",\r\n      \"result\": 5,\r\n      \"errno\": 0,\r\n      \"backing_fd\": 4,\r\n      \"dmabuf_fd\": 5,\r\n      \"size\": 4096\r\n    },\r\n    {\r\n      \"event\": \"mmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"sync-start\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 3,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"cpu-access\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"bytes\": 4096,\r\n      \"checksum\": 522240\r\n    },\r\n    {\r\n      \"event\": \"sync-end\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 7,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"munmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-dmabuf\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-backing\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-provider\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    }\r\n  ],\r\n  \"pretrial_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"pretrial_udmabuf\": false,\r\n  \"pretrial_dmabuf_heaps\": false,\r\n  \"pretrial_provider_devices_present\": false,\r\n  \"kernel_trial_authorized_by_user\": true,\r\n  \"restored_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"restored_wslconfig_exists\": false,\r\n  \"matching_modules_installed\": false,\r\n  \"docker_during_trial\": \"stopped\",\r\n  \"unprivileged_run\": {\r\n    \"status\": \"failed\",\r\n    \"errno\": 13\r\n  },\r\n  \"observation_limits\": [\r\n    \"GDB breakpoints affect timing\",\r\n    \"No callback-return instruction observation\",\r\n    \"Cancellation branch not dynamically exercised; observed count 0 is not forced\"\r\n  ],\r\n  \"physical_dma\": \"not-validated\",\r\n  \"physical_camera\": \"not-run\",\r\n  \"production_application\": \"not-run\",\r\n  \"internal_hal\": \"not-run\",\r\n  \"human_review\": \"pending\",\r\n  \"raw_evidence\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/main/examples/libcamera/validation/issue211/runs/20261031-wsl-cam-3\",\r\n  \"official_allocator_observations\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"bfc0215112bb3a7e30cf66e2ce016dbcc3bd1ad7f7d3ba79d14c868d29417bd2\"\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"0529146d43e1f826240fa9790545e81b69b274dca8173d9da598add516320727\"\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"38433db15aa2928b1e6fe0f54293fd3b4ee34eb1b9b9d5e5b10526c89605d46a\"\r\n    }\r\n  ],\r\n  \"baseline_capture\": {\r\n    \"inferior_exit\": {\r\n      \"exit_code\": 1,\r\n      \"observation_failures\": []\r\n    },\r\n    \"errors\": [\r\n      \"[0:07:17.247127806] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"[0:07:17.258236285] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"Can't allocate buffers\"\r\n    ],\r\n    \"stdout_sha256\": \"2432d60d69ed6e496a45df1c3edac64e9296b1c77f5054a60aa9d40a75ae5bd1\",\r\n    \"stderr_sha256\": \"cdcfbb0f7b1d46f55b30b94e7a1de119dfcfb7ab937fbb18cda4be9397e8e32a\",\r\n    \"raw_url\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/580df5156da7066a60e16ff9b656253b1c17f0c0/examples/libcamera/validation/issue211/runs/20261031-runtime-negative/official-cam-debugger-before\"\r\n  },\r\n  \"source_measurement\": {\r\n    \"sha256\": \"6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1\",\r\n    \"url\": \"https://github.com/TTolsun/libcamera-sdd/blob/d36affef9b3a741581d1c5f0f4cd68425c5dbe15/publication/issue211/config/product-evidence/official-cam-observation.json\",\r\n    \"operation\": \"Exact projection of named original fields, no new runtime execution\"\r\n  }\r\n}", "part_id": "outcome"}], "virtual-principle": [{"text": "고정 libcamera 소스에서 virtual 파이프라인은 실제 센서 대신 소프트웨어 테스트 패턴이나 이미지 입력으로 가상 카메라를 에뮬레이션합니다. 선택한 Virtual2 설정은 400x300 lines 패턴을 공급합니다. 버퍼 할당이 성공하면 cam은 실제 DMA-BUF 버퍼를 요청에 붙여 전달을 준비합니다. NV12 형식에서는 CPU가 변환과 매핑된 버퍼 쓰기를 함께 시도합니다.", "evidence": ["virtual-purpose", "virtual2-config", "cam-request-buffers", "allocator-to-camera", "camera-export", "virtual-buffer-allocation", "pattern-frame"], "covers": ["virtual-principle"], "kind": "behavior", "quote": "# Virtual Pipeline Handler\n\nVirtual pipeline handler emulates fake external camera(s) for testing.\n\n## Parse config file and register cameras\n\n- A sample config file is located at `src/libcamera/pipeline/virtual/data/virtual.yaml`.\n- If libcamera is installed, the config file should be installed at\n  `share/libcamera/pipeline/virtual/virtual.yaml`.\n\n### Config File Format\n\nThe config file contains the information about cameras' properties to register.\nThe config file should be a yaml file with dictionary of the cameraIds\nassociated with their properties as top level. The default value will be applied\nwhen any property is empty.\n\nEach camera block is a dictionary, containing the following keys:\n- `supported_formats` (list of `VirtualCameraData::Resolution`, optional):\n  List of supported resolution and frame rates of the emulated camera\n    - `width` (`unsigned int`, default=1920): Width of the window resolution.\n      This needs to be even.\n    - `height` (`unsigned int`, default=1080): Height of the window resolution.\n    - `frame_rates` (list of `int`, default=`[30,60]` ): Range of the frame\n      rate (per second). If the list contains one value, it's the lower bound\n      and the upper bound. If the list contains two values, the first is the\n      lower bound and the second is the upper bound. No other number of values\n      is allowed.\n- `test_pattern` (`string`): Which test pattern to use as frames. The options\n  are \"bars\", \"lines\". Cannot be set with `frames`.\n  - The test patterns are \"bars\" which means color bars, and \"lines\" which means\n    diagonal lines.\n- `frames` (dictionary):\n  - `path` (`string`): Path to an image, or path to a directory of a series of\n    images. Cannot be set with `test_pattern`.\n    - The path to an image has \".jpg\" extension.\n    - The path to a directory ends with \"/\". The name of the images in the\n      directory are \"{n}.jpg\" with {n} is the sequence of images starting with 0.\n- `location` (`string`, default=\"front\"): The location of the camera. Support\n  \"Front\", \"Back\", and \"External\".\n- `model` (`string`, default=\"Unknown\"): The model name of the camera.\n\nCheck `data/virtual.yaml` as the sample config file.\n\n### Implementation", "part_id": "purpose"}, {"text": "패턴 생성기는 쓰기 동기화를 시도한 뒤 그 범위에서 버퍼의 쓰기용 매핑을 시도합니다.", "evidence": ["pattern-frame"], "covers": ["virtual-principle"], "kind": "behavior", "quote": "int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,\n\t\t\t\t\tconst FrameBuffer *buffer)\n{\n\t/*\n\t * \\todo Assume all planes are contiguous and mapped at different\n\t * offsets on the same fd. This holds true as long as the implementation\n\t * of DmaBufAllocator only allocates contiguous planes. If this will\n\t * change or a different allocator will be used then we need to create\n\t * one dma syncer for each non-contiguous plane.\n\t */\n\tDmaSyncer outDmaSyncer(buffer->planes()[0].fd,\n\t\t\t       DmaSyncer::SyncType::Write);\n\tMappedFrameBuffer mappedFrameBuffer(buffer,\n\t\t\t\t\t    MappedFrameBuffer::MapFlag::Write);\n\n\tconst auto &planes = mappedFrameBuffer.planes();\n\tconst Size &size = cfg.size;\n\tconst PixelFormatInfo &info = PixelFormatInfo::info(cfg.pixelFormat);\n\n\trotateLeft1Column<kARGBSize>(size, template_.get());\n\n\tint ret;\n\n\t/* Convert the template_ to the frame buffer */\n\tswitch (cfg.pixelFormat) {\n\tcase formats::NV12:\n\t\tret = libyuv::ARGBToNV12(template_.get(),\n\t\t\t\t\t size.width * kARGBSize,\n\t\t\t\t\t planes[0].data(), info.stride(size.width, 0),\n\t\t\t\t\t planes[1].data(), info.stride(size.width, 1),\n\t\t\t\t\t size.width, size.height);\n\t\tbreak;\n\n\tcase formats::YUV420:\n\t\tret = libyuv::ARGBToI420(template_.get(),\n\t\t\t\t\t size.width * kARGBSize,\n\t\t\t\t\t planes[0].data(), info.stride(size.width, 0),\n\t\t\t\t\t planes[1].data(), info.stride(size.width, 1),\n\t\t\t\t\t planes[2].data(), info.stride(size.width, 2),\n\t\t\t\t\t size.width, size.height);\n\t\tbreak;\n\n\tcase formats::ABGR8888:\n\tcase formats::XBGR8888:\n\t\tret = libyuv::ARGBCopy(template_.get(),\n\t\t\t\t       size.width * kARGBSize,\n\t\t\t\t       planes[0].data(), info.stride(size.width, 0),\n\t\t\t\t       size.width, size.height);\n\t\tbreak;\n\n\tdefault:\n\t\tLOG(Virtual, Error) << \"Unsupported format\";\n\t\treturn -1;\n\t}\n\n\tif (ret != 0)\n\t\tLOG(Virtual, Error) << \"Conversion failed with \" << ret;\n\n\treturn ret;\n}\n\nvoid ColorBarsGenerator::configure(", "part_id": "buffer"}, {"text": "가상 요청은 비동기로 전달되며 `VirtualCameraData::processRequest`는 목표 시각까지 기다린 뒤 패턴 작성을 시도합니다. 버퍼 메타데이터는 생성 실패를 FrameError로 표시하며, 버퍼 완료 신호를 받았다는 사실만으로 프레임 생성의 성공을 판단할 수 없습니다. 가상 파이프라인의 버퍼 완료 처리 경로에서는 모든 버퍼의 완료 여부를 나타내는 `completeBuffer`의 반환값이 true일 때만 `completeRequest`를 호출합니다. 완료된 요청은 차례가 되면 `requestCompleted`에 연결된 cam 콜백으로 전달되며, 앞선 요청이 미완료이면 뒤 요청의 통지는 보류됩니다.", "evidence": ["virtual-queue", "virtual-frame", "virtual-completion", "pipeline-completion", "camera-notification", "cam-signal-connection"], "covers": ["virtual-principle"], "kind": "behavior", "quote": "void VirtualCameraData::processRequest(Request *request,\n\t\t\t\t       uint64_t targetTimestamp)\n{\n\tconst auto targetTime = std::chrono::steady_clock::time_point{\n\t\tstd::chrono::nanoseconds(targetTimestamp)\n\t};\n\tstd::this_thread::sleep_until(targetTime);\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tbool found = false;\n\t\t/* map buffer and fill test patterns */\n\t\tfor (auto &streamConfig : streamConfigs_) {\n\t\t\tif (stream == &streamConfig.stream) {\n\t\t\t\tFrameMetadata &fmd = buffer->_d()->metadata();\n\n\t\t\t\tfmd.status = FrameMetadata::Status::FrameSuccess;\n\t\t\t\tfmd.sequence = streamConfig.seq++;\n\t\t\t\tfmd.timestamp = targetTimestamp;\n\n\t\t\t\tstd::span<const FrameBuffer::Plane> planes = buffer->planes();\n\t\t\t\tfor (const auto [i, p] : utils::enumerate(planes))\n\t\t\t\t\tfmd.planes()[i].bytesused = p.length;\n\n\t\t\t\tfound = true;\n\n\t\t\t\tif (streamConfig.frameGenerator->generateFrame(\n\t\t\t\t\t    stream->configuration(), buffer))\n\t\t\t\t\tfmd.status = FrameMetadata::Status::FrameError;\n\n\t\t\t\tbufferCompleted.emit(buffer);\n\t\t\t\tbreak;\n\t\t\t}\n\t\t}\n\t\tASSERT(found);\n\t}\n}\n\nvoid VirtualCameraData::processControls(", "part_id": "completion"}], "initial-preparation": [{"text": "기록된 단일 스트림과 출력 옵션 미요청 범위에서 cam은 버퍼를 할당해 각 초기 요청에 연결합니다. 모든 준비가 끝나야 카메라를 시작하며, 할당·요청 생성·버퍼 연결 중 오류가 나면 시작 전에 반환합니다.", "evidence": ["cam-preparation", "product-invocation-options"], "covers": ["initial-preparation"], "kind": "behavior", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();", "part_id": "prepare"}], "initial-submission": [{"text": "cam은 요청을 준비하고 카메라를 시작한 뒤 한도 안에서만 제출하며, 한도 도달 시 제출을 생략하고 0을 반환합니다. 실제 카메라 큐 API는 상태와 요청을 검사해 오류를 반환할 수 있고 성공하면 비동기 호출을 예약하며, 초기 제출 실패 시 cam은 카메라를 중지합니다.", "evidence": ["cam-request-buffers", "camera-queue"], "covers": ["initial-submission"], "kind": "behavior", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete(", "part_id": "start"}], "flow": [{"text": "`CameraSession::requestComplete`는 요청 상태가 `RequestCancelled`이면 반환하고, 그 밖에는 `callLater`로 `CameraSession::processRequest`를 이벤트 루프에 미룹니다. 이는 카메라 매니저 스레드를 막지 않기 위해서입니다.", "evidence": ["callback-and-processing"], "covers": ["flow"], "kind": "behavior", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;\n\n\t/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}\n\nvoid CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;\n\n\tconst Request::BufferMap &buffers = request->buffers();\n\n\t/*\n\t * Compute the frame rate. The timestamp is arbitrarily retrieved from\n\t * the first buffer, as all buffers should have matching timestamps.\n\t */\n\tuint64_t ts = buffers.begin()->second->metadata().timestamp;\n\tdouble fps = ts - last_;\n\tfps = last_ != 0 && fps ? 1000000000.0 / fps : 0.0;\n\tlast_ = ts;\n\n\tbool requeue = true;\n\n\tstd::stringstream info;\n\tinfo << ts / 1000000000 << \".\"\n\t     << std::setw(6) << std::setfill('0') << ts / 1000 % 1000000\n\t     << \" (\" << std::fixed << std::setprecision(2) << fps << \" fps)\";\n\n\tfor (const auto &[stream, buffer] : buffers) {\n\t\tconst FrameMetadata &metadata = buffer->metadata();\n\n\t\tinfo << \" \" << streamNames_[stream]\n\t\t     << \" seq: \" << std::setw(6) << std::setfill('0') << metadata.sequence\n\t\t     << \" bytesused: \";\n\n\t\tunsigned int nplane = 0;\n\t\tfor (const FrameMetadata::Plane &plane : metadata.planes()) {\n\t\t\tinfo << plane.bytesused;\n\t\t\tif (++nplane < metadata.planes().size())\n\t\t\t\tinfo << \"/\";\n\t\t}\n\t}\n\n\tif (sink_) {\n\t\tif (!sink_->processRequest(request))\n\t\t\trequeue = false;\n\t}\n\n\tstd::cout << info.str() << std::endl;\n\n\tif (printMetadata_) {\n\t\tconst ControlList &requestMetadata = request->metadata();\n\t\tfor (const auto &[key, value] : requestMetadata) {\n\t\t\tconst ControlId *id = controls::controls.at(key);\n\t\t\tstd::cout << \"\\t\" << id->name() << \" = \"\n\t\t\t\t  << value.toString() << std::endl;\n\t\t}\n\t}\n\n\t/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}\n\n\t/*\n\t * If the frame sink holds on the request, we'll requeue it later in the\n\t * complete handler.\n\t */\n\tif (!requeue)\n\t\treturn;\n\n\trequest->reuse(Request::ReuseBuffers);\n\tqueueRequest(request);\n}\n\nvoid CameraSession::sinkRelease(Request *request)", "part_id": "dispatch"}, {"text": "세 실제 실행 명령은 화면·파일 출력 옵션을 요청하지 않았습니다. 다른 출력 옵션을 선택한 동작은 이번 실행으로 검증하지 않았습니다.", "evidence": ["product-invocation-options"], "covers": ["flow"], "kind": "behavior", "quote": "{\n  \"schema\": 1,\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\n  \"historical_archive\": \"publication/issue211/cli-evidence.zip\",\n  \"archive_sha256\": \"df8a735a121fa601779647c3b244a6ae0e36018c798659df171c24c760224682\",\n  \"records\": [\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-1/record.json\",\n      \"sha256\": \"4e04b252fd5db261b194972f010fa60d1708368e8ac99ebdb36c385432ff40d6\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-2/record.json\",\n      \"sha256\": \"939672fe872e010b599895b3b17daf4638a40335762f0a211c4ef37cb070ffee\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-3/record.json\",\n      \"sha256\": \"292d5fceea0148bb33a7c47a7cdc2554f2dc18bbd116064211f993ae15ebe0fd\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    }\n  ],\n  \"output_sink_options_requested\": false,\n  \"scope\": \"Observed command options; source inspection of CameraSession::start selects output sinks only through display, SDL or file options. Not a new runtime observation of sink_.\",\n  \"new_runtime\": false\n}", "part_id": "invocation-scope"}, {"text": "`processRequest`가 호출될 때 처리 한도가 설정되어 있고 처리 수가 이미 한도에 도달했다면, `captureDone`을 다시 내지 않고 즉시 반환하여 후속 프레임 처리를 건너뜁니다.", "evidence": ["callback-and-processing"], "covers": ["flow"], "kind": "behavior", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;\n\n\t/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}\n\nvoid CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;\n\n\tconst Request::BufferMap &buffers = request->buffers();\n\n\t/*\n\t * Compute the frame rate. The timestamp is arbitrarily retrieved from\n\t * the first buffer, as all buffers should have matching timestamps.\n\t */\n\tuint64_t ts = buffers.begin()->second->metadata().timestamp;\n\tdouble fps = ts - last_;\n\tfps = last_ != 0 && fps ? 1000000000.0 / fps : 0.0;\n\tlast_ = ts;\n\n\tbool requeue = true;\n\n\tstd::stringstream info;\n\tinfo << ts / 1000000000 << \".\"\n\t     << std::setw(6) << std::setfill('0') << ts / 1000 % 1000000\n\t     << \" (\" << std::fixed << std::setprecision(2) << fps << \" fps)\";\n\n\tfor (const auto &[stream, buffer] : buffers) {\n\t\tconst FrameMetadata &metadata = buffer->metadata();\n\n\t\tinfo << \" \" << streamNames_[stream]\n\t\t     << \" seq: \" << std::setw(6) << std::setfill('0') << metadata.sequence\n\t\t     << \" bytesused: \";\n\n\t\tunsigned int nplane = 0;\n\t\tfor (const FrameMetadata::Plane &plane : metadata.planes()) {\n\t\t\tinfo << plane.bytesused;\n\t\t\tif (++nplane < metadata.planes().size())\n\t\t\t\tinfo << \"/\";\n\t\t}\n\t}\n\n\tif (sink_) {\n\t\tif (!sink_->processRequest(request))\n\t\t\trequeue = false;\n\t}\n\n\tstd::cout << info.str() << std::endl;\n\n\tif (printMetadata_) {\n\t\tconst ControlList &requestMetadata = request->metadata();\n\t\tfor (const auto &[key, value] : requestMetadata) {\n\t\t\tconst ControlId *id = controls::controls.at(key);\n\t\t\tstd::cout << \"\\t\" << id->name() << \" = \"\n\t\t\t\t  << value.toString() << std::endl;\n\t\t}\n\t}\n\n\t/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}\n\n\t/*\n\t * If the frame sink holds on the request, we'll requeue it later in the\n\t * complete handler.\n\t */\n\tif (!requeue)\n\t\treturn;\n\n\trequest->reuse(Request::ReuseBuffers);\n\tqueueRequest(request);\n}\n\nvoid CameraSession::sinkRelease(Request *request)", "part_id": "processing"}, {"text": "`processRequest`는 프레임 정보를 출력하고 처리 수를 하나 늘립니다. `processRequest`는 설정된 한도에 도달하면 `captureDone` 신호를 내고 반환합니다.", "evidence": ["callback-and-processing"], "covers": ["flow"], "kind": "behavior", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;\n\n\t/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}\n\nvoid CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;\n\n\tconst Request::BufferMap &buffers = request->buffers();\n\n\t/*\n\t * Compute the frame rate. The timestamp is arbitrarily retrieved from\n\t * the first buffer, as all buffers should have matching timestamps.\n\t */\n\tuint64_t ts = buffers.begin()->second->metadata().timestamp;\n\tdouble fps = ts - last_;\n\tfps = last_ != 0 && fps ? 1000000000.0 / fps : 0.0;\n\tlast_ = ts;\n\n\tbool requeue = true;\n\n\tstd::stringstream info;\n\tinfo << ts / 1000000000 << \".\"\n\t     << std::setw(6) << std::setfill('0') << ts / 1000 % 1000000\n\t     << \" (\" << std::fixed << std::setprecision(2) << fps << \" fps)\";\n\n\tfor (const auto &[stream, buffer] : buffers) {\n\t\tconst FrameMetadata &metadata = buffer->metadata();\n\n\t\tinfo << \" \" << streamNames_[stream]\n\t\t     << \" seq: \" << std::setw(6) << std::setfill('0') << metadata.sequence\n\t\t     << \" bytesused: \";\n\n\t\tunsigned int nplane = 0;\n\t\tfor (const FrameMetadata::Plane &plane : metadata.planes()) {\n\t\t\tinfo << plane.bytesused;\n\t\t\tif (++nplane < metadata.planes().size())\n\t\t\t\tinfo << \"/\";\n\t\t}\n\t}\n\n\tif (sink_) {\n\t\tif (!sink_->processRequest(request))\n\t\t\trequeue = false;\n\t}\n\n\tstd::cout << info.str() << std::endl;\n\n\tif (printMetadata_) {\n\t\tconst ControlList &requestMetadata = request->metadata();\n\t\tfor (const auto &[key, value] : requestMetadata) {\n\t\t\tconst ControlId *id = controls::controls.at(key);\n\t\t\tstd::cout << \"\\t\" << id->name() << \" = \"\n\t\t\t\t  << value.toString() << std::endl;\n\t\t}\n\t}\n\n\t/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}\n\n\t/*\n\t * If the frame sink holds on the request, we'll requeue it later in the\n\t * complete handler.\n\t */\n\tif (!requeue)\n\t\treturn;\n\n\trequest->reuse(Request::ReuseBuffers);\n\tqueueRequest(request);\n}\n\nvoid CameraSession::sinkRelease(Request *request)", "part_id": "frame-work"}, {"text": "앞서 정한 출력 조건에서 처리 한도가 미설정이거나 처리 수가 아직 한도에 도달하지 않았으면 `CameraSession::processRequest`는 버퍼를 유지해 요청을 재사용하고 제출 도우미 `queueRequest`를 호출합니다.", "evidence": ["reuse-call", "product-invocation-options"], "covers": ["flow"], "kind": "behavior", "quote": "request->reuse(Request::ReuseBuffers);\n\tqueueRequest(request);", "part_id": "reuse-request"}, {"text": "처리 함수는 처리 수를, 제출 도우미는 제출 시도 수를 같은 캡처 한도 값과 서로 다른 시점에 비교합니다.", "evidence": ["callback-and-processing", "submission-limit"], "covers": ["flow"], "kind": "behavior", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;\n\n\t/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}\n\nvoid CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;\n\n\tconst Request::BufferMap &buffers = request->buffers();\n\n\t/*\n\t * Compute the frame rate. The timestamp is arbitrarily retrieved from\n\t * the first buffer, as all buffers should have matching timestamps.\n\t */\n\tuint64_t ts = buffers.begin()->second->metadata().timestamp;\n\tdouble fps = ts - last_;\n\tfps = last_ != 0 && fps ? 1000000000.0 / fps : 0.0;\n\tlast_ = ts;\n\n\tbool requeue = true;\n\n\tstd::stringstream info;\n\tinfo << ts / 1000000000 << \".\"\n\t     << std::setw(6) << std::setfill('0') << ts / 1000 % 1000000\n\t     << \" (\" << std::fixed << std::setprecision(2) << fps << \" fps)\";\n\n\tfor (const auto &[stream, buffer] : buffers) {\n\t\tconst FrameMetadata &metadata = buffer->metadata();\n\n\t\tinfo << \" \" << streamNames_[stream]\n\t\t     << \" seq: \" << std::setw(6) << std::setfill('0') << metadata.sequence\n\t\t     << \" bytesused: \";\n\n\t\tunsigned int nplane = 0;\n\t\tfor (const FrameMetadata::Plane &plane : metadata.planes()) {\n\t\t\tinfo << plane.bytesused;\n\t\t\tif (++nplane < metadata.planes().size())\n\t\t\t\tinfo << \"/\";\n\t\t}\n\t}\n\n\tif (sink_) {\n\t\tif (!sink_->processRequest(request))\n\t\t\trequeue = false;\n\t}\n\n\tstd::cout << info.str() << std::endl;\n\n\tif (printMetadata_) {\n\t\tconst ControlList &requestMetadata = request->metadata();\n\t\tfor (const auto &[key, value] : requestMetadata) {\n\t\t\tconst ControlId *id = controls::controls.at(key);\n\t\t\tstd::cout << \"\\t\" << id->name() << \" = \"\n\t\t\t\t  << value.toString() << std::endl;\n\t\t}\n\t}\n\n\t/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}\n\n\t/*\n\t * If the frame sink holds on the request, we'll requeue it later in the\n\t * complete handler.\n\t */\n\tif (!requeue)\n\t\treturn;\n\n\trequest->reuse(Request::ReuseBuffers);\n\tqueueRequest(request);\n}\n\nvoid CameraSession::sinkRelease(Request *request)", "part_id": "submission-limit"}, {"text": "이번 세 실행에서는 콜백과 후속 처리가 서로 다른 스레드에서 관측됐지만, 모든 실행에서 같은 배치를 보장하지는 않습니다. `requestComplete`에는 취소된 요청의 분기가 있지만, 이번 실행에서는 해당 분기를 동적으로 시험하지 않았습니다.", "evidence": ["product-invocation-official-cam-reader", "callback-and-processing"], "covers": ["flow"], "kind": "behavior", "quote": "{\r\n  \"schema\": 1,\r\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\r\n  \"camera\": \"Virtual2\",\r\n  \"applied_configuration\": \"(0) 400x300-NV12/SMPTE170M\",\r\n  \"status\": \"observed-wsl-virtual-only\",\r\n  \"kernel\": \"6.18.33.2-microsoft-standard-WSL2-issue211\",\r\n  \"results\": [\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        434,\r\n        437\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 434,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        449,\r\n        452\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 449,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        464,\r\n        467\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 464,\r\n      \"allocations\": 4\r\n    }\r\n  ],\r\n  \"source_unmodified\": true,\r\n  \"allocator\": \"udmabuf built-in, /dev/udmabuf root-only; permissions unchanged\",\r\n  \"run_threads\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"callbacks\": [\r\n        437\r\n      ],\r\n      \"processed\": [\r\n        434\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"callbacks\": [\r\n        452\r\n      ],\r\n      \"processed\": [\r\n        449\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"callbacks\": [\r\n        467\r\n      ],\r\n      \"processed\": [\r\n        464\r\n      ]\r\n    }\r\n  ],\r\n  \"inferior_exit_codes\": [\r\n    0,\r\n    0,\r\n    0\r\n  ],\r\n  \"processed_sequences\": [\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ]\r\n  ],\r\n  \"dma_probe_events\": [\r\n    {\r\n      \"event\": \"provider-open\",\r\n      \"provider\": \"/dev/udmabuf\",\r\n      \"result\": 3,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"allocate\",\r\n      \"result\": 5,\r\n      \"errno\": 0,\r\n      \"backing_fd\": 4,\r\n      \"dmabuf_fd\": 5,\r\n      \"size\": 4096\r\n    },\r\n    {\r\n      \"event\": \"mmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"sync-start\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 3,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"cpu-access\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"bytes\": 4096,\r\n      \"checksum\": 522240\r\n    },\r\n    {\r\n      \"event\": \"sync-end\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 7,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"munmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-dmabuf\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-backing\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-provider\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    }\r\n  ],\r\n  \"pretrial_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"pretrial_udmabuf\": false,\r\n  \"pretrial_dmabuf_heaps\": false,\r\n  \"pretrial_provider_devices_present\": false,\r\n  \"kernel_trial_authorized_by_user\": true,\r\n  \"restored_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"restored_wslconfig_exists\": false,\r\n  \"matching_modules_installed\": false,\r\n  \"docker_during_trial\": \"stopped\",\r\n  \"unprivileged_run\": {\r\n    \"status\": \"failed\",\r\n    \"errno\": 13\r\n  },\r\n  \"observation_limits\": [\r\n    \"GDB breakpoints affect timing\",\r\n    \"No callback-return instruction observation\",\r\n    \"Cancellation branch not dynamically exercised; observed count 0 is not forced\"\r\n  ],\r\n  \"physical_dma\": \"not-validated\",\r\n  \"physical_camera\": \"not-run\",\r\n  \"production_application\": \"not-run\",\r\n  \"internal_hal\": \"not-run\",\r\n  \"human_review\": \"pending\",\r\n  \"raw_evidence\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/main/examples/libcamera/validation/issue211/runs/20261031-wsl-cam-3\",\r\n  \"official_allocator_observations\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"bfc0215112bb3a7e30cf66e2ce016dbcc3bd1ad7f7d3ba79d14c868d29417bd2\"\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"0529146d43e1f826240fa9790545e81b69b274dca8173d9da598add516320727\"\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"38433db15aa2928b1e6fe0f54293fd3b4ee34eb1b9b9d5e5b10526c89605d46a\"\r\n    }\r\n  ],\r\n  \"baseline_capture\": {\r\n    \"inferior_exit\": {\r\n      \"exit_code\": 1,\r\n      \"observation_failures\": []\r\n    },\r\n    \"errors\": [\r\n      \"[0:07:17.247127806] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"[0:07:17.258236285] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"Can't allocate buffers\"\r\n    ],\r\n    \"stdout_sha256\": \"2432d60d69ed6e496a45df1c3edac64e9296b1c77f5054a60aa9d40a75ae5bd1\",\r\n    \"stderr_sha256\": \"cdcfbb0f7b1d46f55b30b94e7a1de119dfcfb7ab937fbb18cda4be9397e8e32a\",\r\n    \"raw_url\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/580df5156da7066a60e16ff9b656253b1c17f0c0/examples/libcamera/validation/issue211/runs/20261031-runtime-negative/official-cam-debugger-before\"\r\n  },\r\n  \"source_measurement\": {\r\n    \"sha256\": \"6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1\",\r\n    \"url\": \"https://github.com/TTolsun/libcamera-sdd/blob/d36affef9b3a741581d1c5f0f4cd68425c5dbe15/publication/issue211/config/product-evidence/official-cam-observation.json\",\r\n    \"operation\": \"Exact projection of named original fields, no new runtime execution\"\r\n  }\r\n}", "part_id": "observed"}], "reproduce": [{"text": "1. **준비 (1–3)** 호스트 상태를 바꾸지 않고 사용할 커널의 Kconfig와 의존 조건을 조사하세요.", "evidence": ["product-invocation-reproduction-procedure", "product-invocation-execution-contract"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "environment"}, {"text": "2. **DMA-BUF 할당기 선택:** 선택한 커널의 Kconfig, 의존성, 실제 사용 가능한 모듈과 할당기 후보를 조사하고 결과에 맞는 할당기 하나를 선택하세요. 이 기록과 같은 조건으로 재현하려면 udmabuf를 사용하세요.", "evidence": ["product-invocation-reproduction-procedure", "product-invocation-official-cam-reader", "product-invocation-execution-contract"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "providers"}, {"text": "3. 선택한 커널과 할당기에 필요한 모듈만 설치 여부와 커널 버전 일치를 조사하세요. 기록된 udmabuf 시험에서는 드라이버가 내장되어 있었고 별도 모듈을 설치하지 않았습니다.", "evidence": ["product-invocation-reproduction-procedure", "product-invocation-official-cam-reader"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "modules"}, {"text": "4. **호스트 변경 (4–5)** 변경안, 부팅할 커널과 이미지 SHA-256, 영향, 정확한 백업 경로, 부팅 및 복구 절차가 포함된 호스트 변경 계획에 대해 실행 직전에 별도 승인을 받으세요.", "evidence": ["product-invocation-reproduction-procedure"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "approval"}, {"text": "5. 승인된 계획에 따라 시험 커널을 설치하고 부팅하세요.", "evidence": ["product-invocation-reproduction-procedure"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "kernel-boot"}, {"text": "6. **실행 전 검사 (6–11)** 실행 중인 커널 버전이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지 확인하세요.", "evidence": ["product-invocation-reproduction-procedure"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "kernel-check"}, {"text": "7. WSL root 자식 컨텍스트에서 `/dev/udmabuf`을 열 수 있는 권한을 확인하세요.", "evidence": ["product-invocation-reproduction-procedure"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "access-check"}, {"text": "8. 사용할 Virtual2 YAML에서 크기 400x300과 패턴 값 lines를 하나의 구성 조합으로 대조하세요.", "evidence": ["virtual2-config"], "covers": ["reproduce"], "kind": "behavior", "quote": "\"Virtual2\":\n  supported_formats:\n  - width: 400\n    height: 300\n  test_pattern: \"lines\"", "part_id": "yaml-check"}, {"text": "9. 사용할 cam 명령의 카메라 선택 인자가 `Virtual2`인지 확인하세요.", "evidence": ["product-invocation-options"], "covers": ["reproduce"], "kind": "behavior", "quote": "{\n  \"schema\": 1,\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\n  \"historical_archive\": \"publication/issue211/cli-evidence.zip\",\n  \"archive_sha256\": \"df8a735a121fa601779647c3b244a6ae0e36018c798659df171c24c760224682\",\n  \"records\": [\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-1/record.json\",\n      \"sha256\": \"4e04b252fd5db261b194972f010fa60d1708368e8ac99ebdb36c385432ff40d6\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-2/record.json\",\n      \"sha256\": \"939672fe872e010b599895b3b17daf4638a40335762f0a211c4ef37cb070ffee\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-3/record.json\",\n      \"sha256\": \"292d5fceea0148bb33a7c47a7cdc2554f2dc18bbd116064211f993ae15ebe0fd\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    }\n  ],\n  \"output_sink_options_requested\": false,\n  \"scope\": \"Observed command options; source inspection of CameraSession::start selects output sinks only through display, SDL or file options. Not a new runtime observation of sink_.\",\n  \"new_runtime\": false\n}", "part_id": "camera-selection"}, {"text": "10. 사용할 cam 스트림 인자가 400x300 NV12를 요청하는지 확인하세요.", "evidence": ["product-invocation-options"], "covers": ["reproduce"], "kind": "behavior", "quote": "{\n  \"schema\": 1,\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\n  \"historical_archive\": \"publication/issue211/cli-evidence.zip\",\n  \"archive_sha256\": \"df8a735a121fa601779647c3b244a6ae0e36018c798659df171c24c760224682\",\n  \"records\": [\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-1/record.json\",\n      \"sha256\": \"4e04b252fd5db261b194972f010fa60d1708368e8ac99ebdb36c385432ff40d6\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-2/record.json\",\n      \"sha256\": \"939672fe872e010b599895b3b17daf4638a40335762f0a211c4ef37cb070ffee\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-3/record.json\",\n      \"sha256\": \"292d5fceea0148bb33a7c47a7cdc2554f2dc18bbd116064211f993ae15ebe0fd\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    }\n  ],\n  \"output_sink_options_requested\": false,\n  \"scope\": \"Observed command options; source inspection of CameraSession::start selects output sinks only through display, SDL or file options. Not a new runtime observation of sink_.\",\n  \"new_runtime\": false\n}", "part_id": "stream-request"}, {"text": "11. 실행할 공식 cam 명령에 3프레임을 요청하는 `--capture=3` 인자가 지정되어 있는지 확인합니다.", "evidence": ["product-invocation-options"], "covers": ["reproduce"], "kind": "behavior", "quote": "{\n  \"schema\": 1,\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\n  \"historical_archive\": \"publication/issue211/cli-evidence.zip\",\n  \"archive_sha256\": \"df8a735a121fa601779647c3b244a6ae0e36018c798659df171c24c760224682\",\n  \"records\": [\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-1/record.json\",\n      \"sha256\": \"4e04b252fd5db261b194972f010fa60d1708368e8ac99ebdb36c385432ff40d6\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-2/record.json\",\n      \"sha256\": \"939672fe872e010b599895b3b17daf4638a40335762f0a211c4ef37cb070ffee\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    },\n    {\n      \"archive_entry\": \"generator/issue211/runs/20261031-wsl-cam-3/cam-3/record.json\",\n      \"sha256\": \"292d5fceea0148bb33a7c47a7cdc2554f2dc18bbd116064211f993ae15ebe0fd\",\n      \"cam_arguments\": [\n        \"--camera\",\n        \"Virtual2\",\n        \"--capture=3\",\n        \"--stream\",\n        \"role=video,width=400,height=300,pixelformat=NV12\"\n      ],\n      \"exit_code\": 0\n    }\n  ],\n  \"output_sink_options_requested\": false,\n  \"scope\": \"Observed command options; source inspection of CameraSession::start selects output sinks only through display, SDL or file options. Not a new runtime observation of sink_.\",\n  \"new_runtime\": false\n}", "part_id": "capture-limit-check"}, {"text": "12. **실행·검증 (12–13)** 연결된 실행 절차에 따라 수정하지 않은 공식 cam을 세 독립 프로세스로 실행합니다.", "evidence": ["product-invocation-reproduction-procedure", "product-invocation-official-cam-reader"], "covers": ["reproduce"], "kind": "behavior", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "execution"}, {"text": "13. 새 실행의 증거를 카메라 Virtual2, 실제 적용 스트림 400x300 NV12, 각 독립 실행의 정상 3프레임 처리와 종료 코드 0이라는 기대 결과 조합과 대조하세요.", "evidence": ["product-invocation-official-cam-reader", "product-invocation-reproduction-procedure"], "covers": ["reproduce"], "kind": "behavior", "quote": "{\r\n  \"schema\": 1,\r\n  \"source_commit\": \"293d751a814e0d4c34e85ad457ccd9d5eefd1a61\",\r\n  \"camera\": \"Virtual2\",\r\n  \"applied_configuration\": \"(0) 400x300-NV12/SMPTE170M\",\r\n  \"status\": \"observed-wsl-virtual-only\",\r\n  \"kernel\": \"6.18.33.2-microsoft-standard-WSL2-issue211\",\r\n  \"results\": [\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        434,\r\n        437\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 434,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        449,\r\n        452\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 449,\r\n      \"allocations\": 4\r\n    },\r\n    {\r\n      \"completed_frames\": 3,\r\n      \"cancelled_callbacks\": 0,\r\n      \"observed_tids\": [\r\n        464,\r\n        467\r\n      ],\r\n      \"successful_buffer_sequences\": [\r\n        0,\r\n        1,\r\n        2\r\n      ],\r\n      \"pid\": 464,\r\n      \"allocations\": 4\r\n    }\r\n  ],\r\n  \"source_unmodified\": true,\r\n  \"allocator\": \"udmabuf built-in, /dev/udmabuf root-only; permissions unchanged\",\r\n  \"run_threads\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"callbacks\": [\r\n        437\r\n      ],\r\n      \"processed\": [\r\n        434\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"callbacks\": [\r\n        452\r\n      ],\r\n      \"processed\": [\r\n        449\r\n      ]\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"callbacks\": [\r\n        467\r\n      ],\r\n      \"processed\": [\r\n        464\r\n      ]\r\n    }\r\n  ],\r\n  \"inferior_exit_codes\": [\r\n    0,\r\n    0,\r\n    0\r\n  ],\r\n  \"processed_sequences\": [\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ],\r\n    [\r\n      0,\r\n      1,\r\n      2\r\n    ]\r\n  ],\r\n  \"dma_probe_events\": [\r\n    {\r\n      \"event\": \"provider-open\",\r\n      \"provider\": \"/dev/udmabuf\",\r\n      \"result\": 3,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"allocate\",\r\n      \"result\": 5,\r\n      \"errno\": 0,\r\n      \"backing_fd\": 4,\r\n      \"dmabuf_fd\": 5,\r\n      \"size\": 4096\r\n    },\r\n    {\r\n      \"event\": \"mmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"sync-start\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 3,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"cpu-access\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"bytes\": 4096,\r\n      \"checksum\": 522240\r\n    },\r\n    {\r\n      \"event\": \"sync-end\",\r\n      \"result\": 0,\r\n      \"errno\": 0,\r\n      \"flags\": 7,\r\n      \"retry\": false\r\n    },\r\n    {\r\n      \"event\": \"munmap\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-dmabuf\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-backing\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    },\r\n    {\r\n      \"event\": \"close-provider\",\r\n      \"result\": 0,\r\n      \"errno\": 0\r\n    }\r\n  ],\r\n  \"pretrial_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"pretrial_udmabuf\": false,\r\n  \"pretrial_dmabuf_heaps\": false,\r\n  \"pretrial_provider_devices_present\": false,\r\n  \"kernel_trial_authorized_by_user\": true,\r\n  \"restored_kernel\": \"6.18.33.2-microsoft-standard-WSL2\",\r\n  \"restored_wslconfig_exists\": false,\r\n  \"matching_modules_installed\": false,\r\n  \"docker_during_trial\": \"stopped\",\r\n  \"unprivileged_run\": {\r\n    \"status\": \"failed\",\r\n    \"errno\": 13\r\n  },\r\n  \"observation_limits\": [\r\n    \"GDB breakpoints affect timing\",\r\n    \"No callback-return instruction observation\",\r\n    \"Cancellation branch not dynamically exercised; observed count 0 is not forced\"\r\n  ],\r\n  \"physical_dma\": \"not-validated\",\r\n  \"physical_camera\": \"not-run\",\r\n  \"production_application\": \"not-run\",\r\n  \"internal_hal\": \"not-run\",\r\n  \"human_review\": \"pending\",\r\n  \"raw_evidence\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/main/examples/libcamera/validation/issue211/runs/20261031-wsl-cam-3\",\r\n  \"official_allocator_observations\": [\r\n    {\r\n      \"pid\": 434,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"bfc0215112bb3a7e30cf66e2ce016dbcc3bd1ad7f7d3ba79d14c868d29417bd2\"\r\n    },\r\n    {\r\n      \"pid\": 449,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"0529146d43e1f826240fa9790545e81b69b274dca8173d9da598add516320727\"\r\n    },\r\n    {\r\n      \"pid\": 464,\r\n      \"successful_allocations\": 4,\r\n      \"providers\": [\r\n        \"/dev/udmabuf\"\r\n      ],\r\n      \"exporters\": [\r\n        \"udmabuf\"\r\n      ],\r\n      \"raw_sha256\": \"38433db15aa2928b1e6fe0f54293fd3b4ee34eb1b9b9d5e5b10526c89605d46a\"\r\n    }\r\n  ],\r\n  \"baseline_capture\": {\r\n    \"inferior_exit\": {\r\n      \"exit_code\": 1,\r\n      \"observation_failures\": []\r\n    },\r\n    \"errors\": [\r\n      \"[0:07:17.247127806] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"[0:07:17.258236285] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider\",\r\n      \"Can't allocate buffers\"\r\n    ],\r\n    \"stdout_sha256\": \"2432d60d69ed6e496a45df1c3edac64e9296b1c77f5054a60aa9d40a75ae5bd1\",\r\n    \"stderr_sha256\": \"cdcfbb0f7b1d46f55b30b94e7a1de119dfcfb7ab937fbb18cda4be9397e8e32a\",\r\n    \"raw_url\": \"https://github.com/TTolsun/camera-hal-sdd-generator/tree/580df5156da7066a60e16ff9b656253b1c17f0c0/examples/libcamera/validation/issue211/runs/20261031-runtime-negative/official-cam-debugger-before\"\r\n  },\r\n  \"source_measurement\": {\r\n    \"sha256\": \"6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1\",\r\n    \"url\": \"https://github.com/TTolsun/libcamera-sdd/blob/d36affef9b3a741581d1c5f0f4cd68425c5dbe15/publication/issue211/config/product-evidence/official-cam-observation.json\",\r\n    \"operation\": \"Exact projection of named original fields, no new runtime execution\"\r\n  }\r\n}", "part_id": "results"}, {"text": "이 결과는 WSL 가상 카메라의 시뮬레이션 구성에만 해당하며, 물리 DMA·카메라·제품 앱·사내 HAL은 검증하지 않았습니다. GDB는 타이밍에 영향을 주므로 콜백 반환 명령과 성능은 검증하지 않았습니다.", "evidence": ["product-invocation-reproduction-procedure", "product-invocation-official-cam-reader"], "covers": ["reproduce"], "kind": "limitation", "quote": "# 공식 cam WSL 가상 카메라 검증\n\n## 결론과 다음 행동\n\n먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n\n## 관측된 결과\n\n소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.\n\n세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.\n\nDMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.\n\n`cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.\n\n## 범위와 한계\n\n이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.\n\n권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.\n\nGDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.\n\n## 실행 전 준비\n\n1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.\n2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.\n3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.\n4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.\n5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.\n\n```\nPYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>\n```\n\nCPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.", "part_id": "scope"}]}, "topic_inputs": {"conclusion": "4c375c4652d3793ad86ed309cecce1fe4951dd9edea2a05e25510f1a5d1fdc99", "virtual-principle": "3ee2290a065442c7be3d1be78c6994b296e120210fd2afe61590427f877a961e", "initial-preparation": "ca3ca965d0049aafddcbe5dbe6ce14f4b308c464cbb14775e25bb21783012808", "initial-submission": "1d9f8955dce245f291fc0b20f5de4f58258f44a61d6586a8b117cb22bb0d092d", "flow": "e1fbacd646dabadf485fafc586f8fa91950f355e0f6ed6461b7b00cdf3a39b5c", "reproduce": "5a1c6a63d4a11f387bb4c2d66ed87518bd1aa50cfab4bb0c47e910b5ffb6aec3"}, "reused_topics": ["conclusion", "virtual-principle", "initial-preparation", "initial-submission", "flow", "reproduce"], "replayed_units": [], "generated_topics": [], "topic_agents": {"conclusion": "cli/codex/gpt-6.1-terra", "virtual-principle": "cli/codex/gpt-6.1-terra", "initial-preparation": "cli/codex/gpt-6.1-terra", "initial-submission": "cli/codex/gpt-6.1-terra", "flow": "cli/codex/gpt-6.1-terra", "reproduce": "cli/codex/gpt-6.1-terra"}, "grounding_review": "not-run", "grounding_policy": null, "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "434377186c836fa9d0ea02f9e7b91f624da454b0602ec710fa2993ed69fe1e38", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "c6f80826ee5f2570b2928f47d7e5244913e552f139dfb3d5592402092884d46e", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "a4edf8364d73d169c3f10ecbadf487a8a4dc10328622d07578b281eae810c3aa"}, "validation_model": "ea8e8ebec2906ea5de47f3a9e67f91041ba4108062c0fcf14100de9b9d892487", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "reuse_lineage": {"source_commit": "adfa719f8ed67d18fd8a0739fc088a1f8b9e7252", "body_sha256": "df1a37e0f3a2092aaf62c6eb8ac0df54329e7e89dcdf75a32d6218a04998a413", "topics": ["conclusion", "virtual-principle", "initial-preparation", "initial-submission", "flow", "reproduce"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "dd25f45cf588828d24e18e9e06668ef5febad5e69da726e33f775c92b7daec70"}
generated_visuals: {"schema": 1, "records": {"submission-gate": {"input_fingerprint": "7297f178f3f55201faed6e52d07c15588d22368df418c34c4484e7ed6d28ed89", "draft": {"nodes": [{"id": "alloc_check", "symbol": "allocate", "label": "스트림 버퍼 할당 호출이 실패했는가?", "label_en": "Did the stream buffer allocation call fail?", "shape": "decision", "quote_ids": ["cam-preparation:1"]}, {"id": "err_return", "symbol": "allocate", "label": "오류 값을 반환하고 카메라 시작 전에 종료", "label_en": "Return the error value and end before camera start", "shape": "box", "quote_ids": ["cam-preparation:1", "cam-preparation:4", "cam-preparation:6"]}, {"id": "more_requests", "symbol": "nbuffers", "label": "할당된 최소 버퍼 수만큼 만들 초기 요청이 남았는가?", "label_en": "Requests left to make up to the minimum buffer count?", "shape": "decision", "quote_ids": ["cam-preparation:2", "cam-preparation:4", "cam-preparation:8"]}, {"id": "create_req", "symbol": "createRequest", "label": "요청 생성이 실패했는가?", "label_en": "Did request creation fail?", "shape": "decision", "quote_ids": ["cam-preparation:4"]}, {"id": "attach_buf", "symbol": "addBuffer", "label": "스트림 버퍼 i 연결에 실패했는가?", "label_en": "Failed to attach stream buffer i?", "shape": "decision", "quote_ids": ["cam-preparation:5", "cam-preparation:6"]}, {"id": "store_req", "symbol": "requests_", "label": "단일 스트림의 buffers[i]를 요청 i에 연결한 뒤 요청을 보관", "label_en": "Keep request i after attaching sole stream's buffers[i]", "shape": "process", "quote_ids": ["cam-preparation:5", "cam-preparation:7", "cam-preparation:8"]}, {"id": "ready_done", "symbol": "requests_", "label": "모든 초기 요청·버퍼 준비 완료, 카메라 시작 전 단계 종료", "label_en": "All initial requests and buffers ready before camera start", "shape": "process", "quote_ids": ["cam-preparation:8", "cam-preparation:10"]}], "edges": [{"from": "alloc_check", "to": "err_return", "label": "할당 오류", "label_en": "Alloc error", "condition_ref": "c2:true", "quote_ids": ["cam-preparation:1"]}, {"from": "alloc_check", "to": "more_requests", "label": "할당 성공", "label_en": "Alloc OK", "condition_ref": "c2:false", "quote_ids": ["cam-preparation:1", "cam-preparation:2", "cam-preparation:4"]}, {"from": "more_requests", "to": "create_req", "label": "남은 요청 있음", "label_en": "Requests left", "condition_ref": "always", "quote_ids": ["cam-preparation:4"]}, {"from": "more_requests", "to": "ready_done", "label": "남은 요청 없음", "label_en": "No requests left", "condition_ref": "always", "quote_ids": ["cam-preparation:4", "cam-preparation:8"]}, {"from": "create_req", "to": "err_return", "label": "생성 오류", "label_en": "Create error", "condition_ref": "c0:true", "quote_ids": ["cam-preparation:4", "cam-preparation:1"]}, {"from": "create_req", "to": "attach_buf", "label": "생성 성공", "label_en": "Create OK", "condition_ref": "c0:false", "quote_ids": ["cam-preparation:4", "cam-preparation:6"]}, {"from": "attach_buf", "to": "err_return", "label": "연결 오류", "label_en": "Attach error", "condition_ref": "c2:true", "quote_ids": ["cam-preparation:6", "cam-preparation:1"]}, {"from": "attach_buf", "to": "store_req", "label": "연결 성공", "label_en": "Attach OK", "condition_ref": "c2:false", "quote_ids": ["cam-preparation:5", "cam-preparation:6", "cam-preparation:8"]}, {"from": "store_req", "to": "more_requests", "label": "저장 뒤 남은 요청 다시 확인", "label_en": "Stored: recheck left", "condition_ref": "always", "quote_ids": ["cam-preparation:8", "cam-preparation:4"]}]}, "graph": {"id": "submission-gate", "topic": "initial-preparation", "kind": "decision", "title": "초기 요청들의 준비 반복과 준비 완료", "question": "기록된 단일 스트림·출력 싱크 미요청 구성에서 모든 초기 요청·버퍼는 카메라 시작 전에 어떻게 준비되며 준비 실패는 어떻게 처리됩니까?", "condition_display": "evidence", "nodes": [{"id": "alloc_check", "label": "스트림 버퍼 할당 호출이 실패했는가?", "label_en": "Did the stream buffer allocation call fail?", "shape": "decision", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}, {"id": "err_return", "label": "오류 값을 반환하고 카메라 시작 전에 종료", "label_en": "Return the error value and end before camera start", "shape": "box", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "ret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}"}]}, {"id": "more_requests", "label": "할당된 최소 버퍼 수만큼 만들 초기 요청이 남았는가?", "label_en": "Requests left to make up to the minimum buffer count?", "shape": "decision", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "unsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "requests_.push_back(std::move(request));\n\t}"}]}, {"id": "create_req", "label": "요청 생성이 실패했는가?", "label_en": "Did request creation fail?", "shape": "decision", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}, {"id": "attach_buf", "label": "스트림 버퍼 i 연결에 실패했는가?", "label_en": "Failed to attach stream buffer i?", "shape": "decision", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "ret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}"}]}, {"id": "store_req", "label": "단일 스트림의 buffers[i]를 요청 i에 연결한 뒤 요청을 보관", "label_en": "Keep request i after attaching sole stream's buffers[i]", "shape": "box", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "if (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "requests_.push_back(std::move(request));\n\t}"}]}, {"id": "ready_done", "label": "모든 초기 요청·버퍼 준비 완료, 카메라 시작 전 단계 종료", "label_en": "All initial requests and buffers ready before camera start", "shape": "box", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "requests_.push_back(std::move(request));\n\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "ret = camera_->start();"}]}], "edges": [{"from": "alloc_check", "to": "err_return", "label": "할당 오류 · ret < 0 [true]", "label_en": "Alloc error · ret < 0 [true]", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}, {"from": "alloc_check", "to": "more_requests", "label": "할당 성공 · ret < 0 [false]", "label_en": "Alloc OK · ret < 0 [false]", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "unsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}, {"from": "more_requests", "to": "create_req", "label": "남은 요청 있음", "label_en": "Requests left", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}, {"from": "more_requests", "to": "ready_done", "label": "남은 요청 없음", "label_en": "No requests left", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "requests_.push_back(std::move(request));\n\t}"}]}, {"from": "create_req", "to": "err_return", "label": "생성 오류 · !request [true]", "label_en": "Create error · !request [true]", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}, {"from": "create_req", "to": "attach_buf", "label": "생성 성공 · !request [false]", "label_en": "Create OK · !request [false]", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "ret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}"}]}, {"from": "attach_buf", "to": "err_return", "label": "연결 오류 · ret < 0 [true]", "label_en": "Attach error · ret < 0 [true]", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "ret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}, {"from": "attach_buf", "to": "store_req", "label": "연결 성공 · ret < 0 [false]", "label_en": "Attach OK · ret < 0 [false]", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "ret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "requests_.push_back(std::move(request));\n\t}"}]}, {"from": "store_req", "to": "more_requests", "label": "저장 뒤 남은 요청 다시 확인", "label_en": "Stored: recheck left", "evidence": [{"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "requests_.push_back(std::move(request));\n\t}"}, {"source": "initial-preparation/cam-preparation", "sha256": "0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56", "quote": "for (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "adfa719f8ed67d18fd8a0739fc088a1f8b9e7252", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "initial-submission": {"input_fingerprint": "ac797cd675b788b384ab0fb749c0d6ed1773277e379da288f33ec02a32894573", "draft": {"nodes": [{"id": "start_check", "symbol": "Camera::start", "label": "카메라 시작 결과를 확인합니다.", "label_en": "Check the camera start result.", "shape": "decision", "quote_ids": ["camera-queue:2", "cam-request-buffers:0"]}, {"id": "start_fail", "symbol": "CameraSession::startCapture", "label": "sink가 있으면 중지하고 시작 오류를 반환합니다.", "label_en": "Stop the sink if present and return the start error.", "shape": "box", "quote_ids": ["cam-request-buffers:0"]}, {"id": "remaining", "symbol": "requests_", "label": "처리할 초기 요청이 남았는지 확인합니다.", "label_en": "Check whether initial requests remain.", "shape": "decision", "quote_ids": ["cam-request-buffers:0"]}, {"id": "limit_check", "symbol": "CameraSession::queueRequest", "label": "큐 API 호출 시도 횟수가 설정된 한도에 도달했는지 확인합니다.", "label_en": "Check whether queue API call attempts reached the configured limit.", "shape": "decision", "quote_ids": ["cam-request-buffers:0"]}, {"id": "control_merge", "symbol": "queueCount_", "label": "스크립트가 있을 때만 제어를 병합하고 큐 API 호출 시도 횟수는 항상 1 늘립니다.", "label_en": "Merge controls only with a script; always increment queue API call attempts.", "shape": "process", "quote_ids": ["cam-request-buffers:0"]}, {"id": "camera_queue_check", "symbol": "Camera::queueRequest", "label": "카메라 실행 상태와 요청의 생성 카메라, 상태, 제어 목록, 버퍼와 스트림을 검사합니다.", "label_en": "Check the running state and the request's camera, status, controls, buffers and runs.", "shape": "decision", "quote_ids": ["camera-queue:0"]}, {"id": "queue_error", "symbol": "EINVAL", "label": "검사에 실패하면 API가 음수 오류를 반환합니다.", "label_en": "If a check fails, the API returns a negative error.", "shape": "box", "quote_ids": ["camera-queue:0"]}, {"id": "queue_async", "symbol": "PipelineHandler::queueRequest", "label": "파이프라인 큐 호출을 비동기로 등록하고 API가 0을 반환합니다.", "label_en": "Queue the pipeline call asynchronously and return 0 from the API.", "shape": "box", "quote_ids": ["camera-queue:0"]}, {"id": "caller_check", "symbol": "ret", "label": "호출자가 helper의 반환값이 음수인지 확인합니다.", "label_en": "The caller checks whether the helper's return value is negative.", "shape": "decision", "quote_ids": ["cam-request-buffers:0"]}, {"id": "stop_on_error", "symbol": "stop", "label": "카메라와 존재하는 sink를 중지한 뒤 오류를 반환합니다.", "label_en": "Stop the camera and any sink, then return the error.", "shape": "box", "quote_ids": ["cam-request-buffers:0"]}, {"id": "done", "symbol": "std::cout", "label": "순회가 끝나면 한도 유무에 따른 캡처 안내를 출력하고 0을 반환합니다.", "label_en": "After the loop, print the capture notice for the limit and return 0.", "shape": "box", "quote_ids": ["cam-request-buffers:0"]}], "edges": [{"from": "start_check", "to": "start_fail", "label": "시작 오류", "label_en": "Start error", "condition_ref": "c8:true", "quote_ids": ["cam-request-buffers:0", "camera-queue:2"]}, {"from": "start_check", "to": "remaining", "label": "시작 성공", "label_en": "Start succeeded", "condition_ref": "c8:false", "quote_ids": ["cam-request-buffers:0", "camera-queue:2"]}, {"from": "remaining", "to": "limit_check", "label": "요청이 남음", "label_en": "Requests remain", "condition_ref": "always", "quote_ids": ["cam-request-buffers:0"]}, {"from": "remaining", "to": "done", "label": "요청이 없음", "label_en": "No requests remain", "condition_ref": "always", "quote_ids": ["cam-request-buffers:0"]}, {"from": "limit_check", "to": "caller_check", "label": "도달: API 호출 없이 0", "label_en": "At limit: 0, no call", "condition_ref": "c2:true", "quote_ids": ["cam-request-buffers:0"]}, {"from": "limit_check", "to": "control_merge", "label": "한도 없음 또는 미달", "label_en": "Unset or below limit", "condition_ref": "c2:false", "quote_ids": ["cam-request-buffers:0"]}, {"from": "control_merge", "to": "camera_queue_check", "label": "카메라 큐 API 호출", "label_en": "Call camera queue", "condition_ref": "always", "quote_ids": ["cam-request-buffers:0", "camera-queue:0"]}, {"from": "camera_queue_check", "to": "queue_error", "label": "검사 실패", "label_en": "Checks fail", "condition_ref": "always", "quote_ids": ["camera-queue:0"]}, {"from": "camera_queue_check", "to": "queue_async", "label": "검사 통과", "label_en": "Checks pass", "condition_ref": "always", "quote_ids": ["camera-queue:0"]}, {"from": "queue_error", "to": "caller_check", "label": "오류 반환 후 검사", "label_en": "Check after error", "condition_ref": "always", "quote_ids": ["camera-queue:0", "cam-request-buffers:0"]}, {"from": "queue_async", "to": "caller_check", "label": "0 반환 후 검사", "label_en": "Check after return 0", "condition_ref": "always", "quote_ids": ["camera-queue:0", "cam-request-buffers:0"]}, {"from": "caller_check", "to": "stop_on_error", "label": "음수 결과", "label_en": "Negative result", "condition_ref": "c9:true", "quote_ids": ["cam-request-buffers:0"]}, {"from": "caller_check", "to": "remaining", "label": "음수가 아님", "label_en": "Not negative", "condition_ref": "c9:false", "quote_ids": ["cam-request-buffers:0"]}]}, "graph": {"id": "initial-submission", "topic": "initial-submission", "kind": "decision", "title": "초기 요청 제출 반복과 오류 반환", "question": "같은 기록 구성에서 카메라 시작 뒤 남은 초기 요청을 순회하며 제출 한도를 적용하고 큐 반환 오류와 정상 순회 종료를 어떻게 처리합니까?", "condition_display": "evidence", "nodes": [{"id": "start_check", "label": "카메라 시작 결과를 확인합니다.", "label_en": "Check the camera start result.", "shape": "decision", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start("}, {"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"id": "start_fail", "label": "sink가 있으면 중지하고 시작 오류를 반환합니다.", "label_en": "Stop the sink if present and return the start error.", "shape": "box", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"id": "remaining", "label": "처리할 초기 요청이 남았는지 확인합니다.", "label_en": "Check whether initial requests remain.", "shape": "decision", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"id": "limit_check", "label": "큐 API 호출 시도 횟수가 설정된 한도에 도달했는지 확인합니다.", "label_en": "Check whether queue API call attempts reached the configured limit.", "shape": "decision", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"id": "control_merge", "label": "스크립트가 있을 때만 제어를 병합하고 큐 API 호출 시도 횟수는 항상 1 늘립니다.", "label_en": "Merge controls only with a script; always increment queue API call attempts.", "shape": "box", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"id": "camera_queue_check", "label": "카메라 실행 상태와 요청의 생성 카메라, 상태, 제어 목록, 버퍼와 스트림을 검사합니다.", "label_en": "Check the running state and the request's camera, status, controls, buffers and runs.", "shape": "decision", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}]}, {"id": "queue_error", "label": "검사에 실패하면 API가 음수 오류를 반환합니다.", "label_en": "If a check fails, the API returns a negative error.", "shape": "box", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}]}, {"id": "queue_async", "label": "파이프라인 큐 호출을 비동기로 등록하고 API가 0을 반환합니다.", "label_en": "Queue the pipeline call asynchronously and return 0 from the API.", "shape": "box", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}]}, {"id": "caller_check", "label": "호출자가 helper의 반환값이 음수인지 확인합니다.", "label_en": "The caller checks whether the helper's return value is negative.", "shape": "decision", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"id": "stop_on_error", "label": "카메라와 존재하는 sink를 중지한 뒤 오류를 반환합니다.", "label_en": "Stop the camera and any sink, then return the error.", "shape": "box", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"id": "done", "label": "순회가 끝나면 한도 유무에 따른 캡처 안내를 출력하고 0을 반환합니다.", "label_en": "After the loop, print the capture notice for the limit and return 0.", "shape": "box", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}], "edges": [{"from": "start_check", "to": "start_fail", "label": "시작 오류 · ret [true]", "label_en": "Start error · ret [true]", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}, {"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start("}]}, {"from": "start_check", "to": "remaining", "label": "시작 성공 · ret [false]", "label_en": "Start succeeded · ret [false]", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}, {"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start("}]}, {"from": "remaining", "to": "limit_check", "label": "요청이 남음", "label_en": "Requests remain", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"from": "remaining", "to": "done", "label": "요청이 없음", "label_en": "No requests remain", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"from": "limit_check", "to": "caller_check", "label": "도달: API 호출 없이 0 · captureLimit_ && queueCount_ >= captureLimit_ [true]", "label_en": "At limit: 0, no call · captureLimit_ && queueCount_ >= captureLimit_ [true]", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"from": "limit_check", "to": "control_merge", "label": "한도 없음 또는 미달 · captureLimit_ && queueCount_ >= captureLimit_ [false]", "label_en": "Unset or below limit · captureLimit_ && queueCount_ >= captureLimit_ [false]", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"from": "control_merge", "to": "camera_queue_check", "label": "카메라 큐 API 호출", "label_en": "Call camera queue", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}, {"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}]}, {"from": "camera_queue_check", "to": "queue_error", "label": "검사 실패", "label_en": "Checks fail", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}]}, {"from": "camera_queue_check", "to": "queue_async", "label": "검사 통과", "label_en": "Checks pass", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}]}, {"from": "queue_error", "to": "caller_check", "label": "오류 반환 후 검사", "label_en": "Check after error", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}, {"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"from": "queue_async", "to": "caller_check", "label": "0 반환 후 검사", "label_en": "Check after return 0", "evidence": [{"source": "initial-submission/camera-queue", "sha256": "886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef", "quote": "int Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise"}, {"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"from": "caller_check", "to": "stop_on_error", "label": "음수 결과 · ret < 0 [true]", "label_en": "Negative result · ret < 0 [true]", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}, {"from": "caller_check", "to": "remaining", "label": "음수가 아님 · ret < 0 [false]", "label_en": "Not negative · ret < 0 [false]", "evidence": [{"source": "initial-submission/cam-request-buffers", "sha256": "37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417", "quote": "int CameraSession::startCapture()\n{\n\tint ret;\n\n\t/* Identify the stream with the least number of buffers. */\n\tunsigned int nbuffers = UINT_MAX;\n\tfor (StreamConfiguration &cfg : *config_) {\n\t\tret = allocator_->allocate(cfg.stream());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't allocate buffers\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tunsigned int allocated = allocator_->buffers(cfg.stream()).size();\n\t\tnbuffers = std::min(nbuffers, allocated);\n\t}\n\n\t/*\n\t * TODO: make cam tool smarter to support still capture by for\n\t * example pushing a button. For now run all streams all the time.\n\t */\n\n\tfor (unsigned int i = 0; i < nbuffers; i++) {\n\t\tstd::unique_ptr<Request> request = camera_->createRequest();\n\t\tif (!request) {\n\t\t\tstd::cerr << \"Can't create request\" << std::endl;\n\t\t\treturn -ENOMEM;\n\t\t}\n\n\t\tfor (StreamConfiguration &cfg : *config_) {\n\t\t\tStream *stream = cfg.stream();\n\t\t\tconst std::vector<std::unique_ptr<FrameBuffer>> &buffers =\n\t\t\t\tallocator_->buffers(stream);\n\t\t\tconst std::unique_ptr<FrameBuffer> &buffer = buffers[i];\n\n\t\t\tret = request->addBuffer(stream, buffer.get());\n\t\t\tif (ret < 0) {\n\t\t\t\tstd::cerr << \"Can't set buffer for request\"\n\t\t\t\t\t  << std::endl;\n\t\t\t\treturn ret;\n\t\t\t}\n\n\t\t\tif (sink_)\n\t\t\t\tsink_->mapBuffer(buffer.get());\n\t\t}\n\n\t\trequests_.push_back(std::move(request));\n\t}\n\n\tif (sink_) {\n\t\tret = sink_->start();\n\t\tif (ret) {\n\t\t\tstd::cout << \"Failed to start frame sink\" << std::endl;\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tret = camera_->start();\n\tif (ret) {\n\t\tstd::cout << \"Failed to start capture\" << std::endl;\n\t\tif (sink_)\n\t\t\tsink_->stop();\n\t\treturn ret;\n\t}\n\n\tfor (std::unique_ptr<Request> &request : requests_) {\n\t\tret = queueRequest(request.get());\n\t\tif (ret < 0) {\n\t\t\tstd::cerr << \"Can't queue request\" << std::endl;\n\t\t\tcamera_->stop();\n\t\t\tif (sink_)\n\t\t\t\tsink_->stop();\n\t\t\treturn ret;\n\t\t}\n\t}\n\n\tif (captureLimit_)\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture \" << captureLimit_ << \" frames\"\n\t\t\t  << std::endl;\n\telse\n\t\tstd::cout << \"cam\" << cameraIndex_\n\t\t\t  << \": Capture until user interrupts by SIGINT\"\n\t\t\t  << std::endl;\n\n\treturn 0;\n}\n\nint CameraSession::queueRequest(Request *request)\n{\n\tif (captureLimit_ && queueCount_ >= captureLimit_)\n\t\treturn 0;\n\n\tif (script_)\n\t\trequest->controls().merge(script_->frameControls(queueCount_),\n\t\t\t\t\t  ControlList::MergePolicy::OverwriteExisting);\n\n\tqueueCount_++;\n\n\treturn camera_->queueRequest(request);\n}\n\nvoid CameraSession::requestComplete("}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "adfa719f8ed67d18fd8a0739fc088a1f8b9e7252", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "virtual-frame-path": {"input_fingerprint": "6b3f3d37872084f2590867e5a092292190a7f6cea32201b7a7f6ab295487964d", "draft": {"nodes": {"n0": {"label": "PipelineHandler::queueRequest가 요청을 대기 목록에 넣고 준비 시도", "label_en": "PipelineHandler::queueRequest adds request; tries preparation", "shape": "process", "quote_ids": ["pipeline-dispatch:0", "pipeline-dispatch:1", "pipeline-dispatch:2", "pipeline-register:1"]}, "n1": {"label": "준비된 요청이 차례에 취소 상태입니까?", "label_en": "Is the prepared request cancelled at its turn?", "shape": "decision", "quote_ids": ["pipeline-dispatch:3", "pipeline-dispatch:6", "pipeline-dispatch:8"]}, "n2": {"label": "취소된 요청은 RequestCancelled; 큐 앞부터 완료 통지, 앞 RequestPending이면 보류·중단", "label_en": "RequestCancelled request; notify front; Stop at RequestPending", "shape": "process", "quote_ids": ["pipeline-dispatch:6", "pipeline-register:1", "pipeline-completion:1", "pipeline-completion:4", "pipeline-completion:5", "request-status-completion:2", "virtual-completion:1"]}, "n3": {"label": "가상 핸들러가 queued 호출로 요청 처리와 목표 시각 인수를 넘김", "label_en": "Virtual handler queues request; target time is an argument", "shape": "process", "quote_ids": ["pipeline-dispatch:7", "virtual-queue:0", "virtual-queue:4"]}, "n4": {"label": "수신 측 VirtualCameraData::processRequest가 목표 시각까지 대기", "label_en": "Receiver VirtualCameraData::processRequest waits until target", "shape": "process", "quote_ids": ["virtual-queue:4", "virtual-frame:0"]}, "n5": {"label": "생성 전 FrameSuccess 초기화 뒤, CPU 쓰기 동기화 범위에서 쓰기용 DMA-BUF 매핑 시도", "label_en": "Init FrameSuccess pre-call; try DMA-BUF map in CPU write sync", "shape": "process", "quote_ids": ["pattern-frame:0", "pattern-frame:1", "virtual-frame:2"]}, "n6": {"label": "NV12 형식에서 CPU가 Virtual2 lines 패턴 변환과 매핑 쓰기 시도", "label_en": "For NV12: CPU tries Virtual2 lines conversion and mapped write", "shape": "process", "quote_ids": ["pattern-frame:4", "virtual2-config:0", "pattern-frame:0"]}, "n7": {"label": "프레임 생성 결과가 오류입니까?", "label_en": "Is the frame generation result an error?", "shape": "decision", "quote_ids": ["virtual-frame:5", "pattern-frame:0"]}, "n8": {"label": "두 경우 모두 bufferCompleted로 버퍼 완료 신호; 요청 완료는 별도", "label_en": "Both emit buffer completion; request completion separate", "shape": "process", "quote_ids": ["virtual-frame:6", "virtual-completion:0", "virtual-completion:1", "pipeline-completion:0", "virtual-start:5"]}}, "edges": [{"from": "n0", "to": "n1", "label": "준비 완료 후 차례 확인", "label_en": "Once prepared", "condition_ref": "always", "quote_ids": ["pipeline-dispatch:0", "pipeline-dispatch:2", "pipeline-register:0", "pipeline-dispatch:3", "pipeline-dispatch:9", "pipeline-dispatch:10"]}, {"from": "n1", "to": "n2", "label": "취소됨", "label_en": "Cancelled", "condition_ref": "c10:true", "quote_ids": ["pipeline-dispatch:3", "pipeline-dispatch:6", "pipeline-completion:1", "pipeline-completion:4"]}, {"from": "n1", "to": "n3", "label": "취소 아님", "label_en": "Not cancelled", "condition_ref": "c10:false", "quote_ids": ["pipeline-dispatch:3", "pipeline-dispatch:6", "pipeline-dispatch:7"]}, {"from": "n3", "to": "n4", "label": "queued 호출 + 목표 시각", "label_en": "Queued call + target", "condition_ref": "always", "quote_ids": ["virtual-queue:0", "virtual-queue:4"]}, {"from": "n4", "to": "n5", "label": "일치 스트림만 프레임 생성", "label_en": "Matching stream only", "condition_ref": "always", "quote_ids": ["virtual-frame:0", "virtual-frame:1", "virtual-frame:5", "pattern-frame:0"]}, {"from": "n5", "to": "n6", "label": "변환·매핑 쓰기로", "label_en": "To conversion step", "condition_ref": "always", "quote_ids": ["pattern-frame:0", "pattern-frame:1", "pattern-frame:4", "virtual2-config:0"]}, {"from": "n6", "to": "n7", "label": "생성 결과 반환", "label_en": "Return frame result", "condition_ref": "always", "quote_ids": ["pattern-frame:0", "pattern-frame:4", "pattern-frame:7", "pattern-frame:8", "pattern-frame:9"]}, {"from": "n7", "to": "n8", "label": "오류: FrameError로 변경", "label_en": "Becomes FrameError", "condition_ref": "c17:true", "quote_ids": ["virtual-frame:5", "virtual-frame:6"]}, {"from": "n7", "to": "n8", "label": "정상: FrameSuccess 유지", "label_en": "Keeps FrameSuccess", "condition_ref": "c17:false", "quote_ids": ["virtual-frame:2", "virtual-frame:5", "virtual-frame:6"]}]}, "graph": {"id": "virtual-frame-path", "topic": "virtual-principle", "kind": "flow", "title": "Virtual2 줄 패턴 NV12 변환·기록 시도 흐름", "condition_display": "evidence", "question": "버퍼를 연결한 뒤 가상 파이프라인은 CPU 패턴 기록을 어떻게 시도하고 버퍼 완료를 어떻게 알립니까?", "nodes": [{"id": "n0", "label": "PipelineHandler::queueRequest가 요청을 대기 목록에 넣고 준비 시도", "label_en": "PipelineHandler::queueRequest adds request; tries preparation", "shape": "box", "evidence": [{"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "void PipelineHandler::queueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_queue, request);"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "Camera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->waitingRequests_.push(request);"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "request->_d()->prepare(300ms);\n}"}, {"source": "virtual-principle/pipeline-register", "sha256": "e26bfa8d7aabb043998df27778cce4f5a3724b9130695499701db24012fa111d", "quote": "/**\n * \\fn PipelineHandler::queueRequest()\n * \\brief Queue a request\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the pipeline handler for\n * processing. The request is first added to the internal list of waiting\n * requests which have to be prepared to make sure they are ready for being\n * queued to the pipeline handler.\n *\n * The queue of waiting requests is iterated and up to \\a\n * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler\n * in the same order they have been queued by calling this function.\n *\n * If a Request fails during the preparation phase or if the pipeline handler\n * fails in queuing the request to the hardware the request is cancelled.\n *\n * Keeping track of queued requests ensures automatic completion of all requests\n * when the pipeline handler is stopped with stop(). Request completion shall be\n * signalled by the pipeline handler using the completeRequest() function.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::queueRequest("}]}, {"id": "n1", "label": "준비된 요청이 차례에 취소 상태입니까?", "label_en": "Is the prepared request cancelled at its turn?", "shape": "decision", "evidence": [{"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "/**\n * \\brief Queue one requests to the device\n */\nvoid PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "/**\n * \\brief Queue prepared requests to the device\n *\n * Iterate the list of waiting requests and queue them to the device one\n * by one if they have been prepared.\n */\nvoid PipelineHandler::doQueueRequests(Camera *camera)\n{\n\tCamera::Private *data = camera->_d();\n\twhile (!data->waitingRequests_.empty()) {\n\t\tif (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;"}]}, {"id": "n2", "label": "취소된 요청은 RequestCancelled; 큐 앞부터 완료 통지, 앞 RequestPending이면 보류·중단", "label_en": "RequestCancelled request; notify front; Stop at RequestPending", "shape": "box", "evidence": [{"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}"}, {"source": "virtual-principle/pipeline-register", "sha256": "e26bfa8d7aabb043998df27778cce4f5a3724b9130695499701db24012fa111d", "quote": "/**\n * \\fn PipelineHandler::queueRequest()\n * \\brief Queue a request\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the pipeline handler for\n * processing. The request is first added to the internal list of waiting\n * requests which have to be prepared to make sure they are ready for being\n * queued to the pipeline handler.\n *\n * The queue of waiting requests is iterated and up to \\a\n * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler\n * in the same order they have been queued by calling this function.\n *\n * If a Request fails during the preparation phase or if the pipeline handler\n * fails in queuing the request to the hardware the request is cancelled.\n *\n * Keeping track of queued requests ensures automatic completion of all requests\n * when the pipeline handler is stopped with stop(). Request completion shall be\n * signalled by the pipeline handler using the completeRequest() function.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::queueRequest("}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "ASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}"}, {"source": "virtual-principle/request-status-completion", "sha256": "2efec13b708bff2ca232445ef868877a30facef1b6fa17ddcff47bfd013e2289", "quote": "request->status_ = cancelled_ ? RequestCancelled : RequestComplete;"}, {"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "if (completeBuffer(request, buffer))\n\t\tcompleteRequest(request);\n}"}]}, {"id": "n3", "label": "가상 핸들러가 queued 호출로 요청 처리와 목표 시각 인수를 넘김", "label_en": "Virtual handler queues request; target time is an argument", "shape": "box", "evidence": [{"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "int ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);\n}"}, {"source": "virtual-principle/virtual-queue", "sha256": "8e757a1e7d0904f9affb3c2ba07e42c9f40b5bcd029d7dd834f853192c9192bc", "quote": "int PipelineHandlerVirtual::queueRequestDevice(Camera *camera, Request *request)\n{\n\tVirtualCameraData *data = cameraData(camera);"}, {"source": "virtual-principle/virtual-queue", "sha256": "8e757a1e7d0904f9affb3c2ba07e42c9f40b5bcd029d7dd834f853192c9192bc", "quote": "data->invokeMethod(&VirtualCameraData::processRequest,\n\t\t\t   ConnectionTypeQueued, request,\n\t\t\t   data->targetTimestamp_);"}]}, {"id": "n4", "label": "수신 측 VirtualCameraData::processRequest가 목표 시각까지 대기", "label_en": "Receiver VirtualCameraData::processRequest waits until target", "shape": "box", "evidence": [{"source": "virtual-principle/virtual-queue", "sha256": "8e757a1e7d0904f9affb3c2ba07e42c9f40b5bcd029d7dd834f853192c9192bc", "quote": "data->invokeMethod(&VirtualCameraData::processRequest,\n\t\t\t   ConnectionTypeQueued, request,\n\t\t\t   data->targetTimestamp_);"}, {"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "void VirtualCameraData::processRequest(Request *request,\n\t\t\t\t       uint64_t targetTimestamp)\n{\n\tconst auto targetTime = std::chrono::steady_clock::time_point{\n\t\tstd::chrono::nanoseconds(targetTimestamp)\n\t};\n\tstd::this_thread::sleep_until(targetTime);"}]}, {"id": "n5", "label": "생성 전 FrameSuccess 초기화 뒤, CPU 쓰기 동기화 범위에서 쓰기용 DMA-BUF 매핑 시도", "label_en": "Init FrameSuccess pre-call; try DMA-BUF map in CPU write sync", "shape": "box", "evidence": [{"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,\n\t\t\t\t\tconst FrameBuffer *buffer)\n{\n\t/*\n\t * \\todo Assume all planes are contiguous and mapped at different\n\t * offsets on the same fd. This holds true as long as the implementation\n\t * of DmaBufAllocator only allocates contiguous planes. If this will\n\t * change or a different allocator will be used then we need to create\n\t * one dma syncer for each non-contiguous plane.\n\t */\n\tDmaSyncer outDmaSyncer(buffer->planes()[0].fd,\n\t\t\t       DmaSyncer::SyncType::Write);\n\tMappedFrameBuffer mappedFrameBuffer(buffer,\n\t\t\t\t\t    MappedFrameBuffer::MapFlag::Write);"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "const auto &planes = mappedFrameBuffer.planes();\n\tconst Size &size = cfg.size;\n\tconst PixelFormatInfo &info = PixelFormatInfo::info(cfg.pixelFormat);"}, {"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "fmd.status = FrameMetadata::Status::FrameSuccess;\n\t\t\t\tfmd.sequence = streamConfig.seq++;\n\t\t\t\tfmd.timestamp = targetTimestamp;"}]}, {"id": "n6", "label": "NV12 형식에서 CPU가 Virtual2 lines 패턴 변환과 매핑 쓰기 시도", "label_en": "For NV12: CPU tries Virtual2 lines conversion and mapped write", "shape": "box", "evidence": [{"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "/* Convert the template_ to the frame buffer */\n\tswitch (cfg.pixelFormat) {\n\tcase formats::NV12:\n\t\tret = libyuv::ARGBToNV12(template_.get(),\n\t\t\t\t\t size.width * kARGBSize,\n\t\t\t\t\t planes[0].data(), info.stride(size.width, 0),\n\t\t\t\t\t planes[1].data(), info.stride(size.width, 1),\n\t\t\t\t\t size.width, size.height);\n\t\tbreak;"}, {"source": "virtual-principle/virtual2-config", "sha256": "b9a78428bbde1f8b2a7ae34fc352cf6576ca0f24ee5d0ba7a94a0b790bfd2dc3", "quote": "\"Virtual2\":\n  supported_formats:\n  - width: 400\n    height: 300\n  test_pattern: \"lines\""}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,\n\t\t\t\t\tconst FrameBuffer *buffer)\n{\n\t/*\n\t * \\todo Assume all planes are contiguous and mapped at different\n\t * offsets on the same fd. This holds true as long as the implementation\n\t * of DmaBufAllocator only allocates contiguous planes. If this will\n\t * change or a different allocator will be used then we need to create\n\t * one dma syncer for each non-contiguous plane.\n\t */\n\tDmaSyncer outDmaSyncer(buffer->planes()[0].fd,\n\t\t\t       DmaSyncer::SyncType::Write);\n\tMappedFrameBuffer mappedFrameBuffer(buffer,\n\t\t\t\t\t    MappedFrameBuffer::MapFlag::Write);"}]}, {"id": "n7", "label": "프레임 생성 결과가 오류입니까?", "label_en": "Is the frame generation result an error?", "shape": "decision", "evidence": [{"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "if (streamConfig.frameGenerator->generateFrame(\n\t\t\t\t\t    stream->configuration(), buffer))\n\t\t\t\t\tfmd.status = FrameMetadata::Status::FrameError;"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,\n\t\t\t\t\tconst FrameBuffer *buffer)\n{\n\t/*\n\t * \\todo Assume all planes are contiguous and mapped at different\n\t * offsets on the same fd. This holds true as long as the implementation\n\t * of DmaBufAllocator only allocates contiguous planes. If this will\n\t * change or a different allocator will be used then we need to create\n\t * one dma syncer for each non-contiguous plane.\n\t */\n\tDmaSyncer outDmaSyncer(buffer->planes()[0].fd,\n\t\t\t       DmaSyncer::SyncType::Write);\n\tMappedFrameBuffer mappedFrameBuffer(buffer,\n\t\t\t\t\t    MappedFrameBuffer::MapFlag::Write);"}]}, {"id": "n8", "label": "두 경우 모두 bufferCompleted로 버퍼 완료 신호; 요청 완료는 별도", "label_en": "Both emit buffer completion; request completion separate", "shape": "box", "evidence": [{"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "bufferCompleted.emit(buffer);\n\t\t\t\tbreak;\n\t\t\t}\n\t\t}\n\t\tASSERT(found);\n\t}\n}"}, {"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "void PipelineHandlerVirtual::bufferCompleted(FrameBuffer *buffer)\n{\n\tRequest *request = buffer->request();"}, {"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "if (completeBuffer(request, buffer))\n\t\tcompleteRequest(request);\n}"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "bool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}, {"source": "virtual-principle/virtual-start", "sha256": "a874aaf3a8902d67c4b8bfe9166ff2783f4dc95ba98b2ce2e72b454de78b7a2b", "quote": "data->bufferCompleted.connect(this, &PipelineHandlerVirtual::bufferCompleted);\n\tdata->start();"}]}], "edges": [{"from": "n0", "to": "n1", "label": "준비 완료 후 차례 확인", "label_en": "Once prepared", "evidence": [{"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "void PipelineHandler::queueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_queue, request);"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "request->_d()->prepare(300ms);\n}"}, {"source": "virtual-principle/pipeline-register", "sha256": "e26bfa8d7aabb043998df27778cce4f5a3724b9130695499701db24012fa111d", "quote": "void PipelineHandler::registerRequest(Request *request)\n{\n\t/*\n\t * Connect the request prepared signal to notify the pipeline handler\n\t * when a request is ready to be processed.\n\t */\n\trequest->_d()->prepared.connect(this, [this, request]() {\n\t\tdoQueueRequests(request->_d()->camera());\n\t});\n}"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "/**\n * \\brief Queue one requests to the device\n */\nvoid PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "/*\n\t\t * Pop the request first, in case doQueueRequests() is called\n\t\t * recursively from within doQueueRequest()\n\t\t */\n\t\tdata->waitingRequests_.pop();\n\t\tdoQueueRequest(request);\n\t}\n}"}]}, {"from": "n1", "to": "n2", "label": "취소됨 · request->_d()->cancelled_ [true]", "label_en": "Cancelled · request->_d()->cancelled_ [true]", "evidence": [{"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "/**\n * \\brief Queue one requests to the device\n */\nvoid PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}, {"from": "n1", "to": "n3", "label": "취소 아님 · request->_d()->cancelled_ [false]", "label_en": "Not cancelled · request->_d()->cancelled_ [false]", "evidence": [{"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "/**\n * \\brief Queue one requests to the device\n */\nvoid PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}"}, {"source": "virtual-principle/pipeline-dispatch", "sha256": "cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678", "quote": "int ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);\n}"}]}, {"from": "n3", "to": "n4", "label": "queued 호출 + 목표 시각", "label_en": "Queued call + target", "evidence": [{"source": "virtual-principle/virtual-queue", "sha256": "8e757a1e7d0904f9affb3c2ba07e42c9f40b5bcd029d7dd834f853192c9192bc", "quote": "int PipelineHandlerVirtual::queueRequestDevice(Camera *camera, Request *request)\n{\n\tVirtualCameraData *data = cameraData(camera);"}, {"source": "virtual-principle/virtual-queue", "sha256": "8e757a1e7d0904f9affb3c2ba07e42c9f40b5bcd029d7dd834f853192c9192bc", "quote": "data->invokeMethod(&VirtualCameraData::processRequest,\n\t\t\t   ConnectionTypeQueued, request,\n\t\t\t   data->targetTimestamp_);"}]}, {"from": "n4", "to": "n5", "label": "일치 스트림만 프레임 생성", "label_en": "Matching stream only", "evidence": [{"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "void VirtualCameraData::processRequest(Request *request,\n\t\t\t\t       uint64_t targetTimestamp)\n{\n\tconst auto targetTime = std::chrono::steady_clock::time_point{\n\t\tstd::chrono::nanoseconds(targetTimestamp)\n\t};\n\tstd::this_thread::sleep_until(targetTime);"}, {"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "for (const auto &[stream, buffer] : request->buffers()) {\n\t\tbool found = false;\n\t\t/* map buffer and fill test patterns */\n\t\tfor (auto &streamConfig : streamConfigs_) {\n\t\t\tif (stream == &streamConfig.stream) {\n\t\t\t\tFrameMetadata &fmd = buffer->_d()->metadata();"}, {"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "if (streamConfig.frameGenerator->generateFrame(\n\t\t\t\t\t    stream->configuration(), buffer))\n\t\t\t\t\tfmd.status = FrameMetadata::Status::FrameError;"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,\n\t\t\t\t\tconst FrameBuffer *buffer)\n{\n\t/*\n\t * \\todo Assume all planes are contiguous and mapped at different\n\t * offsets on the same fd. This holds true as long as the implementation\n\t * of DmaBufAllocator only allocates contiguous planes. If this will\n\t * change or a different allocator will be used then we need to create\n\t * one dma syncer for each non-contiguous plane.\n\t */\n\tDmaSyncer outDmaSyncer(buffer->planes()[0].fd,\n\t\t\t       DmaSyncer::SyncType::Write);\n\tMappedFrameBuffer mappedFrameBuffer(buffer,\n\t\t\t\t\t    MappedFrameBuffer::MapFlag::Write);"}]}, {"from": "n5", "to": "n6", "label": "변환·매핑 쓰기로", "label_en": "To conversion step", "evidence": [{"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,\n\t\t\t\t\tconst FrameBuffer *buffer)\n{\n\t/*\n\t * \\todo Assume all planes are contiguous and mapped at different\n\t * offsets on the same fd. This holds true as long as the implementation\n\t * of DmaBufAllocator only allocates contiguous planes. If this will\n\t * change or a different allocator will be used then we need to create\n\t * one dma syncer for each non-contiguous plane.\n\t */\n\tDmaSyncer outDmaSyncer(buffer->planes()[0].fd,\n\t\t\t       DmaSyncer::SyncType::Write);\n\tMappedFrameBuffer mappedFrameBuffer(buffer,\n\t\t\t\t\t    MappedFrameBuffer::MapFlag::Write);"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "const auto &planes = mappedFrameBuffer.planes();\n\tconst Size &size = cfg.size;\n\tconst PixelFormatInfo &info = PixelFormatInfo::info(cfg.pixelFormat);"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "/* Convert the template_ to the frame buffer */\n\tswitch (cfg.pixelFormat) {\n\tcase formats::NV12:\n\t\tret = libyuv::ARGBToNV12(template_.get(),\n\t\t\t\t\t size.width * kARGBSize,\n\t\t\t\t\t planes[0].data(), info.stride(size.width, 0),\n\t\t\t\t\t planes[1].data(), info.stride(size.width, 1),\n\t\t\t\t\t size.width, size.height);\n\t\tbreak;"}, {"source": "virtual-principle/virtual2-config", "sha256": "b9a78428bbde1f8b2a7ae34fc352cf6576ca0f24ee5d0ba7a94a0b790bfd2dc3", "quote": "\"Virtual2\":\n  supported_formats:\n  - width: 400\n    height: 300\n  test_pattern: \"lines\""}]}, {"from": "n6", "to": "n7", "label": "생성 결과 반환", "label_en": "Return frame result", "evidence": [{"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,\n\t\t\t\t\tconst FrameBuffer *buffer)\n{\n\t/*\n\t * \\todo Assume all planes are contiguous and mapped at different\n\t * offsets on the same fd. This holds true as long as the implementation\n\t * of DmaBufAllocator only allocates contiguous planes. If this will\n\t * change or a different allocator will be used then we need to create\n\t * one dma syncer for each non-contiguous plane.\n\t */\n\tDmaSyncer outDmaSyncer(buffer->planes()[0].fd,\n\t\t\t       DmaSyncer::SyncType::Write);\n\tMappedFrameBuffer mappedFrameBuffer(buffer,\n\t\t\t\t\t    MappedFrameBuffer::MapFlag::Write);"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "/* Convert the template_ to the frame buffer */\n\tswitch (cfg.pixelFormat) {\n\tcase formats::NV12:\n\t\tret = libyuv::ARGBToNV12(template_.get(),\n\t\t\t\t\t size.width * kARGBSize,\n\t\t\t\t\t planes[0].data(), info.stride(size.width, 0),\n\t\t\t\t\t planes[1].data(), info.stride(size.width, 1),\n\t\t\t\t\t size.width, size.height);\n\t\tbreak;"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "default:\n\t\tLOG(Virtual, Error) << \"Unsupported format\";\n\t\treturn -1;\n\t}"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "if (ret != 0)\n\t\tLOG(Virtual, Error) << \"Conversion failed with \" << ret;"}, {"source": "virtual-principle/pattern-frame", "sha256": "738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243", "quote": "return ret;\n}"}]}, {"from": "n7", "to": "n8", "label": "오류: FrameError로 변경 · streamConfig.frameGenerator->generateFrame( stream->configuration(), buffer) [true]", "label_en": "Becomes FrameError · streamConfig.frameGenerator->generateFrame( stream->configuration(), buffer) [true]", "evidence": [{"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "if (streamConfig.frameGenerator->generateFrame(\n\t\t\t\t\t    stream->configuration(), buffer))\n\t\t\t\t\tfmd.status = FrameMetadata::Status::FrameError;"}, {"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "bufferCompleted.emit(buffer);\n\t\t\t\tbreak;\n\t\t\t}\n\t\t}\n\t\tASSERT(found);\n\t}\n}"}]}, {"from": "n7", "to": "n8", "label": "정상: FrameSuccess 유지 · streamConfig.frameGenerator->generateFrame( stream->configuration(), buffer) [false]", "label_en": "Keeps FrameSuccess · streamConfig.frameGenerator->generateFrame( stream->configuration(), buffer) [false]", "evidence": [{"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "fmd.status = FrameMetadata::Status::FrameSuccess;\n\t\t\t\tfmd.sequence = streamConfig.seq++;\n\t\t\t\tfmd.timestamp = targetTimestamp;"}, {"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "if (streamConfig.frameGenerator->generateFrame(\n\t\t\t\t\t    stream->configuration(), buffer))\n\t\t\t\t\tfmd.status = FrameMetadata::Status::FrameError;"}, {"source": "virtual-principle/virtual-frame", "sha256": "3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df", "quote": "bufferCompleted.emit(buffer);\n\t\t\t\tbreak;\n\t\t\t}\n\t\t}\n\t\tASSERT(found);\n\t}\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "adfa719f8ed67d18fd8a0739fc088a1f8b9e7252", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "request-completion-order": {"input_fingerprint": "c917d15b017fb4ca9c34ab1f832b8be82c6531d224a0c5f34215d183f295e629", "draft": {"nodes": [{"id": "n0", "symbol": "PipelineHandlerVirtual::bufferCompleted", "label": "bufferCompleted: 가상 프레임 버퍼 완료 수신", "label_en": "bufferCompleted: receive virtual buffer done", "shape": "process", "quote_ids": ["virtual-completion:0"]}, {"id": "n1", "symbol": "completeBuffer", "label": "completeBuffer 판정: 요청의 모든 버퍼 완료 여부", "label_en": "completeBuffer check: all request buffers done?", "shape": "decision", "quote_ids": ["virtual-completion:1", "pipeline-completion:0"]}, {"id": "n2", "symbol": "FrameBuffer", "label": "나머지 버퍼 대기. completeRequest 미호출", "label_en": "Wait for remaining buffers; no completeRequest", "shape": "box", "quote_ids": ["pipeline-completion:0"]}, {"id": "n3", "symbol": "completeRequest", "label": "상태 표시: 정상 RequestComplete, 취소 RequestCancelled", "label_en": "Normal RequestComplete; cancel RequestCancelled", "shape": "process", "quote_ids": ["virtual-completion:1", "pipeline-completion:1", "pipeline-completion:2", "request-status-completion:0", "request-status-completion:2"]}, {"id": "n4", "symbol": "RequestPending", "label": "큐 맨 앞 요청이 RequestPending 상태인지 판정", "label_en": "Is front request in RequestPending state?", "shape": "decision", "quote_ids": ["pipeline-completion:4"]}, {"id": "n5", "symbol": "requestCompleted", "label": "맨 앞 꺼내 requestComplete 호출, requestCompleted 통지", "label_en": "Pop head; requestComplete emits requestCompleted", "shape": "process", "quote_ids": ["camera-notification:1", "cam-signal-connection:0", "pipeline-completion:5"]}, {"id": "n6", "symbol": "queuedRequests_", "label": "뒤 요청 통지 보류, 반복 중단", "label_en": "Hold later notifies, stop loop", "shape": "box", "quote_ids": ["pipeline-completion:4", "pipeline-completion:5"]}, {"id": "n7", "symbol": "queuedRequests_", "label": "큐가 비어 있지 않은가?", "label_en": "Is queue not empty?", "shape": "decision", "quote_ids": ["pipeline-completion:4"]}, {"id": "n8", "symbol": "queuedRequests_", "label": "통지 검사 종료", "label_en": "Notify check ends", "shape": "box", "quote_ids": ["pipeline-completion:4"]}], "edges": [{"from": "n0", "to": "n1", "label": "버퍼 완료 판정", "label_en": "Check buffer done", "condition_ref": "always", "quote_ids": ["virtual-completion:0", "virtual-completion:1"]}, {"from": "n1", "to": "n2", "label": "요청 미완료", "label_en": "Request incomplete", "condition_ref": "c2:false", "quote_ids": ["virtual-completion:1", "pipeline-completion:0"]}, {"from": "n1", "to": "n3", "label": "요청 완료 판정", "label_en": "Request complete", "condition_ref": "c2:true", "quote_ids": ["virtual-completion:1", "pipeline-completion:1"]}, {"from": "n3", "to": "n7", "label": "큐 상태 확인", "label_en": "Check queue", "condition_ref": "always", "quote_ids": ["pipeline-completion:1", "pipeline-completion:4"]}, {"from": "n7", "to": "n4", "label": "남은 요청 있음", "label_en": "Requests remain", "condition_ref": "c0:true", "quote_ids": ["pipeline-completion:4"]}, {"from": "n7", "to": "n8", "label": "큐 비어 있음", "label_en": "Queue empty", "condition_ref": "c0:false", "quote_ids": ["pipeline-completion:4"]}, {"from": "n4", "to": "n6", "label": "RequestPending 상태", "label_en": "RequestPending state", "condition_ref": "c4:true", "quote_ids": ["pipeline-completion:4"]}, {"from": "n4", "to": "n5", "label": "RequestPending 아님", "label_en": "Not RequestPending", "condition_ref": "c4:false", "quote_ids": ["pipeline-completion:4", "pipeline-completion:5", "camera-notification:1", "cam-signal-connection:0"]}, {"from": "n5", "to": "n7", "label": "통지 후 큐 재확인", "label_en": "Recheck queue", "condition_ref": "always", "quote_ids": ["pipeline-completion:4", "pipeline-completion:5", "camera-notification:1"]}, {"from": "n6", "to": "n8", "label": "반복 종료", "label_en": "Loop ends", "condition_ref": "always", "quote_ids": ["pipeline-completion:4"]}]}, "graph": {"id": "request-completion-order", "topic": "virtual-principle", "kind": "flow", "title": "버퍼 완료와 요청 완료·순서 통지는 별개입니다", "condition_display": "evidence", "question": "가상 버퍼 완료 경로의 모든 버퍼 완료 판정과, 완료 표시 뒤 제출 순서 큐의 연속 통지 및 반복 종료는 어떻게 연결됩니까?", "nodes": [{"id": "n0", "label": "bufferCompleted: 가상 프레임 버퍼 완료 수신", "label_en": "bufferCompleted: receive virtual buffer done", "shape": "box", "evidence": [{"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "void PipelineHandlerVirtual::bufferCompleted(FrameBuffer *buffer)\n{\n\tRequest *request = buffer->request();"}]}, {"id": "n1", "label": "completeBuffer 판정: 요청의 모든 버퍼 완료 여부", "label_en": "completeBuffer check: all request buffers done?", "shape": "decision", "evidence": [{"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "if (completeBuffer(request, buffer))\n\t\tcompleteRequest(request);\n}"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "bool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"id": "n2", "label": "나머지 버퍼 대기. completeRequest 미호출", "label_en": "Wait for remaining buffers; no completeRequest", "shape": "box", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "bool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"id": "n3", "label": "상태 표시: 정상 RequestComplete, 취소 RequestCancelled", "label_en": "Normal RequestComplete; cancel RequestCancelled", "shape": "box", "evidence": [{"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "if (completeBuffer(request, buffer))\n\t\tcompleteRequest(request);\n}"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "request->_d()->complete();"}, {"source": "virtual-principle/request-status-completion", "sha256": "2efec13b708bff2ca232445ef868877a30facef1b6fa17ddcff47bfd013e2289", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();"}, {"source": "virtual-principle/request-status-completion", "sha256": "2efec13b708bff2ca232445ef868877a30facef1b6fa17ddcff47bfd013e2289", "quote": "request->status_ = cancelled_ ? RequestCancelled : RequestComplete;"}]}, {"id": "n4", "label": "큐 맨 앞 요청이 RequestPending 상태인지 판정", "label_en": "Is front request in RequestPending state?", "shape": "decision", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}, {"id": "n5", "label": "맨 앞 꺼내 requestComplete 호출, requestCompleted 통지", "label_en": "Pop head; requestComplete emits requestCompleted", "shape": "box", "evidence": [{"source": "virtual-principle/camera-notification", "sha256": "aadfd6b4fdf910083a3d97fb11c623145f71553c9240f8e882d619fce61c43bb", "quote": "requestCompleted.emit(request);\n}"}, {"source": "virtual-principle/cam-signal-connection", "sha256": "837c0da1b2fd6f71aaabdb090306d3deda89c0fae6de39e91393d1111748e1b7", "quote": "camera_->requestCompleted.connect(this, &CameraSession::requestComplete);"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "ASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}"}]}, {"id": "n6", "label": "뒤 요청 통지 보류, 반복 중단", "label_en": "Hold later notifies, stop loop", "shape": "box", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "ASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}"}]}, {"id": "n7", "label": "큐가 비어 있지 않은가?", "label_en": "Is queue not empty?", "shape": "decision", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}, {"id": "n8", "label": "통지 검사 종료", "label_en": "Notify check ends", "shape": "box", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}], "edges": [{"from": "n0", "to": "n1", "label": "버퍼 완료 판정", "label_en": "Check buffer done", "evidence": [{"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "void PipelineHandlerVirtual::bufferCompleted(FrameBuffer *buffer)\n{\n\tRequest *request = buffer->request();"}, {"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "if (completeBuffer(request, buffer))\n\t\tcompleteRequest(request);\n}"}]}, {"from": "n1", "to": "n2", "label": "요청 미완료 · completeBuffer(request, buffer) [false]", "label_en": "Request incomplete · completeBuffer(request, buffer) [false]", "evidence": [{"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "if (completeBuffer(request, buffer))\n\t\tcompleteRequest(request);\n}"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "bool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"from": "n1", "to": "n3", "label": "요청 완료 판정 · completeBuffer(request, buffer) [true]", "label_en": "Request complete · completeBuffer(request, buffer) [true]", "evidence": [{"source": "virtual-principle/virtual-completion", "sha256": "28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da", "quote": "if (completeBuffer(request, buffer))\n\t\tcompleteRequest(request);\n}"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();"}]}, {"from": "n3", "to": "n7", "label": "큐 상태 확인", "label_en": "Check queue", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}, {"from": "n7", "to": "n4", "label": "남은 요청 있음 · !data->queuedRequests_.empty() [true]", "label_en": "Requests remain · !data->queuedRequests_.empty() [true]", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}, {"from": "n7", "to": "n8", "label": "큐 비어 있음 · !data->queuedRequests_.empty() [false]", "label_en": "Queue empty · !data->queuedRequests_.empty() [false]", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}, {"from": "n4", "to": "n6", "label": "RequestPending 상태 · req->status() == Request::RequestPending [true]", "label_en": "RequestPending state · req->status() == Request::RequestPending [true]", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}, {"from": "n4", "to": "n5", "label": "RequestPending 아님 · req->status() == Request::RequestPending [false]", "label_en": "Not RequestPending · req->status() == Request::RequestPending [false]", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "ASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}"}, {"source": "virtual-principle/camera-notification", "sha256": "aadfd6b4fdf910083a3d97fb11c623145f71553c9240f8e882d619fce61c43bb", "quote": "requestCompleted.emit(request);\n}"}, {"source": "virtual-principle/cam-signal-connection", "sha256": "837c0da1b2fd6f71aaabdb090306d3deda89c0fae6de39e91393d1111748e1b7", "quote": "camera_->requestCompleted.connect(this, &CameraSession::requestComplete);"}]}, {"from": "n5", "to": "n7", "label": "통지 후 큐 재확인", "label_en": "Recheck queue", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}, {"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "ASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}"}, {"source": "virtual-principle/camera-notification", "sha256": "aadfd6b4fdf910083a3d97fb11c623145f71553c9240f8e882d619fce61c43bb", "quote": "requestCompleted.emit(request);\n}"}]}, {"from": "n6", "to": "n8", "label": "반복 종료", "label_en": "Loop ends", "evidence": [{"source": "virtual-principle/pipeline-completion", "sha256": "eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "adfa719f8ed67d18fd8a0739fc088a1f8b9e7252", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "completion-flow": {"input_fingerprint": "0e722c0071a5f8f70d2ff1f9fbb331989995408be17f4c1f9afb891c8c17ea84", "draft": {"nodes": {"n0": {"label": "완료된 Request를 받아 CameraSession::requestComplete 진입", "label_en": "Enter CameraSession::requestComplete with Request", "shape": "process", "quote_ids": ["callback-and-processing:0", "app-start:4"]}, "n1": {"label": "Request 상태가 RequestCancelled인지 확인", "label_en": "Check whether Request status is RequestCancelled", "shape": "decision", "quote_ids": ["callback-and-processing:0"]}, "n2": {"label": "requestComplete가 즉시 반환, captureDone 신호 없음", "label_en": "requestComplete returns; no captureDone signal", "shape": "box", "quote_ids": ["callback-and-processing:0", "app-start:4"]}, "n3": {"label": "callLater로 이벤트 루프에 위임해 카메라 매니저 스레드 차단 회피", "label_en": "Defer via callLater; avoids blocking camera manager", "shape": "process", "quote_ids": ["callback-and-processing:1"]}, "n4": {"label": "진입 시 captureLimit_ 설정 AND captureCount_ 도달인지 확인", "label_en": "Entry: captureLimit_ set AND captureCount_ reached?", "shape": "decision", "quote_ids": ["callback-and-processing:2"]}, "n5": {"label": "processRequest가 즉시 반환, captureDone 신호 없이 종료", "label_en": "processRequest returns; no captureDone signal", "shape": "box", "quote_ids": ["callback-and-processing:1", "callback-and-processing:2", "callback-and-processing:10"]}, "n6": {"label": "프레임 정보 출력 후 captureCount_를 1 증가", "label_en": "Print frame info, then increment captureCount_ by 1", "shape": "process", "quote_ids": ["callback-and-processing:2", "callback-and-processing:11", "callback-and-processing:13", "app-start:1"]}, "n7": {"label": "증가 후 captureLimit_ 설정 AND captureCount_ 도달인지 확인", "label_en": "Check: captureLimit_ set AND captureCount_ reached?", "shape": "decision", "quote_ids": ["callback-and-processing:2", "callback-and-processing:13", "app-start:1"]}, "n8": {"label": "captureDone.emit() 신호 후 processRequest가 반환", "label_en": "Emit captureDone, then processRequest returns", "shape": "box", "quote_ids": ["callback-and-processing:2", "callback-and-processing:13"]}, "n9": {"label": "Request::ReuseBuffers로 버퍼 유지 후 queueRequest 호출", "label_en": "Keep buffers (Request::ReuseBuffers); queueRequest", "shape": "process", "quote_ids": ["callback-and-processing:15"]}}, "edges": [{"from": "n0", "to": "n1", "label": "취소 여부 확인", "label_en": "Check cancel status", "condition_ref": "always", "quote_ids": ["callback-and-processing:0"]}, {"from": "n1", "to": "n2", "label": "취소 상태면", "label_en": "If cancelled", "condition_ref": "c9:true", "quote_ids": ["callback-and-processing:0"]}, {"from": "n1", "to": "n3", "label": "취소 아니면", "label_en": "If not cancelled", "condition_ref": "c9:false", "quote_ids": ["callback-and-processing:0", "callback-and-processing:1"]}, {"from": "n3", "to": "n4", "label": "이벤트 루프 실행", "label_en": "Event loop runs", "condition_ref": "always", "quote_ids": ["callback-and-processing:1", "callback-and-processing:2"]}, {"from": "n4", "to": "n5", "label": "한도 설정 AND 도달", "label_en": "Limit set & reached", "condition_ref": "c4:true", "quote_ids": ["callback-and-processing:2"]}, {"from": "n4", "to": "n6", "label": "미설정 또는 미도달", "label_en": "Unset or not reached", "condition_ref": "c4:false", "quote_ids": ["callback-and-processing:2", "callback-and-processing:11"]}, {"from": "n6", "to": "n7", "label": "증가 후 확인", "label_en": "Then check", "condition_ref": "always", "quote_ids": ["callback-and-processing:13"]}, {"from": "n7", "to": "n8", "label": "한도 설정 AND 도달", "label_en": "Limit set & reached", "condition_ref": "c4:true", "quote_ids": ["callback-and-processing:13"]}, {"from": "n7", "to": "n9", "label": "미설정 또는 미도달", "label_en": "Unset or not reached", "condition_ref": "c4:false", "quote_ids": ["callback-and-processing:13", "callback-and-processing:15"]}]}, "graph": {"id": "completion-flow", "topic": "flow", "kind": "decision", "title": "기록된 출력 싱크 미요청 콜백 경로", "question": "기록된 출력 싱크 미요청 경로에서 완료 콜백은 어떤 처리와 종료로 이어집니까?", "condition_display": "evidence", "nodes": [{"id": "n0", "label": "완료된 Request를 받아 CameraSession::requestComplete 진입", "label_en": "Enter CameraSession::requestComplete with Request", "shape": "box", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;"}, {"source": "flow/app-start", "sha256": "6f04ac47e3fa6496c3bc271f987bee51f2793e64b360223d3455b6c080c684f0", "quote": "camera_->requestCompleted.connect(this, &CameraSession::requestComplete);"}]}, {"id": "n1", "label": "Request 상태가 RequestCancelled인지 확인", "label_en": "Check whether Request status is RequestCancelled", "shape": "decision", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;"}]}, {"id": "n2", "label": "requestComplete가 즉시 반환, captureDone 신호 없음", "label_en": "requestComplete returns; no captureDone signal", "shape": "box", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;"}, {"source": "flow/app-start", "sha256": "6f04ac47e3fa6496c3bc271f987bee51f2793e64b360223d3455b6c080c684f0", "quote": "camera_->requestCompleted.connect(this, &CameraSession::requestComplete);"}]}, {"id": "n3", "label": "callLater로 이벤트 루프에 위임해 카메라 매니저 스레드 차단 회피", "label_en": "Defer via callLater; avoids blocking camera manager", "shape": "box", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}"}]}, {"id": "n4", "label": "진입 시 captureLimit_ 설정 AND captureCount_ 도달인지 확인", "label_en": "Entry: captureLimit_ set AND captureCount_ reached?", "shape": "decision", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}]}, {"id": "n5", "label": "processRequest가 즉시 반환, captureDone 신호 없이 종료", "label_en": "processRequest returns; no captureDone signal", "shape": "box", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "if (sink_) {\n\t\tif (!sink_->processRequest(request))\n\t\t\trequeue = false;\n\t}"}]}, {"id": "n6", "label": "프레임 정보 출력 후 captureCount_를 1 증가", "label_en": "Print frame info, then increment captureCount_ by 1", "shape": "box", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "std::cout << info.str() << std::endl;"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}"}, {"source": "flow/app-start", "sha256": "6f04ac47e3fa6496c3bc271f987bee51f2793e64b360223d3455b6c080c684f0", "quote": "queueCount_ = 0;\n\tcaptureCount_ = 0;\n\tcaptureLimit_ = options_[OptCapture].toInteger();\n\tprintMetadata_ = options_.isSet(OptMetadata);"}]}, {"id": "n7", "label": "증가 후 captureLimit_ 설정 AND captureCount_ 도달인지 확인", "label_en": "Check: captureLimit_ set AND captureCount_ reached?", "shape": "decision", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}"}, {"source": "flow/app-start", "sha256": "6f04ac47e3fa6496c3bc271f987bee51f2793e64b360223d3455b6c080c684f0", "quote": "queueCount_ = 0;\n\tcaptureCount_ = 0;\n\tcaptureLimit_ = options_[OptCapture].toInteger();\n\tprintMetadata_ = options_.isSet(OptMetadata);"}]}, {"id": "n8", "label": "captureDone.emit() 신호 후 processRequest가 반환", "label_en": "Emit captureDone, then processRequest returns", "shape": "box", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}"}]}, {"id": "n9", "label": "Request::ReuseBuffers로 버퍼 유지 후 queueRequest 호출", "label_en": "Keep buffers (Request::ReuseBuffers); queueRequest", "shape": "box", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "request->reuse(Request::ReuseBuffers);\n\tqueueRequest(request);\n}"}]}], "edges": [{"from": "n0", "to": "n1", "label": "취소 여부 확인", "label_en": "Check cancel status", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;"}]}, {"from": "n1", "to": "n2", "label": "취소 상태면 · request->status() == Request::RequestCancelled [true]", "label_en": "If cancelled · request->status() == Request::RequestCancelled [true]", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;"}]}, {"from": "n1", "to": "n3", "label": "취소 아니면 · request->status() == Request::RequestCancelled [false]", "label_en": "If not cancelled · request->status() == Request::RequestCancelled [false]", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::requestComplete(Request *request)\n{\n\tif (request->status() == Request::RequestCancelled)\n\t\treturn;"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}"}]}, {"from": "n3", "to": "n4", "label": "이벤트 루프 실행", "label_en": "Event loop runs", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Defer processing of the completed request to the event loop, to avoid\n\t * blocking the camera manager thread.\n\t */\n\tEventLoop::instance()->callLater([this, request]() { processRequest(request); });\n}"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}]}, {"from": "n4", "to": "n5", "label": "한도 설정 AND 도달 · captureLimit_ && captureCount_ >= captureLimit_ [true]", "label_en": "Limit set & reached · captureLimit_ && captureCount_ >= captureLimit_ [true]", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}]}, {"from": "n4", "to": "n6", "label": "미설정 또는 미도달 · captureLimit_ && captureCount_ >= captureLimit_ [false]", "label_en": "Unset or not reached · captureLimit_ && captureCount_ >= captureLimit_ [false]", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "void CameraSession::processRequest(Request *request)\n{\n\t/*\n\t * If we've reached the capture limit, we're done. This doesn't\n\t * duplicate the check below that emits the captureDone signal, as this\n\t * function will be called for each request still in flight after the\n\t * capture limit is reached and we don't want to emit the signal every\n\t * single time.\n\t */\n\tif (captureLimit_ && captureCount_ >= captureLimit_)\n\t\treturn;"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "std::cout << info.str() << std::endl;"}]}, {"from": "n6", "to": "n7", "label": "증가 후 확인", "label_en": "Then check", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}"}]}, {"from": "n7", "to": "n8", "label": "한도 설정 AND 도달 · captureLimit_ && captureCount_ >= captureLimit_ [true]", "label_en": "Limit set & reached · captureLimit_ && captureCount_ >= captureLimit_ [true]", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}"}]}, {"from": "n7", "to": "n9", "label": "미설정 또는 미도달 · captureLimit_ && captureCount_ >= captureLimit_ [false]", "label_en": "Unset or not reached · captureLimit_ && captureCount_ >= captureLimit_ [false]", "evidence": [{"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "/*\n\t * Notify the user that capture is complete if the limit has just been\n\t * reached.\n\t */\n\tcaptureCount_++;\n\tif (captureLimit_ && captureCount_ >= captureLimit_) {\n\t\tcaptureDone.emit();\n\t\treturn;\n\t}"}, {"source": "flow/callback-and-processing", "sha256": "1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d", "quote": "request->reuse(Request::ReuseBuffers);\n\tqueueRequest(request);\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "adfa719f8ed67d18fd8a0739fc088a1f8b9e7252", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}}, "body_sha256": "dd25f45cf588828d24e18e9e06668ef5febad5e69da726e33f775c92b7daec70"}
---

# WSL 공식 cam 가상 캡처 확인

**가상 캡처가 막힌 지점부터 확인하고, 완료 알림이 프레임 처리로 이어지는 경로를 따라가세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 이번 기준 재현에서 기본 WSL 커널은 DMA-BUF 할당기를 노출하지 않았고, 공식 cam은 버퍼를 할당하지 못했습니다. | [할당기를 준비하자 공식 cam 캡처가 완료됐습니다](#할당기를-준비하자-공식-cam-캡처가-완료됐습니다) |
| 고정 libcamera 소스에서 virtual 파이프라인은 실제 센서 대신 소프트웨어 테스트 패턴이나 이미지 입력으로 가상 카메라를 에뮬레이션합니다. | [가상 파이프라인이 영상을 만들고 요청 완료를 알립니다](#가상-파이프라인이-영상을-만들고-요청-완료를-알립니다) |
| 기록된 단일 스트림과 출력 옵션 미요청 범위에서 cam은 버퍼를 할당해 각 초기 요청에 연결합니다. | [여러 초기 요청을 단일 스트림에 맞춰 준비합니다](#여러-초기-요청을-단일-스트림에-맞춰-준비합니다) |
| cam은 요청을 준비하고 카메라를 시작한 뒤 한도 안에서만 제출하며, 한도 도달 시 제출을 생략하고 0을 반환합니다. | [준비된 초기 요청을 한도 안에서 제출합니다](#준비된-초기-요청을-한도-안에서-제출합니다) |
| `CameraSession::requestComplete`는 요청 상태가 `RequestCancelled`이면 반환하고, 그 밖에는 `callLater`로 `CameraSession::processRequest`를 이벤트 루프에 미룹니다. | [cam이 완료 알림을 받아 이벤트 루프에서 프레임을 처리합니다.](#cam이-완료-알림을-받아-이벤트-루프에서-프레임을-처리합니다) |
| **준비 (1–3)** 호스트 상태를 바꾸지 않고 사용할 커널의 Kconfig와 의존 조건을 조사하세요. | [지원 커널과 장치 접근을 확인한 뒤 재현합니다](#지원-커널과-장치-접근을-확인한-뒤-재현합니다) |

## 할당기를 준비하자 공식 cam 캡처가 완료됐습니다

**가상 시험 구성입니다. 실제 제품의 지원·성능 주장으로 사용하지 마세요.**

이번 기준 재현에서 기본 WSL 커널은 DMA-BUF 할당기를 노출하지 않았고, 공식 cam은 버퍼를 할당하지 못했습니다. `product-evidence/libcamera-official-cam-trial/official-cam-reader.txt:1`

<!-- sdd:visual:observed-kernel-boundaries -->
### 기본 커널·시험 커널·복구 후 관측 범위

```mermaid
flowchart TB
%% sdd:translations {"공식 cam 관측": "Official cam observation", "공식 cam의 Virtual2 캡처는 <br/>세 실행에서 각각 3프레임을 <br/>완료했습니다.": "Official cam completed <br/>three Virtual2 frames in <br/>each of three runs.", "기본 WSL 커널은 DMA-BUF <br/>할당기를 노출하지 <br/>않았습니다.": "The default WSL kernel did <br/>not expose a DMA-BUF <br/>allocator.", "기본 커널을 복구했고 <br/>.wslconfig는 없었습니다.": "The default kernel was <br/>restored and .wslconfig was <br/>absent.", "별도 DMA-BUF 프로브는 <br/>4,096바이트를 할당하고 <br/>CPU로 접근했습니다.": "The separate DMA-BUF probe <br/>allocated 4,096 bytes and <br/>accessed them on the CPU.", "별도 프로브 관측": "Separate probe observation", "시험 WSL2 커널에 udmabuf이 <br/>내장돼 있었습니다.": "The test WSL2 kernel had <br/>built-in udmabuf.", "시험 구성": "Test configuration", "시험 후 복구": "Restored after the trial"}
  v_baseline["기본 WSL 커널은 DMA-BUF <br/>할당기를 노출하지 <br/>않았습니다."]
  v_trial["시험 WSL2 커널에 udmabuf이 <br/>내장돼 있었습니다."]
  v_camera["공식 cam의 Virtual2 캡처는 <br/>세 실행에서 각각 3프레임을 <br/>완료했습니다."]
  v_cpu["별도 DMA-BUF 프로브는 <br/>4,096바이트를 할당하고 <br/>CPU로 접근했습니다."]
  v_restored["기본 커널을 복구했고 <br/>.wslconfig는 없었습니다."]
  v_baseline -->|"시험 구성"| v_trial
  v_trial -->|"공식 cam 관측"| v_camera
  v_trial -->|"별도 프로브 관측"| v_cpu
  v_trial -->|"시험 후 복구"| v_restored
```

[Mermaid 원문](official-cam-validation.observed-kernel-boundaries.mmd)

??? note "그림 근거와 확인 범위"
    어느 커널에서 공식 cam과 별도 DMA-BUF 프로브를 관찰했으며 시험 종료 시 어떤 상태였습니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The default WSL kernel did not expose a DMA-BUF allocator.">기본 WSL 커널은 DMA-BUF 할당기를 노출하지 않았습니다.</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
    | <span data-sdd-label-en="The test WSL2 kernel had built-in udmabuf.">시험 WSL2 커널에 udmabuf이 내장돼 있었습니다.</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
    | <span data-sdd-label-en="Official cam completed three Virtual2 frames in each of three runs.">공식 cam의 Virtual2 캡처는 세 실행에서 각각 3프레임을 완료했습니다.</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) · [product-evidence/libcamera-official-cam-trial/official-cam-reader.txt:1](#source-d84e6ca3abcfec11) |
    | <span data-sdd-label-en="The separate DMA-BUF probe allocated 4,096 bytes and accessed them on the CPU.">별도 DMA-BUF 프로브는 4,096바이트를 할당하고 CPU로 접근했습니다.</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
    | <span data-sdd-label-en="The default kernel was restored and .wslconfig was absent.">기본 커널을 복구했고 .wslconfig는 없었습니다.</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
    | <span data-sdd-label-en="Test configuration">시험 구성</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
    | <span data-sdd-label-en="Official cam observation">공식 cam 관측</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
    | <span data-sdd-label-en="Separate probe observation">별도 프로브 관측</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
    | <span data-sdd-label-en="Restored after the trial">시험 후 복구</span> | [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc) |
<!-- /sdd:visual:observed-kernel-boundaries -->

승인된 UDMABUF 시험 커널의 WSL 가상 파이프라인 시뮬레이션에서 수정하지 않은 공식 cam이 Virtual2 400x300 NV12로 세 독립 프로세스에서 실행되어, 각 실행의 3프레임 정상 완료와 udmabuf 할당 성공이 관측되었습니다. 별도 DMA-BUF 프로브에서는 CPU 접근 성공이 관측되었습니다. 시험 후 기본 커널로 원복되어 현재 상태 그대로는 이 시험을 재실행할 수 없습니다. `product-evidence/libcamera-official-cam-trial/official-cam-reader.txt:1`, `product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1`

근거 원문: [product-evidence/libcamera-official-cam-trial/execution-contract.txt:1](#source-6722470b9620a771) · [product-evidence/libcamera-official-cam-trial/official-cam-reader.txt:1](#source-d84e6ca3abcfec11) · [product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1](#source-10812730226e86cc)

## 가상 파이프라인이 영상을 만들고 요청 완료를 알립니다

고정 libcamera 소스에서 virtual 파이프라인은 실제 센서 대신 소프트웨어 테스트 패턴이나 이미지 입력으로 가상 카메라를 에뮬레이션합니다. 선택한 Virtual2 설정은 400x300 lines 패턴을 공급합니다. 버퍼 할당이 성공하면 cam은 실제 DMA-BUF 버퍼를 요청에 붙여 전달을 준비합니다. NV12 형식에서는 CPU가 변환과 매핑된 버퍼 쓰기를 함께 시도합니다. `src/libcamera/pipeline/virtual/README.md:3`, `src/libcamera/pipeline/virtual/data/virtual.yaml:28`, `src/apps/cam/camera_session.cpp:365`, `src/libcamera/framebuffer_allocator.cpp:86`, `src/libcamera/camera.cpp:963`, `src/libcamera/pipeline/virtual/virtual.cpp:356`, `src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47`

<!-- sdd:visual:virtual-dmabuf-attachment -->
### 가상 DMA-BUF 할당과 cam 요청 연결

```mermaid
flowchart TB
%% sdd:translations {"cam은 구성된 스트림에 <br/>allocate#40;#41;를 호출합니다.": "cam calls allocate#40;#41; for <br/>the configured stream.", "cam은 새 요청에 해당 <br/>인덱스의 스트림 버퍼를 <br/>addBuffer#40;#41;로 연결합니다.": "cam uses addBuffer#40;#41; to <br/>attach the indexed stream <br/>buffer to the new request.", "가상 DMA-BUF 할당기가 <br/>유효합니까?": "Is the virtual DMA-BUF <br/>allocator valid?", "가상 파이프라인은 <br/>-ENOBUFS를 반환하고 cam은 <br/>할당 실패로 -ENOMEM을 <br/>반환합니다.": "The virtual pipeline <br/>returns -ENOBUFS and cam <br/>returns -ENOMEM for <br/>allocation failure.", "가상 파이프라인은 플레인 <br/>크기와 구성의 버퍼 수로 <br/>내보냅니다.": "The virtual pipeline <br/>exports using plane sizes <br/>and the configured buffer <br/>count.", "검사 통과 후": "After checks pass", "아니오": "No", "예": "Yes", "카메라는 구성 상태와 활성 <br/>스트림을 검사한 뒤 <br/>파이프라인에 동기 <br/>위임합니다.": "Camera checks configured <br/>state and active stream, <br/>then calls the pipeline <br/>with blocking delivery.", "카메라로 전달": "Pass to Camera", "할당 성공 후": "After successful allocation"}
  v_allocate["cam은 구성된 스트림에 <br/>allocate#40;#41;를 호출합니다."]
  v_camera_export["카메라는 구성 상태와 활성 <br/>스트림을 검사한 뒤 <br/>파이프라인에 동기 <br/>위임합니다."]
  v_virtual_guard{"가상 DMA-BUF 할당기가 <br/>유효합니까?"}
  v_failure["가상 파이프라인은 <br/>-ENOBUFS를 반환하고 cam은 <br/>할당 실패로 -ENOMEM을 <br/>반환합니다."]
  v_export["가상 파이프라인은 플레인 <br/>크기와 구성의 버퍼 수로 <br/>내보냅니다."]
  v_attach["cam은 새 요청에 해당 <br/>인덱스의 스트림 버퍼를 <br/>addBuffer#40;#41;로 연결합니다."]
  v_allocate -->|"카메라로 전달"| v_camera_export
  v_camera_export -->|"검사 통과 후"| v_virtual_guard
  v_virtual_guard -->|"아니오"| v_failure
  v_virtual_guard -->|"예"| v_export
  v_export -->|"할당 성공 후"| v_attach
```

[Mermaid 원문](official-cam-validation.virtual-dmabuf-attachment.mmd)

??? note "그림 근거와 확인 범위"
    가상 파이프라인이 DMA-BUF를 내보내고 cam이 요청에 연결하기까지 어떤 호출과 조건을 거칩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="cam calls allocate() for the configured stream.">cam은 구성된 스트림에 allocate&#40;&#41;를 호출합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Camera checks configured state and active stream, then calls the pipeline with blocking delivery.">카메라는 구성 상태와 활성 스트림을 검사한 뒤 파이프라인에 동기 위임합니다.</span> | [src/libcamera/camera.cpp:963](#source-80fd4657ae4c65d1) |
    | <span data-sdd-label-en="Is the virtual DMA-BUF allocator valid?">가상 DMA-BUF 할당기가 유효합니까?</span> | [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) |
    | <span data-sdd-label-en="The virtual pipeline returns -ENOBUFS and cam returns -ENOMEM for allocation failure.">가상 파이프라인은 -ENOBUFS를 반환하고 cam은 할당 실패로 -ENOMEM을 반환합니다.</span> | [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) · [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="The virtual pipeline exports using plane sizes and the configured buffer count.">가상 파이프라인은 플레인 크기와 구성의 버퍼 수로 내보냅니다.</span> | [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) |
    | <span data-sdd-label-en="cam uses addBuffer() to attach the indexed stream buffer to the new request.">cam은 새 요청에 해당 인덱스의 스트림 버퍼를 addBuffer&#40;&#41;로 연결합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Pass to Camera">카메라로 전달</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) · [src/libcamera/framebuffer_allocator.cpp:86](#source-e91194807faa9e0c) · [src/libcamera/camera.cpp:963](#source-80fd4657ae4c65d1) |
    | <span data-sdd-label-en="After checks pass">검사 통과 후</span> | [src/libcamera/camera.cpp:963](#source-80fd4657ae4c65d1) · [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) |
    | <span data-sdd-label-en="No">아니오</span> | [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) · [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) |
    | <span data-sdd-label-en="After successful allocation">할당 성공 후</span> | [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) · [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
<!-- /sdd:visual:virtual-dmabuf-attachment -->

<!-- sdd:visual:virtual-frame-path -->
### Virtual2 줄 패턴 NV12 변환·기록 시도 흐름

```mermaid
flowchart TB
%% sdd:translations {"NV12 형식에서 CPU가 <br/>Virtual2 lines 패턴 변환과 <br/>매핑 쓰기 시도": "For NV12: CPU tries <br/>Virtual2 lines conversion <br/>and mapped write", "PipelineHandler::<br/>queueRequest가 요청을 대기 <br/>목록에 넣고 준비 시도": "PipelineHandler::<br/>queueRequest adds request; <br/>tries preparation", "queued 호출 + 목표 시각": "Queued call + target", "가상 핸들러가 queued 호출로 <br/>요청 처리와 목표 시각 <br/>인수를 넘김": "Virtual handler queues <br/>request; target time is an <br/>argument", "두 경우 모두 <br/>bufferCompleted로 버퍼 완료 <br/>신호; 요청 완료는 별도": "Both emit buffer <br/>completion; request <br/>completion separate", "변환·매핑 쓰기로": "To conversion step", "생성 결과 반환": "Return frame result", "생성 전 FrameSuccess 초기화 <br/>뒤, CPU 쓰기 동기화 <br/>범위에서 쓰기용 DMA-BUF <br/>매핑 시도": "Init FrameSuccess pre-call; <br/>try DMA-BUF map in CPU <br/>write sync", "수신 측 <br/>VirtualCameraData::<br/>processRequest가 목표 <br/>시각까지 대기": "Receiver <br/>VirtualCameraData::<br/>processRequest waits until <br/>target", "오류: FrameError로 변경 <br/>#91;true#93;": "Becomes FrameError #91;true#93;", "일치 스트림만 프레임 생성": "Matching stream only", "정상: FrameSuccess 유지 <br/>#91;false#93;": "Keeps FrameSuccess #91;false#93;", "준비 완료 후 차례 확인": "Once prepared", "준비된 요청이 차례에 취소 <br/>상태입니까?": "Is the prepared request <br/>cancelled at its turn?", "취소 아님 #91;false#93;": "Not cancelled #91;false#93;", "취소된 요청은 <br/>RequestCancelled; 큐 앞부터 <br/>완료 통지, 앞 <br/>RequestPending이면 보류·중단": "RequestCancelled request; <br/>notify front; Stop at <br/>RequestPending", "취소됨 #91;true#93;": "Cancelled #91;true#93;", "프레임 생성 결과가 <br/>오류입니까?": "Is the frame generation <br/>result an error?"}
  v_n0["PipelineHandler::<br/>queueRequest가 요청을 대기 <br/>목록에 넣고 준비 시도"]
  v_n1{"준비된 요청이 차례에 취소 <br/>상태입니까?"}
  v_n2["취소된 요청은 <br/>RequestCancelled; 큐 앞부터 <br/>완료 통지, 앞 <br/>RequestPending이면 보류·중단"]
  v_n3["가상 핸들러가 queued 호출로 <br/>요청 처리와 목표 시각 <br/>인수를 넘김"]
  v_n4["수신 측 <br/>VirtualCameraData::<br/>processRequest가 목표 <br/>시각까지 대기"]
  v_n5["생성 전 FrameSuccess 초기화 <br/>뒤, CPU 쓰기 동기화 <br/>범위에서 쓰기용 DMA-BUF <br/>매핑 시도"]
  v_n6["NV12 형식에서 CPU가 <br/>Virtual2 lines 패턴 변환과 <br/>매핑 쓰기 시도"]
  v_n7{"프레임 생성 결과가 <br/>오류입니까?"}
  v_n8["두 경우 모두 <br/>bufferCompleted로 버퍼 완료 <br/>신호; 요청 완료는 별도"]
  v_n0 -->|"준비 완료 후 차례 확인"| v_n1
  v_n1 -->|"취소됨 #91;true#93;"| v_n2
  v_n1 -->|"취소 아님 #91;false#93;"| v_n3
  v_n3 -->|"queued 호출 + 목표 시각"| v_n4
  v_n4 -->|"일치 스트림만 프레임 생성"| v_n5
  v_n5 -->|"변환·매핑 쓰기로"| v_n6
  v_n6 -->|"생성 결과 반환"| v_n7
  v_n7 -->|"오류: FrameError로 변경 <br/>#91;true#93;"| v_n8
  v_n7 -->|"정상: FrameSuccess 유지 <br/>#91;false#93;"| v_n8
```

[Mermaid 원문](official-cam-validation.virtual-frame-path.mmd)

??? note "그림 근거와 확인 범위"
    버퍼를 연결한 뒤 가상 파이프라인은 CPU 패턴 기록을 어떻게 시도하고 버퍼 완료를 어떻게 알립니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="PipelineHandler::queueRequest adds request; tries preparation">PipelineHandler::queueRequest가 요청을 대기 목록에 넣고 준비 시도</span> | [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) · [src/libcamera/pipeline_handler.cpp:435](#source-4fe013027055fa2d) |
    | <span data-sdd-label-en="Is the prepared request cancelled at its turn?">준비된 요청이 차례에 취소 상태입니까?</span> | [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) |
    | <span data-sdd-label-en="RequestCancelled request; notify front; Stop at RequestPending">취소된 요청은 RequestCancelled; 큐 앞부터 완료 통지, 앞 RequestPending이면 보류·중단</span> | [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) · [src/libcamera/pipeline_handler.cpp:435](#source-4fe013027055fa2d) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) · [src/libcamera/request.cpp:125](#source-0626196def047e5c) · [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) |
    | <span data-sdd-label-en="Virtual handler queues request; target time is an argument">가상 핸들러가 queued 호출로 요청 처리와 목표 시각 인수를 넘김</span> | [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) · [src/libcamera/pipeline/virtual/virtual.cpp:412](#source-1c0d5dcdba46688e) |
    | <span data-sdd-label-en="Receiver VirtualCameraData::processRequest waits until target">수신 측 VirtualCameraData::processRequest가 목표 시각까지 대기</span> | [src/libcamera/pipeline/virtual/virtual.cpp:412](#source-1c0d5dcdba46688e) · [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) |
    | <span data-sdd-label-en="Init FrameSuccess pre-call; try DMA-BUF map in CPU write sync">생성 전 FrameSuccess 초기화 뒤, CPU 쓰기 동기화 범위에서 쓰기용 DMA-BUF 매핑 시도</span> | [src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47](#source-fa5429fa2c62882d) · [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) |
    | <span data-sdd-label-en="For NV12: CPU tries Virtual2 lines conversion and mapped write">NV12 형식에서 CPU가 Virtual2 lines 패턴 변환과 매핑 쓰기 시도</span> | [src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47](#source-fa5429fa2c62882d) · [src/libcamera/pipeline/virtual/data/virtual.yaml:28](#source-9858e22e2225cc10) |
    | <span data-sdd-label-en="Is the frame generation result an error?">프레임 생성 결과가 오류입니까?</span> | [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) · [src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47](#source-fa5429fa2c62882d) |
    | <span data-sdd-label-en="Both emit buffer completion; request completion separate">두 경우 모두 bufferCompleted로 버퍼 완료 신호; 요청 완료는 별도</span> | [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) · [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) · [src/libcamera/pipeline/virtual/virtual.cpp:373](#source-4726a7d0b3f38c49) |
    | <span data-sdd-label-en="Once prepared">준비 완료 후 차례 확인</span> | [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) · [src/libcamera/pipeline_handler.cpp:435](#source-4fe013027055fa2d) |
    | <span data-sdd-label-en="Cancelled · request-&gt;_d()-&gt;cancelled_ [true]">취소됨 · request-&gt;&#95;d&#40;&#41;-&gt;cancelled&#95; &#91;true&#93;</span> | [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Not cancelled · request-&gt;_d()-&gt;cancelled_ [false]">취소 아님 · request-&gt;&#95;d&#40;&#41;-&gt;cancelled&#95; &#91;false&#93;</span> | [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) |
    | <span data-sdd-label-en="Queued call + target">queued 호출 + 목표 시각</span> | [src/libcamera/pipeline/virtual/virtual.cpp:412](#source-1c0d5dcdba46688e) |
    | <span data-sdd-label-en="Matching stream only">일치 스트림만 프레임 생성</span> | [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) · [src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47](#source-fa5429fa2c62882d) |
    | <span data-sdd-label-en="To conversion step">변환·매핑 쓰기로</span> | [src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47](#source-fa5429fa2c62882d) · [src/libcamera/pipeline/virtual/data/virtual.yaml:28](#source-9858e22e2225cc10) |
    | <span data-sdd-label-en="Return frame result">생성 결과 반환</span> | [src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47](#source-fa5429fa2c62882d) |
    | <span data-sdd-label-en="Becomes FrameError · streamConfig.frameGenerator-&gt;generateFrame( stream-&gt;configuration(), buffer) [true]">오류: FrameError로 변경 · streamConfig.frameGenerator-&gt;generateFrame&#40; stream-&gt;configuration&#40;&#41;, buffer&#41; &#91;true&#93;</span> | [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) |
    | <span data-sdd-label-en="Keeps FrameSuccess · streamConfig.frameGenerator-&gt;generateFrame( stream-&gt;configuration(), buffer) [false]">정상: FrameSuccess 유지 · streamConfig.frameGenerator-&gt;generateFrame&#40; stream-&gt;configuration&#40;&#41;, buffer&#41; &#91;false&#93;</span> | [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) |
<!-- /sdd:visual:virtual-frame-path -->

<!-- sdd:visual:request-completion-order -->
### 버퍼 완료와 요청 완료·순서 통지는 별개입니다

```mermaid
flowchart TB
%% sdd:translations {"RequestPending 상태 #91;true#93;": "RequestPending state #91;true#93;", "RequestPending 아님 #91;false#93;": "Not RequestPending #91;false#93;", "bufferCompleted: 가상 <br/>프레임 버퍼 완료 수신": "bufferCompleted: receive <br/>virtual buffer done", "completeBuffer 판정: 요청의 <br/>모든 버퍼 완료 여부": "completeBuffer check: all <br/>request buffers done?", "나머지 버퍼 대기. <br/>completeRequest 미호출": "Wait for remaining buffers; <br/>no completeRequest", "남은 요청 있음 #91;true#93;": "Requests remain #91;true#93;", "뒤 요청 통지 보류, 반복 중단": "Hold later notifies, stop <br/>loop", "맨 앞 꺼내 requestComplete <br/>호출, requestCompleted 통지": "Pop head; requestComplete <br/>emits requestCompleted", "반복 종료": "Loop ends", "버퍼 완료 판정": "Check buffer done", "상태 표시: 정상 <br/>RequestComplete, 취소 <br/>RequestCancelled": "Normal RequestComplete; <br/>cancel RequestCancelled", "요청 미완료 #91;false#93;": "Request incomplete #91;false#93;", "요청 완료 판정 #91;true#93;": "Request complete #91;true#93;", "큐 맨 앞 요청이 <br/>RequestPending 상태인지 판정": "Is front request in <br/>RequestPending state?", "큐 비어 있음 #91;false#93;": "Queue empty #91;false#93;", "큐 상태 확인": "Check queue", "큐가 비어 있지 않은가?": "Is queue not empty?", "통지 검사 종료": "Notify check ends", "통지 후 큐 재확인": "Recheck queue"}
  v_n0["bufferCompleted: 가상 <br/>프레임 버퍼 완료 수신"]
  v_n1{"completeBuffer 판정: 요청의 <br/>모든 버퍼 완료 여부"}
  v_n2["나머지 버퍼 대기. <br/>completeRequest 미호출"]
  v_n3["상태 표시: 정상 <br/>RequestComplete, 취소 <br/>RequestCancelled"]
  v_n4{"큐 맨 앞 요청이 <br/>RequestPending 상태인지 판정"}
  v_n5["맨 앞 꺼내 requestComplete <br/>호출, requestCompleted 통지"]
  v_n6["뒤 요청 통지 보류, 반복 중단"]
  v_n7{"큐가 비어 있지 않은가?"}
  v_n8["통지 검사 종료"]
  v_n0 -->|"버퍼 완료 판정"| v_n1
  v_n1 -->|"요청 미완료 #91;false#93;"| v_n2
  v_n1 -->|"요청 완료 판정 #91;true#93;"| v_n3
  v_n3 -->|"큐 상태 확인"| v_n7
  v_n7 -->|"남은 요청 있음 #91;true#93;"| v_n4
  v_n7 -->|"큐 비어 있음 #91;false#93;"| v_n8
  v_n4 -->|"RequestPending 상태 #91;true#93;"| v_n6
  v_n4 -->|"RequestPending 아님 #91;false#93;"| v_n5
  v_n5 -->|"통지 후 큐 재확인"| v_n7
  v_n6 -->|"반복 종료"| v_n8
```

[Mermaid 원문](official-cam-validation.request-completion-order.mmd)

??? note "그림 근거와 확인 범위"
    가상 버퍼 완료 경로의 모든 버퍼 완료 판정과, 완료 표시 뒤 제출 순서 큐의 연속 통지 및 반복 종료는 어떻게 연결됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="bufferCompleted: receive virtual buffer done">bufferCompleted: 가상 프레임 버퍼 완료 수신</span> | [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) |
    | <span data-sdd-label-en="completeBuffer check: all request buffers done?">completeBuffer 판정: 요청의 모든 버퍼 완료 여부</span> | [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Wait for remaining buffers; no completeRequest">나머지 버퍼 대기. completeRequest 미호출</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Normal RequestComplete; cancel RequestCancelled">상태 표시: 정상 RequestComplete, 취소 RequestCancelled</span> | [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) · [src/libcamera/request.cpp:125](#source-0626196def047e5c) |
    | <span data-sdd-label-en="Is front request in RequestPending state?">큐 맨 앞 요청이 RequestPending 상태인지 판정</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Pop head; requestComplete emits requestCompleted">맨 앞 꺼내 requestComplete 호출, requestCompleted 통지</span> | [src/libcamera/camera.cpp:1481](#source-655b027df7d08524) · [src/apps/cam/camera_session.cpp:305](#source-fb9506413ce52fb0) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Hold later notifies, stop loop">뒤 요청 통지 보류, 반복 중단</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Is queue not empty?">큐가 비어 있지 않은가?</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Notify check ends">통지 검사 종료</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Check buffer done">버퍼 완료 판정</span> | [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) |
    | <span data-sdd-label-en="Request incomplete · completeBuffer(request, buffer) [false]">요청 미완료 · completeBuffer&#40;request, buffer&#41; &#91;false&#93;</span> | [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Request complete · completeBuffer(request, buffer) [true]">요청 완료 판정 · completeBuffer&#40;request, buffer&#41; &#91;true&#93;</span> | [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Check queue">큐 상태 확인</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Requests remain · !data-&gt;queuedRequests_.empty() [true]">남은 요청 있음 · &#33;data-&gt;queuedRequests&#95;.empty&#40;&#41; &#91;true&#93;</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Queue empty · !data-&gt;queuedRequests_.empty() [false]">큐 비어 있음 · &#33;data-&gt;queuedRequests&#95;.empty&#40;&#41; &#91;false&#93;</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="RequestPending state · req-&gt;status() == Request::RequestPending [true]">RequestPending 상태 · req-&gt;status&#40;&#41; == Request::RequestPending &#91;true&#93;</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
    | <span data-sdd-label-en="Not RequestPending · req-&gt;status() == Request::RequestPending [false]">RequestPending 아님 · req-&gt;status&#40;&#41; == Request::RequestPending &#91;false&#93;</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) · [src/libcamera/camera.cpp:1481](#source-655b027df7d08524) · [src/apps/cam/camera_session.cpp:305](#source-fb9506413ce52fb0) |
    | <span data-sdd-label-en="Recheck queue">통지 후 큐 재확인</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) · [src/libcamera/camera.cpp:1481](#source-655b027df7d08524) |
    | <span data-sdd-label-en="Loop ends">반복 종료</span> | [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) |
<!-- /sdd:visual:request-completion-order -->

패턴 생성기는 쓰기 동기화를 시도한 뒤 그 범위에서 버퍼의 쓰기용 매핑을 시도합니다. `src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47`

가상 요청은 비동기로 전달되며 `VirtualCameraData::processRequest`는 목표 시각까지 기다린 뒤 패턴 작성을 시도합니다. 버퍼 메타데이터는 생성 실패를 FrameError로 표시하며, 버퍼 완료 신호를 받았다는 사실만으로 프레임 생성의 성공을 판단할 수 없습니다. 가상 파이프라인의 버퍼 완료 처리 경로에서는 모든 버퍼의 완료 여부를 나타내는 `completeBuffer`의 반환값이 true일 때만 `completeRequest`를 호출합니다. 완료된 요청은 차례가 되면 `requestCompleted`에 연결된 cam 콜백으로 전달되며, 앞선 요청이 미완료이면 뒤 요청의 통지는 보류됩니다. `src/libcamera/pipeline/virtual/virtual.cpp:412`, `src/libcamera/pipeline/virtual/virtual.cpp:138`, `src/libcamera/pipeline/virtual/virtual.cpp:515`, `src/libcamera/pipeline_handler.cpp:563`, `src/libcamera/camera.cpp:1481`, `src/apps/cam/camera_session.cpp:305`

근거 원문: [src/libcamera/pipeline/virtual/README.md:3](#source-4f7002340059b1cf) · [src/libcamera/pipeline/virtual/data/virtual.yaml:28](#source-9858e22e2225cc10) · [src/libcamera/pipeline/virtual/virtual.cpp:356](#source-1868fec3abf482b8) · [src/libcamera/pipeline/virtual/virtual.cpp:412](#source-1c0d5dcdba46688e) · [src/libcamera/pipeline/virtual/virtual.cpp:138](#source-995da70adf556e1f) · [src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47](#source-fa5429fa2c62882d) · [src/libcamera/pipeline/virtual/virtual.cpp:515](#source-ab86b02a265cd2b8) · [src/libcamera/pipeline_handler.cpp:469](#source-5e575d092c08b32d) · [src/libcamera/pipeline_handler.cpp:563](#source-7cb889331b58a531) · [src/libcamera/camera.cpp:1481](#source-655b027df7d08524) · [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) · [src/apps/cam/camera_session.cpp:305](#source-fb9506413ce52fb0) · [src/libcamera/framebuffer_allocator.cpp:86](#source-e91194807faa9e0c) · [src/libcamera/camera.cpp:963](#source-80fd4657ae4c65d1) · [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) · [src/libcamera/pipeline/virtual/virtual.cpp:373](#source-4726a7d0b3f38c49) · [src/libcamera/pipeline_handler.cpp:435](#source-4fe013027055fa2d) · [src/libcamera/request.cpp:125](#source-0626196def047e5c)

## 여러 초기 요청을 단일 스트림에 맞춰 준비합니다

**가상 시험 구성입니다. 실제 제품의 지원·성능 주장으로 사용하지 마세요.**

기록된 단일 스트림과 출력 옵션 미요청 범위에서 cam은 버퍼를 할당해 각 초기 요청에 연결합니다. 모든 준비가 끝나야 카메라를 시작하며, 할당·요청 생성·버퍼 연결 중 오류가 나면 시작 전에 반환합니다. `src/apps/cam/camera_session.cpp:365`, `product-evidence/libcamera-official-cam-trial/invocation-options.txt:1`

<!-- sdd:visual:submission-gate -->
### 초기 요청들의 준비 반복과 준비 완료

```mermaid
flowchart TB
%% sdd:translations {"남은 요청 없음": "No requests left", "남은 요청 있음": "Requests left", "단일 스트림의 buffers#91;i#93;를 <br/>요청 i에 연결한 뒤 요청을 <br/>보관": "Keep request i after <br/>attaching sole stream#39;s <br/>buffers#91;i#93;", "모든 초기 요청·버퍼 준비 <br/>완료, 카메라 시작 전 단계 <br/>종료": "All initial requests and <br/>buffers ready before camera <br/>start", "생성 성공 #91;false#93;": "Create OK #91;false#93;", "생성 오류 #91;true#93;": "Create error #91;true#93;", "스트림 버퍼 i 연결에 <br/>실패했는가?": "Failed to attach stream <br/>buffer i?", "스트림 버퍼 할당 호출이 <br/>실패했는가?": "Did the stream buffer <br/>allocation call fail?", "연결 성공 #91;false#93;": "Attach OK #91;false#93;", "연결 오류 #91;true#93;": "Attach error #91;true#93;", "오류 값을 반환하고 카메라 <br/>시작 전에 종료": "Return the error value and <br/>end before camera start", "요청 생성이 실패했는가?": "Did request creation fail?", "저장 뒤 남은 요청 다시 확인": "Stored: recheck left", "할당 성공 #91;false#93;": "Alloc OK #91;false#93;", "할당 오류 #91;true#93;": "Alloc error #91;true#93;", "할당된 최소 버퍼 수만큼 <br/>만들 초기 요청이 남았는가?": "Requests left to make up to <br/>the minimum buffer count?"}
  v_alloc_check{"스트림 버퍼 할당 호출이 <br/>실패했는가?"}
  v_err_return["오류 값을 반환하고 카메라 <br/>시작 전에 종료"]
  v_more_requests{"할당된 최소 버퍼 수만큼 <br/>만들 초기 요청이 남았는가?"}
  v_create_req{"요청 생성이 실패했는가?"}
  v_attach_buf{"스트림 버퍼 i 연결에 <br/>실패했는가?"}
  v_store_req["단일 스트림의 buffers#91;i#93;를 <br/>요청 i에 연결한 뒤 요청을 <br/>보관"]
  v_ready_done["모든 초기 요청·버퍼 준비 <br/>완료, 카메라 시작 전 단계 <br/>종료"]
  v_alloc_check -->|"할당 오류 #91;true#93;"| v_err_return
  v_alloc_check -->|"할당 성공 #91;false#93;"| v_more_requests
  v_more_requests -->|"남은 요청 있음"| v_create_req
  v_more_requests -->|"남은 요청 없음"| v_ready_done
  v_create_req -->|"생성 오류 #91;true#93;"| v_err_return
  v_create_req -->|"생성 성공 #91;false#93;"| v_attach_buf
  v_attach_buf -->|"연결 오류 #91;true#93;"| v_err_return
  v_attach_buf -->|"연결 성공 #91;false#93;"| v_store_req
  v_store_req -->|"저장 뒤 남은 요청 다시 확인"| v_more_requests
```

[Mermaid 원문](official-cam-validation.submission-gate.mmd)

??? note "그림 근거와 확인 범위"
    기록된 단일 스트림·출력 싱크 미요청 구성에서 모든 초기 요청·버퍼는 카메라 시작 전에 어떻게 준비되며 준비 실패는 어떻게 처리됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Did the stream buffer allocation call fail?">스트림 버퍼 할당 호출이 실패했는가?</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Return the error value and end before camera start">오류 값을 반환하고 카메라 시작 전에 종료</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Requests left to make up to the minimum buffer count?">할당된 최소 버퍼 수만큼 만들 초기 요청이 남았는가?</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Did request creation fail?">요청 생성이 실패했는가?</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Failed to attach stream buffer i?">스트림 버퍼 i 연결에 실패했는가?</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Keep request i after attaching sole stream&#x27;s buffers[i]">단일 스트림의 buffers&#91;i&#93;를 요청 i에 연결한 뒤 요청을 보관</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="All initial requests and buffers ready before camera start">모든 초기 요청·버퍼 준비 완료, 카메라 시작 전 단계 종료</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Alloc error · ret &lt; 0 [true]">할당 오류 · ret &lt; 0 &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Alloc OK · ret &lt; 0 [false]">할당 성공 · ret &lt; 0 &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Requests left">남은 요청 있음</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="No requests left">남은 요청 없음</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Create error · !request [true]">생성 오류 · &#33;request &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Create OK · !request [false]">생성 성공 · &#33;request &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Attach error · ret &lt; 0 [true]">연결 오류 · ret &lt; 0 &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Attach OK · ret &lt; 0 [false]">연결 성공 · ret &lt; 0 &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
    | <span data-sdd-label-en="Stored: recheck left">저장 뒤 남은 요청 다시 확인</span> | [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) |
<!-- /sdd:visual:submission-gate -->

근거 원문: [src/apps/cam/camera_session.cpp:365](#source-4c93e74b4521da77) · [product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1](#source-67134777ea4213e0) · [product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1](#source-e326d2b05d8f4ef8) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) · [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad)

## 준비된 초기 요청을 한도 안에서 제출합니다

**가상 시험 구성입니다. 실제 제품의 지원·성능 주장으로 사용하지 마세요.**

cam은 요청을 준비하고 카메라를 시작한 뒤 한도 안에서만 제출하며, 한도 도달 시 제출을 생략하고 0을 반환합니다. 실제 카메라 큐 API는 상태와 요청을 검사해 오류를 반환할 수 있고 성공하면 비동기 호출을 예약하며, 초기 제출 실패 시 cam은 카메라를 중지합니다. `src/apps/cam/camera_session.cpp:365`, `src/libcamera/camera.cpp:1330`

<!-- sdd:visual:initial-submission -->
### 초기 요청 제출 반복과 오류 반환

```mermaid
flowchart TB
%% sdd:translations {"0 반환 후 검사": "Check after return 0", "sink가 있으면 중지하고 시작 <br/>오류를 반환합니다.": "Stop the sink if present <br/>and return the start error.", "검사 실패": "Checks fail", "검사 통과": "Checks pass", "검사에 실패하면 API가 음수 <br/>오류를 반환합니다.": "If a check fails, the API <br/>returns a negative error.", "도달: API 호출 없이 0 #91;true#93;": "At limit: 0, no call #91;true#93;", "순회가 끝나면 한도 유무에 <br/>따른 캡처 안내를 출력하고 <br/>0을 반환합니다.": "After the loop, print the <br/>capture notice for the <br/>limit and return 0.", "스크립트가 있을 때만 제어를 <br/>병합하고 큐 API 호출 시도 <br/>횟수는 항상 1 늘립니다.": "Merge controls only with a <br/>script; always increment <br/>queue API call attempts.", "시작 성공 #91;false#93;": "Start succeeded #91;false#93;", "시작 오류 #91;true#93;": "Start error #91;true#93;", "오류 반환 후 검사": "Check after error", "요청이 남음": "Requests remain", "요청이 없음": "No requests remain", "음수 결과 #91;true#93;": "Negative result #91;true#93;", "음수가 아님 #91;false#93;": "Not negative #91;false#93;", "처리할 초기 요청이 남았는지 <br/>확인합니다.": "Check whether initial <br/>requests remain.", "카메라 시작 결과를 <br/>확인합니다.": "Check the camera start <br/>result.", "카메라 실행 상태와 요청의 <br/>생성 카메라, 상태, 제어 <br/>목록, 버퍼와 스트림을 <br/>검사합니다.": "Check the running state and <br/>the request#39;s camera, <br/>status, controls, buffers <br/>and runs.", "카메라 큐 API 호출": "Call camera queue", "카메라와 존재하는 sink를 <br/>중지한 뒤 오류를 반환합니다.": "Stop the camera and any <br/>sink, then return the error.", "큐 API 호출 시도 횟수가 <br/>설정된 한도에 도달했는지 <br/>확인합니다.": "Check whether queue API <br/>call attempts reached the <br/>configured limit.", "파이프라인 큐 호출을 <br/>비동기로 등록하고 API가 0을 <br/>반환합니다.": "Queue the pipeline call <br/>asynchronously and return 0 <br/>from the API.", "한도 없음 또는 미달 #91;false#93;": "Unset or below limit #91;false#93;", "호출자가 helper의 반환값이 <br/>음수인지 확인합니다.": "The caller checks whether <br/>the helper#39;s return value <br/>is negative."}
  v_start_check{"카메라 시작 결과를 <br/>확인합니다."}
  v_start_fail["sink가 있으면 중지하고 시작 <br/>오류를 반환합니다."]
  v_remaining{"처리할 초기 요청이 남았는지 <br/>확인합니다."}
  v_limit_check{"큐 API 호출 시도 횟수가 <br/>설정된 한도에 도달했는지 <br/>확인합니다."}
  v_control_merge["스크립트가 있을 때만 제어를 <br/>병합하고 큐 API 호출 시도 <br/>횟수는 항상 1 늘립니다."]
  v_camera_queue_check{"카메라 실행 상태와 요청의 <br/>생성 카메라, 상태, 제어 <br/>목록, 버퍼와 스트림을 <br/>검사합니다."}
  v_queue_error["검사에 실패하면 API가 음수 <br/>오류를 반환합니다."]
  v_queue_async["파이프라인 큐 호출을 <br/>비동기로 등록하고 API가 0을 <br/>반환합니다."]
  v_caller_check{"호출자가 helper의 반환값이 <br/>음수인지 확인합니다."}
  v_stop_on_error["카메라와 존재하는 sink를 <br/>중지한 뒤 오류를 반환합니다."]
  v_done["순회가 끝나면 한도 유무에 <br/>따른 캡처 안내를 출력하고 <br/>0을 반환합니다."]
  v_start_check -->|"시작 오류 #91;true#93;"| v_start_fail
  v_start_check -->|"시작 성공 #91;false#93;"| v_remaining
  v_remaining -->|"요청이 남음"| v_limit_check
  v_remaining -->|"요청이 없음"| v_done
  v_limit_check -->|"도달: API 호출 없이 0 #91;true#93;"| v_caller_check
  v_limit_check -->|"한도 없음 또는 미달 #91;false#93;"| v_control_merge
  v_control_merge -->|"카메라 큐 API 호출"| v_camera_queue_check
  v_camera_queue_check -->|"검사 실패"| v_queue_error
  v_camera_queue_check -->|"검사 통과"| v_queue_async
  v_queue_error -->|"오류 반환 후 검사"| v_caller_check
  v_queue_async -->|"0 반환 후 검사"| v_caller_check
  v_caller_check -->|"음수 결과 #91;true#93;"| v_stop_on_error
  v_caller_check -->|"음수가 아님 #91;false#93;"| v_remaining
```

[Mermaid 원문](official-cam-validation.initial-submission.mmd)

??? note "그림 근거와 확인 범위"
    같은 기록 구성에서 카메라 시작 뒤 남은 초기 요청을 순회하며 제출 한도를 적용하고 큐 반환 오류와 정상 순회 종료를 어떻게 처리합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Check the camera start result.">카메라 시작 결과를 확인합니다.</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) · [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Stop the sink if present and return the start error.">sink가 있으면 중지하고 시작 오류를 반환합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Check whether initial requests remain.">처리할 초기 요청이 남았는지 확인합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Check whether queue API call attempts reached the configured limit.">큐 API 호출 시도 횟수가 설정된 한도에 도달했는지 확인합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Merge controls only with a script; always increment queue API call attempts.">스크립트가 있을 때만 제어를 병합하고 큐 API 호출 시도 횟수는 항상 1 늘립니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Check the running state and the request&#x27;s camera, status, controls, buffers and runs.">카메라 실행 상태와 요청의 생성 카메라, 상태, 제어 목록, 버퍼와 스트림을 검사합니다.</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="If a check fails, the API returns a negative error.">검사에 실패하면 API가 음수 오류를 반환합니다.</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="Queue the pipeline call asynchronously and return 0 from the API.">파이프라인 큐 호출을 비동기로 등록하고 API가 0을 반환합니다.</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="The caller checks whether the helper&#x27;s return value is negative.">호출자가 helper의 반환값이 음수인지 확인합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Stop the camera and any sink, then return the error.">카메라와 존재하는 sink를 중지한 뒤 오류를 반환합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="After the loop, print the capture notice for the limit and return 0.">순회가 끝나면 한도 유무에 따른 캡처 안내를 출력하고 0을 반환합니다.</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Start error · ret [true]">시작 오류 · ret &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) · [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="Start succeeded · ret [false]">시작 성공 · ret &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) · [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="Requests remain">요청이 남음</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="No requests remain">요청이 없음</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="At limit: 0, no call · captureLimit_ &amp;&amp; queueCount_ &gt;= captureLimit_ [true]">도달: API 호출 없이 0 · captureLimit&#95; &amp;&amp; queueCount&#95; &gt;= captureLimit&#95; &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Unset or below limit · captureLimit_ &amp;&amp; queueCount_ &gt;= captureLimit_ [false]">한도 없음 또는 미달 · captureLimit&#95; &amp;&amp; queueCount&#95; &gt;= captureLimit&#95; &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Call camera queue">카메라 큐 API 호출</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) · [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="Checks fail">검사 실패</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="Checks pass">검사 통과</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) |
    | <span data-sdd-label-en="Check after error">오류 반환 후 검사</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) · [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Check after return 0">0 반환 후 검사</span> | [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) · [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Negative result · ret &lt; 0 [true]">음수 결과 · ret &lt; 0 &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
    | <span data-sdd-label-en="Not negative · ret &lt; 0 [false]">음수가 아님 · ret &lt; 0 &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) |
<!-- /sdd:visual:initial-submission -->

근거 원문: [src/apps/cam/camera_session.cpp:365](#source-5723cb743173a3dd) · [src/libcamera/camera.cpp:1330](#source-d6d48aa78159fb58) · [product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1](#source-67134777ea4213e0) · [product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1](#source-e326d2b05d8f4ef8) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) · [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad)

## cam이 완료 알림을 받아 이벤트 루프에서 프레임을 처리합니다.

**가상 시험 구성입니다. 실제 제품의 지원·성능 주장으로 사용하지 마세요.**

`CameraSession::requestComplete`는 요청 상태가 `RequestCancelled`이면 반환하고, 그 밖에는 `callLater`로 `CameraSession::processRequest`를 이벤트 루프에 미룹니다. 이는 카메라 매니저 스레드를 막지 않기 위해서입니다. `src/apps/cam/camera_session.cpp:467`

<!-- sdd:visual:completion-flow -->
### 기록된 출력 싱크 미요청 콜백 경로

```mermaid
flowchart TB
%% sdd:translations {"Request 상태가 <br/>RequestCancelled인지 확인": "Check whether Request <br/>status is RequestCancelled", "Request::ReuseBuffers로 <br/>버퍼 유지 후 queueRequest <br/>호출": "Keep buffers <br/>#40;Request::ReuseBuffers#41;; <br/>queueRequest", "callLater로 이벤트 루프에 <br/>위임해 카메라 매니저 스레드 <br/>차단 회피": "Defer via callLater; avoids <br/>blocking camera manager", "captureDone.emit#40;#41; 신호 후 <br/>processRequest가 반환": "Emit captureDone, then <br/>processRequest returns", "processRequest가 즉시 반환, <br/>captureDone 신호 없이 종료": "processRequest returns; no <br/>captureDone signal", "requestComplete가 즉시 <br/>반환, captureDone 신호 없음": "requestComplete returns; no <br/>captureDone signal", "미설정 또는 미도달 #91;false#93;": "Unset or not reached #91;false#93;", "완료된 Request를 받아 <br/>CameraSession::<br/>requestComplete 진입": "Enter <br/>CameraSession::<br/>requestComplete with Request", "이벤트 루프 실행": "Event loop runs", "증가 후 captureLimit#95; 설정 <br/>AND captureCount#95; 도달인지 <br/>확인": "Check: captureLimit#95; set <br/>AND captureCount#95; reached?", "증가 후 확인": "Then check", "진입 시 captureLimit#95; 설정 <br/>AND captureCount#95; 도달인지 <br/>확인": "Entry: captureLimit#95; set <br/>AND captureCount#95; reached?", "취소 상태면 #91;true#93;": "If cancelled #91;true#93;", "취소 아니면 #91;false#93;": "If not cancelled #91;false#93;", "취소 여부 확인": "Check cancel status", "프레임 정보 출력 후 <br/>captureCount#95;를 1 증가": "Print frame info, then <br/>increment captureCount#95; by 1", "한도 설정 AND 도달 #91;true#93;": "Limit set #38; reached #91;true#93;"}
  v_n0["완료된 Request를 받아 <br/>CameraSession::<br/>requestComplete 진입"]
  v_n1{"Request 상태가 <br/>RequestCancelled인지 확인"}
  v_n2["requestComplete가 즉시 <br/>반환, captureDone 신호 없음"]
  v_n3["callLater로 이벤트 루프에 <br/>위임해 카메라 매니저 스레드 <br/>차단 회피"]
  v_n4{"진입 시 captureLimit#95; 설정 <br/>AND captureCount#95; 도달인지 <br/>확인"}
  v_n5["processRequest가 즉시 반환, <br/>captureDone 신호 없이 종료"]
  v_n6["프레임 정보 출력 후 <br/>captureCount#95;를 1 증가"]
  v_n7{"증가 후 captureLimit#95; 설정 <br/>AND captureCount#95; 도달인지 <br/>확인"}
  v_n8["captureDone.emit#40;#41; 신호 후 <br/>processRequest가 반환"]
  v_n9["Request::ReuseBuffers로 <br/>버퍼 유지 후 queueRequest <br/>호출"]
  v_n0 -->|"취소 여부 확인"| v_n1
  v_n1 -->|"취소 상태면 #91;true#93;"| v_n2
  v_n1 -->|"취소 아니면 #91;false#93;"| v_n3
  v_n3 -->|"이벤트 루프 실행"| v_n4
  v_n4 -->|"한도 설정 AND 도달 #91;true#93;"| v_n5
  v_n4 -->|"미설정 또는 미도달 #91;false#93;"| v_n6
  v_n6 -->|"증가 후 확인"| v_n7
  v_n7 -->|"한도 설정 AND 도달 #91;true#93;"| v_n8
  v_n7 -->|"미설정 또는 미도달 #91;false#93;"| v_n9
```

[Mermaid 원문](official-cam-validation.completion-flow.mmd)

??? note "그림 근거와 확인 범위"
    기록된 출력 싱크 미요청 경로에서 완료 콜백은 어떤 처리와 종료로 이어집니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Enter CameraSession::requestComplete with Request">완료된 Request를 받아 CameraSession::requestComplete 진입</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) · [src/apps/cam/camera_session.cpp:283](#source-fed2a2e4116ab528) |
    | <span data-sdd-label-en="Check whether Request status is RequestCancelled">Request 상태가 RequestCancelled인지 확인</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="requestComplete returns; no captureDone signal">requestComplete가 즉시 반환, captureDone 신호 없음</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) · [src/apps/cam/camera_session.cpp:283](#source-fed2a2e4116ab528) |
    | <span data-sdd-label-en="Defer via callLater; avoids blocking camera manager">callLater로 이벤트 루프에 위임해 카메라 매니저 스레드 차단 회피</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Entry: captureLimit_ set AND captureCount_ reached?">진입 시 captureLimit&#95; 설정 AND captureCount&#95; 도달인지 확인</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="processRequest returns; no captureDone signal">processRequest가 즉시 반환, captureDone 신호 없이 종료</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Print frame info, then increment captureCount_ by 1">프레임 정보 출력 후 captureCount&#95;를 1 증가</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) · [src/apps/cam/camera_session.cpp:283](#source-fed2a2e4116ab528) |
    | <span data-sdd-label-en="Check: captureLimit_ set AND captureCount_ reached?">증가 후 captureLimit&#95; 설정 AND captureCount&#95; 도달인지 확인</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) · [src/apps/cam/camera_session.cpp:283](#source-fed2a2e4116ab528) |
    | <span data-sdd-label-en="Emit captureDone, then processRequest returns">captureDone.emit&#40;&#41; 신호 후 processRequest가 반환</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Keep buffers (Request::ReuseBuffers); queueRequest">Request::ReuseBuffers로 버퍼 유지 후 queueRequest 호출</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Check cancel status">취소 여부 확인</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="If cancelled · request-&gt;status() == Request::RequestCancelled [true]">취소 상태면 · request-&gt;status&#40;&#41; == Request::RequestCancelled &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="If not cancelled · request-&gt;status() == Request::RequestCancelled [false]">취소 아니면 · request-&gt;status&#40;&#41; == Request::RequestCancelled &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Event loop runs">이벤트 루프 실행</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Limit set &amp; reached · captureLimit_ &amp;&amp; captureCount_ &gt;= captureLimit_ [true]">한도 설정 AND 도달 · captureLimit&#95; &amp;&amp; captureCount&#95; &gt;= captureLimit&#95; &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Unset or not reached · captureLimit_ &amp;&amp; captureCount_ &gt;= captureLimit_ [false]">미설정 또는 미도달 · captureLimit&#95; &amp;&amp; captureCount&#95; &gt;= captureLimit&#95; &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Then check">증가 후 확인</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Limit set &amp; reached · captureLimit_ &amp;&amp; captureCount_ &gt;= captureLimit_ [true]">한도 설정 AND 도달 · captureLimit&#95; &amp;&amp; captureCount&#95; &gt;= captureLimit&#95; &#91;true&#93;</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
    | <span data-sdd-label-en="Unset or not reached · captureLimit_ &amp;&amp; captureCount_ &gt;= captureLimit_ [false]">미설정 또는 미도달 · captureLimit&#95; &amp;&amp; captureCount&#95; &gt;= captureLimit&#95; &#91;false&#93;</span> | [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) |
<!-- /sdd:visual:completion-flow -->

세 실제 실행 명령은 화면·파일 출력 옵션을 요청하지 않았습니다. 다른 출력 옵션을 선택한 동작은 이번 실행으로 검증하지 않았습니다. `processRequest`가 호출될 때 처리 한도가 설정되어 있고 처리 수가 이미 한도에 도달했다면, `captureDone`을 다시 내지 않고 즉시 반환하여 후속 프레임 처리를 건너뜁니다. `product-evidence/libcamera-official-cam-trial/invocation-options.txt:1`, `src/apps/cam/camera_session.cpp:467`

`processRequest`는 프레임 정보를 출력하고 처리 수를 하나 늘립니다. `processRequest`는 설정된 한도에 도달하면 `captureDone` 신호를 내고 반환합니다. 앞서 정한 출력 조건에서 처리 한도가 미설정이거나 처리 수가 아직 한도에 도달하지 않았으면 `CameraSession::processRequest`는 버퍼를 유지해 요청을 재사용하고 제출 도우미 `queueRequest`를 호출합니다. 처리 함수는 처리 수를, 제출 도우미는 제출 시도 수를 같은 캡처 한도 값과 서로 다른 시점에 비교합니다. `src/apps/cam/camera_session.cpp:467`, `src/apps/cam/camera_session.cpp:557`, `product-evidence/libcamera-official-cam-trial/invocation-options.txt:1`, `src/apps/cam/camera_session.cpp:453`

이번 세 실행에서는 콜백과 후속 처리가 서로 다른 스레드에서 관측됐지만, 모든 실행에서 같은 배치를 보장하지는 않습니다. `requestComplete`에는 취소된 요청의 분기가 있지만, 이번 실행에서는 해당 분기를 동적으로 시험하지 않았습니다. `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1`, `src/apps/cam/camera_session.cpp:467`

근거 원문: [src/apps/cam/camera_session.cpp:467](#source-24d83931ed92dc57) · [src/apps/cam/camera_session.cpp:453](#source-a93e2b65e7577aaf) · [src/apps/cam/camera_session.cpp:283](#source-fed2a2e4116ab528) · [src/apps/cam/camera_session.h:61](#source-3122754fc16929a5) · [src/apps/cam/camera_session.cpp:557](#source-eb19d6a7f4a0f3f0) · [product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1](#source-67134777ea4213e0) · [product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1](#source-e326d2b05d8f4ef8) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) · [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad)

## 지원 커널과 장치 접근을 확인한 뒤 재현합니다

**가상 시험 구성입니다. 실제 제품의 지원·성능 주장으로 사용하지 마세요.**

1. **준비 (1–3)** 호스트 상태를 바꾸지 않고 사용할 커널의 Kconfig와 의존 조건을 조사하세요. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`, `product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1`

2. **DMA-BUF 할당기 선택:** 선택한 커널의 Kconfig, 의존성, 실제 사용 가능한 모듈과 할당기 후보를 조사하고 결과에 맞는 할당기 하나를 선택하세요. 이 기록과 같은 조건으로 재현하려면 udmabuf를 사용하세요. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`, `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1`, `product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1`

3. 선택한 커널과 할당기에 필요한 모듈만 설치 여부와 커널 버전 일치를 조사하세요. 기록된 udmabuf 시험에서는 드라이버가 내장되어 있었고 별도 모듈을 설치하지 않았습니다. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`, `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1`

4. **호스트 변경 (4–5)** 변경안, 부팅할 커널과 이미지 SHA-256, 영향, 정확한 백업 경로, 부팅 및 복구 절차가 포함된 호스트 변경 계획에 대해 실행 직전에 별도 승인을 받으세요. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`

5. 승인된 계획에 따라 시험 커널을 설치하고 부팅하세요. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`

6. **실행 전 검사 (6–11)** 실행 중인 커널 버전이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지 확인하세요. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`

7. WSL root 자식 컨텍스트에서 `/dev/udmabuf`을 열 수 있는 권한을 확인하세요. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`

8. 사용할 Virtual2 YAML에서 크기 400x300과 패턴 값 lines를 하나의 구성 조합으로 대조하세요. `src/libcamera/pipeline/virtual/data/virtual.yaml:28`

9. 사용할 cam 명령의 카메라 선택 인자가 `Virtual2`인지 확인하세요. `product-evidence/libcamera-official-cam-trial/invocation-options.txt:1`

10. 사용할 cam 스트림 인자가 400x300 NV12를 요청하는지 확인하세요. `product-evidence/libcamera-official-cam-trial/invocation-options.txt:1`

11. 실행할 공식 cam 명령에 3프레임을 요청하는 `--capture=3` 인자가 지정되어 있는지 확인합니다. `product-evidence/libcamera-official-cam-trial/invocation-options.txt:1`

12. **실행·검증 (12–13)** 연결된 실행 절차에 따라 수정하지 않은 공식 cam을 세 독립 프로세스로 실행합니다. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`, `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1`

13. 새 실행의 증거를 카메라 Virtual2, 실제 적용 스트림 400x300 NV12, 각 독립 실행의 정상 3프레임 처리와 종료 코드 0이라는 기대 결과 조합과 대조하세요. `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1`, `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`

<!-- sdd:visual:reproduction-flow -->
### 환경 확인에서 재현 실행까지

```mermaid
flowchart TB
%% sdd:translations {"YAML은 400×300 lines. cam <br/>인자를 확인합니다. --camera <br/>Virtual2 --capture#61;3 <br/>--stream <br/>role#61;video,width#61;400,height#61;<br/>300,pixelformat#61;NV12": "YAML uses 400×300 lines. <br/>Check cam arguments: <br/>--camera Virtual2 <br/>--capture#61;3 --stream <br/>role#61;video,width#61;400,height#61;<br/>300,pixelformat#61;NV12", "각 실행의 실제 적용값 대조: <br/>Virtual2, 400×300 <br/>NV12/SMPTE170M. 시퀀스 0–2, <br/>요청 상태 1, 버퍼 상태 0, <br/>종료 코드 0": "Compare each run with <br/>expected Virtual2 and <br/>400×300 NV12/SMPTE170M. <br/>Check sequences 0–2, <br/>request status 1, buffer <br/>status 0, and exit code 0.", "격리된 환경에서 호스트 변경 <br/>없이 조사합니다. Kconfig, <br/>의존성, 사용 가능한 모듈을 <br/>확인하고 DMA-BUF 할당기 <br/>하나를 선택합니다.": "Start read-only in an <br/>isolated test environment. <br/>Check Kconfig support, <br/>dependencies, and available <br/>modules. Choose one DMA-BUF <br/>allocator.", "계획에 Docker 중지가 있는가?": "Does the plan require <br/>stopping Docker?", "고정 소스와 빌드 확인 뒤 <br/>실행": "Run after checking the <br/>pinned source and build", "공식 cam을 세 독립 <br/>프로세스로 실행": "Run official cam in three <br/>independent processes", "그 다음 부팅": "Then boot", "두 조건이 일치": "Both checks pass", "변경 불필요": "No host change needed", "부팅 뒤 실제 환경 확인": "Check the running <br/>environment", "새 경로에서 실행별 기록 확인": "Check each run in the new <br/>evidence directory", "생략": "Skip", "수정하지 않은 293d751a, <br/>디버그 Meson 빌드, GDB 도구 <br/>경로, 컴파일된 DMA-BUF <br/>프로브 확인": "Check unmodified 293d751a, <br/>its debug Meson build, the <br/>GDB tools prefix, and the <br/>compiled DMA-BUF probe", "승인을 받은 뒤 Docker 중지": "Stop Docker after approval", "승인한 계획 확인": "Check the approved plan", "승인한 시험 커널로 부팅": "Boot the approved test <br/>kernel", "시험 소스와 빌드도 확인": "Also check the test source <br/>and build", "시험 환경 선택": "Choose the test environment", "실행 중인 커널이 <br/>6.18.33.2-microsoft-standard<br/>-WSL2-issue211이고 root가 <br/>/dev/udmabuf을 열 수 있는가?": "Is the running kernel <br/>6.18.33.2-microsoft-standard<br/>-WSL2-issue211 and can root <br/>open /dev/udmabuf?", "영향·백업 경로·커널 <br/>이미지와 SHA-256·부팅·복구 <br/>절차를 기록하고 별도 승인": "Document impact, backup <br/>path, kernel image and <br/>SHA-256, boot and recovery. <br/>Get separate approval", "캡처 중단": "Stop before capture", "필요": "Required", "하나라도 다름": "Either check fails", "호스트 변경이 필요한가?": "Does the test require host <br/>changes?"}
  v_survey["격리된 환경에서 호스트 변경 <br/>없이 조사합니다. Kconfig, <br/>의존성, 사용 가능한 모듈을 <br/>확인하고 DMA-BUF 할당기 <br/>하나를 선택합니다."]
  v_host{"호스트 변경이 필요한가?"}
  v_approval["영향·백업 경로·커널 <br/>이미지와 SHA-256·부팅·복구 <br/>절차를 기록하고 별도 승인"]
  v_docker{"계획에 Docker 중지가 있는가?"}
  v_stop_docker["승인을 받은 뒤 Docker 중지"]
  v_boot["승인한 시험 커널로 부팅"]
  v_device{"실행 중인 커널이 <br/>6.18.33.2-microsoft-standard<br/>-WSL2-issue211이고 root가 <br/>/dev/udmabuf을 열 수 있는가?"}
  v_stop["캡처 중단"]
  v_run["공식 cam을 세 독립 <br/>프로세스로 실행"]
  v_confirm["각 실행의 실제 적용값 대조: <br/>Virtual2, 400×300 <br/>NV12/SMPTE170M. 시퀀스 0–2, <br/>요청 상태 1, 버퍼 상태 0, <br/>종료 코드 0"]
  v_options["YAML은 400×300 lines. cam <br/>인자를 확인합니다. --camera <br/>Virtual2 --capture#61;3 <br/>--stream <br/>role#61;video,width#61;400,height#61;<br/>300,pixelformat#61;NV12"]
  v_build["수정하지 않은 293d751a, <br/>디버그 Meson 빌드, GDB 도구 <br/>경로, 컴파일된 DMA-BUF <br/>프로브 확인"]
  v_survey -->|"시험 환경 선택"| v_host
  v_host -->|"필요"| v_approval
  v_host -->|"변경 불필요"| v_device
  v_approval -->|"승인한 계획 확인"| v_docker
  v_docker -->|"필요"| v_stop_docker
  v_docker -->|"생략"| v_boot
  v_stop_docker -->|"그 다음 부팅"| v_boot
  v_boot -->|"부팅 뒤 실제 환경 확인"| v_device
  v_device -->|"하나라도 다름"| v_stop
  v_device -->|"두 조건이 일치"| v_options
  v_run -->|"새 경로에서 실행별 기록 확인"| v_confirm
  v_options -->|"시험 소스와 빌드도 확인"| v_build
  v_build -->|"고정 소스와 빌드 확인 뒤 <br/>실행"| v_run
```

[Mermaid 원문](official-cam-validation.reproduction-flow.mmd)

??? note "그림 근거와 확인 범위"
    기존 WSL에 기록된 시험 커널을 설치하는 호스트 변경이 필요한 경우, 승인과 실행 전 검사를 거쳐 어떤 조건에서 재현을 진행합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Start read-only in an isolated test environment. Check Kconfig support, dependencies, and available modules. Choose one DMA-BUF allocator.">격리된 환경에서 호스트 변경 없이 조사합니다. Kconfig, 의존성, 사용 가능한 모듈을 확인하고 DMA-BUF 할당기 하나를 선택합니다.</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Does the test require host changes?">호스트 변경이 필요한가?</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Document impact, backup path, kernel image and SHA-256, boot and recovery. Get separate approval">영향·백업 경로·커널 이미지와 SHA-256·부팅·복구 절차를 기록하고 별도 승인</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Does the plan require stopping Docker?">계획에 Docker 중지가 있는가?</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Stop Docker after approval">승인을 받은 뒤 Docker 중지</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Boot the approved test kernel">승인한 시험 커널로 부팅</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Is the running kernel 6.18.33.2-microsoft-standard-WSL2-issue211 and can root open /dev/udmabuf?">실행 중인 커널이 6.18.33.2-microsoft-standard-WSL2-issue211이고 root가 /dev/udmabuf을 열 수 있는가?</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Stop before capture">캡처 중단</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Run official cam in three independent processes">공식 cam을 세 독립 프로세스로 실행</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Compare each run with expected Virtual2 and 400×300 NV12/SMPTE170M. Check sequences 0–2, request status 1, buffer status 0, and exit code 0.">각 실행의 실제 적용값 대조: Virtual2, 400×300 NV12/SMPTE170M. 시퀀스 0–2, 요청 상태 1, 버퍼 상태 0, 종료 코드 0</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) · [product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1](#source-e326d2b05d8f4ef8) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) |
    | <span data-sdd-label-en="YAML uses 400×300 lines. Check cam arguments: --camera Virtual2 --capture=3 --stream role=video,width=400,height=300,pixelformat=NV12">YAML은 400×300 lines. cam 인자를 확인합니다. --camera Virtual2 --capture=3 --stream role=video,width=400,height=300,pixelformat=NV12</span> | [src/libcamera/pipeline/virtual/data/virtual.yaml:28](#source-9858e22e2225cc10) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) |
    | <span data-sdd-label-en="Check unmodified 293d751a, its debug Meson build, the GDB tools prefix, and the compiled DMA-BUF probe">수정하지 않은 293d751a, 디버그 Meson 빌드, GDB 도구 경로, 컴파일된 DMA-BUF 프로브 확인</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Choose the test environment">시험 환경 선택</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Required">필요</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="No host change needed">변경 불필요</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Check the approved plan">승인한 계획 확인</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Required">필요</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Skip">생략</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Then boot">그 다음 부팅</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Check the running environment">부팅 뒤 실제 환경 확인</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Either check fails">하나라도 다름</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Both checks pass">두 조건이 일치</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) · [src/libcamera/pipeline/virtual/data/virtual.yaml:28](#source-9858e22e2225cc10) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) |
    | <span data-sdd-label-en="Check each run in the new evidence directory">새 경로에서 실행별 기록 확인</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Also check the test source and build">시험 소스와 빌드도 확인</span> | [src/libcamera/pipeline/virtual/data/virtual.yaml:28](#source-9858e22e2225cc10) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) · [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
    | <span data-sdd-label-en="Run after checking the pinned source and build">고정 소스와 빌드 확인 뒤 실행</span> | [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad) |
<!-- /sdd:visual:reproduction-flow -->

실행 확인 항목: 이 결과는 WSL 가상 카메라의 시뮬레이션 구성에만 해당하며, 물리 DMA·카메라·제품 앱·사내 HAL은 검증하지 않았습니다. GDB는 타이밍에 영향을 주므로 콜백 반환 명령과 성능은 검증하지 않았습니다. `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`, `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1`

근거 원문: [src/libcamera/pipeline/virtual/data/virtual.yaml:28](#source-9858e22e2225cc10) · [product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1](#source-67134777ea4213e0) · [product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1](#source-e326d2b05d8f4ef8) · [product-evidence/libcamera-official-cam-trial/invocation-options.txt:1](#source-077dc6a73bad3108) · [product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1](#source-5a006a90fe9f46ad)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 무엇이 캡처를 막았고, 어떤 조건에서 공식 cam 캡처가 성공했으며, 현재 바로 재실행할 수 있습니까? | [할당기를 준비하자 공식 cam 캡처가 완료됐습니다](#할당기를-준비하자-공식-cam-캡처가-완료됐습니다) | 코드 근거와 설명 연결 |
    | 센서 없이 가상 캡처가 가능한 이유와, Virtual2의 줄무늬 영상이 실제 DMA-BUF·요청·완료 알림 경로를 거쳐 cam에 전달되는 원리는 무엇입니까? | [가상 파이프라인이 영상을 만들고 요청 완료를 알립니다](#가상-파이프라인이-영상을-만들고-요청-완료를-알립니다) | 코드 근거와 설명 연결 |
    | 기록된 단일 스트림·출력 싱크 미요청 구성에서 모든 초기 요청·버퍼는 카메라 시작 전에 어떻게 준비되며 준비 실패는 어떻게 처리됩니까? | [여러 초기 요청을 단일 스트림에 맞춰 준비합니다](#여러-초기-요청을-단일-스트림에-맞춰-준비합니다) | 코드 근거와 설명 연결 |
    | 같은 기록 구성에서 카메라 시작 뒤 남은 초기 요청을 순회하며 제출 한도를 적용하고 큐 반환 오류와 정상 순회 종료를 어떻게 처리합니까? | [준비된 초기 요청을 한도 안에서 제출합니다](#준비된-초기-요청을-한도-안에서-제출합니다) | 코드 근거와 설명 연결 |
    | 완료 알림을 받은 함수가 왜 후속 처리를 이벤트 루프로 미루며, 정상 요청과 취소 요청은 어떻게 나뉩니까? | [cam이 완료 알림을 받아 이벤트 루프에서 프레임을 처리합니다.](#cam이-완료-알림을-받아-이벤트-루프에서-프레임을-처리합니다) | 코드 근거와 설명 연결 |
    | 개발자는 캡처 전에 어떤 환경·권한·소스 조건을 확인하고, 어느 절차로 재현하며, 결과를 어디까지 적용할 수 있습니까? | [지원 커널과 장치 접근을 확인한 뒤 재현합니다](#지원-커널과-장치-접근을-확인한-뒤-재현합니다) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-6722470b9620a771"></a>

??? note "제품 자료: product-evidence/libcamera-official-cam-trial/execution-contract.txt:1"
    소스와 별도로 제공된 자료입니다. 제공자·버전·적용 범위를 아래 기록에서 확인하세요. 자동 검사는 사람 승인이 아닙니다.
    
    `product-evidence/libcamera-official-cam-trial/execution-contract.txt:1`에서 시작하는 발췌입니다. 종료 줄은 9이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fe1292511ffbf64b3e2aaee046d28048675c0283b82187cfa421e0431c834e0d`
    
    ```text
    {
      "url": "https://github.com/TTolsun/camera-hal-sdd-generator/issues/211",
      "updated_at": "2026-10-31T06:00:33Z",
      "verbatim_contract_lines": [
        "1. 선택한 커널의 Kconfig·의존성·실제 사용 가능한 모듈·할당기 후보를 조사하고 하나를 선택합니다. 기존 WSL에 새 배포판을 추가하는 것만으로 커널이 격리된다고 취급하지 않습니다.",
        "2. 기존 WSL/Docker에 영향을 주지 않는 시험 환경을 우선합니다. 현재 호스트의 공유 커널·모듈·.wslconfig를 변경하거나 배포판/VM을 종료해야 하면 영향과 복구 절차를 먼저 구체화하고 실행 직전에 별도 승인을 받습니다. 기존 PR 병합·Pages 배포 승인을 이런 호스트 변경의 승인으로 확대하지 않습니다."
      ]
    }
    
    ```
    
    ```json
    {
      "type": "project-document",
      "supplier": "GitHub issue211 execution contract, verbatim selected lines",
      "version": "2026-10-31T06:00:33Z",
      "date": "2026-10-31",
      "valid_until": "2026-10-31",
      "product": "libcamera-official-cam-trial",
      "release": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "configuration": "wsl2-virtual2-official-cam-udmabuf",
      "feature": "wsl-virtual-capture",
      "conditions": [
        "Source 293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
        "WSL2 custom UDMABUF kernel, root child, Virtual2 400x300 NV12",
        "GDB observation; no timing/return/physical/internal HAL qualification"
      ],
      "sha256": "fe1292511ffbf64b3e2aaee046d28048675c0283b82187cfa421e0431c834e0d"
    }
    ```

<a id="source-d84e6ca3abcfec11"></a>

??? note "제품 자료: product-evidence/libcamera-official-cam-trial/official-cam-reader.txt:1"
    소스와 별도로 제공된 자료입니다. 제공자·버전·적용 범위를 아래 기록에서 확인하세요. 자동 검사는 사람 승인이 아닙니다.
    
    `product-evidence/libcamera-official-cam-trial/official-cam-reader.txt:1`에서 시작하는 발췌입니다. 종료 줄은 249이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6ad6510d9624cd8075ccdc0a4622214c441afc5a778a2e577b4c7a76bf10efc0`
    
    ```text
    {
      "schema": 1,
      "source_commit": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "camera": "Virtual2",
      "applied_configuration": "(0) 400x300-NV12/SMPTE170M",
      "status": "observed-wsl-virtual-only",
      "kernel": "6.18.33.2-microsoft-standard-WSL2-issue211",
      "results": [
        {
          "completed_frames": 3,
          "cancelled_callbacks": 0,
          "observed_tids": [
            434,
            437
          ],
          "successful_buffer_sequences": [
            0,
            1,
            2
          ],
          "pid": 434,
          "allocations": 4
        },
        {
          "completed_frames": 3,
          "cancelled_callbacks": 0,
          "observed_tids": [
            449,
            452
          ],
          "successful_buffer_sequences": [
            0,
            1,
            2
          ],
          "pid": 449,
          "allocations": 4
        },
        {
          "completed_frames": 3,
          "cancelled_callbacks": 0,
          "observed_tids": [
            464,
            467
          ],
          "successful_buffer_sequences": [
            0,
            1,
            2
          ],
          "pid": 464,
          "allocations": 4
        }
      ],
      "source_unmodified": true,
      "allocator": "udmabuf built-in, /dev/udmabuf root-only; permissions unchanged",
      "run_threads": [
        {
          "pid": 434,
          "callbacks": [
            437
          ],
          "processed": [
            434
          ]
        },
        {
          "pid": 449,
          "callbacks": [
            452
          ],
          "processed": [
            449
          ]
        },
        {
          "pid": 464,
          "callbacks": [
            467
          ],
          "processed": [
            464
          ]
        }
      ],
      "inferior_exit_codes": [
        0,
        0,
        0
      ],
      "processed_sequences": [
        [
          0,
          1,
          2
        ],
        [
          0,
          1,
          2
        ],
        [
          0,
          1,
          2
        ]
      ],
      "dma_probe_events": [
        {
          "event": "provider-open",
          "provider": "/dev/udmabuf",
          "result": 3,
          "errno": 0
        },
        {
          "event": "allocate",
          "result": 5,
          "errno": 0,
          "backing_fd": 4,
          "dmabuf_fd": 5,
          "size": 4096
        },
        {
          "event": "mmap",
          "result": 0,
          "errno": 0
        },
        {
          "event": "sync-start",
          "result": 0,
          "errno": 0,
          "flags": 3,
          "retry": false
        },
        {
          "event": "cpu-access",
          "result": 0,
          "errno": 0,
          "bytes": 4096,
          "checksum": 522240
        },
        {
          "event": "sync-end",
          "result": 0,
          "errno": 0,
          "flags": 7,
          "retry": false
        },
        {
          "event": "munmap",
          "result": 0,
          "errno": 0
        },
        {
          "event": "close-dmabuf",
          "result": 0,
          "errno": 0
        },
        {
          "event": "close-backing",
          "result": 0,
          "errno": 0
        },
        {
          "event": "close-provider",
          "result": 0,
          "errno": 0
        }
      ],
      "pretrial_kernel": "6.18.33.2-microsoft-standard-WSL2",
      "pretrial_udmabuf": false,
      "pretrial_dmabuf_heaps": false,
      "pretrial_provider_devices_present": false,
      "kernel_trial_authorized_by_user": true,
      "restored_kernel": "6.18.33.2-microsoft-standard-WSL2",
      "restored_wslconfig_exists": false,
      "matching_modules_installed": false,
      "docker_during_trial": "stopped",
      "unprivileged_run": {
        "status": "failed",
        "errno": 13
      },
      "observation_limits": [
        "GDB breakpoints affect timing",
        "No callback-return instruction observation",
        "Cancellation branch not dynamically exercised; observed count 0 is not forced"
      ],
      "physical_dma": "not-validated",
      "physical_camera": "not-run",
      "production_application": "not-run",
      "internal_hal": "not-run",
      "human_review": "pending",
      "raw_evidence": "https://github.com/TTolsun/camera-hal-sdd-generator/tree/main/examples/libcamera/validation/issue211/runs/20261031-wsl-cam-3",
      "official_allocator_observations": [
        {
          "pid": 434,
          "successful_allocations": 4,
          "providers": [
            "/dev/udmabuf"
          ],
          "exporters": [
            "udmabuf"
          ],
          "raw_sha256": "bfc0215112bb3a7e30cf66e2ce016dbcc3bd1ad7f7d3ba79d14c868d29417bd2"
        },
        {
          "pid": 449,
          "successful_allocations": 4,
          "providers": [
            "/dev/udmabuf"
          ],
          "exporters": [
            "udmabuf"
          ],
          "raw_sha256": "0529146d43e1f826240fa9790545e81b69b274dca8173d9da598add516320727"
        },
        {
          "pid": 464,
          "successful_allocations": 4,
          "providers": [
            "/dev/udmabuf"
          ],
          "exporters": [
            "udmabuf"
          ],
          "raw_sha256": "38433db15aa2928b1e6fe0f54293fd3b4ee34eb1b9b9d5e5b10526c89605d46a"
        }
      ],
      "baseline_capture": {
        "inferior_exit": {
          "exit_code": 1,
          "observation_failures": []
        },
        "errors": [
          "[0:07:17.247127806] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider",
          "[0:07:17.258236285] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider",
          "Can't allocate buffers"
        ],
        "stdout_sha256": "2432d60d69ed6e496a45df1c3edac64e9296b1c77f5054a60aa9d40a75ae5bd1",
        "stderr_sha256": "cdcfbb0f7b1d46f55b30b94e7a1de119dfcfb7ab937fbb18cda4be9397e8e32a",
        "raw_url": "https://github.com/TTolsun/camera-hal-sdd-generator/tree/580df5156da7066a60e16ff9b656253b1c17f0c0/examples/libcamera/validation/issue211/runs/20261031-runtime-negative/official-cam-debugger-before"
      },
      "source_measurement": {
        "sha256": "6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1",
        "url": "https://github.com/TTolsun/libcamera-sdd/blob/d36affef9b3a741581d1c5f0f4cd68425c5dbe15/publication/issue211/config/product-evidence/official-cam-observation.json",
        "operation": "Exact projection of named original fields, no new runtime execution"
      }
    }
    
    ```
    
    ```json
    {
      "type": "measurement",
      "supplier": "Source-pinned official cam trial; raw events, GDB, syscall and cleanup records",
      "version": "6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1",
      "date": "2026-10-31",
      "valid_until": "2026-10-31",
      "product": "libcamera-official-cam-trial",
      "release": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "configuration": "wsl2-virtual2-official-cam-udmabuf",
      "feature": "wsl-virtual-capture",
      "conditions": [
        "Source 293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
        "WSL2 custom UDMABUF kernel, root child, Virtual2 400x300 NV12",
        "GDB observation; no timing/return/physical/internal HAL qualification"
      ],
      "sha256": "6ad6510d9624cd8075ccdc0a4622214c441afc5a778a2e577b4c7a76bf10efc0"
    }
    ```

<a id="source-10812730226e86cc"></a>

??? note "제품 자료: product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1"
    소스와 별도로 제공된 자료입니다. 제공자·버전·적용 범위를 아래 기록에서 확인하세요. 자동 검사는 사람 승인이 아닙니다.
    
    `product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt:1`에서 시작하는 발췌입니다. 종료 줄은 38이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `93f4c8ea45fc873453b7739b88105877f6b1bc60ed7f3f6a280b15d8b131a9a7`
    
    ````text
    # 공식 cam WSL 가상 카메라 검증
    
    ## 결론과 다음 행동
    
    먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.
    
    ## 관측된 결과
    
    소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.
    
    세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.
    
    DMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.
    
    `cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.
    
    ## 범위와 한계
    
    이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.
    
    권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.
    
    GDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.
    
    ## 실행 전 준비
    
    1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.
    2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.
    3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.
    4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.
    5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.
    
    ```
    PYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>
    ```
    
    CPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.
    
    ````
    
    ```json
    {
      "type": "project-document",
      "supplier": "Source-pinned official cam trial; raw events, GDB, syscall and cleanup records",
      "version": "580df5156da7066a60e16ff9b656253b1c17f0c0",
      "date": "2026-10-31",
      "valid_until": "2026-10-31",
      "product": "libcamera-official-cam-trial",
      "release": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "configuration": "wsl2-virtual2-official-cam-udmabuf",
      "feature": "wsl-virtual-capture",
      "conditions": [
        "Source 293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
        "WSL2 custom UDMABUF kernel, root child, Virtual2 400x300 NV12",
        "GDB observation; no timing/return/physical/internal HAL qualification"
      ],
      "sha256": "93f4c8ea45fc873453b7739b88105877f6b1bc60ed7f3f6a280b15d8b131a9a7"
    }
    ```

<a id="source-4f7002340059b1cf"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/README.md:3"
    `src/libcamera/pipeline/virtual/README.md:3`에서 시작하는 발췌입니다. 종료 줄은 47이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a5bd122270c864d666142a7027e54f0948d458545dd452fbfe97b87e7d66565c`
    
    ```text
    # Virtual Pipeline Handler
    
    Virtual pipeline handler emulates fake external camera(s) for testing.
    
    ## Parse config file and register cameras
    
    - A sample config file is located at `src/libcamera/pipeline/virtual/data/virtual.yaml`.
    - If libcamera is installed, the config file should be installed at
      `share/libcamera/pipeline/virtual/virtual.yaml`.
    
    ### Config File Format
    
    The config file contains the information about cameras' properties to register.
    The config file should be a yaml file with dictionary of the cameraIds
    associated with their properties as top level. The default value will be applied
    when any property is empty.
    
    Each camera block is a dictionary, containing the following keys:
    - `supported_formats` (list of `VirtualCameraData::Resolution`, optional):
      List of supported resolution and frame rates of the emulated camera
        - `width` (`unsigned int`, default=1920): Width of the window resolution.
          This needs to be even.
        - `height` (`unsigned int`, default=1080): Height of the window resolution.
        - `frame_rates` (list of `int`, default=`[30,60]` ): Range of the frame
          rate (per second). If the list contains one value, it's the lower bound
          and the upper bound. If the list contains two values, the first is the
          lower bound and the second is the upper bound. No other number of values
          is allowed.
    - `test_pattern` (`string`): Which test pattern to use as frames. The options
      are "bars", "lines". Cannot be set with `frames`.
      - The test patterns are "bars" which means color bars, and "lines" which means
        diagonal lines.
    - `frames` (dictionary):
      - `path` (`string`): Path to an image, or path to a directory of a series of
        images. Cannot be set with `test_pattern`.
        - The path to an image has ".jpg" extension.
        - The path to a directory ends with "/". The name of the images in the
          directory are "{n}.jpg" with {n} is the sequence of images starting with 0.
    - `location` (`string`, default="front"): The location of the camera. Support
      "Front", "Back", and "External".
    - `model` (`string`, default="Unknown"): The model name of the camera.
    
    Check `data/virtual.yaml` as the sample config file.
    
    ### Implementation
    ```

<a id="source-9858e22e2225cc10"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/data/virtual.yaml:28"
    `src/libcamera/pipeline/virtual/data/virtual.yaml:28`에서 시작하는 발췌입니다. 종료 줄은 32이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b9a78428bbde1f8b2a7ae34fc352cf6576ca0f24ee5d0ba7a94a0b790bfd2dc3`
    
    ```text
    "Virtual2":
      supported_formats:
      - width: 400
        height: 300
      test_pattern: "lines"
    ```

<a id="source-1868fec3abf482b8"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/virtual.cpp:356"
    `src/libcamera/pipeline/virtual/virtual.cpp:356`에서 시작하는 발췌입니다. 종료 줄은 373이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `17db9f86c10efedebf2b21298865cea7070c1c384427e7a2e386899273d07f86`
    
    ```text
    int PipelineHandlerVirtual::exportFrameBuffers([[maybe_unused]] Camera *camera,
    					       Stream *stream,
    					       std::vector<std::unique_ptr<FrameBuffer>> *buffers)
    {
    	if (!dmaBufAllocator_.isValid())
    		return -ENOBUFS;
    
    	const StreamConfiguration &config = stream->configuration();
    	const PixelFormatInfo &info = PixelFormatInfo::info(config.pixelFormat);
    
    	std::vector<unsigned int> planeSizes;
    	for (size_t i = 0; i < info.numPlanes(); ++i)
    		planeSizes.push_back(info.planeSize(config.size, i));
    
    	return dmaBufAllocator_.exportBuffers(config.bufferCount, planeSizes, buffers);
    }
    
    int PipelineHandlerVirtual::start(
    ```

<a id="source-1c0d5dcdba46688e"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/virtual.cpp:412"
    `src/libcamera/pipeline/virtual/virtual.cpp:412`에서 시작하는 발췌입니다. 종료 줄은 438이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8e757a1e7d0904f9affb3c2ba07e42c9f40b5bcd029d7dd834f853192c9192bc`
    
    ```text
    int PipelineHandlerVirtual::queueRequestDevice(Camera *camera, Request *request)
    {
    	VirtualCameraData *data = cameraData(camera);
    
    	data->processControls(request->controls());
    
    	/*
    	 * TODO: Skip frames if we can't keep up with the maximum frame
    	 * duration.
    	 */
    	data->targetTimestamp_ = std::max(
    		currentTimestamp(),
    		data->targetTimestamp_ + data->targetFrameDuration_ * 1000);
    
    	request->_d()->metadata().set(controls::SensorTimestamp,
    				      data->targetTimestamp_);
    	request->_d()->metadata().set(controls::FrameDuration,
    				      data->targetFrameDuration_);
    
    	data->invokeMethod(&VirtualCameraData::processRequest,
    			   ConnectionTypeQueued, request,
    			   data->targetTimestamp_);
    
    	return 0;
    }
    
    bool PipelineHandlerVirtual::match(
    ```

<a id="source-995da70adf556e1f"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/virtual.cpp:138"
    `src/libcamera/pipeline/virtual/virtual.cpp:138`에서 시작하는 발췌입니다. 종료 줄은 175이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `3aa1f6c1a27781a50ede523a3aa971590d1a2a0fdc4d8730ec320bd03d5586df`
    
    ```text
    void VirtualCameraData::processRequest(Request *request,
    				       uint64_t targetTimestamp)
    {
    	const auto targetTime = std::chrono::steady_clock::time_point{
    		std::chrono::nanoseconds(targetTimestamp)
    	};
    	std::this_thread::sleep_until(targetTime);
    
    	for (const auto &[stream, buffer] : request->buffers()) {
    		bool found = false;
    		/* map buffer and fill test patterns */
    		for (auto &streamConfig : streamConfigs_) {
    			if (stream == &streamConfig.stream) {
    				FrameMetadata &fmd = buffer->_d()->metadata();
    
    				fmd.status = FrameMetadata::Status::FrameSuccess;
    				fmd.sequence = streamConfig.seq++;
    				fmd.timestamp = targetTimestamp;
    
    				std::span<const FrameBuffer::Plane> planes = buffer->planes();
    				for (const auto [i, p] : utils::enumerate(planes))
    					fmd.planes()[i].bytesused = p.length;
    
    				found = true;
    
    				if (streamConfig.frameGenerator->generateFrame(
    					    stream->configuration(), buffer))
    					fmd.status = FrameMetadata::Status::FrameError;
    
    				bufferCompleted.emit(buffer);
    				break;
    			}
    		}
    		ASSERT(found);
    	}
    }
    
    void VirtualCameraData::processControls(
    ```

<a id="source-fa5429fa2c62882d"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47"
    `src/libcamera/pipeline/virtual/test_pattern_generator.cpp:47`에서 시작하는 발췌입니다. 종료 줄은 108이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `738b0b9f5b7bfe29a00c643ec5f51174b012a5798ed3bf0c7e0e2b7f8bdc1243`
    
    ```text
    int TestPatternGenerator::generateFrame(const StreamConfiguration &cfg,
    					const FrameBuffer *buffer)
    {
    	/*
    	 * \todo Assume all planes are contiguous and mapped at different
    	 * offsets on the same fd. This holds true as long as the implementation
    	 * of DmaBufAllocator only allocates contiguous planes. If this will
    	 * change or a different allocator will be used then we need to create
    	 * one dma syncer for each non-contiguous plane.
    	 */
    	DmaSyncer outDmaSyncer(buffer->planes()[0].fd,
    			       DmaSyncer::SyncType::Write);
    	MappedFrameBuffer mappedFrameBuffer(buffer,
    					    MappedFrameBuffer::MapFlag::Write);
    
    	const auto &planes = mappedFrameBuffer.planes();
    	const Size &size = cfg.size;
    	const PixelFormatInfo &info = PixelFormatInfo::info(cfg.pixelFormat);
    
    	rotateLeft1Column<kARGBSize>(size, template_.get());
    
    	int ret;
    
    	/* Convert the template_ to the frame buffer */
    	switch (cfg.pixelFormat) {
    	case formats::NV12:
    		ret = libyuv::ARGBToNV12(template_.get(),
    					 size.width * kARGBSize,
    					 planes[0].data(), info.stride(size.width, 0),
    					 planes[1].data(), info.stride(size.width, 1),
    					 size.width, size.height);
    		break;
    
    	case formats::YUV420:
    		ret = libyuv::ARGBToI420(template_.get(),
    					 size.width * kARGBSize,
    					 planes[0].data(), info.stride(size.width, 0),
    					 planes[1].data(), info.stride(size.width, 1),
    					 planes[2].data(), info.stride(size.width, 2),
    					 size.width, size.height);
    		break;
    
    	case formats::ABGR8888:
    	case formats::XBGR8888:
    		ret = libyuv::ARGBCopy(template_.get(),
    				       size.width * kARGBSize,
    				       planes[0].data(), info.stride(size.width, 0),
    				       size.width, size.height);
    		break;
    
    	default:
    		LOG(Virtual, Error) << "Unsupported format";
    		return -1;
    	}
    
    	if (ret != 0)
    		LOG(Virtual, Error) << "Conversion failed with " << ret;
    
    	return ret;
    }
    
    void ColorBarsGenerator::configure(
    ```

<a id="source-ab86b02a265cd2b8"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/virtual.cpp:515"
    `src/libcamera/pipeline/virtual/virtual.cpp:515`에서 시작하는 발췌입니다. 종료 줄은 523이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `28644312a9d533446fd2224c0294814b45f335d63f67b78e19dff31eae9537da`
    
    ```text
    void PipelineHandlerVirtual::bufferCompleted(FrameBuffer *buffer)
    {
    	Request *request = buffer->request();
    
    	if (completeBuffer(request, buffer))
    		completeRequest(request);
    }
    
    REGISTER_PIPELINE_HANDLER
    ```

<a id="source-5e575d092c08b32d"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:469"
    `src/libcamera/pipeline_handler.cpp:469`에서 시작하는 발췌입니다. 종료 줄은 530이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `cb607d060ba4eb069998bde3ed10bd4cdec9a7315e40b4b5da7ba877b5f98678`
    
    ```text
    void PipelineHandler::queueRequest(Request *request)
    {
    	LIBCAMERA_TRACEPOINT(request_queue, request);
    
    	Camera *camera = request->_d()->camera();
    	Camera::Private *data = camera->_d();
    	data->waitingRequests_.push(request);
    
    	request->_d()->prepare(300ms);
    }
    
    /**
     * \brief Queue one requests to the device
     */
    void PipelineHandler::doQueueRequest(Request *request)
    {
    	LIBCAMERA_TRACEPOINT(request_device_queue, request);
    
    	Camera *camera = request->_d()->camera();
    	Camera::Private *data = camera->_d();
    	data->queuedRequests_.push_back(request);
    
    	request->_d()->sequence_ = data->requestSequence_++;
    
    	if (request->_d()->cancelled_) {
    		completeRequest(request);
    		return;
    	}
    
    	int ret = queueRequestDevice(camera, request);
    	if (ret)
    		cancelRequest(request);
    }
    
    /**
     * \brief Queue prepared requests to the device
     *
     * Iterate the list of waiting requests and queue them to the device one
     * by one if they have been prepared.
     */
    void PipelineHandler::doQueueRequests(Camera *camera)
    {
    	Camera::Private *data = camera->_d();
    	while (!data->waitingRequests_.empty()) {
    		if (data->queuedRequests_.size() == maxQueuedRequestsDevice_)
    			break;
    
    		Request *request = data->waitingRequests_.front();
    		if (!request->_d()->prepared_)
    			break;
    
    		/*
    		 * Pop the request first, in case doQueueRequests() is called
    		 * recursively from within doQueueRequest()
    		 */
    		data->waitingRequests_.pop();
    		doQueueRequest(request);
    	}
    }
    
    /**
     * \fn PipelineHandler::queueRequestDevice()
    ```

<a id="source-7cb889331b58a531"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:563"
    `src/libcamera/pipeline_handler.cpp:563`에서 시작하는 발췌입니다. 종료 줄은 613이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `eae578aef59d31f488400f7739ce0af433b2a47d857efdca754584f4b850b637`
    
    ```text
    bool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)
    {
    	Camera *camera = request->_d()->camera();
    	camera->bufferCompleted.emit(request, buffer);
    	return request->_d()->completeBuffer(buffer);
    }
    
    /**
     * \brief Signal request completion
     * \param[in] request The request that has completed
     *
     * The pipeline handler shall call this function to notify the \a camera that
     * the request has completed. The request is no longer managed by the pipeline
     * handler and shall not be accessed once this function returns.
     *
     * This function ensures that requests will be returned to the application in
     * submission order, the pipeline handler may call it on any complete request
     * without any ordering constraint.
     *
     * \context This function shall be called from the CameraManager thread.
     */
    void PipelineHandler::completeRequest(Request *request)
    {
    	Camera *camera = request->_d()->camera();
    
    	request->_d()->complete();
    
    	Camera::Private *data = camera->_d();
    
    	while (!data->queuedRequests_.empty()) {
    		Request *req = data->queuedRequests_.front();
    		if (req->status() == Request::RequestPending)
    			break;
    
    		ASSERT(!req->hasPendingBuffers());
    		data->queuedRequests_.pop_front();
    		camera->requestComplete(req);
    	}
    
    	/* Allow any waiting requests to be queued to the pipeline. */
    	doQueueRequests(camera);
    }
    
    /**
     * \brief Cancel request and signal its completion
     * \param[in] request The request to cancel
     *
     * This function cancels and completes the request. The same rules as for
     * completeRequest() apply.
     */
    void PipelineHandler::cancelRequest(
    ```

<a id="source-655b027df7d08524"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1481"
    `src/libcamera/camera.cpp:1481`에서 시작하는 발췌입니다. 종료 줄은 1491이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `aadfd6b4fdf910083a3d97fb11c623145f71553c9240f8e882d619fce61c43bb`
    
    ```text
    void Camera::requestComplete(Request *request)
    {
    	/* Disconnected cameras are still able to complete requests. */
    	if (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,
    				  true))
    		LOG(Camera, Fatal) << "Trying to complete a request when stopped";
    
    	requestCompleted.emit(request);
    }
    
    } /* namespace libcamera */
    ```

<a id="source-5723cb743173a3dd"></a>

??? note "소스 근거: src/apps/cam/camera_session.cpp:365"
    `src/apps/cam/camera_session.cpp:365`에서 시작하는 발췌입니다. 종료 줄은 467이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `37ab5790b8eb30e2c5c484e7a3e86f59ec2a4927dcbf8c1b2aa8ffd9ba5af417`
    
    ```text
    int CameraSession::startCapture()
    {
    	int ret;
    
    	/* Identify the stream with the least number of buffers. */
    	unsigned int nbuffers = UINT_MAX;
    	for (StreamConfiguration &cfg : *config_) {
    		ret = allocator_->allocate(cfg.stream());
    		if (ret < 0) {
    			std::cerr << "Can't allocate buffers" << std::endl;
    			return -ENOMEM;
    		}
    
    		unsigned int allocated = allocator_->buffers(cfg.stream()).size();
    		nbuffers = std::min(nbuffers, allocated);
    	}
    
    	/*
    	 * TODO: make cam tool smarter to support still capture by for
    	 * example pushing a button. For now run all streams all the time.
    	 */
    
    	for (unsigned int i = 0; i < nbuffers; i++) {
    		std::unique_ptr<Request> request = camera_->createRequest();
    		if (!request) {
    			std::cerr << "Can't create request" << std::endl;
    			return -ENOMEM;
    		}
    
    		for (StreamConfiguration &cfg : *config_) {
    			Stream *stream = cfg.stream();
    			const std::vector<std::unique_ptr<FrameBuffer>> &buffers =
    				allocator_->buffers(stream);
    			const std::unique_ptr<FrameBuffer> &buffer = buffers[i];
    
    			ret = request->addBuffer(stream, buffer.get());
    			if (ret < 0) {
    				std::cerr << "Can't set buffer for request"
    					  << std::endl;
    				return ret;
    			}
    
    			if (sink_)
    				sink_->mapBuffer(buffer.get());
    		}
    
    		requests_.push_back(std::move(request));
    	}
    
    	if (sink_) {
    		ret = sink_->start();
    		if (ret) {
    			std::cout << "Failed to start frame sink" << std::endl;
    			return ret;
    		}
    	}
    
    	ret = camera_->start();
    	if (ret) {
    		std::cout << "Failed to start capture" << std::endl;
    		if (sink_)
    			sink_->stop();
    		return ret;
    	}
    
    	for (std::unique_ptr<Request> &request : requests_) {
    		ret = queueRequest(request.get());
    		if (ret < 0) {
    			std::cerr << "Can't queue request" << std::endl;
    			camera_->stop();
    			if (sink_)
    				sink_->stop();
    			return ret;
    		}
    	}
    
    	if (captureLimit_)
    		std::cout << "cam" << cameraIndex_
    			  << ": Capture " << captureLimit_ << " frames"
    			  << std::endl;
    	else
    		std::cout << "cam" << cameraIndex_
    			  << ": Capture until user interrupts by SIGINT"
    			  << std::endl;
    
    	return 0;
    }
    
    int CameraSession::queueRequest(Request *request)
    {
    	if (captureLimit_ && queueCount_ >= captureLimit_)
    		return 0;
    
    	if (script_)
    		request->controls().merge(script_->frameControls(queueCount_),
    					  ControlList::MergePolicy::OverwriteExisting);
    
    	queueCount_++;
    
    	return camera_->queueRequest(request);
    }
    
    void CameraSession::requestComplete(
    ```

<a id="source-fb9506413ce52fb0"></a>

??? note "소스 근거: src/apps/cam/camera_session.cpp:305"
    `src/apps/cam/camera_session.cpp:305`에서 시작하는 발췌입니다. 종료 줄은 307이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `837c0da1b2fd6f71aaabdb090306d3deda89c0fae6de39e91393d1111748e1b7`
    
    ```text
    	camera_->requestCompleted.connect(this, &CameraSession::requestComplete);
    
    #ifdef HAVE_KMS
    ```

<a id="source-e91194807faa9e0c"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:86"
    `src/libcamera/framebuffer_allocator.cpp:86`에서 시작하는 발췌입니다. 종료 줄은 119이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `860da864490293ef6a9228ca9babb066369470fecf3936e4b0807c8e43364403`
    
    ```text
    int FrameBufferAllocator::allocate(Stream *stream)
    {
    	const auto &[it, inserted] = buffers_.try_emplace(stream);
    
    	if (!inserted) {
    		LOG(Allocator, Error) << "Buffers already allocated for stream";
    		return -EBUSY;
    	}
    
    	int ret = camera_->exportFrameBuffers(stream, &it->second);
    	if (ret == -EINVAL)
    		LOG(Allocator, Error)
    			<< "Stream is not part of " << camera_->id()
    			<< " active configuration";
    
    	if (ret < 0)
    		buffers_.erase(it);
    
    	return ret;
    }
    
    /**
     * \brief Free buffers previously allocated for a \a stream
     * \param[in] stream The stream
     *
     * Free buffers allocated with allocate().
     *
     * This invalidates the buffers returned by buffers().
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -EACCES The camera is not in a state where buffers can be freed
     * \retval -EINVAL The allocator do not handle the \a stream
     */
    int FrameBufferAllocator::free(
    ```

<a id="source-80fd4657ae4c65d1"></a>

??? note "소스 근거: src/libcamera/camera.cpp:963"
    `src/libcamera/camera.cpp:963`에서 시작하는 발췌입니다. 종료 줄은 1007이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `bfd7aa3f1785e3d1dbc4c8507aafbb7c799371e924ec743523f6078a3c37640f`
    
    ```text
    int Camera::exportFrameBuffers(Stream *stream,
    			       std::vector<std::unique_ptr<FrameBuffer>> *buffers)
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraConfigured);
    	if (ret < 0)
    		return ret;
    
    	if (streams().find(stream) == streams().end())
    		return -EINVAL;
    
    	if (d->activeStreams_.find(stream) == d->activeStreams_.end())
    		return -EINVAL;
    
    	return d->pipe_->invokeMethod(&PipelineHandler::exportFrameBuffers,
    				      ConnectionTypeBlocking, this, stream,
    				      buffers);
    }
    
    /**
     * \brief Acquire the camera device for exclusive access
     *
     * After opening the device with open(), exclusive access must be obtained
     * before performing operations that change the device state. This function is
     * not blocking, if the device has already been acquired (by the same or another
     * process) the -EBUSY error code is returned.
     *
     * Acquiring a camera may limit usage of any other camera(s) provided by the
     * same pipeline handler to the same instance of libcamera. The limit is in
     * effect until all cameras from the pipeline handler are released. Other
     * instances of libcamera can still list and examine the cameras but will fail
     * if they attempt to acquire() any of them.
     *
     * Once exclusive access isn't needed anymore, the device should be released
     * with a call to the release() function.
     *
     * \context This function is \threadsafe. It may only be called when the camera
     * is in the Available state as defined in \ref camera_operation.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EBUSY The camera is not free and can't be acquired by the caller
     */
    int Camera::acquire(
    ```

<a id="source-d6d48aa78159fb58"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1330"
    `src/libcamera/camera.cpp:1330`에서 시작하는 발췌입니다. 종료 줄은 1400이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `886535d24df67a4b6f18fd5ed7b1db02e74e189ebfcb7ddd396eb86cf30980ef`
    
    ```text
    int Camera::queueRequest(Request *request)
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraRunning);
    	if (ret < 0)
    		return ret;
    
    	/* Requests can only be queued to the camera that created them. */
    	if (request->_d()->camera() != this) {
    		LOG(Camera, Error) << "Request was not created by this camera";
    		return -EXDEV;
    	}
    
    	if (request->status() != Request::RequestPending) {
    		LOG(Camera, Error) << request->toString() << " is not valid";
    		return -EINVAL;
    	}
    
    	/* Make sure the Request has a valid control list. */
    	if (request->controls().infoMap() != &controls()) {
    		LOG(Camera, Error) << "Overwriting Request::controls() is not allowed";
    		return -EINVAL;
    	}
    
    	/*
    	 * The camera state may change until the end of the function. No locking
    	 * is however needed as PipelineHandler::queueRequest() will handle
    	 * this.
    	 */
    
    	if (request->buffers().empty()) {
    		LOG(Camera, Error) << "Request contains no buffers";
    		return -EINVAL;
    	}
    
    	for (const auto &[stream, buffer] : request->buffers()) {
    		if (d->activeStreams_.find(stream) == d->activeStreams_.end()) {
    			LOG(Camera, Error) << "Invalid request";
    			return -EINVAL;
    		}
    	}
    
    	/* Pre-process AeEnable. */
    	patchControlList(request->controls());
    
    	d->pipe_->invokeMethod(&PipelineHandler::queueRequest,
    			       ConnectionTypeQueued, request);
    
    	return 0;
    }
    
    /**
     * \brief Start capture from camera
     * \param[in] controls Controls to be applied before starting the Camera
     *
     * Start the camera capture session, optionally providing a list of controls to
     * apply before starting. Once the camera is started the application can queue
     * requests to the camera to process and return to the application until the
     * capture session is terminated with \a stop().
     *
     * \context This function may only be called when the camera is in the
     * Configured state as defined in \ref camera_operation, and shall be
     * synchronized by the caller with other functions that affect the camera
     * state.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not in a state where it can be started
     */
    int Camera::start(
    ```

<a id="source-4726a7d0b3f38c49"></a>

??? note "소스 근거: src/libcamera/pipeline/virtual/virtual.cpp:373"
    `src/libcamera/pipeline/virtual/virtual.cpp:373`에서 시작하는 발췌입니다. 종료 줄은 395이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a874aaf3a8902d67c4b8bfe9166ff2783f4dc95ba98b2ce2e72b454de78b7a2b`
    
    ```text
    int PipelineHandlerVirtual::start(Camera *camera, const ControlList *controls)
    {
    	VirtualCameraData *data = cameraData(camera);
    
    	/* By default target the highest frame rate allowed by the config. */
    	data->targetFrameDuration_ = data->config_.frameDurationLimits[0];
    	ASSERT(data->targetFrameDuration_ > 0);
    
    	if (controls)
    		data->processControls(*controls);
    
    	data->targetTimestamp_ = 0;
    
    	for (auto &s : data->streamConfigs_)
    		s.seq = 0;
    
    	data->bufferCompleted.connect(this, &PipelineHandlerVirtual::bufferCompleted);
    	data->start();
    
    	return 0;
    }
    
    void PipelineHandlerVirtual::stopDevice(
    ```

<a id="source-4fe013027055fa2d"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:435"
    `src/libcamera/pipeline_handler.cpp:435`에서 시작하는 발췌입니다. 종료 줄은 469이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e26bfa8d7aabb043998df27778cce4f5a3724b9130695499701db24012fa111d`
    
    ```text
    void PipelineHandler::registerRequest(Request *request)
    {
    	/*
    	 * Connect the request prepared signal to notify the pipeline handler
    	 * when a request is ready to be processed.
    	 */
    	request->_d()->prepared.connect(this, [this, request]() {
    		doQueueRequests(request->_d()->camera());
    	});
    }
    
    /**
     * \fn PipelineHandler::queueRequest()
     * \brief Queue a request
     * \param[in] request The request to queue
     *
     * This function queues a capture request to the pipeline handler for
     * processing. The request is first added to the internal list of waiting
     * requests which have to be prepared to make sure they are ready for being
     * queued to the pipeline handler.
     *
     * The queue of waiting requests is iterated and up to \a
     * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler
     * in the same order they have been queued by calling this function.
     *
     * If a Request fails during the preparation phase or if the pipeline handler
     * fails in queuing the request to the hardware the request is cancelled.
     *
     * Keeping track of queued requests ensures automatic completion of all requests
     * when the pipeline handler is stopped with stop(). Request completion shall be
     * signalled by the pipeline handler using the completeRequest() function.
     *
     * \context This function is called from the CameraManager thread.
     */
    void PipelineHandler::queueRequest(
    ```

<a id="source-0626196def047e5c"></a>

??? note "소스 근거: src/libcamera/request.cpp:125"
    `src/libcamera/request.cpp:125`에서 시작하는 발췌입니다. 종료 줄은 139이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2efec13b708bff2ca232445ef868877a30facef1b6fa17ddcff47bfd013e2289`
    
    ```text
    void Request::Private::complete()
    {
    	Request *request = _o<Request>();
    
    	ASSERT(request->status() == RequestPending);
    	ASSERT(!hasPendingBuffers());
    
    	request->status_ = cancelled_ ? RequestCancelled : RequestComplete;
    
    	LOG(Request, Debug) << request->toString();
    
    	LIBCAMERA_TRACEPOINT(request_complete, this);
    }
    
    void Request::Private::doCancelRequest()
    ```

<a id="source-4c93e74b4521da77"></a>

??? note "소스 근거: src/apps/cam/camera_session.cpp:365"
    `src/apps/cam/camera_session.cpp:365`에서 시작하는 발췌입니다. 종료 줄은 422이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0d14fd27f930b07e23e8bbfe0e8b58d62e414bf7a7dab34789501d1c55423e56`
    
    ```text
    int CameraSession::startCapture()
    {
    	int ret;
    
    	/* Identify the stream with the least number of buffers. */
    	unsigned int nbuffers = UINT_MAX;
    	for (StreamConfiguration &cfg : *config_) {
    		ret = allocator_->allocate(cfg.stream());
    		if (ret < 0) {
    			std::cerr << "Can't allocate buffers" << std::endl;
    			return -ENOMEM;
    		}
    
    		unsigned int allocated = allocator_->buffers(cfg.stream()).size();
    		nbuffers = std::min(nbuffers, allocated);
    	}
    
    	/*
    	 * TODO: make cam tool smarter to support still capture by for
    	 * example pushing a button. For now run all streams all the time.
    	 */
    
    	for (unsigned int i = 0; i < nbuffers; i++) {
    		std::unique_ptr<Request> request = camera_->createRequest();
    		if (!request) {
    			std::cerr << "Can't create request" << std::endl;
    			return -ENOMEM;
    		}
    
    		for (StreamConfiguration &cfg : *config_) {
    			Stream *stream = cfg.stream();
    			const std::vector<std::unique_ptr<FrameBuffer>> &buffers =
    				allocator_->buffers(stream);
    			const std::unique_ptr<FrameBuffer> &buffer = buffers[i];
    
    			ret = request->addBuffer(stream, buffer.get());
    			if (ret < 0) {
    				std::cerr << "Can't set buffer for request"
    					  << std::endl;
    				return ret;
    			}
    
    			if (sink_)
    				sink_->mapBuffer(buffer.get());
    		}
    
    		requests_.push_back(std::move(request));
    	}
    
    	if (sink_) {
    		ret = sink_->start();
    		if (ret) {
    			std::cout << "Failed to start frame sink" << std::endl;
    			return ret;
    		}
    	}
    
    	ret = camera_->start();
    ```

<a id="source-67134777ea4213e0"></a>

??? note "제품 자료: product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1"
    소스와 별도로 제공된 자료입니다. 제공자·버전·적용 범위를 아래 기록에서 확인하세요. 자동 검사는 사람 승인이 아닙니다.
    
    `product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt:1`에서 시작하는 발췌입니다. 종료 줄은 9이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fe1292511ffbf64b3e2aaee046d28048675c0283b82187cfa421e0431c834e0d`
    
    ```text
    {
      "url": "https://github.com/TTolsun/camera-hal-sdd-generator/issues/211",
      "updated_at": "2026-10-31T06:00:33Z",
      "verbatim_contract_lines": [
        "1. 선택한 커널의 Kconfig·의존성·실제 사용 가능한 모듈·할당기 후보를 조사하고 하나를 선택합니다. 기존 WSL에 새 배포판을 추가하는 것만으로 커널이 격리된다고 취급하지 않습니다.",
        "2. 기존 WSL/Docker에 영향을 주지 않는 시험 환경을 우선합니다. 현재 호스트의 공유 커널·모듈·.wslconfig를 변경하거나 배포판/VM을 종료해야 하면 영향과 복구 절차를 먼저 구체화하고 실행 직전에 별도 승인을 받습니다. 기존 PR 병합·Pages 배포 승인을 이런 호스트 변경의 승인으로 확대하지 않습니다."
      ]
    }
    
    ```
    
    ```json
    {
      "type": "project-document",
      "supplier": "GitHub issue211 execution contract, verbatim selected lines",
      "version": "2026-10-31T06:00:33Z",
      "date": "2026-10-31",
      "valid_until": "2026-10-31",
      "product": "libcamera-official-cam-trial",
      "release": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "configuration": "wsl2-virtual2-official-cam-udmabuf",
      "feature": "recorded-no-output-sink",
      "conditions": [
        "Source 293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
        "WSL2 custom UDMABUF kernel, root child, Virtual2 400x300 NV12",
        "GDB observation; no timing/return/physical/internal HAL qualification"
      ],
      "sha256": "fe1292511ffbf64b3e2aaee046d28048675c0283b82187cfa421e0431c834e0d"
    }
    ```

<a id="source-e326d2b05d8f4ef8"></a>

??? note "제품 자료: product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1"
    소스와 별도로 제공된 자료입니다. 제공자·버전·적용 범위를 아래 기록에서 확인하세요. 자동 검사는 사람 승인이 아닙니다.
    
    `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt:1`에서 시작하는 발췌입니다. 종료 줄은 249이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6ad6510d9624cd8075ccdc0a4622214c441afc5a778a2e577b4c7a76bf10efc0`
    
    ```text
    {
      "schema": 1,
      "source_commit": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "camera": "Virtual2",
      "applied_configuration": "(0) 400x300-NV12/SMPTE170M",
      "status": "observed-wsl-virtual-only",
      "kernel": "6.18.33.2-microsoft-standard-WSL2-issue211",
      "results": [
        {
          "completed_frames": 3,
          "cancelled_callbacks": 0,
          "observed_tids": [
            434,
            437
          ],
          "successful_buffer_sequences": [
            0,
            1,
            2
          ],
          "pid": 434,
          "allocations": 4
        },
        {
          "completed_frames": 3,
          "cancelled_callbacks": 0,
          "observed_tids": [
            449,
            452
          ],
          "successful_buffer_sequences": [
            0,
            1,
            2
          ],
          "pid": 449,
          "allocations": 4
        },
        {
          "completed_frames": 3,
          "cancelled_callbacks": 0,
          "observed_tids": [
            464,
            467
          ],
          "successful_buffer_sequences": [
            0,
            1,
            2
          ],
          "pid": 464,
          "allocations": 4
        }
      ],
      "source_unmodified": true,
      "allocator": "udmabuf built-in, /dev/udmabuf root-only; permissions unchanged",
      "run_threads": [
        {
          "pid": 434,
          "callbacks": [
            437
          ],
          "processed": [
            434
          ]
        },
        {
          "pid": 449,
          "callbacks": [
            452
          ],
          "processed": [
            449
          ]
        },
        {
          "pid": 464,
          "callbacks": [
            467
          ],
          "processed": [
            464
          ]
        }
      ],
      "inferior_exit_codes": [
        0,
        0,
        0
      ],
      "processed_sequences": [
        [
          0,
          1,
          2
        ],
        [
          0,
          1,
          2
        ],
        [
          0,
          1,
          2
        ]
      ],
      "dma_probe_events": [
        {
          "event": "provider-open",
          "provider": "/dev/udmabuf",
          "result": 3,
          "errno": 0
        },
        {
          "event": "allocate",
          "result": 5,
          "errno": 0,
          "backing_fd": 4,
          "dmabuf_fd": 5,
          "size": 4096
        },
        {
          "event": "mmap",
          "result": 0,
          "errno": 0
        },
        {
          "event": "sync-start",
          "result": 0,
          "errno": 0,
          "flags": 3,
          "retry": false
        },
        {
          "event": "cpu-access",
          "result": 0,
          "errno": 0,
          "bytes": 4096,
          "checksum": 522240
        },
        {
          "event": "sync-end",
          "result": 0,
          "errno": 0,
          "flags": 7,
          "retry": false
        },
        {
          "event": "munmap",
          "result": 0,
          "errno": 0
        },
        {
          "event": "close-dmabuf",
          "result": 0,
          "errno": 0
        },
        {
          "event": "close-backing",
          "result": 0,
          "errno": 0
        },
        {
          "event": "close-provider",
          "result": 0,
          "errno": 0
        }
      ],
      "pretrial_kernel": "6.18.33.2-microsoft-standard-WSL2",
      "pretrial_udmabuf": false,
      "pretrial_dmabuf_heaps": false,
      "pretrial_provider_devices_present": false,
      "kernel_trial_authorized_by_user": true,
      "restored_kernel": "6.18.33.2-microsoft-standard-WSL2",
      "restored_wslconfig_exists": false,
      "matching_modules_installed": false,
      "docker_during_trial": "stopped",
      "unprivileged_run": {
        "status": "failed",
        "errno": 13
      },
      "observation_limits": [
        "GDB breakpoints affect timing",
        "No callback-return instruction observation",
        "Cancellation branch not dynamically exercised; observed count 0 is not forced"
      ],
      "physical_dma": "not-validated",
      "physical_camera": "not-run",
      "production_application": "not-run",
      "internal_hal": "not-run",
      "human_review": "pending",
      "raw_evidence": "https://github.com/TTolsun/camera-hal-sdd-generator/tree/main/examples/libcamera/validation/issue211/runs/20261031-wsl-cam-3",
      "official_allocator_observations": [
        {
          "pid": 434,
          "successful_allocations": 4,
          "providers": [
            "/dev/udmabuf"
          ],
          "exporters": [
            "udmabuf"
          ],
          "raw_sha256": "bfc0215112bb3a7e30cf66e2ce016dbcc3bd1ad7f7d3ba79d14c868d29417bd2"
        },
        {
          "pid": 449,
          "successful_allocations": 4,
          "providers": [
            "/dev/udmabuf"
          ],
          "exporters": [
            "udmabuf"
          ],
          "raw_sha256": "0529146d43e1f826240fa9790545e81b69b274dca8173d9da598add516320727"
        },
        {
          "pid": 464,
          "successful_allocations": 4,
          "providers": [
            "/dev/udmabuf"
          ],
          "exporters": [
            "udmabuf"
          ],
          "raw_sha256": "38433db15aa2928b1e6fe0f54293fd3b4ee34eb1b9b9d5e5b10526c89605d46a"
        }
      ],
      "baseline_capture": {
        "inferior_exit": {
          "exit_code": 1,
          "observation_failures": []
        },
        "errors": [
          "[0:07:17.247127806] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider",
          "[0:07:17.258236285] [20972] ERROR DmaBufAllocator dma_buf_allocator.cpp:119 Could not open any dma-buf provider",
          "Can't allocate buffers"
        ],
        "stdout_sha256": "2432d60d69ed6e496a45df1c3edac64e9296b1c77f5054a60aa9d40a75ae5bd1",
        "stderr_sha256": "cdcfbb0f7b1d46f55b30b94e7a1de119dfcfb7ab937fbb18cda4be9397e8e32a",
        "raw_url": "https://github.com/TTolsun/camera-hal-sdd-generator/tree/580df5156da7066a60e16ff9b656253b1c17f0c0/examples/libcamera/validation/issue211/runs/20261031-runtime-negative/official-cam-debugger-before"
      },
      "source_measurement": {
        "sha256": "6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1",
        "url": "https://github.com/TTolsun/libcamera-sdd/blob/d36affef9b3a741581d1c5f0f4cd68425c5dbe15/publication/issue211/config/product-evidence/official-cam-observation.json",
        "operation": "Exact projection of named original fields, no new runtime execution"
      }
    }
    
    ```
    
    ```json
    {
      "type": "measurement",
      "supplier": "Source-pinned official cam trial; raw events, GDB, syscall and cleanup records",
      "version": "6724319768e46327e26f324d536ccaf22e9b71852e055a7b3c91318f0c11a7f1",
      "date": "2026-10-31",
      "valid_until": "2026-10-31",
      "product": "libcamera-official-cam-trial",
      "release": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "configuration": "wsl2-virtual2-official-cam-udmabuf",
      "feature": "recorded-no-output-sink",
      "conditions": [
        "Source 293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
        "WSL2 custom UDMABUF kernel, root child, Virtual2 400x300 NV12",
        "GDB observation; no timing/return/physical/internal HAL qualification"
      ],
      "sha256": "6ad6510d9624cd8075ccdc0a4622214c441afc5a778a2e577b4c7a76bf10efc0"
    }
    ```

<a id="source-077dc6a73bad3108"></a>

??? note "제품 자료: product-evidence/libcamera-official-cam-trial/invocation-options.txt:1"
    소스와 별도로 제공된 자료입니다. 제공자·버전·적용 범위를 아래 기록에서 확인하세요. 자동 검사는 사람 승인이 아닙니다.
    
    `product-evidence/libcamera-official-cam-trial/invocation-options.txt:1`에서 시작하는 발췌입니다. 종료 줄은 48이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `58f37ca820c4c97c55a55cdab58f88fae76edf6b2a9b0ed365fd0552ed33b4c5`
    
    ```text
    {
      "schema": 1,
      "source_commit": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "historical_archive": "publication/issue211/cli-evidence.zip",
      "archive_sha256": "df8a735a121fa601779647c3b244a6ae0e36018c798659df171c24c760224682",
      "records": [
        {
          "archive_entry": "generator/issue211/runs/20261031-wsl-cam-3/cam-1/record.json",
          "sha256": "4e04b252fd5db261b194972f010fa60d1708368e8ac99ebdb36c385432ff40d6",
          "cam_arguments": [
            "--camera",
            "Virtual2",
            "--capture=3",
            "--stream",
            "role=video,width=400,height=300,pixelformat=NV12"
          ],
          "exit_code": 0
        },
        {
          "archive_entry": "generator/issue211/runs/20261031-wsl-cam-3/cam-2/record.json",
          "sha256": "939672fe872e010b599895b3b17daf4638a40335762f0a211c4ef37cb070ffee",
          "cam_arguments": [
            "--camera",
            "Virtual2",
            "--capture=3",
            "--stream",
            "role=video,width=400,height=300,pixelformat=NV12"
          ],
          "exit_code": 0
        },
        {
          "archive_entry": "generator/issue211/runs/20261031-wsl-cam-3/cam-3/record.json",
          "sha256": "292d5fceea0148bb33a7c47a7cdc2554f2dc18bbd116064211f993ae15ebe0fd",
          "cam_arguments": [
            "--camera",
            "Virtual2",
            "--capture=3",
            "--stream",
            "role=video,width=400,height=300,pixelformat=NV12"
          ],
          "exit_code": 0
        }
      ],
      "output_sink_options_requested": false,
      "scope": "Observed command options; source inspection of CameraSession::start selects output sinks only through display, SDL or file options. Not a new runtime observation of sink_.",
      "new_runtime": false
    }
    
    ```
    
    ```json
    {
      "type": "measurement",
      "supplier": "SHA-verified original official cam argument records; source-scoped projection",
      "version": "58f37ca820c4c97c55a55cdab58f88fae76edf6b2a9b0ed365fd0552ed33b4c5",
      "date": "2026-10-31",
      "valid_until": "2026-10-31",
      "product": "libcamera-official-cam-trial",
      "release": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "configuration": "wsl2-virtual2-official-cam-udmabuf",
      "feature": "recorded-no-output-sink",
      "conditions": [
        "Source 293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
        "WSL2 custom UDMABUF kernel, root child, Virtual2 400x300 NV12",
        "GDB observation; no timing/return/physical/internal HAL qualification"
      ],
      "sha256": "58f37ca820c4c97c55a55cdab58f88fae76edf6b2a9b0ed365fd0552ed33b4c5"
    }
    ```

<a id="source-5a006a90fe9f46ad"></a>

??? note "제품 자료: product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1"
    소스와 별도로 제공된 자료입니다. 제공자·버전·적용 범위를 아래 기록에서 확인하세요. 자동 검사는 사람 승인이 아닙니다.
    
    `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt:1`에서 시작하는 발췌입니다. 종료 줄은 38이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `93f4c8ea45fc873453b7739b88105877f6b1bc60ed7f3f6a280b15d8b131a9a7`
    
    ````text
    # 공식 cam WSL 가상 카메라 검증
    
    ## 결론과 다음 행동
    
    먼저 아래 준비 1번부터 시작합니다. 호스트 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.
    
    ## 관측된 결과
    
    소스 `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`을 수정하지 않은 디버그 빌드의 공식 cam은 시험 커널 `6.18.33.2-microsoft-standard-WSL2-issue211`의 WSL `Virtual2` 카메라(400x300 NV12)에서 프레임 3개를 처리했습니다. 실행 세 개(PID 434, 449, 464)는 모두 request와 sequence 0~2에서 status 1, buffer_status 0을 기록했습니다.
    
    세 기록은 PID, request, sequence로 묶어 status를 비교합니다. 콜백 TID(437, 452, 467)와 처리 TID(434, 449, 464)는 실행마다 달랐으므로 같아야 하는 키가 아니라 속성으로 기록합니다.
    
    DMA 프로브는 `/dev/udmabuf` 열기, 4096바이트 할당, mmap, RW START(flags 3), CPU 접근, RW END(flags 7), munmap과 닫기를 모두 errno 0으로 마쳤습니다. 0.5초 시간 초과 시험은 시간 초과(exit 1)로 끝났고, 정리 반환 코드는 모두 0이었습니다. 반환 코드 0은 정리가 성공했다는 뜻이며, 정리 이벤트가 0개라는 뜻이 아닙니다. 없는 provider는 errno 2, 지원하지 않는 ioctl은 errno 25로 실패했습니다.
    
    `cancelled_callbacks` 0은 세 실행 모두에서 관측된 값입니다. 다만 취소 분기를 동적으로 실행한 결과가 아니며, 0으로 강제한 값도 아닙니다.
    
    ## 범위와 한계
    
    이 결과는 `simulation=true`로 로드된 가상 파이프라인 시뮬레이션 구성의 WSL 가상 카메라 범위에만 해당합니다. 시험 커널에서 성공했다고 해서 복구된 기본 커널(`6.18.33.2-microsoft-standard-WSL2`)이 지원한다는 뜻은 아닙니다. 기본 커널은 allocator를 노출하지 않았습니다. 시험 커널에서는 udmabuf이 내장이었고, 일치하는 모듈은 설치하지 않았습니다.
    
    권한 없는 실행의 errno 13은 이번 시험 커널 실행에만 해당하며, 앞으로 모든 권한 없는 실행을 뜻하지 않습니다. `/dev/udmabuf` 권한은 root 전용 그대로 두었습니다. 복구 후 커널은 기본 커널로 돌아왔고 `.wslconfig`는 존재하지 않습니다.
    
    GDB 중단점은 타이밍에 영향을 주므로 콜백 반환이나 타이밍·성능을 확정하는 증거가 아닙니다. 물리 DMA, 물리 카메라, 제품 앱, 사내 HAL은 검증하지 않았고, 사람 검토는 pending 상태입니다.
    
    ## 실행 전 준비
    
    1. 호스트 상태를 바꾸지 않고 커널을 조사합니다. 커널 태그 `linux-msft-wsl-6.18.33.2`(commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`, 이미지 SHA-256 `cf23bf492a00a5c7517e221b0d8f742ea3cffa9351823191a5ba5c476ba15460`)의 `CONFIG_UDMABUF`, `CONFIG_DMA_SHARED_BUFFER`, `CONFIG_MEMFD_CREATE`(또는 `CONFIG_COMPILE_TEST`), `CONFIG_MMU`, 할당기 후보 `CONFIG_DMABUF_HEAPS`를 확인합니다. `CONFIG_UDMABUF`는 bool이므로 모듈이 아니라 내장 여부만 확인하고, 실제 사용 가능한 모듈과 할당기 후보를 조사한 뒤 사용할 할당기를 하나 선택합니다. `CONFIG_UDMABUF`는 테스트·디버그 용도의 기능이며, 잘못 사용하면 사용자 공간에서 커널 드라이버를 교착시킬 수 있으므로 시험 환경 밖에서 사용하지 않습니다. 기존 WSL에 배포판을 추가하는 것만으로 커널이 격리된다고 보지 않습니다. 커널 빌드 예시는 [prepare_kernel.sh](../validation/issue211/prepare_kernel.sh)이며, 실행 전 태그와 출력 위치를 확인합니다. 이 예시와 [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh)는 기록된 예시이므로 로컬 경로와 설정을 현재 환경에서 다시 확인해야 하며, 실행 전 각 스크립트의 실제 동작과 입력을 직접 읽어 확인합니다. 이 예시들은 커널을 설치하거나 부팅하지 않으며, 설치와 부팅은 2단계 계획과 승인 뒤에만 수행합니다.
    2. 기존 WSL·Docker에 영향을 주지 않는 시험 환경을 먼저 검토합니다. 공유 커널 모듈 변경, 공유 커널 재부팅, `.wslconfig` 변경, 배포판 또는 VM 종료, Docker 중지가 필요하면 영향, 정확한 백업 경로, 부팅할 커널과 이미지 SHA-256, 부팅 절차, 복구 절차를 포함한 호스트 변경 계획을 작성합니다. 복구 기준은 이번 시험 복구 후 확인된 기본 커널 `6.18.33.2-microsoft-standard-WSL2`와 `.wslconfig` 부재 상태입니다. 이 계획은 PR 병합·Pages 배포 승인으로 대신하지 않으며, 실행 직전에 별도 호스트 승인을 받습니다. 승인 전에는 Docker를 중지하거나 WSL을 종료하지 않습니다.
    3. 호스트 승인 후 승인된 계획의 각 단계를 하나씩 수행합니다. 계획이 Docker 중지를 요구하는 환경이면 승인 후 Docker를 중지하고, 그 다음에 공유 커널을 재부팅합니다. Docker 중지가 필요 없으면 이 단계를 생략합니다. 커널 준비는 영향 없는 단계부터 진행하며, 준비 절차는 1단계 예시와 2단계 계획을 따릅니다. 선택한 커널과 할당기가 실제로 요구하는 모듈은 1단계에서 확인해 계획에 포함합니다. 이번 기록된 시험에서 일치하는 모듈을 설치하지 않은 것은 그 시험의 사실이며, 이후 모든 준비를 금지하지 않습니다. `kernel_trial.py`는 자동으로 실행하지 않습니다.
    4. 실행 중인 커널이 `6.18.33.2-microsoft-standard-WSL2-issue211`인지, root가 `/dev/udmabuf`을 열 수 있는지 확인합니다. 하나라도 다르면 캡처하지 않습니다.
    5. WSL root 자식 컨텍스트에서 아래 명령을 실행합니다. `<new-evidence-directory>`는 존재하지 않는 경로여야 하며, 명령이 이 경로를 새로 만듭니다. 미리 빈 디렉터리를 만들지 않습니다. `<private-extracted-tools-prefix>`는 `usr/bin/gdb`와 `usr/share/gdb`를 포함하는 디렉터리입니다. `<compiled-dmabuf-probe>`는 `dmabuf_probe.c`를 `gcc -std=c11 -Wall -Wextra -Werror -O0 -g`로 컴파일한 결과입니다. `<unmodified-source-at-293d751a>`, `<its-debug-meson-build>`, `<private-extracted-tools-prefix>`, `<compiled-dmabuf-probe>`의 실제 경로는 현재 환경에서 확인해 채웁니다. [prepare_runtime.sh](../validation/issue211/prepare_runtime.sh) 예시가 가리키는 산출 위치는 참고만 하며, 실행 전 실제 존재와 293d751a 고정 여부를 확인합니다.
    
    ```
    PYTHONPATH=<generator>/src python3 <generator>/examples/libcamera/runtime/run_cam.py --source <unmodified-source-at-293d751a> --build <its-debug-meson-build> --tools <private-extracted-tools-prefix> --probe <compiled-dmabuf-probe> --out <new-evidence-directory>
    ```
    
    CPU 전용 과거 프로브는 [README.md](README.md)를, 원본 관측 기록은 [observation.json](../validation/issue211/runs/20261031-wsl-cam-3/observation.json)을 참고합니다.
    
    ````
    
    ```json
    {
      "type": "project-document",
      "supplier": "Source-pinned official cam trial; raw events, GDB, syscall and cleanup records",
      "version": "580df5156da7066a60e16ff9b656253b1c17f0c0",
      "date": "2026-10-31",
      "valid_until": "2026-10-31",
      "product": "libcamera-official-cam-trial",
      "release": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
      "configuration": "wsl2-virtual2-official-cam-udmabuf",
      "feature": "recorded-no-output-sink",
      "conditions": [
        "Source 293d751a814e0d4c34e85ad457ccd9d5eefd1a61",
        "WSL2 custom UDMABUF kernel, root child, Virtual2 400x300 NV12",
        "GDB observation; no timing/return/physical/internal HAL qualification"
      ],
      "sha256": "93f4c8ea45fc873453b7739b88105877f6b1bc60ed7f3f6a280b15d8b131a9a7"
    }
    ```

<a id="source-24d83931ed92dc57"></a>

??? note "소스 근거: src/apps/cam/camera_session.cpp:467"
    `src/apps/cam/camera_session.cpp:467`에서 시작하는 발췌입니다. 종료 줄은 561이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1cc65de3cbc313bb70f938f939d3d99420f17526290c216b538bbf117adbfd6d`
    
    ```text
    void CameraSession::requestComplete(Request *request)
    {
    	if (request->status() == Request::RequestCancelled)
    		return;
    
    	/*
    	 * Defer processing of the completed request to the event loop, to avoid
    	 * blocking the camera manager thread.
    	 */
    	EventLoop::instance()->callLater([this, request]() { processRequest(request); });
    }
    
    void CameraSession::processRequest(Request *request)
    {
    	/*
    	 * If we've reached the capture limit, we're done. This doesn't
    	 * duplicate the check below that emits the captureDone signal, as this
    	 * function will be called for each request still in flight after the
    	 * capture limit is reached and we don't want to emit the signal every
    	 * single time.
    	 */
    	if (captureLimit_ && captureCount_ >= captureLimit_)
    		return;
    
    	const Request::BufferMap &buffers = request->buffers();
    
    	/*
    	 * Compute the frame rate. The timestamp is arbitrarily retrieved from
    	 * the first buffer, as all buffers should have matching timestamps.
    	 */
    	uint64_t ts = buffers.begin()->second->metadata().timestamp;
    	double fps = ts - last_;
    	fps = last_ != 0 && fps ? 1000000000.0 / fps : 0.0;
    	last_ = ts;
    
    	bool requeue = true;
    
    	std::stringstream info;
    	info << ts / 1000000000 << "."
    	     << std::setw(6) << std::setfill('0') << ts / 1000 % 1000000
    	     << " (" << std::fixed << std::setprecision(2) << fps << " fps)";
    
    	for (const auto &[stream, buffer] : buffers) {
    		const FrameMetadata &metadata = buffer->metadata();
    
    		info << " " << streamNames_[stream]
    		     << " seq: " << std::setw(6) << std::setfill('0') << metadata.sequence
    		     << " bytesused: ";
    
    		unsigned int nplane = 0;
    		for (const FrameMetadata::Plane &plane : metadata.planes()) {
    			info << plane.bytesused;
    			if (++nplane < metadata.planes().size())
    				info << "/";
    		}
    	}
    
    	if (sink_) {
    		if (!sink_->processRequest(request))
    			requeue = false;
    	}
    
    	std::cout << info.str() << std::endl;
    
    	if (printMetadata_) {
    		const ControlList &requestMetadata = request->metadata();
    		for (const auto &[key, value] : requestMetadata) {
    			const ControlId *id = controls::controls.at(key);
    			std::cout << "\t" << id->name() << " = "
    				  << value.toString() << std::endl;
    		}
    	}
    
    	/*
    	 * Notify the user that capture is complete if the limit has just been
    	 * reached.
    	 */
    	captureCount_++;
    	if (captureLimit_ && captureCount_ >= captureLimit_) {
    		captureDone.emit();
    		return;
    	}
    
    	/*
    	 * If the frame sink holds on the request, we'll requeue it later in the
    	 * complete handler.
    	 */
    	if (!requeue)
    		return;
    
    	request->reuse(Request::ReuseBuffers);
    	queueRequest(request);
    }
    
    void CameraSession::sinkRelease(Request *request)
    ```

<a id="source-a93e2b65e7577aaf"></a>

??? note "소스 근거: src/apps/cam/camera_session.cpp:453"
    `src/apps/cam/camera_session.cpp:453`에서 시작하는 발췌입니다. 종료 줄은 467이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1e0c758f1f31a09a5f212f7cfc6f11637a365912ec73efa9e59f0bf32a97a220`
    
    ```text
    int CameraSession::queueRequest(Request *request)
    {
    	if (captureLimit_ && queueCount_ >= captureLimit_)
    		return 0;
    
    	if (script_)
    		request->controls().merge(script_->frameControls(queueCount_),
    					  ControlList::MergePolicy::OverwriteExisting);
    
    	queueCount_++;
    
    	return camera_->queueRequest(request);
    }
    
    void CameraSession::requestComplete(Request *request)
    ```

<a id="source-fed2a2e4116ab528"></a>

??? note "소스 근거: src/apps/cam/camera_session.cpp:283"
    `src/apps/cam/camera_session.cpp:283`에서 시작하는 발췌입니다. 종료 줄은 346이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6f04ac47e3fa6496c3bc271f987bee51f2793e64b360223d3455b6c080c684f0`
    
    ```text
    int CameraSession::start()
    {
    	int ret;
    
    	queueCount_ = 0;
    	captureCount_ = 0;
    	captureLimit_ = options_[OptCapture].toInteger();
    	printMetadata_ = options_.isSet(OptMetadata);
    
    	ret = camera_->configure(config_.get());
    	if (ret < 0) {
    		std::cout << "Failed to configure camera" << std::endl;
    		return ret;
    	}
    
    	streamNames_.clear();
    	for (unsigned int index = 0; index < config_->size(); ++index) {
    		StreamConfiguration &cfg = config_->at(index);
    		streamNames_[cfg.stream()] = "cam" + std::to_string(cameraIndex_)
    					   + "-stream" + std::to_string(index);
    	}
    
    	camera_->requestCompleted.connect(this, &CameraSession::requestComplete);
    
    #ifdef HAVE_KMS
    	if (options_.isSet(OptDisplay))
    		sink_ = std::make_unique<KMSSink>(options_[OptDisplay].toString());
    #endif
    
    #ifdef HAVE_SDL
    	if (options_.isSet(OptSDL))
    		sink_ = std::make_unique<SDLSink>();
    #endif
    
    	if (options_.isSet(OptFile)) {
    		std::unique_ptr<FileSink> sink =
    			std::make_unique<FileSink>(camera_.get(), streamNames_);
    
    		if (!options_[OptFile].toString().empty()) {
    			ret = sink->setFilePattern(options_[OptFile]);
    			if (ret)
    				return ret;
    		}
    
    		sink_ = std::move(sink);
    	}
    
    	if (sink_) {
    		ret = sink_->configure(*config_);
    		if (ret < 0) {
    			std::cout << "Failed to configure frame sink"
    				  << std::endl;
    			return ret;
    		}
    
    		sink_->requestProcessed.connect(this, &CameraSession::sinkRelease);
    	}
    
    	allocator_ = std::make_unique<FrameBufferAllocator>(camera_);
    
    	return startCapture();
    }
    
    void CameraSession::stop()
    ```

<a id="source-3122754fc16929a5"></a>

??? note "소스 근거: src/apps/cam/camera_session.h:61"
    `src/apps/cam/camera_session.h:61`에서 시작하는 발췌입니다. 종료 줄은 68이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d1dd7739a5bca1909d81a1d336de9ee15a51005f05f733f1c958d72f96117bec`
    
    ```text
    std::shared_ptr<libcamera::Camera> camera_;
    	std::unique_ptr<libcamera::CameraConfiguration> config_;
    
    	std::unique_ptr<CaptureScript> script_;
    
    	std::map<const libcamera::Stream *, std::string> streamNames_;
    	std::unique_ptr<FrameSink> sink_;
    	unsigned int cameraIndex_;
    ```

<a id="source-eb19d6a7f4a0f3f0"></a>

??? note "소스 근거: src/apps/cam/camera_session.cpp:557"
    `src/apps/cam/camera_session.cpp:557`에서 시작하는 발췌입니다. 종료 줄은 558이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5a8a9a7c7f09b886f5286eea0793521d017e38b53e50f94cd976404e01658f08`
    
    ```text
    request->reuse(Request::ReuseBuffers);
    	queueRequest(request);
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `product-evidence/libcamera-official-cam-trial/execution-contract.txt`, `product-evidence/libcamera-official-cam-trial/invocation-execution-contract.txt`, `product-evidence/libcamera-official-cam-trial/invocation-official-cam-reader.txt`, `product-evidence/libcamera-official-cam-trial/invocation-options.txt`, `product-evidence/libcamera-official-cam-trial/invocation-reproduction-procedure.txt`, `product-evidence/libcamera-official-cam-trial/official-cam-reader.txt`, `product-evidence/libcamera-official-cam-trial/reproduction-procedure.txt`, `src/apps/cam/camera_session.cpp`, `src/apps/cam/camera_session.h`, `src/libcamera/camera.cpp`, `src/libcamera/framebuffer_allocator.cpp`, `src/libcamera/pipeline/virtual/README.md`, `src/libcamera/pipeline/virtual/data/virtual.yaml`, `src/libcamera/pipeline/virtual/test_pattern_generator.cpp`, `src/libcamera/pipeline/virtual/virtual.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `adfa719f8e`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-21 · 사람 검토 전

다음 단계: [공식 cam 재현 절차](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/OFFICIAL_CAM.md)
