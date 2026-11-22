# Caveats and Troubleshooting

Start at the last successful call or notification. Isolate where the result diverged during configuration, submission, completion, resource access, or module loading.

## Order for narrowing down configuration failures

When investigating, inside `Camera::configure`, observe the return value `ret` of the existing `isAccessAllowed` call that passes `Private::CameraAcquired` and `Private::CameraConfigured` as arguments. If `ret < 0`, record the failure branch where `Camera::configure` returns the same `ret`. When investigating the existing `Camera::Private::isAccessAllowed` call, first distinguish the earlier branch that returns `-ENODEV` when `allowDisconnected` is false and `disconnected_` is true. Otherwise, review the range comparison of `currentState` with `low` and `high`, and the return of `0` within the range; outside the range, check in order the code locations of `ASSERT`, the error log, and the return of `-EACCES`.

### Branch that narrows down configuration failures

```mermaid
flowchart TB

  v_access{"State and access allowed?"}
  v_accesserror["Return access error"]
  v_valid{"Does validate#40;#41; return <br/>Valid?"}
  v_invalid["Return -EINVAL"]
  v_device["PipelineHandler::configure#40;#41;"]
  v_ret{"Is ret nonzero?"}
  v_device-error["Return nonzero ret unchanged"]
  v_streams["Next: check stream <br/>associations"]
  v_access -->|"No"| v_accesserror
  v_access -->|"Yes: validate input"| v_valid
  v_valid -->|"No: Adjusted is also <br/>rejected"| v_invalid
  v_valid -->|"Yes: configure device"| v_device
  v_device -->|"Check return value"| v_ret
  v_ret -->|"Yes"| v_device-error
  v_ret -->|"No: zero"| v_streams
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

Distinguish input-check failures from device-implementation failures, in that order. The success path in the figure below still includes the stream connection check.

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

| Elements and transitions | Source evidence |
| --- | --- |
| State and access allowed? | src/libcamera/camera.cpp:1163 |
| Return access error | src/libcamera/camera.cpp:1163 |
| Does validate() return Valid? | src/libcamera/camera.cpp:1163 |
| Return -EINVAL | src/libcamera/camera.cpp:1163 |
| PipelineHandler::configure() | src/libcamera/camera.cpp:1163 |
| Is ret nonzero? | src/libcamera/camera.cpp:1191 |
| Return nonzero ret unchanged | src/libcamera/camera.cpp:1191 |
| Next: check stream associations | src/libcamera/camera.cpp:1191 |
| No | src/libcamera/camera.cpp:1163 |
| Yes: validate input | src/libcamera/camera.cpp:1163 |
| No: Adjusted is also rejected | src/libcamera/camera.cpp:1163 |
| Yes: configure device | src/libcamera/camera.cpp:1163 |
| Check return value | src/libcamera/camera.cpp:1163 |
| Yes | src/libcamera/camera.cpp:1191 |
| No: zero | src/libcamera/camera.cpp:1191 |

</details>

### Branch that checks stream connection after configuration succeeds

```mermaid
flowchart TB

  v_start["After checks and configure <br/>succeed"]
  v_stream["Observe each cfg.stream#40;#41;"]
  v_null{"Is stream null?"}
  v_failure["Code locations: Fatal and <br/>subsequent clear/-EINVAL <br/>#40;execution not asserted#41;"]
  v_valid["Assign configuration#95; and <br/>insert active stream"]
  v_next["After remaining streams: <br/>Configured and 0"]
  v_start -->|"Each entry"| v_stream
  v_stream -->|"Check original result"| v_null
  v_null -->|"Yes: failure code locations"| v_failure
  v_null -->|"No"| v_valid
  v_valid -->|"After loop"| v_next
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

Which code locations are observed for the state check and validation, and for the case where cfg.stream() is null after PipelineHandler::configure succeeds?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

