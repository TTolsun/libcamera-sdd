from pathlib import Path
import json,shutil
from sdd.runtime_evidence import require_success,sha256
r=Path(__file__).resolve().parent.parent;w=r/'build/issue211-virtual';repo=r/'build/libcamera-sdd-issue211';p=repo/'publication/issue211-virtual';extra=p/'integration'
for name in ['package-current-final','split-integration-evidence']:
 source=w/'executions'/name;require_success(source);shutil.copytree(source,extra/'packaging-executions'/name)
for name in ['verify-package-issue211-virtual.py','verify-public-evidence-archives.py','finalize-evidence-package-index.py']:
 shutil.copy2(r/'build'/name,extra/'operators'/name)
files={item.relative_to(p).as_posix():sha256(item) for item in sorted(p.rglob('*')) if item.is_file() and item!=p/'evidence-index.json'}
run=json.loads((p/'run.json').read_bytes());manifest=json.loads((repo/'docs/site-manifest.json').read_bytes());assert run['manifest_sha256']==sha256(repo/'docs/site-manifest.json')
(p/'evidence-index.json').write_text(json.dumps(dict(schema=1,files=files,site_manifest=run['manifest_sha256'],site_outputs=manifest['outputs']),indent=2)+'\n',encoding='utf-8')
assert all((repo/path).stat().st_size<100_000_000 for path in ['publication/issue211-virtual/'+key for key in files])
print('Final package indexed',len(files),'files; every file below GitHub limit')
