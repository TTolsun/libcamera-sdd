# Issue 241: a preserved publication contract and its actual execution

This release adds a source-bound Korean/English validation document for one previously fixed reader question: the three `Request::addBuffer()` rejection checks and the subsequent request/buffer linking boundary. It adds a seven-node bilingual decision diagram and publishes original execution records. The main handbook and its historical review states are preserved.

- [Korean document](https://ttolsun.github.io/libcamera-sdd/validation/issue241/camera-requests.html)
- [English document](https://ttolsun.github.io/libcamera-sdd/validation/issue241/en/camera-requests.html)
- [Generator issue](https://github.com/TTolsun/camera-hal-sdd-generator/issues/241)
- Generator implementation: [PR 254](https://github.com/TTolsun/camera-hal-sdd-generator/pull/254), [PR 263](https://github.com/TTolsun/camera-hal-sdd-generator/pull/263), [PR 265](https://github.com/TTolsun/camera-hal-sdd-generator/pull/265).

## What is new and what was already available

Issue 214 already supplied input fingerprints, publication plans, execution journals and evidence-checked checkpoints. This work links those existing records to a versioned, opt-in operation contract: target sections/questions, completion criteria, prerequisite reports, source/generator basis, generation/translation/review profiles, policy inputs, exclusions and classified discoveries. Immutable revisions and plans retain previous bytes; the existing latest plan remains a convenient view.

Actual generation, translation, independent review and export entrypoints enforce the declared basis. Changes need a reasoned new revision; live input changes fail before acceptance. A short output transaction protects cooperating writes and restores only this operation's known output bytes. It retains external edits and does not lock the source repository or stop parallel sessions. This is filesystem observation and cooperating writer protection, not an OS-wide atomic compare-and-swap guarantee.

The real translation run exposed two required defects that were fixed before completion: catalog writes/profile selection needed the same acceptance boundary, and independent profile copies lost the loader's original input snapshots. Existing reuse decisions (#242), failure classification (#243), CLI syntax and impact schema 1 remain outside this work's ownership.

## Fixed inputs and independent CLI settings

[The comparison plan](comparison-plan.json) was saved before successful native drafting. It fixes `camera-requests/request/buffer-rejection`, source `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`, `src/libcamera/request.cpp:475–505` (31 lines), SHA-256 `c1c0b55f2925856df843fa155a14bb07eb616f52b6bde75cd3b0b5a4ab03b64a`. Passed-fence ownership is excluded. The original public facts corpus was retained and the selected source window was refreshed; this is not fresh whole-source Clang extraction.

Generation, translation and a separately configured independent review all use native Codex CLI, `gpt-6.1-terra`, `-c model_reasoning_effort="high"`. Resolved executable/argv and original requests, responses and receipts are in the archives. No direct model API, alternate CLI, saved answer or hand-authored manuscript substitutes for a fresh successful call. Declared bilingual graph labels are distinguished from newly translated strings; the graph received a fresh independent source review.

Final runtime generator: `1365ccb54a7b1bb42d1d5f9ae038e817b97debc3`. Existing public-profile limits were retained; no new operation-wide token/time/call budget was imposed. Archival configurations intentionally retain their original absolute paths and hashes. Reproduction on a different checkout needs explicit path changes and a new contract revision; editing old snapshots in place would destroy the evidence.

## Plan versus actual execution

The [machine-readable comparison](comparison.json) links each invocation to existing generation journals, call receipts, revision and immutable plans. Byte-identical receipt copies in checkpoints count once. There are **13 completed native document calls**, excluding generator code reviews and controlled test doubles.

| Actual step | Fresh calls | Measured command wall time | Result |
|---|---:|---:|---|
| Missing prerequisite | 0 | 3.885 s | Failed before drafting; existing report gate reused. |
| First generation + source grounding | 2 | 41.722 s | Completed; original plan archived. |
| Identical resume | 0 | 9.572 s | Existing checkpoint validated; first plans preserved. |
| Unrecorded question change | 0 | 4.174 s | Refused; previous manuscript bytes preserved. |
| Export before independent reports | 0 | 6.323 s | Refused. |
| First actual English translation | 8 | 262.743 s | 85 new strings; declared graph labels counted separately. |
| Revision 4 input correction | 1 | 45.035 s | Four extra strings: actual avoidable preparation rework. |
| Final independent content review | 1 | 27.516 s | Passed, zero unresolved findings. |
| Final independent graph review | 1 | 33.844 s | Passed, zero findings. |
| Final immutable plan / export / local verification | 0 | 26.517 / 62.845 / 2.040 s | Reviewed manuscript/catalog unchanged; four HTML pages, zero broken links. |

Other actual rechecks, refused calls and their wall times remain in the comparison rather than being omitted from a successful total. The first translation module invocation exited zero but did no work; it is explicitly a **no-op preparation error**, not successful translation. The next invocation used the actual `localization_cli.main()` entrypoint. No failed model call was replaced with a fabricated success.

## Why revisions and rechecks were necessary

The [final contract](operation.json) is revision 6. Original chained revisions and plans are inside `case-originals.tar.gz`.

1. Revision 1 fixed the operation, policies and public question before inference. Missing policy proof and unrecorded changes were refused.
2. Revision 2 adopted the reviewed/CI-tested translation acceptance fix (PR 263). Existing Korean work was rechecked with zero calls before translation.
3. Revision 3 adopted the profile snapshot fix (PR 265). Parallel main had also merged PR 257. Adoption stopped before model calls until the **actual merged main**, not merely the PR head, passed CI. Existing Korean and English work then passed current checks with zero fresh calls.
4. Revision 4 attempted to remove a standalone sample's missing next-document link. The generator's legacy default footer still targeted `overview.md`, so independent-review preflight refused again. The earlier premature resolution remains in history and is explicitly corrected.
5. Revision 5 used the supported local Markdown template override to omit that standalone next-task footer. It did not invent a dummy manuscript, edit generated HTML or weaken the checker. Current checks then passed and both independent reviews ran fresh.
6. Revision 6 bound exact final report hashes and resolved the confirmed blockers. It prepared a plan and exported without regenerating the reviewed manuscript merely to update its timestamp.

The six requested scenarios are covered on actual entrypoints by `tests/test_publication_operation.py`: identical resume, missing prior policy, live input edit with old output preservation, selected integration-ref change while unrelated refs remain usable, explicit user-scope revision, and a deferred nonblocking follow-up that does not silently expand scope. Those controlled tests use explicit transport doubles. Native observations above separately cover resume, preconditions, mutation refusal, actual parallel integration, reasoned revisions and a deferred metadata glossary warning. They are not six fresh model experiments.

## Verification and measurement limits

- Independent native generator reviews 19-core, 21-translation and 22-profiles reported no further findings after corrections. Earlier findings, failed preparation and stopped partial tests remain archived. An exhausted automatic review service is not counted as a review.
- PR CI: [41904992053](https://github.com/TTolsun/camera-hal-sdd-generator/actions/runs/41904992053) passed Linux 2,844 / Windows 2,843 + 1 skipped per Python version; [41909433412](https://github.com/TTolsun/camera-hal-sdd-generator/actions/runs/41909433412) passed Linux 2,868 / Windows 2,867 + 1 skipped; [41914257959](https://github.com/TTolsun/camera-hal-sdd-generator/actions/runs/41914257959) passed Linux 2,887 / Windows 2,886 + 1 skipped. Each matrix used Python 3.11 and 3.14.
- [Actual merged-main CI 41915848219](https://github.com/TTolsun/camera-hal-sdd-generator/actions/runs/41915848219) passed all four environments at runtime commit `1365ccb`. Original metadata is in `profiles-merged-ci.json`.
- Final site build ID: `55d3c07a23b9a1870a24cd47bdbe87f51d9b4674cf8d732acfabddb273079b20`, 88 manifest-owned outputs plus its manifest. [Browser checks](browser-verification.json) confirmed bilingual rendering, diagram enlargement/search, source disclosure, language navigation and document search. Human content/translation approval remains pending.
- Official upstream and its public mirror were checked at `be7e83e91348250c015aad6d6f59f1468555bae8`. Compared with fixed source 293, changes are version, libipa AGC and Python bindings; `request.cpp` is unchanged. The mirror was already synchronized (`Everything up-to-date`), not newly advanced by this task. This is a bounded source-impact check, not latest-source runtime or hardware validation.
- Blocking defects and evidence gaps were repaired before export. The nonblocking metadata `LLM` glossary warning remains explicitly deferred. Full-book visual/reader audits (#215/#163), future policy/source changes, human review and internal HAL validation still require their own work.
- The observed prevention is early refusal before spending calls and preservation of already completed work through explicit replanning. Checkpoint reuse itself belongs to #214/#242. There is **no same-input old-generator native baseline**, so general call/time savings are not established. The historical 79 fresh reviews were necessary after a policy change; the evidence does not show that all 79 were preventable.
- Invocation wall time is separate from per-call seconds. Parent preparation and nested translation journals overlap; summing them does not measure elapsed time. Human investigation, CI/network waiting outside these invocations and a causal critical path were not measured.
- Initial resume changed `generated_at` and `checkpoint_units` metadata. The initial full raw manuscript was not saved then; the first hash was later matched exactly by a clearly labeled reconstruction of those two fields. This does not establish original byte identity or count as fresh CLI generation. See [resume comparison](resume-comparison.json).

## Original evidence

`case-originals.tar.gz` preserves exact input snapshots, original failed/successful invocations, six chained revisions, all plans/journals/checkpoints, native receipts and requests/responses, final manuscripts/catalog, source facts/window and independent reports. `generator-review-originals.tar.gz` preserves native code reviews and intermediate local logs, including stopped or failed runs. [Evidence manifest](evidence-manifest.json) records archive/file hashes. [Scripts](scripts/) show the actual orchestration and collection; the committed seed helper alone is not the completed experiment.

Deployment success and live checks are recorded separately in the public PR and final generator record after this commit is merged. This evidence package does not claim deployment merely because the local site passed.
