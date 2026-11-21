# ForDeveloper

List cameras in an environment where cam is available. If a camera is detected, save frames from the first one. Then open the code entry points for discovery, configuration, and startup.

- Code that checks cancellation status
- Caveats and Troubleshooting

## Try running it directly

Use `cam -l` to list the cameras detected on the system, and use `cam -c 1 --capture=10 --file` to capture 10 frames from the first camera and save them to disk. If problems occur, you can obtain detailed libcamera debug logs with `LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l`.

<details open>
<summary>Section-wide evidence: 1</summary>

- `README.rst``L107` excerpt · [Full source `L107`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/README.rst#L107)

</details>

## When to start discovery and use the camera

When you call `CameraManager::start()`, the camera manager starts up and enumerates every device on the system. Once you’ve confirmed the manager is running, you can list the available cameras. You can use each camera until it’s disconnected or the manager stops.

<details open>
<summary>Section-wide evidence: 1</summary>

- `src/libcamera/camera_manager.cpp``L329` excerpt · [Full source `L329`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera_manager.cpp#L329)

</details>

## Where to check configuration application and success status

`Camera::configure()` returns the negative error value if the access state check produces one; if the check passes, it clears each `StreamConfiguration`'s previous stream association to `nullptr`, checks `validate()`, and returns `-EINVAL` if the result is not `Valid`. For a valid configuration, `Camera::configure()` calls `PipelineHandler::configure` with `ConnectionTypeBlocking` and returns its return value unchanged if that value is nonzero. The API contract states that when the function returns, each `StreamConfiguration` in `config` is associated with a `Stream` instance, which can be retrieved with `stream()`.

### Checks before configuration is applied and pipeline results

```mermaid
flowchart TB

  v_access{"Call <br/>isAccessAllowed#40;Private::<br/>CameraAcquired, <br/>Private::CameraConfigured#41;. <br/>Is the access result <br/>negative?"}
  v_access_return["Return the access result <br/>ret."]
  v_reset["Call cfg.setStream#40;nullptr#41; <br/>for each cfg in the <br/>existing #42;config to reset <br/>its connection."]
  v_validation{"Did config-#62;validate#40;#41; <br/>return a status other than <br/>CameraConfiguration::Valid?"}
  v_validation_return["Return -EINVAL because <br/>validate#40;#41; returned a <br/>status other than <br/>CameraConfiguration::Valid."]
  v_log["Prepare and output the <br/>stream configuration log."]
  v_pipeline["Call <br/>PipelineHandler::configure <br/>through invokeMethod with <br/>ConnectionTypeBlocking."]
  v_pipeline_check{"Is the pipeline call#39;s <br/>return value ret true?"}
  v_pipeline_return["Return the pipeline call#39;s <br/>return value ret."]
  v_next["Continue to <br/>activeStreams#95;.clear#40;#41; and <br/>the separate stream <br/>connection check. This is <br/>not the function#39;s <br/>successful return."]
  v_access -->|"If the access result is <br/>negative, return ret. #91;true#93;"| v_access_return
  v_access -->|"If the access result is not <br/>negative, reset the <br/>connections. #91;false#93;"| v_reset
  v_reset -->|"Validate after resetting <br/>each connection."| v_validation
  v_validation -->|"If the returned status is <br/>not <br/>CameraConfiguration::Valid, <br/>return -EINVAL. #91;true#93;"| v_validation_return
  v_validation -->|"If the returned status is <br/>CameraConfiguration::Valid, <br/>prepare the log. #91;false#93;"| v_log
  v_log -->|"Call the pipeline after <br/>outputting the log."| v_pipeline
  v_pipeline -->|"Check the call result."| v_pipeline_check
  v_pipeline_check -->|"If ret is true, return ret. <br/>#91;true#93;"| v_pipeline_return
  v_pipeline_check -->|"If ret is false, continue <br/>to the next check. #91;false#93;"| v_next
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

In what order does Camera::configure perform the access check, stream connection initialization, validation, and pipeline return-value check?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

LLM diagram draft · before human review

Authoring model: `cli/codex/gpt-6.1-terra`

| Elements and transitions | Source evidence |
| --- | --- |
| Call isAccessAllowed(Private::CameraAcquired, Private::CameraConfigured). Is the access result negative? | src/libcamera/camera.cpp:1191 |
| Return the access result ret. | src/libcamera/camera.cpp:1191 |
| Call cfg.setStream(nullptr) for each cfg in the existing \*config to reset its connection. | src/libcamera/camera.cpp:1191 |
| Did config-\>validate() return a status other than CameraConfiguration::Valid? | src/libcamera/camera.cpp:1191 |
| Return -EINVAL because validate() returned a status other than CameraConfiguration::Valid. | src/libcamera/camera.cpp:1191 |
| Prepare and output the stream configuration log. | src/libcamera/camera.cpp:1191 |
| Call PipelineHandler::configure through invokeMethod with ConnectionTypeBlocking. | src/libcamera/camera.cpp:1191 |
| Is the pipeline call's return value ret true? | src/libcamera/camera.cpp:1191 |
| Return the pipeline call's return value ret. | src/libcamera/camera.cpp:1191 |
| Continue to activeStreams\_.clear() and the separate stream connection check. This is not the function's successful return. | src/libcamera/camera.cpp:1191 |
| If the access result is negative, return ret. · ret \< 0 \[true\] | src/libcamera/camera.cpp:1191 |
| If the access result is not negative, reset the connections. · ret \< 0 \[false\] | src/libcamera/camera.cpp:1191 |
| Validate after resetting each connection. | src/libcamera/camera.cpp:1191 |
| If the returned status is not CameraConfiguration::Valid, return -EINVAL. · config-\>validate() != CameraConfiguration::Valid \[true\] | src/libcamera/camera.cpp:1191 |
| If the returned status is CameraConfiguration::Valid, prepare the log. · config-\>validate() != CameraConfiguration::Valid \[false\] | src/libcamera/camera.cpp:1191 |
| Call the pipeline after outputting the log. | src/libcamera/camera.cpp:1191 |
| Check the call result. | src/libcamera/camera.cpp:1191 |
| If ret is true, return ret. · ret \[true\] | src/libcamera/camera.cpp:1191 |
| If ret is false, continue to the next check. · ret \[false\] | src/libcamera/camera.cpp:1191 |

</details>

### One-time initialization of the stream list and success status

```mermaid
flowchart TB

  v_handler_return["PipelineHandler::configure <br/>has returned normally with <br/>0."]
  v_clear["Camera clears <br/>activeStreams#95;."]
  v_loop["Camera iterates over each <br/>StreamConfiguration as cfg."]
  v_check{"Camera obtains cfg.stream#40;#41; <br/>and checks whether stream <br/>is absent."}
  v_fatal["When Camera prints the <br/>Fatal message, the program <br/>terminates immediately."]
  v_update["Camera updates the Stream <br/>configuration#95; from cfg and <br/>inserts stream into <br/>activeStreams#95;."]
  v_configured["After the loop, Camera sets <br/>the state to <br/>Private::CameraConfigured."]
  v_camera_return["Camera::configure returns 0."]
  v_handler_return -->|"Execution continues after <br/>PipelineHandler::configure <br/>returns 0."| v_clear
  v_clear -->|"Camera iterates over the <br/>configurations after <br/>clearing activeStreams#95;."| v_loop
  v_loop -->|"Camera checks stream when <br/>there is another cfg."| v_check
  v_check -->|"If the condition is true, <br/>Camera prints a Fatal <br/>message. · #33;stream #91;true#93;"| v_fatal
  v_check -->|"If the condition is false, <br/>Camera updates the Stream. <br/>· #33;stream #91;false#93;"| v_update
  v_update -->|"Camera continues the loop <br/>after the update."| v_loop
  v_loop -->|"Camera sets the state when <br/>the loop ends."| v_configured
  v_configured -->|"Camera::configure returns <br/>after setting the state."| v_camera_return
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

After successful pipeline configuration, how do activeStreams\_ initialization, updates to each StreamConfiguration, and the success state follow?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

LLM diagram draft · before human review

Authoring model: `cli/codex/gpt-6.1-terra`

| Elements and transitions | Source evidence |
| --- | --- |
| PipelineHandler::configure has returned normally with 0. | src/libcamera/camera.cpp:1191 |
| Camera clears activeStreams\_. | src/libcamera/camera.cpp:1191 |
| Camera iterates over each StreamConfiguration as cfg. | src/libcamera/camera.cpp:1191 |
| Camera obtains cfg.stream() and checks whether stream is absent. | src/libcamera/camera.cpp:1191 |
| When Camera prints the Fatal message, the program terminates immediately. | src/libcamera/camera.cpp:1191 · src/libcamera/base/log.cpp:1022 |
| Camera updates the Stream configuration\_ from cfg and inserts stream into activeStreams\_. | src/libcamera/camera.cpp:1191 |
| After the loop, Camera sets the state to Private::CameraConfigured. | src/libcamera/camera.cpp:1191 |
| Camera::configure returns 0. | src/libcamera/camera.cpp:1191 |
| Execution continues after PipelineHandler::configure returns 0. | src/libcamera/camera.cpp:1191 |
| Camera iterates over the configurations after clearing activeStreams\_. | src/libcamera/camera.cpp:1191 |
| Camera checks stream when there is another cfg. | src/libcamera/camera.cpp:1191 |
| If the condition is true, Camera prints a Fatal message. · !stream \[true\] | src/libcamera/camera.cpp:1191 |
| If the condition is false, Camera updates the Stream. · !stream \[false\] | src/libcamera/camera.cpp:1191 |
| Camera continues the loop after the update. | src/libcamera/camera.cpp:1191 |
| Camera sets the state when the loop ends. | src/libcamera/camera.cpp:1191 |
| Camera::configure returns after setting the state. | src/libcamera/camera.cpp:1191 |

</details>

When the pipeline call succeeds, `Camera::configure()` clears `activeStreams_` and checks `cfg.stream()` for each configuration. If a stream is missing, execution enters the `Fatal` log path, and under the `LOG` contract, execution is aborted and the program terminates immediately after the message is printed. If every configuration has a stream, `Camera::configure()` updates each stream's `configuration_` to the corresponding configuration and adds the stream to `activeStreams_`. Camera::configure() then sets the state to `CameraConfigured` and returns `0`.

<details open>
<summary>Section-wide evidence: 3</summary>

- `src/libcamera/camera.cpp`[`L1191`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1191) · `L1183` excerpt · [Full source `L1183`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1183) · `L1191`
- `src/libcamera/base/log.cpp``L1022` excerpt · [Full source `L1022`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/base/log.cpp#L1022)

</details>

## Reflecting start control values and pipeline results

If `controls` is present, `Camera::start` makes a copy of `ControlList`, preprocesses it with `patchControlList`, and passes the copy; otherwise, it passes `nullptr`. In both branches, it calls `PipelineHandler::start` with `ConnectionTypeBlocking`, and that function is called from the `CameraManager` thread. If the call result `ret` is nonzero, `Camera::start` returns `ret` unchanged without setting the `CameraRunning` state; if `ret` is zero, it sets the `CameraRunning` state and returns 0.

### The relationship and boundaries between startup control values and the application of pipeline results

```mermaid
flowchart TB

  v_access{"It checks whether the <br/>CameraConfigured access <br/>result is negative."}
  v_returned["It returns a negative <br/>access result or a nonzero <br/>pipeline result unchanged."]
  v_assertion["When enabled, ASSERT checks <br/>whether requestSequence#95; is <br/>zero."]
  v_fatal["If the ASSERT condition is <br/>false, it logs a Fatal <br/>error and aborts execution."]
  v_ndebug["If NDEBUG is defined before <br/>including log.h, ASSERT <br/>generates no code."]
  v_controls{"It chooses what to pass <br/>based on whether controls <br/>is present."}
  v_copy["It copies controls and <br/>applies patchControlList to <br/>copy."]
  v_null["It passes nullptr when <br/>controls is absent."]
  v_invoke["PipelineHandler::start runs <br/>on the CameraManager thread <br/>via ConnectionTypeBlocking."]
  v_result{"It checks whether the <br/>pipeline call result ret is <br/>zero."}
  v_running["If the result is zero, it <br/>sets the state to <br/>Private::CameraRunning."]
  v_access -->|"It returns the negative <br/>result unchanged. #91;true#93;"| v_returned
  v_access -->|"If the result is not <br/>negative, execution reaches <br/>ASSERT. #91;false#93;"| v_assertion
  v_assertion -->|"If the enabled assertion is <br/>false, execution aborts."| v_fatal
  v_assertion -->|"ASSERT code generation <br/>depends on the NDEBUG <br/>definition."| v_ndebug
  v_assertion -->|"If execution continues, it <br/>checks controls."| v_controls
  v_controls -->|"If controls is present, it <br/>copies and patches it. <br/>#91;true#93;"| v_copy
  v_controls -->|"If controls is absent, it <br/>uses nullptr. #91;false#93;"| v_null
  v_copy -->|"It passes the address of <br/>the patched copy. #91;true#93;"| v_invoke
  v_null -->|"It passes nullptr. #91;false#93;"| v_invoke
  v_invoke -->|"It stores the call result <br/>in ret and checks it."| v_result
  v_result -->|"If the result is nonzero, <br/>it returns it unchanged. <br/>#91;true#93;"| v_returned
  v_result -->|"If the result is zero, it <br/>updates the state. #91;false#93;"| v_running
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

How do ASSERT, control-value branches, blocking pipeline calls, and return-value branches lead to returning the original error or updating CameraRunning?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

LLM diagram draft · before human review

Authoring model: `cli/codex/gpt-6.1-terra`

| Elements and transitions | Source evidence |
| --- | --- |
| It checks whether the CameraConfigured access result is negative. | src/libcamera/camera.cpp:1400 |
| It returns a negative access result or a nonzero pipeline result unchanged. | src/libcamera/camera.cpp:1400 |
| When enabled, ASSERT checks whether requestSequence\_ is zero. | src/libcamera/camera.cpp:1400 · src/libcamera/base/log.cpp:1022 |
| If the ASSERT condition is false, it logs a Fatal error and aborts execution. | src/libcamera/base/log.cpp:1022 |
| If NDEBUG is defined before including log.h, ASSERT generates no code. | src/libcamera/base/log.cpp:1022 |
| It chooses what to pass based on whether controls is present. | src/libcamera/camera.cpp:1400 |
| It copies controls and applies patchControlList to copy. | src/libcamera/camera.cpp:1400 |
| It passes nullptr when controls is absent. | src/libcamera/camera.cpp:1400 |
| PipelineHandler::start runs on the CameraManager thread via ConnectionTypeBlocking. | src/libcamera/camera.cpp:1400 · src/libcamera/pipeline_handler.cpp:343 |
| It checks whether the pipeline call result ret is zero. | src/libcamera/camera.cpp:1400 |
| If the result is zero, it sets the state to Private::CameraRunning. | src/libcamera/camera.cpp:1400 |
| It returns the negative result unchanged. · ret \< 0 \[true\] | src/libcamera/camera.cpp:1400 |
| If the result is not negative, execution reaches ASSERT. · ret \< 0 \[false\] | src/libcamera/camera.cpp:1400 |
| If the enabled assertion is false, execution aborts. | src/libcamera/base/log.cpp:1022 |
| ASSERT code generation depends on the NDEBUG definition. | src/libcamera/base/log.cpp:1022 |
| If execution continues, it checks controls. | src/libcamera/camera.cpp:1400 · src/libcamera/base/log.cpp:1022 |
| If controls is present, it copies and patches it. · controls \[true\] | src/libcamera/camera.cpp:1400 |
| If controls is absent, it uses nullptr. · controls \[false\] | src/libcamera/camera.cpp:1400 |
| It passes the address of the patched copy. · controls \[true\] | src/libcamera/camera.cpp:1400 |
| It passes nullptr. · controls \[false\] | src/libcamera/camera.cpp:1400 |
| It stores the call result in ret and checks it. | src/libcamera/camera.cpp:1400 |
| If the result is nonzero, it returns it unchanged. · ret \[true\] | src/libcamera/camera.cpp:1400 |
| If the result is zero, it updates the state. · ret \[false\] | src/libcamera/camera.cpp:1400 |

</details>

`Camera::start` executes `ASSERT(d->requestSequence_ == 0)` before calling `PipelineHandler::start`. If this check fails, `ASSERT` logs an error message at the `Fatal` log level and aborts program execution, behaving differently from a normal error return. If `NDEBUG` is defined before `log.h` is included, `ASSERT` generates no code.

<details open>
<summary>Section-wide evidence: 3</summary>

- `src/libcamera/camera.cpp``L1400` excerpt · [Full source `L1400`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1400)
- `src/libcamera/pipeline_handler.cpp``L343` excerpt · [Full source `L343`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L343)
- `src/libcamera/base/log.cpp``L1022` excerpt · [Full source `L1022`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/base/log.cpp#L1022)

</details>

## Code to check the cancellation state

Open the callback connected to `Camera::requestCompleted` in the app and find the branch that reads `Request::status()` and handles `RequestCancelled`. Before using the image, check that each `FrameBuffer::metadata().status` is `FrameSuccess`. Follow Status determination and code for completion notification after stopping.

In System overview, you can find CameraManager's discovery entry point and the role of each component. Before modifying callback or request-processing code, check Request submission and completion, Session state and resources, and Thread boundaries.

## Source manuscripts and review records

<details open>
<summary>Run it and read the design rationale</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-11-04 05:02:45+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence files: `README.rst`, `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `293d751a81`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status record date: 2026-11-04 · Before human review

</details>

Markdown source ↗

Open earlier detail

</details>

<details open>
<summary>Camera discovery</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-11-04 07:00:44+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence files: `src/libcamera/base/event_dispatcher_poll.cpp`, `src/libcamera/base/log.cpp`, `src/libcamera/base/thread.cpp`, `src/libcamera/camera_manager.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `293d751a81`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status record date: 2026-11-04 · Before human review

</details>

Markdown source ↗

Open earlier detail

</details>

<details open>
<summary>Stream configuration</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-11-20 16:39:43+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence files: `include/libcamera/geometry.h`, `include/libcamera/internal/camera.h`, `include/libcamera/pixel_format.h`, `src/libcamera/base/log.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/formats.cpp`, `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp`, `src/libcamera/pixel_format.cpp`, `src/libcamera/sensor/camera_sensor_legacy.cpp`, `src/libcamera/sensor/camera_sensor_raw.cpp`, `src/libcamera/stream.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `adfa719f8e`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status recorded on: 2026-11-21 · Awaiting human review

</details>

Markdown source ↗

Open earlier detail

</details>

<details open>
<summary>Capture start</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-11-04 05:03:21+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence files: `src/libcamera/base/log.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/controls.cpp`, `src/libcamera/pipeline_handler.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `293d751a81`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status record date: 2026-11-04 · Before human review

</details>

Markdown source ↗

Open earlier detail

</details>

<details open>
<summary>libcamera design document</summary>

- **Contracts between documents**: Automated comparison report · Before human review

Open earlier detail

</details>

Download page Markdown · Reader edition source map
