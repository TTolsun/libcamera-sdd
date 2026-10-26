# Sidebar resizing and reader glossary update

The generator provides pointer and keyboard resizing of the desktop navigation, automatic text wrapping, persisted widths across pages and editions, and double-click reset. Mobile navigation and print retain their existing layout. See browser-verification.json and the three Chrome screenshots.

The official upstream and its mirror still point to `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`. The existing structural facts and all original manuscripts are unchanged. The existing request, buffer and IPA categories contained unexplained uses of metadata and frame buffer; glossary.yaml and source-review.json document two source-backed editorial definitions and their affected pages. English values are editorial configuration, with human review pending. No model or CLI reproduction was performed for this update.

The site has 46 HTML pages, no broken links, verified output hashes and identical repeat builds. The older facts helper cannot pass against a tracked-source-only snapshot: 639 referenced generated-header locations are unavailable, and two newer excerpt-based prose sections have no class selectors. All 8,005 tracked-source citation positions were checked successfully. This is a reuse build, not a fresh Clang extraction; the unsuccessful helper result is retained in facts-helper-result.json.

Historical generation records and approvals remain intact under their existing paths. The new catalog is english.json. GitHub Pages deployment status and the live URL are checked separately after the publication PR merges. No internal HAL or device validation is established.
