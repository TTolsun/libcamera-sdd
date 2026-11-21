# ForDeveloper CameraManager wording

This release revises the English paragraph in the camera discovery section. The Korean source, linked code, and the previous download toolbar are preserved. The source translation delta and independent review are recorded alongside this file.

The exact editable English catalog is included in `english-release.json.gz`. Decompress it as `english-release.json` and point the normal generator’s `site.english_catalog` setting to it when building from the matching Korean source. The catalog contains the same source/page fingerprints as the preceding release.

To reproduce the site, check out this public release and the recorded generator commit with the manifest’s Python dependencies.

```sh
python publication/find-camera-wording/reproduce.py --generator /path/to/camera-hal-sdd-generator --out /path/to/reproduced-site
```
