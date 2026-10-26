# Public libcamera publication delta

Generator `1eefc75fbe1eee588c3ac76255aa6cd05f16b9dd`; source `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`. Copy the immutable 20 manuscripts from `../../qwen-full/publication/manuscripts`, then override only the three files in `manuscripts/`. The catalog here is the final catalog. Existing structural facts remain under `../../qwen-full/publication/facts.json`; recollect public source excerpts at the source commit above when rebuilding. Use the exact generator commit above with the frozen `sections.yaml` and `visuals.yaml` supplied here. These inputs select the historical public scope, three whole-paragraph deletions on two pages, and the six-part framebuffer allocator page. This release does not claim that the latest default Team/onboarding documents were generated. The two selected HTTP pages retain original generation timestamps and authors. Maintenance time and whole-object hashes are in recomposition.json; this is zero-call selection, not a new CLI generation trial. Only framebuffer-allocator.md is newly generated through Hermes. Exact call archives are under `../../cli-runners/libcamera/framebuffer-allocator/`; requests, responses, receipts, stdout and existing common stderr retain their original bytes. Failed attempts are summaries/hashes only; raw failures remain local. Model supported=true is not semantic approval; consult the selected allocator review and its observations. Prepared site checks are not Pages deployment success. Human approval is pending; internal HAL/device validation was not performed.

## Rendering identity versus new execution

New allocator generation and new display translations use separately selected Hermes `qwen3.5:9b-ctx64k` with `--provider custom --reasoning high`; the verification records the actual configured arguments. API-only settings such as agent.think and agent.num_ctx are not forwarded as CLI options; Hermes reasoning is selected explicitly by --reasoning high. Offline export keeps the original vendor-assurance HTTP visual identity so its saved visual pin remains verifiable. This rendering-only identity is not a request to the old model and does not bypass model-change invalidation for a new CLI generation trial. The measured build blocks model/CLI chat and records zero model calls. A generic render-only configuration is shown below; raw local configs and absolute paths are not published.

Copy the baseline manuscripts and the three overrides into a separate render workspace, use the catalog here, and pin the public source checkout to the source commit above. Point the render configuration to these exact snapshots (paths below are relative to that workspace), preserving the original-source evidence bindings. Do not replace them with the generator checkout's newer default sections or visual definitions.

```yaml
paths:
  sections_file: publication/issue97/sections.yaml
visuals:
  file: publication/issue97/visuals.yaml
agent:
  kind: ollama
  model: qwen3.5:9b
  base_url: http://localhost:11434
  allow_direct_api: false
```

The selected generation uses the exact native Hermes profile archived with the CLI evidence. Its custom loopback provider requests context 65536, temperature 0.1 and presence penalty 0.0, while CLI model/provider/reasoning remain ctx64k/custom/high. The archived driver supplies HERMES_HOME only to a copied child environment; its audit is matched to every receipt by prompt/stdout hashes and multiplicity. Private profile directories, bootstrap logs and environment files are excluded. runtime-investigation.json documents installed-code AST analysis; it is not a wire capture or model-weight attestation.

[Final English semantic review](translation-review.json) binds this exact catalog, the actual new/retained string counts and the complete selected translation-run set. Each translation run has separate native profile/audit evidence under `../../cli-runners/libcamera/framebuffer-allocator/translation-runtime/`. A selection marked `metadata_created_after_execution: true` was derived after the audited execution; it is not evidence of a pre-run selection record. Its profile/audit/receipt bindings remain checked, and human approval stays pending.

## Collect pinned excerpts and render without model calls

Copy the immutable baseline structural facts into `render/facts/facts.json` first. Configure `render/sdd.yaml` to read that local facts file, the pinned public source checkout, the frozen snapshots above, the copied manuscripts and this final English catalog. The following refreshes public source excerpts for the selected questions, including export-return-code; it performs no fresh Clang parse and no model generation. Raw local facts and configs may contain local paths and are deliberately not published. Do not patch generated HTML.

Save this as `collect_render_evidence.py` and run it from the render workspace parent:

```python
from pathlib import Path
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.evidence import collect

cfg = load(Path("render/sdd.yaml"))
assert cfg.agent.kind == "ollama" and cfg.agent.allow_direct_api is False
model = KnowledgeModel.load(cfg.facts_path)
assert model.meta["source_commit"] == "2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f"
collect(cfg, model)
model.save(cfg.facts_path)
```

```sh
python collect_render_evidence.py
sdd --config render/sdd.yaml export-site --out render/build/site
```

The rendering identity above rejects direct model API calls; export-site renders and validates the saved manuscripts. New allocator generation and translation are the separately archived Hermes ctx64k/high executions, not this offline rendering step.

[Legacy policy regression](legacy-policy-regression.json) verifies 11 existing active LLM pages, including the two selected pages, with zero model calls. Its scope explicitly excludes the new allocator page.
