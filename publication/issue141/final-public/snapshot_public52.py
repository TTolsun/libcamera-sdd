"""Read an immutable public PR tree into a fresh own verification directory."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import tarfile
import re
import sys

w = Path('build/issue141').resolve()
repo = w/'public-sdd'
commit = sys.argv[1] if len(sys.argv)>1 else '33fcb28355a0bad043813eb006dc0e7ae745464e'
assert re.fullmatch(r'[0-9a-f]{40}', commit)
out = w/('public-release-'+commit[:8])
assert not out.exists()
archive = w/('public-release-'+commit[:8]+'.tar')
assert not archive.exists()
subprocess.run(['git','-C',str(repo),'archive','--format=tar','--output',str(archive),commit,
                'docs','run.json','generation-receipts.json','publication/goal-138-140'],check=True)
out.mkdir()
with tarfile.open(archive) as tf:
    members = tf.getmembers()
    for item in members:
        name = PurePosixPath(item.name)
        assert not name.is_absolute() and '..' not in name.parts
        assert ':' not in item.name and '\\' not in item.name
        assert item.isdir() or item.isfile()
        assert (out/item.name).resolve().is_relative_to(out)
    tf.extractall(out, members=members, filter='data')
package = out/'publication/goal-138-140'
manifest = json.loads((package/'package-manifest.json').read_bytes())
assert manifest['schema'] == 1
for name, expected in manifest['files'].items():
    rel = PurePosixPath(name)
    assert not rel.is_absolute() and '..' not in rel.parts and ':' not in name and '\\' not in name
    path = package/name
    assert path.resolve().is_relative_to(package.resolve()) and path.is_file()
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
actual = {p.relative_to(package).as_posix() for p in package.rglob('*') if p.is_file()}
assert actual == set(manifest['files']) | {'package-manifest.json'}
summary = dict(candidate_commit=commit,scope='Immutable public candidate snapshot and all declared package hashes; not merged/Pages/native CLI verification',
    snapshot=str(out),archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),
    package_files_verified=len(manifest['files']),extra_files=[],package_manifest_sha256=hashlib.sha256((package/'package-manifest.json').read_bytes()).hexdigest())
(w/('public52-package-snapshot-'+commit[:8]+'.json')).write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
