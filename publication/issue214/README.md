# Issue214 public validation and publication evidence

Only public libcamera inputs are included. Original runtime and structural facts are at 293; the upstream mirror advances to 0.8.0 with identical referenced source files. No new hardware or internal HAL trial is claimed.

- `run.json`, `generator-merge.json`: source/generator/build identities and actual CI.
- `profiles`, `config`, `facts293.json.gz`, `manuscripts`, `english.json`: exact release inputs. 26 other manuscripts retain public PR71 bytes.
- `consistency-review.json`: final current-policy native independent review. Unresolved findings stay visible and human approval stays pending.
- `cli-evidence.zip`, `archive-index.json`, `native-call-verification.json`: original native requests/responses/stdout/receipts/checkpoints/progress, including rejected/old-policy attempts. Nothing in prior-attempts is relabelled as a current approval.
- `per-item-visualization.json`, `window-reviews`, `reviewed-source-windows.json`:63 individual questions and supplied literal source windows, omission reasons and deferred editorial findings. Not completion of #215 or #163.
- `benchmark`: fixed PR69 before/after wall clock, separate cProfile and byte-identical 5-contract/461-claim comparison. The frozen historical validator experiment is not current-policy approval.
- `two-exports.json`, `site-manifest.json`: two normal exports with identical complete manifests/outputs. Failed/withdrawn earlier-policy exports stay in prior-attempts.
- `length-policy-correction.json`: no implicit prose/artifact/growth caps. Size is measured; explicit project limits remain optional. Source/ownership/duplicate checks remain enforced.

## Reproduction boundaries

Use the generator merge in generator-merge.json and its locked dependencies. These profiles freeze the actual original local paths and historical authentication identities; they are not global defaults. To restore elsewhere, copy profiles to a work root, config to config/, manuscripts to run/manuscripts/, decompress facts to run/facts/facts.json, put english.json in run/english.json, and extract cli-evidence.zip at that work root. Relocate local input/output/style/template/prompt/Mermaid paths consistently in every profile. Preserve historical agent.command values used only to authenticate existing figures; fresh execution uses generation.yaml/translation-agent.yaml and independent-review.yaml with the exact selected CLI/model/args. Retain original report/receipt bytes, source commit and human-review status. Report declarations must point to those exact reports. Source checkout must be 293. The historical compile database path records the original extraction; a fresh extraction/build needs an actual newly prepared compilation database and is not claimed by re-export.

Path relocation changes the manifest configuration hash. Do not claim a relocated run has the original build_id; verify its own full manifest and output digests. Never replace a missing/failed selected CLI with another CLI/API/stored response/manual manuscript and call it a new successful generation/review.

Pages and live artifact proof is obtained after merge and linked in the publication PR/issue214. No public recurring schedule is installed.
