"""Restore evidence bytes only. This does not invoke a model or verify fresh generation."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import zipfile

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('archive', type=Path)
ap.add_argument('--out', type=Path)
ap.add_argument('--prefix', default='')
args = ap.parse_args()
if args.out:
    args.out = args.out.resolve()
    if args.out.exists():
        raise ValueError('Restoration needs a new directory; existing files are never overwritten')
    args.out.mkdir(parents=True)
verified, restored = {}, 0
with zipfile.ZipFile(args.archive) as z:
    index = json.loads(z.read('index.json'))
    for record in index['files']:
        name = record['path']
        rel = PurePosixPath(name)
        if rel.is_absolute() or '..' in rel.parts or ':' in name or '\\' in name:
            raise ValueError('Unsafe evidence path')
        sha = record['sha256']
        if not re.fullmatch('[0-9a-f]{64}', sha):
            raise ValueError('Invalid blob identity')
        if sha not in verified:
            data = z.read('blobs/' + sha)
            if hashlib.sha256(data).hexdigest() != sha:
                raise ValueError('Evidence blob checksum mismatch')
            verified[sha] = len(data)
        if verified[sha] != record['bytes']:
            raise ValueError('Evidence size mismatch')
        if args.out and name.startswith(args.prefix):
            destination = args.out.joinpath(*rel.parts)
            if not destination.resolve().is_relative_to(args.out):
                raise ValueError('Evidence path escapes output')
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(z.read('blobs/' + sha))
            restored += 1
print(json.dumps(dict(verified_files=len(index['files']), verified_blobs=len(verified), restored_files=restored,
                      new_model_calls=0, fresh_generation_proven_by_restoration=False)))
