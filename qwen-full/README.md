# Complete local Qwen trial

Generator PR89 and its merged commit are recorded in summary.json. The pinned source is public libcamera 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f. Existing 300-TU structural facts were reused; source excerpts were recollected. No internal HAL data is included.

The HTTP repair trial covers 13 sections / 19 manuscripts / 10 model-authored explanation documents / 56 topics / 387 statements. evaluation.json records generation, exact real-response provenance, audit, translation, 42-page site verification and repeat-build identity. The final repair retained all 56 topics and made no new prose-generation calls; 13 typography-dependent display strings were translated. publishable=false is the automatic trial boundary, not a human approval record.

model-calls.zip contains exact archived requests/responses/receipts, including failed retries. prior-trials records failed/intermediate reports and original digests; local workspace paths in those reports are redacted explicitly. The isolated rejected v35 call folders are also archived. Facts path redactions are described separately. Human-authored response bundles or replacement manuscripts were not used.

publication/ contains the final 20 manuscripts and catalog, retaining main's previously tested Hermes-generated IPA validation page. publication.json records the final 44-page build, 1,731 translated strings, zero missing translations and zero broken links. This composition is distinct from the 13-section HTTP trial; its existing CLI proof remains under ../cli-runners/libcamera/.

Reader evaluation records distinguish browser interaction from HTTP reading and actual device execution. Browser screenshots show the generator-owned sidebar hierarchy. Human approval, internal HAL/model validation, device tests and a request/time/thread runtime logging template remain outside this test.

Rebuild with generator b74ae8ef3a7c6e0dc446047a0752a6873c2610f5, its libcamera sections/scenarios/visuals/glossary/style, publication/manuscripts, publication/facts.json and publication/english.json. Point an isolated config at the pinned public source and these artifacts, run export-site, verify-site and repeat export-site; do not re-author the Markdown or patch generated HTML. The model itself is not deterministic; reuse only responses that pass current validation.

SHA256.json covers this evidence package. It detects changed bytes and does not establish human approval or semantic correctness.
