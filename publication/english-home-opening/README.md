# English opening sentence update

The earlier release and its review remain in [the reader edition record](../issue353-reader-edition/README.md). This follow-up updates the English opening sentence and reuses the verified input and canonical baseline. The new independent bilingual review is in english-intro-review.json.

Check out this public release and its recorded generator commit, then install the dependencies listed in the site manifest. Run the following command with a new output directory. It verifies the original projection inputs, the preceding public manifest, and all artifacts in this release, including the published review.

```sh
python publication/english-home-opening/reproduce.py --generator /path/to/camera-hal-sdd-generator --out /path/to/reproduced-site
```