| Elements and transitions | Source evidence |
| --- | --- |
| After checks and configure succeed | src/libcamera/camera.cpp:1163 |
| Observe each cfg.stream() | src/libcamera/camera.cpp:1163 |
| Is stream null? | src/libcamera/camera.cpp:1163 |
| Code locations: Fatal and subsequent clear/-EINVAL (execution not asserted) | src/libcamera/camera.cpp:1163 |
| Assign configuration\_ and insert active stream | src/libcamera/camera.cpp:1163 |
| After remaining streams: Configured and 0 | src/libcamera/camera.cpp:1163 |
| Each entry | src/libcamera/camera.cpp:1163 |
| Check original result | src/libcamera/camera.cpp:1163 |
| Yes: failure code locations | src/libcamera/camera.cpp:1163 |
| No | src/libcamera/camera.cpp:1163 |
| After loop | src/libcamera/camera.cpp:1163 |

</details>

### Branch to observe in the configuration access check

```mermaid
flowchart TB

  v_disconnected{"Disconnection disallowed <br/>and disconnected#95;?"}
  v_removed["Return -ENODEV"]
  v_range{"low ≤ currentState ≤ high?"}
  v_allowed["Return 0"]
  v_denied["ASSERT, log and -EACCES <br/>code locations"]
  v_disconnected -->|"Yes"| v_removed
  v_disconnected -->|"No"| v_range
  v_range -->|"Yes"| v_allowed
  v_range -->|"No: observe following code"| v_denied
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

Checks disconnection first, then checks the state scope. Code after assertions and logs is not definitively described as actual execution results.

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

| Elements and transitions | Source evidence |
| --- | --- |
| Disconnection disallowed and disconnected\_? | src/libcamera/camera.cpp:709 |
| Return -ENODEV | src/libcamera/camera.cpp:709 |
| low ≤ currentState ≤ high? | src/libcamera/camera.cpp:709 |
| Return 0 | src/libcamera/camera.cpp:709 |
| ASSERT, log and -EACCES code locations | src/libcamera/camera.cpp:709 |
| Yes | src/libcamera/camera.cpp:709 |
| No | src/libcamera/camera.cpp:709 |
| Yes | src/libcamera/camera.cpp:709 |
| No: observe following code | src/libcamera/camera.cpp:709 |

</details>

### Investigation plan for checking the actual implementation of configuration calls

```mermaid
flowchart TB

  v_validate["Plan: record config type <br/>and validate implementation"]
  v_result{"Compare existing validate <br/>result with Valid"}
  v_invalid["-EINVAL code location"]
  v_handler["Plan: record actual <br/>configure implementation"]
  v_return["Observe ret: return <br/>unchanged if nonzero"]
  v_validate -->|"Observe existing call result"| v_result
  v_result -->|"Not Valid"| v_invalid
  v_result -->|"Valid: observe original <br/>configure call"| v_handler
  v_handler -->|"Record original call ret"| v_return
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

This is a plan to observe the type, implementation, and return value of an existing call that has passed the state check. It does not call validation or configuration again.

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

| Elements and transitions | Source evidence |
| --- | --- |
| Plan: record config type and validate implementation | src/libcamera/camera.cpp:1191 |
| Compare existing validate result with Valid | src/libcamera/camera.cpp:1191 |
| -EINVAL code location | src/libcamera/camera.cpp:1203 |
| Plan: record actual configure implementation | src/libcamera/camera.cpp:1191 |
| Observe ret: return unchanged if nonzero | src/libcamera/camera.cpp:1191 |
| Observe existing call result | src/libcamera/camera.cpp:1191 |
| Not Valid | src/libcamera/camera.cpp:1203 |
| Valid: observe original configure call | src/libcamera/camera.cpp:1191 |
| Record original call ret | src/libcamera/camera.cpp:1191 |

</details>

`Adjusted` from `CameraConfiguration::validate()` means the configuration has been adjusted so that it is valid; parameters may have changed for any stream, or stream configurations may have been removed. A caller that receives `Adjusted` must check the configuration carefully.

