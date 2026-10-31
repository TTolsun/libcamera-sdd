# Cancellation precondition for device submission

The Korean and English Pipeline request guide now explicitly states that doQueueRequest calls
queueRequestDevice and assigns ret only when the request is not already cancelled. The preceding
paragraph retains the cancelled request's completeRequest call and early return. Nonzero ret
handling and the device implementer's parameter/buffer obligation remain source-bound.

Generator [PR205](https://github.com/TTolsun/camera-hal-sdd-generator/pull/205) and [PR206](https://github.com/TTolsun/camera-hal-sdd-generator/pull/206), commit `bebbfe010fdb1cbb1e8dac75dad7e473aa347299`.
Official libcamera HEAD is still `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`. Existing fresh Meson/Ninja/libclang structural facts
are retained and source excerpts recollected; no new structural extraction or hardware execution
is claimed. [Source windows](source-window-review.json) distinguish the bounded review from
unreviewed source/runtime scope.

The [previous automatic report](previous-consistency-review.json) preserves both original
ambiguous findings, one Korean and its English translation. The current manifest-owned
[report](../../docs/contract-consistency.json) has zero contradictions. The original Korean/English ambiguity pair is now assessed compatible,
and one different insufficient-evidence finding for a next-step navigation link remains.
Its exact verdict is preserved in [finding resolution](finding-resolution.json); ordinary link checks
verify that the target exists, without manually changing the model assessment. Verdicts were produced by independent Codex CLI, not edited.
This is automatic source review, not human approval or an exhaustive proof of runtime behavior.

New prose and changed English strings use independent Claude Code 2.1.314, exact
`claude-haiku-5-5`, `--effort high --setting-sources project,local`. [Preflight](preflight.json)
records actual provider modelUsage and high support. Source grounding and bilingual consistency
use independent Codex `gpt-6.1-terra`, `-c model_reasoning_effort="high"`.
[Profiles](profiles/), [new receipts](new-receipts.json), [native evidence](cli-evidence.zip),
and its [hash index](cli-evidence-index.json) preserve exact per-run settings and execution results.
Historical receipts are identified separately and are not fresh inference. Global defaults
were not changed. No alternate model, CLI, direct API, saved answer or manual manuscript
substituted for new generation. A sandboxed preflight stalled and was stopped; the exact same
CLI/model/effort succeeded outside the restricted sandbox. Initial local pytest temp-directory
access failed; a writable workspace temp directory passed 212 focused tests.
The first draft exceeded the prose growth limit and independent grounding rejected its omitted no-fence early-return condition. It was preserved and regenerated through the same Haiku CLI with the existing focused writing mode and a complete question. Earlier output and generation records remain preserved.

Only pipeline-requests.md changed among the previous manuscripts. Full bilingual review also
found an existing English paragraph expanding waiting requests to all pending requests. The same
Haiku CLI retranslated it as all waiting requests; its Korean original was unchanged.
The full audit rejected a generated claim that the cancelRequest body was unconfirmed. A corrected
call-only question and separate submission/failure units regenerated through the same Haiku CLI
remove that claim. Rejected artifacts and all verdicts remain in the evidence archive. The approval ledger and
request-lifecycle.md, including its unexecuted callback investigation plan, are byte-identical;
see [preservation](manuscript-preservation.json). No accept command was executed.
[Independent grounding](independent-grounding.json) reviews all generated pipeline statements.
The original historical figure identity remains solely for verification; no new inference
uses its historical render profile. New review uses its separate explicit profile.

[Build checks](build-validation.json): build `a87b1174ecb59e15b5309927409174d462f592a7b9bb6360adf4589d4de2d008`, 257 owned outputs,
zero broken internal links; two ordinary generator exports produced an identical manifest.
[Browser checks](browser-validation.json) verify both languages and mobile reading.
Generated HTML was not manually edited. Actual application callback execution and internal
Camera HAL validation remain not-run. Existing human approval state is unchanged.
Post-merge Pages workflow and public manifest/all-output hash checks are recorded in the release PR.
