"""Restore exact public facts bytes, including evidence order; no model/extraction."""
from pathlib import Path
import argparse
import hashlib
import json
import tempfile

from sdd.facts.model import KnowledgeModel

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--base', type=Path, required=True)
parser.add_argument('--overlay', type=Path, default=Path(__file__).with_name('facts-overlay.json'))
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
patch = json.loads(args.overlay.read_bytes())
assert hashlib.sha256(args.base.read_bytes()).hexdigest() == patch['base_sha256'], 'Wrong public base facts'
target = args.out.resolve()
if target.exists():
    raise ValueError('Output already exists; preserve it and choose a new path')
model = KnowledgeModel.load(args.base)
assert model.meta['source_commit'] == patch['source_commit']
for key in patch['remove_evidence']:
    model.evidence.pop(key)
model.evidence.update(patch['replace_evidence'])
order = patch['evidence_order']
assert len(order) == len(set(order)) and set(order) == set(model.evidence), 'Invalid evidence order'
model.evidence = {key: model.evidence[key] for key in order}
target.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix='.facts-restore-', dir=target.parent) as temporary:
    path = Path(temporary) / 'facts.json'
    model.save(path)
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == patch['derived_sha256'], 'Derived facts hash mismatch'
    with target.open('xb') as stream:
        stream.write(raw)
print('Restored exact hash-verified public facts; new extraction/model calls: 0')