Execution verification item: The investigation plan may compare the result of `config->validate()` in `Camera::configure` with `CameraConfiguration::Valid` and also record whether the function returns `-EINVAL` when the results differ.

This is an investigation plan to record, in the existing call stack, the actual dynamic type of `config` and the `validate` implementation that is executed. If the state check and validation pass, it plans to observe the concrete implementation and return value of `PipelineHandler::configure`, which is invoked through `pipe_`'s `invokeMethod`; if the return value is nonzero, it plans to record the branch in which `Camera::configure` returns that value unchanged.

When investigating, in `Camera::configure()`, after passing the access check and configuration validation, and when the return value of `PipelineHandler::configure` is 0, observe the result `stream` of each `cfg.stream()` and the null check result. If `stream` is null, check the Fatal log `Pipeline handler failed to update stream configuration` and the `-EINVAL` return path after `activeStreams_.clear()`.

<details open>
<summary>Section-wide evidence: 10</summary>

- `src/libcamera/camera.cpp``L1195` excerpt · [Full source `L1195`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1195) · `L716` excerpt · [Full source `L716`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L716) · `L709` excerpt · [Full source `L709`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L709) · `L323` excerpt · [Full source `L323`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L323) · `L343` excerpt · [Full source `L343`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L343) · `L1203` excerpt · [Full source `L1203`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1203) · `L1191` excerpt · [Full source `L1191`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1191) · `L1225` excerpt · [Full source `L1225`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1225) · `L1163` · `L342`

</details>

## Request Submission Failures and Missing Completion Notifications

See also: Checking readiness waits and timeouts · Distinguishing request acceptance from completion notification · Observation plan for app callback connections and threads

**Leave a note before the interruption.**

Copy the template below, fill in the blanks, and compare it with the original notes when you resume.

- Enter the reported symptoms and conditions: \_\_\_\_.
- Enter the directly observed values and where they were checked: \_\_\_\_.
- Enter your interpretation of the document and any provisional assumptions: \_\_\_\_.
- Write down what you have not yet verified: \_\_\_\_.
- Enter the next check and the branches based on its result: \_\_\_\_.
- Enter the URL and section location of the supporting document: \_\_\_\_.

Leave unobserved values as unconfirmed, and do not call state-changing functions again to observe them.

When you resume, compare the reports, observations, and interpretations with the original notes to check that they have not been mixed together.

The first investigation item records the return value and calling file of the original `queueRequest` call, distinguishing a return value of 0 as normal acceptance from a negative value as a submission error. Normal acceptance is recorded separately from capture completion.

### When the last buffer has completed but no request completion notification arrives

```mermaid
flowchart TB

  v_check{"Track same submission"}
  v_last{"completeBuffer return"}
  v_entry{"completeRequest entry"}
  v_caller["Check handler path"]
  v_head{"Check target status and <br/>queue front"}
  v_held["Earlier request pending"]
  v_emit["Check emit and app slot"]
  v_unknown["Withhold judgment"]
  v_check -->|"Identity confirmed"| v_last
  v_check -->|"Submission identity <br/>unmatched or unconfirmed"| v_unknown
  v_last -->|"Returned true"| v_entry
  v_last -->|"Returned false or return <br/>unknown"| v_unknown
  v_entry -->|"No entry during complete <br/>path observation"| v_caller
  v_entry -->|"Entry observed"| v_head
  v_entry -->|"Coverage incomplete"| v_unknown
  v_head -->|"Target RequestComplete, <br/>earlier front <br/>RequestPending, break <br/>observed this pass"| v_held
  v_head -->|"Target requestComplete <br/>observed"| v_emit
  v_head -->|"Status or flow unknown"| v_unknown
```

