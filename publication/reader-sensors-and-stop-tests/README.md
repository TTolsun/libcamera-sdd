# Raspberry Pi sensor support and target-board stop tests

Both reader languages describe the Raspberry Pi helper registration for the IMX585 and IMX676, the 8-line margin and the source of the SHR0 condition. A diagram shows how the selected margin limits requested exposure. The target-board stop checklist and both Developer diagrams carry forward from the earlier independent publication.

The archived inputs include the editable English catalog, named source facts, the reader profile, source selectors, the shared graph and the two regenerated manuscripts. SHA-256 values in the release record describe uncompressed input bytes. The impact and comparison records bind the isolated sensor experiment independently from the ForVendor wording and figure. The experiment pins #132; the integrated release keeps the direct PDFs from #133.

In the generator checkout, install the pinned dependencies and the Playwright Chromium shell. Run the commands below after checking out the generator and official libcamera commits in `release.json`.

```sh
uv sync --frozen --extra pdf
uv run python -m playwright install chromium --only-shell
uv run python /path/to/public-repo/publication/reader-sensors-and-stop-tests/prepare-workspace.py --generator . --source /path/to/libcamera --out /path/to/workspace
uv run sdd --config /path/to/workspace/final-review.yaml audit-consistency
uv run sdd --config /path/to/workspace/release.yaml export-site --out /path/to/site
```

A fresh native audit records new receipt metadata, and a different checkout path can change the aggregate build ID. The published repeat comparison records the original site and PDF hashes.
