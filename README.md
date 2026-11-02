# libcamera-sdd

This repository publishes public libcamera source-history records and the design documents (SDD) generated from them. The generator tool is in the separate repository TTolsun/camera-hal-sdd-generator.

## Contents
- publication/issue211/ and publication/issue211-reader/: original records, unchanged by the latest update.
- publication/issue211-virtual/: virtual-principle update with config, manuscripts, profiles, reviews, native-call-verification.json, evidence-index.json, and an indexed cli-evidence.zip.
- Previous root README, run, and receipts: kept in the previous-release directory.

## Public pages
- Korean: https://ttolsun.github.io/libcamera-sdd/official-cam-validation.html
- English: https://ttolsun.github.io/libcamera-sdd/en/official-cam-validation.html

## Scope
- Baseline: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61. Upstream recorded separately as df8e348d64b4932a0676256ed24f0da3ee9438bc, not identical to the baseline.
- Fresh writing and translation used Claude CLI claude-haiku-5-5. Independent grounding used Codex CLI gpt-6.1-terra. No alternate model, API, or manual prose fallback was used.
- Automatic checks are not human approval. Hardware, sensor, ISP, physical DMA, product-app, and internal-HAL validation are not established.
