# Request diagnosis navigation

The Korean and English troubleshooting pages now name the two symptoms in the second section: request submission failure and a missing completion notification. The original anchor `failure-location` remains valid. Three first-time automated readers completed their tasks on the previous public build, but the developer followed the generic failure heading while investigating stream configuration and had to backtrack. Three fresh readers repeated the tasks on the candidate. The developer found the configuration branch without the earlier detour. These runs do not measure human comprehension or device behavior.

The [generator change and trial record](https://github.com/TTolsun/camera-hal-sdd-generator/pull/368) also document a new manuscript written by the Luna CLI. That isolated trial did not supply replacement prose for the public pages.

## Rebuild

1. Prepare a workspace with the preceding release's `publication/reader-sensors-and-stop-tests/prepare-workspace.py` at the source and generator revisions specified by that release. Its README lists dependencies and the commands.
2. In the prepared workspace replace `config/reader-edition-integrated.yaml` with the adjacent `reader-edition.yaml`. Merge the six entries in `visual-review-update.json` into the existing `items` mapping in `config/integrated-visual-reviews.json`. Preserve the other entries and manuscript reviews. These overrides apply to the pinned public inputs.
3. With the generator revision identified in `release.json`, run the native consistency audit using the prepared `final-review.yaml`. Use `release.yaml` for `export-site` and `verify-site`. New audit receipts and different absolute workspace paths can change the build ID.

`visual-decisions.json` records the independent Terra High review of the six items whose headings or hierarchy fingerprints changed. The reviewers saw the source-bound diagrams, the connected source excerpts and the supplementary public libcamera implementation files. Human review remains pending.
