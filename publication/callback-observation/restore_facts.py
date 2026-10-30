"""Restore the exact newly extracted public snapshot; this is not a new extraction."""
from pathlib import Path
import argparse,hashlib,json,zipfile
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
root=Path(__file__).resolve().parent
record=json.loads((root/'structural-facts.json').read_bytes())
archive=root/'structural-facts.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest()==record['archive_sha256']
with zipfile.ZipFile(archive) as z:
    raw=z.read('facts.json')
assert hashlib.sha256(raw).hexdigest()==record['facts_sha256']
assert json.loads(raw)['meta']['source_commit']==record['source_commit']
a.out.parent.mkdir(parents=True,exist_ok=True)
with a.out.open('xb') as f:f.write(raw)
print('Restored exact public source293 extraction; no model or extraction was invoked.')
