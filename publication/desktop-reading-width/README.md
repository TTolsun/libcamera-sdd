# Desktop reading width

The public site uses the shared layout from [generator PR 371](https://github.com/TTolsun/camera-hal-sdd-generator/pull/371). At a 1600 px viewport the left menu and the article start 72 px farther left. The text column grows from 720 to 792 px. The page outline stays in its original position.

## Reproduce the site

1. Restore the public inputs for [the preceding UVC release](../uvc-configuration-provenance/README.md). Its public commit is `27e85026b553a48f19dcb96d10cc53a557c4ddfb`. Use generator merge `49e8139` and the same public libcamera revision, `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`.
2. Run `python -m sdd.localization_cli --config release.yaml --out english-release.json` in that release workspace. The stylesheet version changes the 32 Korean page hashes used by the English catalog. All 2,064 translations and their source contexts match the preceding catalog.
3. Decompress `integrated-visual-reviews.json.gz` to `config/integrated-visual-reviews.json`. Check its uncompressed SHA-256 against the `item_visual_reviews` input in the published site manifest.
4. Run `sdd --config release.yaml export-site`, followed by `sdd --config release.yaml verify-site`.

## Verification

The comparison covered all 166 HTML files. The only HTML differences were version parameters on local stylesheet and script references. The 334 Mermaid sources, 72 Markdown files, and 22 PDFs were byte-identical. Browser measurements cover the 20 Korean and English reader pages at desktop and mobile widths.

The visual audit hashes complete linked HTML files, including asset URLs. As a result, 182 of the 210 item fingerprints changed. The [layout review and item bindings](layout-review.json) record both fingerprints for every item, the prior ledger hash, the independent Codex CLI assessment, and the browser measurements. The original item judgments, source windows, figures, and human review states are preserved.
