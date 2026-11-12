# First-run and upstream control verification

This trial used public libcamera source at `da6a6ed33ed0ab305f10b6f8b44736150d39cef4`. The official source and the repository's `upstream/master` pointed to the same commit. The scoped site explains the change of `ColourTemperature` to `inout` and shows how the Raspberry Pi IPA handles the request. It has its own source-bound manifest. The integrated site retains its separate build and source basis.

- [Korean page](https://ttolsun.github.io/libcamera-sdd/upstream/colour-temperature/colour-temperature.html)
- [English page](https://ttolsun.github.io/libcamera-sdd/upstream/colour-temperature/en/colour-temperature.html)
- [Source change](https://gitlab.freedesktop.org/camera/libcamera/-/commit/b6922ed2d2f1e7fbbeb25437571fa215c663ef5a)
- [Generator issue](https://github.com/TTolsun/camera-hal-sdd-generator/issues/304) · [Generator PR](https://github.com/TTolsun/camera-hal-sdd-generator/pull/307)

## First-run trial

The Q1 sample answered what the application must do with a fence left on a buffer after a request times out. The configured diagram followed the same contract. The Meson/Ninja build produced the compile DB and generated headers. The sample analyzed the `request.cpp` translation unit and read the pinned Git source excerpt. The prepared doctor check took 0.949 s, extraction 24.353 s, and the first plan 6.938 s. These are automatic wall times in this environment. A missing DB was also exercised with the public mini-HAL example. Preparation invoked the document generation model zero times.

| Stage | New CLI calls | Native input / output tokens | Outcome |
| --- | ---: | ---: | --- |
| Draft | 1 | 15,166 / 114 | Source-cited answer and configured figure generated |
| First independent review attempt | 0 | Unmeasured | A default navigation target did not exist in the single-page configuration |
| Draft after navigation correction | 0 | Unmeasured | Validated one completed design checkpoint |
| Independent contract review | 1 | 14,171 / 183 | One batch passed with zero unresolved findings |
| Independent review rerun with unchanged inputs | 0 | Unmeasured | Reused the reviewed batch and its original receipt |
| Local preview | 0 | Unmeasured | Two HTML files, zero broken links, verified manifest and bundled Mermaid |

Generation and review used separate Codex CLI configurations with `gpt-6.1-terra` and `model_reasoning_effort="high"`. The WSL Python process ran the logged-in Windows CLI executable. The figures were configured from source citations. Native token totals include cached input and reasoning inside their corresponding totals. No monetary charge, human setup time, device behavior or internal HAL was measured.

## Upstream supplement

The public page separates the core control contract from Raspberry Pi IPA request handling and the `awb.status` metadata branch. The graph covers the monochrome-sensor, missing-algorithm and manual-AWB paths. Source windows are pinned in [sections.yaml](sections.yaml) and [visuals.yaml](visuals.yaml). The scope excludes IMX832 tuning validation, other IPA implementations and actual camera behavior.

For this scoped extraction, GCC's `-Werror` promoted a Clang C99-designator warning in `controls.cpp`. The analysis copy of its compile command adds `-Wno-error=c99-designator`. During translation, an edit to the generator triggered input-change protection. A later run stopped at the configured six-call limit. The next run used the same inputs and limit, reused completed translation batches and continued with the remaining strings. [Execution summary](execution.json)

The bilingual contract review is automatic and human approval remains pending. The published manifest and internal-link checks apply to the scoped site.

The final local build verified six HTML pages with zero broken links. Both language editions rendered the figure in Chrome. A separate CLI review supported the graph labels and every checked branch. The manifest includes 92 files.
