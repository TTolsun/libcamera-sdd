# Callback observation plan separated from source contracts

Generator [PR198](https://github.com/TTolsun/camera-hal-sdd-generator/pull/198) implements the separation.
[Reproduction follow-up PR202](https://github.com/TTolsun/camera-hal-sdd-generator/pull/202), final generator `eeb747f3b773b76aecdc4e6a2f7e2f29a7e9eb23`.
Observed official public libcamera snapshot and public upstream/master history are `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`. No recurring public schedule was installed.

The lifecycle guide now places the completeRequest caller obligations in a contract answer and the proposed
application callback entry/return/thread observations in a separate execution-check paragraph and `kind: limitation`
metadata. Both Korean and English explicitly state that the plan has not been executed and the callback result
remains unverified. No libcamera application callback was executed for this change.

The reusable consistency pipeline preserves `statement_kinds` in Korean claims and their displayed English
paragraphs. Matching includes the actual execution-check label, so these English paragraphs are now reviewed
instead of being omitted at the label's colon. Labels do not establish successful execution or excuse unsupported
runtime assertions. Current automatic review has 2 unresolved findings; no contradiction.
The previous automatic report is preserved byte-for-byte under previous-release for comparison, not overwritten
or reclassified as human approval. The current report is manifest-owned docs/contract-consistency.json.

All new lifecycle prose and changed English display strings use independent Claude Code CLI 2.1.314,
exact model `claude-haiku-5-5`, `--effort high`. [Preflight](preflight.json) and [native receipts](new-receipts.json)
record actual model usage and per-run settings. Global defaults were not changed. The complete changed manuscript
was independently source-reviewed through Codex CLI `gpt-6.1-terra`, `-c model_reasoning_effort="high"`;
see [review result](independent-grounding.json). The same separate profile performs cross-document review.
That source review supports 26 source statements and retains one unexecuted callback plan as insufficient evidence;
it does not certify callback execution. Its original negative verdict remains visible.
No alternate model, CLI, direct API, saved response or manual manuscript replaced generation.
The initial whole-page regeneration omitted the last-buffer condition in one completion obligation;
the independent reviewer rejected it. The same Haiku CLI regenerated that unit with the condition
required in its question contract. Other exact completed units/topics were revalidated or retained
with their original provenance, not reported as fresh inference. The first translation request
exceeded the CLI's complete-prompt size budget before launch; the retry uses one complete
source-bound display unit per call. Initial outputs, errors and rejected review receipts remain archived.
The return-value observation was also regenerated through the same Haiku CLI after review found an
unnecessary log-availability assumption. Its question now asks only for the return value and
success/error distinction. Earlier strict source-entailment reviews of the explicitly unexecuted
callback plan are preserved, including their insufficient-evidence reasons; no verdict was edited.
The independent review report distinguishes source-supported statements from any unverified plan.
No interpretation of a plan establishes actual application callback execution.
The source293 refresh retains only authenticated, source-identical historical translations through the standard
cross-commit carryover path. The exact [origin catalog](translation-origin.json) and recorded source_carryover
lineage distinguish retained values from new inference. The 49 context-dependent units required actual new Haiku
calls. A batch that weakened a caller's shall obligation to should was rejected; no accepted response was manually
imported to declare success. The same CLI regenerated the units with explicit Korean must/must-not guidance.
Three further strings from the final main integration were also generated through that CLI.

Actual public reproduction found the example preflight incorrectly requiring product material to be in source Git.
It now checks only exact canonical material records in their own domain, while structural/source locations remain
Git-owned and damaged or colliding records fail. [The final facts preflight](facts-verification.json) passes.
Main's executable identity normalization also exposed an old figure fingerprint. The strict legacy verifier accepts
only the exact configured historical command/source/rules/model/arguments and rechecks the graph; the original
record was not rewritten and no historical model inference was made. Changed and unknown fingerprints still fail.

[Source windows](source-window-review.json) and remaining runtime evidence distinguish the bounded editorial
correction from unreviewed application/device execution. Four new official commits arrived after the first candidate.
The existing Meson/Ninja + libclang pipeline freshly extracted source293 with zero parsing errors, and configured
excerpts were recollected. See [extraction](extraction293.json), [upstream scope](upstream-review.json),
[exact structural archive](structural-facts.json), and [revalidation](source293-revalidation.json).
Use restore_facts.py --out NEW_PATH to restore the hash-verified fresh archive; restoration is not new extraction.
The source212 candidate and failed attempts remain in the CLI evidence archive. The original human approval
ledger remains byte-identical; manuscript source metadata is revalidated by the standard carry-forward path.
See [body preservation](manuscript-preservation.json) for exact changes after the upstream update. Historical visual
generation identities are retained solely for verification, with no new inference through that historical profile.
Prior run and receipt index are retained in previous-release; earlier publication evidence remains intact.

Build `b018b0476d52c50044e87e3ddcb6d12bbe1bfadf4e15902dab7f850fd2dad0ee` owns 257 outputs; [build checks](build-validation.json) found no broken links
and two ordinary exports produced the identical manifest. [Browser checks](browser-validation.json) cover both
languages and the separate unexecuted plan. No generated HTML was manually edited.
[Raw CLI records](cli-evidence.zip), [hash index](cli-evidence-index.json), and [execution profiles](profiles/)
preserve actual per-run settings and records. Absolute local paths are historical execution metadata and require
corresponding reproduction inputs. Saved responses are evidence, not substitutes for fresh CLI calls.

Human approval, callback/device execution and internal Camera HAL validation remain pending.
Post-merge Pages and live artifact verification are recorded in the public release PR.
