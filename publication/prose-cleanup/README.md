# Public prose cleanup evidence

Generator PR: [camera-hal-sdd-generator #179](https://github.com/TTolsun/camera-hal-sdd-generator/pull/179).

The initial audit covers every reader paragraph/list item on all 60 Korean/English pages of public release
`e9322a2e2fc3061e57257dc8ec705fc40abad680`: 842 units. Tables, code, figures and folded audit records are
outside this prose audit. Page decisions are candidates, with explicit conditions to preserve.

`fixed-e117/` is a controlled, same-source editing proof for public libcamera
`e117198c015057761bb0bbaa85f963c41ce412d7`. Four manuscripts were generated and grounded through the
independent Codex CLI, explicitly selecting `gpt-6.1-terra` and `model_reasoning_effort="high"`.
The answer text decreases from 11,271 to 9,595 characters; quotes, audit metadata and rendered HTML
paragraph counts are excluded. The final editorial round found no remaining audited repetition or
required-information loss. All automatic reviews retain human review pending.

The constructor load-success precondition, module-path error log, ownership, callback targets,
sensor-control arguments, caller obligations and licensing conditions are preserved. No manuscript
or generated HTML was manually rewritten. Failed calls, retries, editorial rounds and completed-unit
checkpoint reuse are retained, and are not presented as independent fresh-model trials.

Original call records, execution settings, source facts, checkpoints and run ledgers are retained locally.
They are not mirrored in this package because they include machine-local operational metadata.
`local-record-hashes.json` preserves their byte counts and SHA-256 values without exposing their contents.
Historical public receipts for unchanged manuscripts were restored and checked, not counted as new calls.
The read-only authorship check verifies original CLI records and current source contracts for
19 LLM documents, including the mixed historical/checkpoint lineage. It does not apply the separate
independent-fresh-trial benchmark or modify lineage to pass it. Document lifecycle checks cover 28 manuscripts.

For a new reproduction, use a public e117 checkout and the generator's libcamera example profile with
your own source/build/output paths and an actual Meson compilation database. This editing proof reused
published facts and recollected source excerpts; it does not claim a new complete extraction or
latest-upstream deployment. Scripts are archived as text for inspection and describe the local checks;
they do not substitute saved responses for actual CLI execution or promise identical new model outputs.

The public `docs/` output will be updated after integrating these changes with the latest public-source
release. Deployment, live manifest/file hashes, bilingual checks and reader screenshots are recorded separately.
This is public libcamera test evidence, not internal Camera HAL or device verification, human approval,
or a recurring public generation schedule.
