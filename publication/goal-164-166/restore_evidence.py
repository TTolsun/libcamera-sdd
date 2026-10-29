"""Restore original public evidence bytes; never launch a model or execute records."""
from pathlib import Path
import argparse,hashlib,json,zipfile

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--out',type=Path,required=True)
ap.add_argument('--prefix',default='')
args=ap.parse_args();root=Path(__file__).resolve().parent
index=json.loads((root/'archive-index.json').read_text(encoding='utf-8'))
archive=root/'execution-evidence.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest()==index['archive_sha256'],'Archive hash mismatch'
out=args.out.resolve();count=0
with zipfile.ZipFile(archive) as z:
 assert json.loads(z.read('index.json'))['files']==index['files']
 for name,record in index['files'].items():
  if not name.startswith(args.prefix):continue
  target=(out/name).resolve()
  if not target.is_relative_to(out):raise ValueError('Unsafe archive path')
  data=z.read('blobs/'+record['sha256'])
  assert len(data)==record['bytes'] and hashlib.sha256(data).hexdigest()==record['sha256']
  target.parent.mkdir(parents=True,exist_ok=True)
  with target.open('xb') as f:f.write(data)
  count+=1
print(f'Restored {count} original files; new model calls: 0')
