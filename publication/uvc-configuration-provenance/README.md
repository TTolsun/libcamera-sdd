# Reading the UVC guide example and active stream values

The developer guide revisits the 640×480 Viewfinder example. It separates the code that the guide runs from the caller's decision to accept an adjusted configuration. It also explains which active stream fields come from format validation and which returned fields the UVC handler compares after applying a format.

## Reproduce the updated public inputs

1. Prepare the preceding release using [the UVC Viewfinder release instructions](../uvc-viewfinder-configuration/README.md). Keep the public libcamera revision in `release.json`.
2. Apply the whole-file inputs listed in the adjacent `inputs.json` to that workspace. Decompress files with the `.gz` suffix before comparing the uncompressed SHA-256.
3. For JSON updates, delete the keys listed in `remove_before_merge` from the corresponding mappings and merge the updated entries. Set `publication.operation_id` in `release.yaml` to `formal-libcamera-adfa-uvc-evidence-followup`.
4. Use the generator revision in `release.json`. Run the native consistency audit with `final-review.yaml`, then run `export-site` and `verify-site` with `release.yaml`. A fresh audit receipt or a different workspace path can change the recorded build ID.

The public manuscript uses the project's Terra High publishing profile. The [generator PR](https://github.com/TTolsun/camera-hal-sdd-generator/pull/370) documents the separate fresh Luna CLI writing trial and its independent source review. The configuration example describes the public source path. The trial contains no measurements on a target board.

A fresh automated reader used the Korean ForDeveloper prose and figure without consulting source excerpts. The reader distinguished the printed example from the caller's acceptance policy and identified both the validation-time layout values and the size/FourCC comparison after applying the device format. The earlier public reader had been unable to recover either distinction from the prose and figure alone.
