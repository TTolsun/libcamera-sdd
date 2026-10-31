Publication note: issue #211 official cam validation developer SDD

Scope
- Rewrites the official-cam-validation page as a developer SDD: conclusion, callback → event loop → processing, then reproduction prerequisites.
- Raw PID/JSON fields and repeated scope notices move to collapsed evidence. Each scoped section keeps its link to that evidence and to the original manuscripts and evidence.
- No new camera or kernel trial in this documentation update.
- Source and original runtime trial remain at 293d751a814e0d4c34e85ad457ccd9d5eefd1a61. Original runtime records stay in publication/issue211/ and the generator issue211 record.
- The public previous release is preserved in previous-release/.

Automatic checks
- Native generation and translation: claude-haiku-5-5 with --effort high --setting-sources project,local.
- Independent source and bilingual reading review: codex gpt-6.1-terra with -c model_reasoning_effort="high".
- These are automatic checks. They are not a human reader study and not manuscript approval. No approval or reader-study pass is claimed.

Package contents
- config/
- manuscripts/
- profiles/
- reviews/
- evidence-index.json
- cli-evidence.zip
- previous-release/

Unvalidated
- Hardware DMA, camera hardware, product apps, and internal HAL remain unvalidated.

Deployment
- Deployment is prepared before merge. The final deployment proof will be recorded in the publication PR, not claimed here.
