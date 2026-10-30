# Persistent sidebar navigation and allocator preconditions

Generator [PR195](https://github.com/TTolsun/camera-hal-sdd-generator/pull/195) and follow-up
[PR197](https://github.com/TTolsun/camera-hal-sdd-generator/pull/197), merged `774677a08bb710a65d0129f7bb7ce27995dd320b`.
Official source and public upstream mirror both remain `212c689fcf2450bbfbaab25c7472895ac277b5d6`. No public recurring schedule was installed.

Reader groups, task sections and scenario branches use native details/summary disclosures. Same-tab choices survive
document/pagination links, reload, Korean/English switches and history, including rapid navigation and nested choices.
The user's latest instruction sets every group, task and scenario branch to initially collapsed, including the current branch.
Explicit previously saved open choices still restore under unchanged IDs.
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
Six nested JSON response wrappers discovered in English display strings were rejected by the generator and actually
retranslated through the same Haiku/high CLI. Their original values and receipts are retained; no saved wrapper was manually unwrapped.

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
Restore the previous source212 snapshot first, then use restore_facts.py --base BASE --out OUT; ordered evidence keys preserve the exact serialized hash.
Twenty-seven unchanged manuscripts, original visual drafts, prior model identities and human-review status remain intact.
The previous root run and receipt index are copied byte-for-byte in [previous-release](previous-release/).
The initially deployed sidebar run/catalog are retained in [initial-release](initial-release/).

Build `85bf88f3eed937d9536096ad920b3c6b5cc7702272e1af0f84f17e19083b3ad9` has 257 manifest-owned outputs and zero broken links. The second build has the same manifest.
The site was generated through the ordinary export/verify gate; no generated HTML was manually edited.
Pages workflow success and actual public URL/hash/browser checks are recorded after merge in
[generator issue194](https://github.com/TTolsun/camera-hal-sdd-generator/issues/194).
Human approval, independent reader-task testing, internal Camera HAL and device verification remain pending.
