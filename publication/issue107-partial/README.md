# Partial regeneration for issue 107

Four pages were rewritten with the improved generator: `vendor-overview` and the new `team-overview` came from Haiku 5.5 subagents (effort high) through the response-bundle path, and `vendor-assurance` and the new `onboarding` came from the Hermes CLI with the `qwen3.5:9b-ctx64k` alias and high reasoning. The other design pages are the previous public manuscripts, revalidated against the current facts. The site therefore mixes manuscripts from two generator versions.

Nine design pages could not be regenerated: `vendor-integration`, `overview`, `pipeline-handler`, `ipa`, `ipu3-lsc-flow`, `rkisp1-dewarp`, `camera-model`, `request-lifecycle` and `ipa-module-validation`. A single malformed item from the 9B model aborts its whole section, and a full regeneration was not attempted. The generator repository's evaluation record explains the causes, measured times and the before/after reader judgments: `docs/inhouse/records/reader-evaluation-107.md`.

The English catalog now has 1,871 strings. The strings added in this run were translated by Haiku 5.5 subagents and accepted only after the generator's translation checks. Known quality limits remain in the new pages (for example an English article in an execution-check sentence of `onboarding`).

The site has 50 verified HTML pages, no broken links and identical repeat builds. Human review is still pending, and neither internal HAL validation nor device validation was performed.

Evidence in this directory: `calls/` (per-call receipts of the four pages), `response-bundles/` (requests and responses of the Haiku pages), `manuscripts/`, `timing-final-runs.jsonl`, `english.json`, `sections.yaml`, `visuals.yaml` and `verification.json`.
