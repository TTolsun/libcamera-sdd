# ForVendor

Applications use the common Camera API to configure devices and capture images. A device-specific PipelineHandler implementation matches the required media devices with devices in the system and configures the hardware pipeline according to the stream configuration. To evaluate adoption, check the hardware and build conditions, then test first capture and stopping on the target board.

- Check platform and build support
- Plan first capture and stop tests

## Items to check on the device

On the target device, test normal capture and stopping with incomplete requests separately. For each submission, record the number of completion callbacks, the request status, and the status of each buffer. Determine separately whether the request was canceled and whether capture succeeded for each frame. Check Contract and evidence for completion notification after stopping.

Compare Benefits of adopting a common API and Hardware and build conditions, then check the device-specific implementation responsibilities in Integration guide. Support scope and validation covers the first capture on a customer board, configuration constraints, and performance evidence.

## Boundary between hardware and the common layer

When all media devices needed for a single pipeline are found, the implementer of `PipelineHandler::match()` must call `MediaDevice::acquire()` to acquire each device, then create one or more corresponding `Camera` instances, store them internally, register them with the camera manager, and return `true`. When not all required media devices are found, the implementer of `PipelineHandler::match()` must not acquire any devices if none have yet been acquired; if some have already been acquired, the implementer must call `MediaDevice::release()` to release all acquired devices and return `false`. `PipelineHandler::match()` is called on the `CameraManager` thread and, if it returns `true`, a new `PipelineHandler` instance is created and that instance's `match()` is called.

### Acquisition and registration for device matching and cleanup on failure

```mermaid
flowchart TB

  v_call["CameraManager calls match <br/>with the enumerator."]
  v_found{"Were all media devices <br/>required for this pipeline <br/>found?"}
  v_acquire["Acquire all devices <br/>required for this pipeline."]
  v_register["Create and store the <br/>cameras, register them with <br/>CameraManager, then return <br/>true."]
  v_repeat["Create a new handler <br/>instance and call match <br/>again."]
  v_failure["Acquire no devices, or <br/>release all devices already <br/>acquired, then return false."]
  v_call -->|"The match implementation <br/>checks the devices."| v_found
  v_found -->|"All required devices were <br/>found."| v_acquire
  v_found -->|"A required device is <br/>missing."| v_failure
  v_acquire -->|"Register the cameras after <br/>acquisition."| v_register
  v_register -->|"The call returned true."| v_repeat
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

Who matches devices and registers cameras, and how are the acquired devices handled depending on the match result?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

| Elements and transitions | Source evidence |
| --- | --- |
| CameraManager calls match with the enumerator. | src/libcamera/pipeline_handler.cpp:91 |
| Were all media devices required for this pipeline found? | src/libcamera/pipeline_handler.cpp:91 |
| Acquire all devices required for this pipeline. | src/libcamera/pipeline_handler.cpp:91 |
| Create and store the cameras, register them with CameraManager, then return true. | src/libcamera/pipeline_handler.cpp:91 |
| Create a new handler instance and call match again. | src/libcamera/pipeline_handler.cpp:109 |
| Acquire no devices, or release all devices already acquired, then return false. | src/libcamera/pipeline_handler.cpp:97 |
| The match implementation checks the devices. | src/libcamera/pipeline_handler.cpp:91 |
| All required devices were found. | src/libcamera/pipeline_handler.cpp:91 |
| A required device is missing. | src/libcamera/pipeline_handler.cpp:91 · src/libcamera/pipeline_handler.cpp:97 |
| Register the cameras after acquisition. | src/libcamera/pipeline_handler.cpp:91 |
| The call returned true. | src/libcamera/pipeline_handler.cpp:91 · src/libcamera/pipeline_handler.cpp:109 |

</details>

<details open>
<summary>Section-wide evidence: 3</summary>

- `src/libcamera/pipeline_handler.cpp``L91` excerpt · [Full source `L91`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L91) · `L97` excerpt · [Full source `L97`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L97) · `L109` excerpt · [Full source `L109`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L109)

</details>

## Source manuscripts and review records

<details open>
<summary>libcamera design document</summary>

- **Contracts between documents**: Automated comparison report · Before human review

Open earlier detail

</details>

<details open>
<summary>Integration guide</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-11-20 16:39:26+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence files: `include/libcamera/camera.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/camera.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline_handler.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `adfa719f8e`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status recorded on: 2026-11-21 · Awaiting human review

</details>

Markdown source ↗ Mermaid source ↗

Open earlier detail

</details>

Download page Markdown · Reader edition source map
