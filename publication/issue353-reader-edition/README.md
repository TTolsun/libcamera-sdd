# Published libcamera reader edition

This release collects ten canonical reader pages in Korean and ten in English. The earlier URLs open their new destinations or preserved details. See `release.json` for the pinned upstream commit and publication checks, `migration-ledger.json` for the earlier review-item locations, and `reader-history.json` for three actual historical source comparisons. `portable-native-review.json` records item fingerprints, published source locations, and independent CLI receipt digests. Human review is pending.

## Reproduce the published artifact

1. Check out this release in the public SDD repository and fetch the earlier public commit recorded in `release.json`.
2. Check out the generator at the recorded merge commit. Install the Python dependency versions listed in `docs/site-manifest.json`, plus the generator's runtime prerequisites.
3. Run the reproducibility check from this repository with a new output directory.

```sh
python publication/issue353-reader-edition/reproduce.py --generator /path/to/camera-hal-sdd-generator --out /path/to/reproduced-reader-edition
```

The script checks each file against the earlier Git manifest, applies the exact YAML bytes preserved in the portable reader profile with the same generator, and compares the output with the current release manifest. It also revalidates the published independent review record against those outputs and resolved evidence windows. It does not rerun the independent Codex calls or execute libcamera. The original publication used the generator's normal CLI export and verification path with source-bound generation and review evidence. Review counts do not imply human approval or physical-device verification.
