# Generated navigation and contract-review scope

The remaining finding was a review-scope problem, not a manuscript defect. The final next-step
link in the request-queue scenario names the completeRequest document; it does not assert an
execution order or completion guarantee. Its target exists with the expected title and same
source commit. [Investigation](scope-investigation.json) preserves the exact link/target hash,
and the [previous report](previous-consistency-review.json) preserves the original native
insufficient-evidence finding unchanged. No old verdict was relabelled compatible.

Generator [PR207](https://github.com/TTolsun/camera-hal-sdd-generator/pull/207), commit `9505f6c9eb31f439485d263f828b36189dbcf4dd`,
recognizes only the exact final default-template link selected by current section/scenario
configuration and a matching current local Markdown document title. It records these links in
excluded_navigation with target hashes. Missing/stale targets fail before model review. Mixed
prose, custom hints/templates, nonterminal links, fenced examples, fragment links and generated
LLM answers remain in the ordinary claim path. Publication enforcement recomputes the scope
records and rejects tampering. Final HTML link/anchor checks remain with verify-site.
This is deterministic navigation integrity, not a model/runtime verdict or human approval.

The [current report](../../docs/contract-consistency.json) freshly reviews the retained runtime
and analysis claims through independent Codex `gpt-6.1-terra`,
`-c model_reasoning_effort="high"`. It has no contradiction and 1 automatic
unresolved findings in its configured scope. Every previous report and native receipt remains
preserved. A DIFFERENT English stop/completion-condition claim (catalog/298a01caad3d54f6/en)
remains automatically ambiguous and stays in runtime review; the scope fix does not suppress
this uncertainty or force a zero count. See scope-investigation.json for the exact current finding. This is not an exhaustive all-pairs proof or hardware/callback verification.

All manuscript, English-catalog and source-facts bytes are unchanged; see
[input preservation](input-preservation.json). There was no new prose generation, translation,
manual manuscript correction or fresh structural extraction. Official libcamera HEAD remains
`293d751a814e0d4c34e85ad457ccd9d5eefd1a61`; the exact previous Meson/Ninja/libclang snapshot remains authenticated through
[facts reference](facts-reference.json). Source excerpts and document links remain intact.
The generation profile remains independent Claude Code 2.1.314, exact `claude-haiku-5-5`,
`--effort high --setting-sources project,local`; [native preflight](preflight.json) confirms actual
modelUsage and high support. Global defaults are unchanged. No alternate model/CLI, direct API,
saved response or manual prose substituted for new generation or review.
[Profiles](profiles/), [new receipts](new-receipts.json), [native archive](cli-evidence.zip) and
[hash index](cli-evidence-index.json) distinguish fresh review/preflight calls from retained history.

The [effective human approval state](approval-state.json) is unchanged: both inputs have no
approval ledger or accepted entries; no accept command ran. The callback investigation plan is
byte-identical and actual callback execution/internal HAL validation remain not-run.
[Build validation](build-validation.json) records 60 HTML pages, 257 owned outputs, zero broken
links and identical repeated manifests. [Browser checks](browser-validation.json) verify the
request-queue navigation in both languages. No generated HTML was edited manually.
Post-merge Pages and public manifest/all-output hash checks are recorded in the release PR.