These are source-based investigation examples. Track each submission using the camera, a run separated by stop/start, a new per-submission generation, and Request\*. Also record Request::sequence() after doQueueRequest assigns sequence\_. The sequence resets between runs and wraps on overflow. Request::reuse() can resubmit the same object, so neither cookie nor address alone identifies a submission. Example A: the last completeBuffer for target submission 42 returned true. If continuous observation covered the handler's intended completion path, including delayed branches, with no dropped records, yet no completeRequest entry was observed, inspect the callback branches and conditions for any deferred metadata or completion work. Do not assume a particular handler requires such work. Do not infer the completeBuffer return value from bufferCompleted.emit alone. Example B: target submission 42 entered completeRequest and became RequestComplete after complete(), but earlier submission 41 at queuedRequests\_.front() is RequestPending. The observed break keeps the target queued in this pass; it does not mean the target stays queued forever. Trace submission 41's pending buffers and completion path, recheck subsequent queue heads, and observe the target's Camera::requestComplete call. Then separately confirm the actual requestCompleted.emit and entry into the application slot. If the target is already at the front, check its status and the queue-processing flow. Distinguish RequestCancelled separately. Withhold judgment if submission identity or the required observation coverage is incomplete. Do not re-invoke state-mutating functions to observe them. [`pipeline_handler.cpp:491`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L491) · [`pipeline_handler.cpp:401`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L401) · [`request.cpp:385`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/request.cpp#L385) · [`pipeline_handler.cpp:567`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L567) · [`pipeline_handler.cpp:566`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L566) · [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) · [`pipeline_handler.cpp:556`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L556) · [`pipeline_handler.cpp:588`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L588) · [`request.cpp:132`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/request.cpp#L132) · [`pipeline_handler.cpp:593`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L593) · [`pipeline_handler.cpp:594`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L594) · [`pipeline_handler.cpp:599`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L599) · [`camera.cpp:1488`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1488) · [`bound_method.cpp:40`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/base/bound_method.cpp#L40)

| Current check | Observation | Next check |
| --- | --- | --- |
| Track same submission | Identity confirmed | completeBuffer return [`pipeline_handler.cpp:491`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L491) · [`pipeline_handler.cpp:567`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L567) · [`pipeline_handler.cpp:566`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L566) |
| Track same submission | Submission identity unmatched or unconfirmed | Withhold judgment [`pipeline_handler.cpp:491`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L491) · [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) · [`pipeline_handler.cpp:593`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L593) |
| completeBuffer return | Returned true | completeRequest entry [`pipeline_handler.cpp:567`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L567) · [`pipeline_handler.cpp:556`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L556) · [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) |
| completeBuffer return | Returned false or return unknown | Withhold judgment [`pipeline_handler.cpp:567`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L567) · [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) · [`pipeline_handler.cpp:593`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L593) |
| completeRequest entry | No entry during complete path observation | Check handler path [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) · [`pipeline_handler.cpp:556`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L556) |
| completeRequest entry | Entry observed | Check target status and queue front [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) · [`pipeline_handler.cpp:588`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L588) · [`pipeline_handler.cpp:593`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L593) |
| completeRequest entry | Coverage incomplete | Withhold judgment [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) · [`pipeline_handler.cpp:593`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L593) |
| Check target status and queue front | Target RequestComplete, earlier front RequestPending, break observed this pass | Earlier request pending [`pipeline_handler.cpp:593`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L593) · [`pipeline_handler.cpp:594`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L594) |
| Check target status and queue front | Target requestComplete observed | Check emit and app slot [`pipeline_handler.cpp:599`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L599) |
| Check target status and queue front | Status or flow unknown | Withhold judgment [`pipeline_handler.cpp:593`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L593) · [`pipeline_handler.cpp:594`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L594) · [`pipeline_handler.cpp:584`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L584) |

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

Where did it stop after the last buffer completed?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

