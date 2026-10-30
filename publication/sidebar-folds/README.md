# Persistent sidebar navigation and allocator preconditions

Generator [PR195](https://github.com/TTolsun/camera-hal-sdd-generator/pull/195), merged `0c1feca3254becc2be39a0c30f585f0c099c5095`.
Official source and public upstream mirror both remain `212c689fcf2450bbfbaab25c7472895ac277b5d6`. No public recurring schedule was installed.

Reader groups, task sections and scenario branches use native details/summary disclosures. Same-tab choices survive
document/pagination links, reload, Korean/English switches and history, including rapid navigation and nested choices.
Folds restore before menu scroll. Mobile focus targets the outermost visible closed ancestor and controls have 44px touch targets.
See [actual browser checks](browser-validation.json) and [build/link/repeat checks](build-validation.json).

The source-window review found missing allocate() configuration/stopped/active-stream preconditions and the distinction
between EACCES and EINVAL in the existing allocator detail. The generated addition retains both invalid-stream conditions.
[Review windows and exclusions](source-window-review.json) distinguish existing detail, scope exclusions and unreviewed source.
This is a bounded public-source supplement, not a claim that the complete source has been reviewed.

New drafting and translation use independent Claude Code CLI 2.1.314, exact model `claude-haiku-5-5`, `--effort high`.
The official npm package is local to the task; its official Node wrapper resolves the executable. Global defaults were not changed.
An initial native-executable launch error and a corrected question-contract validation failure remain archived. Successful
checkpoint reuse is recorded separately and is not a new inference. Every new Claude native receipt exposes only the selected Haiku model.

The complete changed allocator manuscript was independently grounded through Codex CLI `gpt-6.1-terra`,
`-c model_reasoning_effort="high"`; see [review result](independent-grounding.json). Cross-document review uses the separate
`paths.consistency_profile`, with 68 completed source-bound batches and four automatic unresolved findings retained.
Some independent batches ran concurrently; overlapping completed receipts and the first assembly failure are preserved.
The final ordinary audit reassembled and enforced the final exact checkpoint/receipt set. No alternative model or direct API was used.

[Native originals](cli-evidence.zip), their [hash index](cli-evidence-index.json), [receipt index](new-receipts.json),
and [execution profiles](profiles/) preserve the actual calls. Profiles retain local reproduction paths as historical execution data;
they require corresponding source/build/CLI paths for a new run. Saved responses are evidence, not substitutes for a fresh CLI run.
The render profile preserves the original identity of an unchanged historical visual solely for verification, while all new
consistency checks select the independent review profile. It performs no historical model inference.

Structural facts were reused from the hash-verified public archive and source212 overlay, then configured public source excerpts
were recollected; [this release overlay](facts-overlay.json) records the differences. This is not fresh Clang extraction.
Twenty-seven unchanged manuscripts, original visual drafts, prior model identities and human-review status remain intact.
The previous root run and receipt index are copied byte-for-byte in [previous-release](previous-release/).

Build `efa07f052b201bc0c40b8f45d43a9ec1eb1850f5f0aaa5c86bc01f3e1bc04af0` has 257 manifest-owned outputs and zero broken links. The second build has the same manifest.
The site was generated through the ordinary export/verify gate; no generated HTML was manually edited.
Pages workflow success and actual public URL/hash/browser checks are recorded after merge in
[generator issue194](https://github.com/TTolsun/camera-hal-sdd-generator/issues/194).
Human approval, independent reader-task testing, internal Camera HAL and device verification remain pending.
