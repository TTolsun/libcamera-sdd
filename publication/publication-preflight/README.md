# Translation source preflight and a complete pre-merge publication trial

This release adds a Korean/English answer and four-node source-bound diagram for the supplied-fence condition in `Request::addBuffer()`. The earlier issue241 sample explicitly excluded this condition. The new document explains that, after earlier rejection checks and buffer linking, `fence && fence->isValid()` controls the call to `setFence(std::move(fence))`. Full failure ownership, hardware behavior and whole-handbook validation are excluded.

- [Korean document](https://ttolsun.github.io/libcamera-sdd/validation/publication-preflight/camera-requests.html)
- [English document](https://ttolsun.github.io/libcamera-sdd/validation/publication-preflight/en/camera-requests.html)
- [Generator PR272](https://github.com/TTolsun/camera-hal-sdd-generator/pull/272)
- [Preregistered scope](https://github.com/TTolsun/camera-hal-sdd-generator/blob/825e261c8aaf25e924659b623b97e414fb68d899/docs/records/publication-preflight.md)

The root handbook and all earlier issue241 records remain unchanged by this release. This is a bounded public libcamera validation, not internal HAL or hardware verification.

## Implemented behavior

The existing generated-next-document check now runs during source rendering, including private translation preparation. The translation module validates the complete temporary Korean site's links, anchors and assets **before translation inference** and records `translation-preflight` in existing generation journals. A failed check retains the manuscript and catalog. `python -m sdd.localization_cli` now invokes its actual main entrypoint instead of returning a no-op success.

A private preview links to an explicitly pending notice until independent bilingual review exists. It does not synthesize a passed review or use an older report as current proof. Public export still requires existing source, manuscript, receipt, independent review and bilingual checks.

The pre-merge CI gate exercises the real generation, catalog preparation, separate translation profile, independent review profile, export and site verification entrypoints, then injects final-save failure after a distinct manifest is written. It checks exact prior site/manuscript/journal preservation. Only the CLI process is an explicit test double; it is not fresh inference or human approval. The existing full CI suite still runs after the early gate. Reuse decisions, failure taxonomy and CI deduplication policy are unchanged.

## Actual native execution and prevention evidence

[comparison.json](comparison.json) links original invocation times, file hashes, immutable contract revisions, native receipts and the generator merge time.

| Observation | Result |
|---|---|
| Canonical missing-next-target copy of the old public sample | Actual module CLI failed in `translation-preflight`; **0 model calls**; manuscript and catalog SHA-256 unchanged. |
| First archival fixture attempt | An extra paragraph separator made the footer noncanonical. Existing manuscript-integrity validation refused it. Original bad01 records remain; this is **not** credited as the intended missing-target check. The separate corrected bad02 fixture produced that check. |
| Healthy new reader sample | New generation/grounding, translation, separate content and diagram reviews, export and site verification all finished **before the generator PR merged**. |
| Input repair after healthy translation | **0** input-correction translation reruns; no footer-driven manuscript repair. |
| Model response repair | **1 necessary retry**: the first translation response repeated `{{0}}` in string12. Existing exact-placeholder validation rejected it. Original response and retry receipts remain. |
| Independent review | Content passed with zero unresolved findings; bilingual diagram passed with zero findings. Human review remains pending. |
| Post-merge adoption | Candidate and actual merged file trees matched. Contract revision3 explicitly adopted the merge; current checks and a real post-merge export/site verification passed without rewriting reviewed manuscript/catalog bytes or new model calls. |

There are **13 completed native document transport calls**: two generation/grounding, nine translation attempts (eight initial batches plus one response-validation retry), one independent content review and one independent graph review. The separate native generator code review reported zero findings and is not part of those13. Byte-equivalent checkpoint receipt copies count once. Declared English graph labels and the deterministic source-location label are distinguished from85 newly translated strings; the final catalog has86 strings and zero missing values.

Historical issue241 had an additional four-string translation batch after a footer-input correction. This trial demonstrates that the same class of missing target is rejected before translation. It does **not** show that the historical first eight legitimate translation calls were all avoidable, or that all work and model retries disappeared. The bad01 fixture correction itself cost preparation work and is retained honestly.

## Source, profiles and release basis

Source: `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`, `src/libcamera/request.cpp:475–505`, SHA-256 `c1c0b55f2925856df843fa155a14bb07eb616f52b6bde75cd3b0b5a4ab03b64a`. Existing public facts were preserved and the selected source window was refreshed through generation. This is not a new whole-source Clang extraction.

Official upstream and the public upstream mirror were both checked at `be7e83e91348250c015aad6d6f59f1468555bae8`. `request.cpp` is unchanged from the fixed source commit. The mirror was already synchronized; no new upstream advance is claimed.

Generation/translation use native Codex CLI, `gpt-6.1-terra`, `-c model_reasoning_effort="high"`, with the existing public profile. Independent review uses a separate explicit review.yaml with the same approved CLI/model/effort. Actual resolved arguments, original requests/responses and receipts are archived. No direct model API, alternate CLI, saved answer or manually authored source prose replaces a fresh successful inference. Global settings and internal profiles were not changed.

Pre-merge candidate: `825e261c8aaf25e924659b623b97e414fb68d899`. Generator merge: `3023f5c95eb6b1347a0597bb8bad46d96f30ea5e`. All seven preregistered native stages finished before that merge; current contract, plans and post-merge execution records preserve both bases.

[CI41940078637](https://github.com/TTolsun/camera-hal-sdd-generator/actions/runs/41940078637) passed the29-test early gate in all four environments, followed by Linux Python3.11/3.14 each **2,980 passed** and Windows Python3.11/3.14 each **2,979 passed,1 skipped**. Original metadata and full CI logs are included. Local failed and successful focused tests remain archived rather than being combined into a fictional all-pass run.

## Site checks and limits

Final build ID: `bae7adb7ba99cb951db2f6ad675dcd922f7c74cdccf411f9110c71becafa5d26`;88 manifest-owned outputs plus the manifest, four HTML pages and zero broken links. [Browser verification](browser-verification.json) confirmed bilingual rendering, language navigation, graph enlargement/fit and fence search with two matches. Screenshots were inspected in tool output; no separately saved screenshot file is claimed.

The known nonblocking metadata `LLM` glossary warning remains deferred. Human content/translation approval, the full handbook and internal HAL/hardware verification remain outside this trial.

Invocation wall times are separate from overlapping parent/child generation journals. This new question and current public profile differ from historical issue241. There is no same-input old-generator native timing baseline and no measured external-wait critical path; general speedup or guaranteed saved minutes are not established.

`native-originals.tar.gz` preserves bad01/bad02/good01 inputs, raw failed/successful invocations, manuscripts/catalog, all revisions/plans/journals/checkpoints and original native requests/responses/receipts. `generator-checks.tar.gz` preserves the native code review and earlier focused-test logs. [Scripts](scripts/) show preparation, exact CLI invocation, collection and packaging. Original absolute paths/hashes are retained: reproduction in another checkout needs explicit new paths and a new contract revision, not in-place rewriting of the archived input basis. [Evidence manifest](evidence-manifest.json) records packaged file hashes.

Pages success and live manifest/output verification are reported in the public PR after merge; local success alone is not deployment proof.