| Elements and transitions | Source evidence |
| --- | --- |
| Track same submission | src/libcamera/pipeline_handler.cpp:428 |
| completeBuffer return | src/libcamera/pipeline_handler.cpp:547 |
| completeRequest entry | src/libcamera/pipeline_handler.cpp:547 |
| Check handler path | src/libcamera/pipeline_handler.cpp:547 |
| Check target status and queue front | src/libcamera/pipeline_handler.cpp:547 |
| Earlier request pending | src/libcamera/pipeline_handler.cpp:547 |
| Check emit and app slot | src/libcamera/pipeline_handler.cpp:547 |
| Withhold judgment | src/libcamera/pipeline_handler.cpp:547 |
| Identity confirmed | src/libcamera/pipeline_handler.cpp:428 |
| Submission identity unmatched or unconfirmed | src/libcamera/pipeline_handler.cpp:428 |
| Returned true | src/libcamera/pipeline_handler.cpp:547 |
| Returned false or return unknown | src/libcamera/pipeline_handler.cpp:547 |
| No entry during complete path observation | src/libcamera/pipeline_handler.cpp:547 |
| Entry observed | src/libcamera/pipeline_handler.cpp:547 |
| Coverage incomplete | src/libcamera/pipeline_handler.cpp:547 |
| Target RequestComplete, earlier front RequestPending, break observed this pass | src/libcamera/pipeline_handler.cpp:547 |
| Target requestComplete observed | src/libcamera/pipeline_handler.cpp:547 |
| Status or flow unknown | src/libcamera/pipeline_handler.cpp:547 |

</details>

## Distinguishing duplicate allocation from export failure

If `inserted` from `try_emplace` is false, `FrameBufferAllocator::allocate` logs an error stating that the buffers have already been allocated and returns `-EBUSY`. `FrameBufferAllocator::allocate()` stores the return value of `exportFrameBuffers()` in `ret` and, if `ret` is negative, removes the corresponding `buffers_` entry using `buffers_.erase(it)`. When `FrameBufferAllocator::allocate` calls `exportFrameBuffers`, it returns the resulting `ret` regardless of whether the value is negative.

### Relationships and boundaries in distinguishing duplicate allocation from export failure

