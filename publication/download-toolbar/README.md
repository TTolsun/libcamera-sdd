# Whole-document download button

The 20 Korean and English reader pages now offer an icon button with a native format picker. The PDF opens the whole-document print view and the Markdown option downloads the complete edition.

The previous release supplied the reviewed material and source pin. Rebuild from the public inputs with the [recorded generator commit](release.json) and the package versions in the site manifest.

```sh
python publication/download-toolbar/reproduce.py --generator /path/to/camera-hal-sdd-generator --out /path/to/new-directory
```
