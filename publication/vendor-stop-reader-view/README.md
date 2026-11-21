# Vendor capture and stop tests

ForVendor shows how to compare normal capture with a run stopped while requests are pending. Its diagram uses eight nodes from the stop-notification recipe, including four nodes also used in the Developer view. Both language editions use the same graph definition. The approved English paragraph retains its link to the stop and disconnect explanation. The source commit is recorded in release.json.

The publication used the normal site export, native Codex CLI visual review, and the PDF toolchain recorded in site-manifest.json. The full check covered 202 rendered items. It does not record a new physical-board test.

## Reproduce the published files

Check out this public release and the generator revision in release.json. Install the Python dependencies recorded in the manifest, including the PDF extras and matching Playwright Chromium headless shell. Run the following from this release directory with a new output directory.

```sh
python reproduce.py --generator /path/to/camera-hal-sdd-generator --out /path/to/new-output
```

The script reconstructs 672 reader and supporting artifacts from the pinned historical Korean seed, the editable compressed English catalog, the reader profile, and the source-bound figure recipe. It copies the sealed audit and manifest from this release, then checks the complete artifact inventory and hashes. The original independent verdicts for the changed items are summarized in review-results.json. The replay does not run a new model review.
