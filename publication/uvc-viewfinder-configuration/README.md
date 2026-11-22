# Following a single Viewfinder configuration through UVC

The developer chapter traces a 640×480 request across validation, device format negotiation and the application's active stream. The example uses public libcamera source at `adfa719f`. The requested value is illustrative. The chapter contains no target-board measurements.

The [generator change and reading trial](https://github.com/TTolsun/camera-hal-sdd-generator/pull/369) record where the baseline reader lost the UVC path and how a fresh reader answered the same question using only the generated chapter and its source excerpts.

## Reproduce the public inputs

1. Prepare the preceding public workspace. Follow the instructions in [role-reading](../role-reading/README.md) and its referenced base preparation script using the source revision in `release.json`.
2. For each whole-file input listed in `inputs.json`, copy the adjacent file to the specified workspace destination. Decompress files ending in `.gz` first. The recorded SHA-256 hashes describe uncompressed bytes.
3. For each JSON update, remove any keys named in `remove_before_merge` from their respective mappings, then merge the supplied entries into the named mappings in the corresponding workspace file. Preserve the remaining evidence and visual reviews. Set `publication.operation_id` in `release.yaml` to `formal-libcamera-adfa-uvc-stream-configuration`.
4. Using the merged generator identified by `release.json`, run the native consistency audit with the workspace's `final-review.yaml`. Run `export-site` and `verify-site` with `release.yaml`. New CLI receipts or a different workspace path can change the aggregate build ID.

The public manuscript, translation and independent source check used the Terra High profile. A separate Luna High CLI run exercised a more explicit writing prompt. Its automated checks passed and its independent review requested clarification. The [trial record](https://github.com/TTolsun/camera-hal-sdd-generator/blob/5e7fb50bd5d4ed2943ba9d2cfc8ed4bc28322bb9/examples/libcamera/validation/role-reading/stream-configuration.md) records both verdicts. Human review and measurements on a physical USB camera remain open.
