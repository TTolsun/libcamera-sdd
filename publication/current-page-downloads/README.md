# Current-page and whole-document downloads

The 20 Korean and English reader pages each provide two download scopes. Current page prints or downloads just the selected article and its evidence. Whole document includes the ten reader pages in that language. The four whole-document files match the preceding release.

The previous release supplied the reviewed material and source pin. Rebuild from the public inputs with the [recorded generator commit](release.json) and the package versions in the site manifest.

```sh
python publication/current-page-downloads/reproduce.py --generator /path/to/camera-hal-sdd-generator --out /path/to/new-directory
```
