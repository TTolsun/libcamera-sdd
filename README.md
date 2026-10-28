# libcamera design documentation

Current update: [pipeline-handler, vendor-integration, ipu3-lsc-flow rewritten with the Claude Code CLI](publication/issue107-claude-part2/README.md) (Haiku 5.5, effort high). The site still mixes pages from several generator runs; see run.json authors.

Current update: [ipa-module-validation, rkisp1-dewarp rewritten with the Claude Code CLI](publication/issue107-claude-part1/README.md) (Haiku 5.5, effort high). The site still mixes pages from several generator runs; see run.json authors.

Current update: [partial regeneration for issue 107](publication/issue107-partial/README.md). Four pages (vendor overview, support and verification, the new team overview and onboarding) were rewritten with the improved generator; the other design pages are the previous manuscripts, so the site mixes two generator versions. 

Current UI update: restrained sidebar highlights and preserved menu scroll position across document navigation. [Interaction checks and screenshots](publication/sidebar-feedback/README.md). The [23-document reader-task classification](publication/sidebar-classification/README.md), including the IPA diagnostic and IPU3 LSC reference placement, is preserved.

[Public Korean and English documents](https://ttolsun.github.io/libcamera-sdd/) support dragging the desktop sidebar boundary to resize it. Titles wrap automatically, the width persists across pages and editions, and double-click resets it. Mouse feedback stays around the short grip; keyboard focus remains visible locally. Selected menu rows use one quiet rounded surface. The menu keeps its vertical scroll position across document and language navigation within the same tab. [Current update and checks](publication/sidebar-feedback/README.md) cover 46 HTML pages, no broken links, identical repeat builds and Chrome interaction checks. Metadata and frame buffer glossary entries now explain terms already used in the request, buffer and IPA categories.

Existing facts, manuscripts, original generation times, model labels and review states are preserved. This update makes no fresh extraction or CLI inference claim. GitHub Pages deployment is checked separately from the local build; its live status is available in repository deployments. Human approval, internal HAL validation and device validation are not established.

Historical evidence: [selected CLI runs](cli-runners/libcamera/verification.json), [prior publication](publication/issue97/README.md), [HTTP Qwen trial](qwen-full/README.md), [reader loop](qwen-reader-loop/README.md), and [current run record](run.json).
