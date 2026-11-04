from pathlib import Path
import hashlib,json,subprocess,zipfile
from sdd.site_build import verify_site
from sdd.runtime_evidence import sha256
root=Path(__file__).resolve().parent.parent;repo=root/'build/libcamera-sdd-issue211';pkg=repo/'publication/issue211-virtual'
validated=verify_site(repo/'docs')
expected=json.loads((pkg/'evidence-index.json').read_text())
for rel,digest in expected['files'].items():
    if sha256(pkg/rel)!=digest:raise ValueError('Package file changed: '+rel)
with zipfile.ZipFile(pkg/'cli-evidence.zip') as archive:
    entries=json.loads((pkg/'archive-index.json').read_text())
    if set(archive.namelist())!=set(entries):raise ValueError('Archive index differs')
    for rel,digest in entries.items():
        if hashlib.sha256(archive.read(rel)).hexdigest()!=digest:raise ValueError('Archive changed: '+rel)
changed=subprocess.check_output(['git','diff','--name-only','origin/main'],cwd=repo,text=True).splitlines()
integration_entries=json.loads((pkg/'integration/archive-index.json').read_text())
parts=json.loads((pkg/'integration/archive-parts.json').read_bytes());seen=set()
for part in parts['parts']:
    path=pkg/'integration'/part['path'];assert sha256(path)==part['sha256'] and path.stat().st_size<100_000_000
    with zipfile.ZipFile(path) as archive:
        assert set(archive.namelist())==set(part['entries'])
        for rel in archive.namelist():
            assert rel not in seen;seen.add(rel)
            assert hashlib.sha256(archive.read(rel)).hexdigest()==integration_entries[rel],rel
assert seen==set(integration_entries)
assert all(p.startswith('publication/issue211-virtual/') for p in changed if p.startswith('publication/'))
if any(not (p.startswith(('docs/','publication/issue211-virtual/')) or p in ['.gitattributes','README.md','run.json','generation-receipts.json']) for p in changed):raise ValueError('Unexpected public source or history change')
subprocess.run(['git','diff','--exit-code','origin/main','--','publication/issue211','publication/issue193','publication/issue193-comment-followup','publication/issue211-reader'],cwd=repo,check=True,stdout=subprocess.PIPE)
# Check committed/staged bytes in one Git batch; .gitattributes must not change digests.
manifest=json.loads((repo/'docs/site-manifest.json').read_text())
owned={'docs/'+p:d for p,d in manifest['outputs'].items()}|{'docs/site-manifest.json':sha256(repo/'docs/site-manifest.json')}
owned.update({name:sha256(repo/name) for name in ['README.md','run.json','generation-receipts.json']})
for rel,digest in expected['files'].items():owned['publication/issue211-virtual/'+rel]=digest
owned['publication/issue211-virtual/evidence-index.json']=sha256(pkg/'evidence-index.json')
objects=subprocess.check_output(['git','ls-files','-s'],cwd=repo,text=True)
mapping={line.split('\t',1)[1]:line.split()[1] for line in objects.splitlines()}
ids=[mapping[p] for p in owned]
raw=subprocess.check_output(['git','cat-file','--batch'],input=('\n'.join(ids)+'\n').encode(),cwd=repo)
offset=0
for rel,digest in owned.items():
    end=raw.index(b'\n',offset);size=int(raw[offset:end].split()[-1]);data=raw[end+1:end+1+size];offset=end+size+2
    if hashlib.sha256(data).hexdigest()!=digest:raise ValueError('Git normalized original bytes: '+rel)
print(json.dumps(dict(schema=1,site=validated,package_files=len(expected['files']),archive_files=len(entries),staged_hashes_checked=len(owned),original_history_unchanged=True)))
