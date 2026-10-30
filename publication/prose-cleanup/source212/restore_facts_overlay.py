"""Restore a derived public facts snapshot; never run extraction or a model."""
from pathlib import Path
import argparse,hashlib,json,tempfile
from sdd.facts.model import KnowledgeModel

ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--base',type=Path,required=True)
ap.add_argument('--overlay',type=Path,required=True)
ap.add_argument('--out',type=Path,required=True)
args=ap.parse_args();patch=json.loads(args.overlay.read_bytes())
assert hashlib.sha256(args.base.read_bytes()).hexdigest()==patch['base_sha256'],'Wrong public base facts'
target=args.out.resolve()
if target.exists():raise ValueError('Output already exists; preserve it and choose a new path')
model=KnowledgeModel.load(args.base)
assert model.meta['source_commit']==patch['source_commit']
for key in patch['remove_evidence']:model.evidence.pop(key)
model.evidence.update(patch['replace_evidence'])
target.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='.facts-restore-',dir=target.parent) as folder:
    temporary=Path(folder)/'facts.json';model.save(temporary);raw=temporary.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==patch['derived_sha256'],'Derived facts hash mismatch'
    with target.open('xb') as stream:stream.write(raw)
print('Restored hash-verified public facts; new extraction/model calls: 0')