```mermaid
flowchart TB

  v_insert{"Is the stream already <br/>present?"}
  v_busy["Log the duplicate <br/>allocation and return <br/>-EBUSY. Keep the existing <br/>buffers#95; entry."]
  v_export["Export buffers to the new <br/>entry and save the result <br/>in ret."]
  v_invalid{"Check whether ret is <br/>-EINVAL."}
  v_log["Log that stream is not part <br/>of the active configuration."]
  v_failure{"Check whether the export <br/>result is negative."}
  v_erase["Erase the new buffers#95; <br/>entry."]
  v_result["Return the export result <br/>ret."]
  v_insert -->|"If already present, return <br/>for duplicate allocation. <br/>#91;true#93;"| v_busy
  v_insert -->|"If not already present, <br/>export the buffers. #91;false#93;"| v_export
  v_export -->|"Check the export result."| v_invalid
  v_invalid -->|"If ret is -EINVAL, log the <br/>error. #91;true#93;"| v_log
  v_invalid -->|"If ret is not -EINVAL, <br/>check whether it is <br/>negative. #91;false#93;"| v_failure
  v_log -->|"After logging, check <br/>whether ret is negative."| v_failure
  v_failure -->|"If the result is negative, <br/>erase the entry. #91;true#93;"| v_erase
  v_erase -->|"After erasing the entry, <br/>return ret."| v_result
  v_failure -->|"If the result is not <br/>negative, keep the entry <br/>and return ret. #91;false#93;"| v_result
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

How do duplicate allocation and export failure differ in processing flow, return values, and handling of buffers\_ entries?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

LLM diagram draft · before human review

Authoring model: `cli/codex/gpt-6.1-terra`

| Elements and transitions | Source evidence |
| --- | --- |
| Is the stream already present? | src/libcamera/framebuffer_allocator.cpp:86 |
| Log the duplicate allocation and return -EBUSY. Keep the existing buffers\_ entry. | src/libcamera/framebuffer_allocator.cpp:86 |
| Export buffers to the new entry and save the result in ret. | src/libcamera/framebuffer_allocator.cpp:86 |
| Check whether ret is -EINVAL. | src/libcamera/framebuffer_allocator.cpp:86 |
| Log that stream is not part of the active configuration. | src/libcamera/framebuffer_allocator.cpp:86 |
| Check whether the export result is negative. | src/libcamera/framebuffer_allocator.cpp:86 |
| Erase the new buffers\_ entry. | src/libcamera/framebuffer_allocator.cpp:86 |
| Return the export result ret. | src/libcamera/framebuffer_allocator.cpp:86 |
| If already present, return for duplicate allocation. · !inserted \[true\] | src/libcamera/framebuffer_allocator.cpp:86 |
| If not already present, export the buffers. · !inserted \[false\] | src/libcamera/framebuffer_allocator.cpp:86 |
| Check the export result. | src/libcamera/framebuffer_allocator.cpp:86 |
| If ret is -EINVAL, log the error. · ret == -EINVAL \[true\] | src/libcamera/framebuffer_allocator.cpp:86 |
| If ret is not -EINVAL, check whether it is negative. · ret == -EINVAL \[false\] | src/libcamera/framebuffer_allocator.cpp:86 |
| After logging, check whether ret is negative. | src/libcamera/framebuffer_allocator.cpp:86 |
| If the result is negative, erase the entry. · ret \< 0 \[true\] | src/libcamera/framebuffer_allocator.cpp:86 |
| After erasing the entry, return ret. | src/libcamera/framebuffer_allocator.cpp:86 |
| If the result is not negative, keep the entry and return ret. · ret \< 0 \[false\] | src/libcamera/framebuffer_allocator.cpp:86 |

</details>

<details open>
<summary>Section-wide evidence: 2</summary>

- `src/libcamera/framebuffer_allocator.cpp``L86` excerpt · [Full source `L86`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/framebuffer_allocator.cpp#L86) · `L95` excerpt · [Full source `L95`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/framebuffer_allocator.cpp#L95)

</details>

## Validity period of the reference returned by buffers

`buffers()` must be called only after buffers have been successfully allocated for the stream with `allocate()`. The buffers returned by `buffers()` remain valid until `free()` is called for the same stream or the `FrameBufferAllocator` instance is destroyed.

### Relationship and boundaries of the lifetime of the reference returned by buffers

```mermaid
flowchart TB

  v_allocate["Successfully allocate <br/>buffers for the stream with <br/>allocate#40;#41;."]
  v_buffers["Call buffers#40;#41; only after <br/>successfully allocating <br/>buffers for the stream."]
  v_returned["Returned buffers are valid <br/>until the first of the two <br/>events below."]
  v_free["Calling free#40;#41; for the same <br/>stream is an event that <br/>ends validity."]
  v_allocator["Destruction of the <br/>FrameBufferAllocator <br/>instance is an event that <br/>ends validity."]
  v_allocate -->|"Call buffers#40;#41; only after <br/>successful allocation."| v_buffers
  v_buffers -->|"Returned buffers are valid <br/>until the first of the two <br/>events below."| v_returned
  v_returned -->|"Calling free#40;#41; for the same <br/>stream can end validity."| v_free
  v_returned -->|"Destruction of the <br/>FrameBufferAllocator <br/>instance can end validity."| v_allocator
