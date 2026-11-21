# Direct PDF downloads

Each of the ten articles in each language has a downloadable PDF. Both editions also include a complete PDF. The generator renders the final print views with bundled assets and checks all diagrams before publication. PDF and Markdown links download files in place.

To reproduce this release, use the recorded generator commit, its locked PDF dependencies, matching Chromium and Korean/English system fonts. Byte-for-byte comparisons depend on the rendering environment.

```sh
uv sync --extra pdf
uv run --extra pdf python -m playwright install chromium --only-shell
uv run --extra pdf python /path/to/libcamera-sdd/publication/direct-pdf-downloads/reproduce.py --generator /path/to/camera-hal-sdd-generator --out /path/to/new-directory
```