```

Mermaid source

<details open>
<summary>Diagram evidence and verification scope</summary>

When can buffers() be called, and what event ends the lifetime of the returned buffers?

Source-linked interpretation · automatic link check only · meaning and device execution not yet verified

LLM diagram draft · before human review

Authoring model: `cli/codex/gpt-6.1-terra`

| Elements and transitions | Source evidence |
| --- | --- |
| Successfully allocate buffers for the stream with allocate(). | src/libcamera/framebuffer_allocator.cpp:141 |
| Call buffers() only after successfully allocating buffers for the stream. | src/libcamera/framebuffer_allocator.cpp:141 |
| Returned buffers are valid until the first of the two events below. | src/libcamera/framebuffer_allocator.cpp:142 |
| Calling free() for the same stream is an event that ends validity. | src/libcamera/framebuffer_allocator.cpp:142 |
| Destruction of the FrameBufferAllocator instance is an event that ends validity. | src/libcamera/framebuffer_allocator.cpp:142 |
| Call buffers() only after successful allocation. | src/libcamera/framebuffer_allocator.cpp:141 |
| Returned buffers are valid until the first of the two events below. | src/libcamera/framebuffer_allocator.cpp:142 |
| Calling free() for the same stream can end validity. | src/libcamera/framebuffer_allocator.cpp:142 |
| Destruction of the FrameBufferAllocator instance can end validity. | src/libcamera/framebuffer_allocator.cpp:142 |

</details>

<details open>
<summary>Section-wide evidence: 2</summary>

- `src/libcamera/framebuffer_allocator.cpp``L141` excerpt · [Full source `L141`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/framebuffer_allocator.cpp#L141) · `L142` excerpt · [Full source `L142`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/framebuffer_allocator.cpp#L142)

</details>

## Distinguishing metadata errors

If the size of ipaModuleInfo is smaller than sizeof(`info_`), or if moduleAPIVersion does not match `IPA_MODULE_API_VERSION`, loadIPAModuleInfo() returns -EINVAL.

<details open>
<summary>Section-wide evidence: 1</summary>

- `src/libcamera/ipa_module.cpp``L268` excerpt · [Full source `L268`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/ipa_module.cpp#L268)

</details>

## When the signature file cannot be opened

If the signature file cannot be opened, `loadIPAModuleInfo` returns 0.

<details open>
<summary>Section-wide evidence: 1</summary>

- `src/libcamera/ipa_module.cpp``L316` excerpt · [Full source `L316`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/ipa_module.cpp#L316)

</details>

## Source manuscripts and review records

<details open>
<summary>Investigation of configuration and request errors</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-11-11 17:00:45+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence files: `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `be7e83e913`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status recorded: 2026-11-12 · Before human review

</details>

Markdown source ↗

Open earlier detail

</details>

<details open>
<summary>FrameBufferAllocator Failures and Reference Lifetime</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-11-20 18:07:38+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence file: `src/libcamera/framebuffer_allocator.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `adfa719f8e`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status recorded on: 2026-11-21 · Awaiting human review

</details>

Markdown source ↗

Open earlier detail

</details>

<details open>
<summary>IPA module information check and missing signature file</summary>

- **Generation method**: Extracted facts and LLM explanation
- **Validation scope**: Tables and figures are created from facts, and the explanations are written by the LLM. Citation, sentence, and configured structure checks are applied.
- **Automated check**: Passed (`ok`). The items checked are listed in the verification scope. Whether the explanation content is correct is checked by a human reviewer.
- **Human review**: Before human review
- **Analysis baseline commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Document generation time**: `2026-10-29 20:32:19+00:00`
- **Sentence generation model**: `cli/codex/gpt-6.1-terra`
- **Contracts between documents**: Automated comparison report · Before human review

<details open>
<summary>Record from when the manuscript was written</summary>

This is a record saved in the manuscript as of that time. It may differ from the current document's standards.

- Evidence file: `src/libcamera/ipa_module.cpp`
- Evidence level: code verified (static analysis, simple_compdb configuration, commit `212c689fcf`)
- Automated check (citation, sentence, and configured structure checks): passed
- Review status record date: 2026-10-30 · Before human review

</details>

Markdown source ↗

Open earlier detail

</details>

Download page Markdown · Reader edition source map
