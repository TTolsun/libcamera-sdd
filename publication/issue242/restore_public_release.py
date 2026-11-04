"""Relocate the latest public evidence without editing original receipts."""
import gzip,hashlib,json,shutil,subprocess,zipfile
from pathlib import Path
import yaml

root=Path.cwd();repo=root/'build/issue242-publication/libcamera-sdd'
p=repo/'publication/issue211-virtual/integration'
out=root/'build/issue242-publication/release-01';out.mkdir(exist_ok=True)
parts=json.loads((p/'archive-parts.json').read_text(encoding='utf-8'))
index=json.loads((p/'archive-index.json').read_text(encoding='utf-8'))
restored={}
for part in parts['parts']:
    archive=p/part['path']
    if hashlib.sha256(archive.read_bytes()).hexdigest()!=part['sha256']:
        raise ValueError('Original public archive changed')
    with zipfile.ZipFile(archive) as source:
        for item in source.infolist():
            prefix='workspace/current-main-integration/'
            if item.is_dir() or not item.filename.startswith(prefix):continue
            relative=item.filename[len(prefix):]
            target=(out/relative).resolve()
            if not target.is_relative_to(out):raise ValueError('Unsafe archive member')
            raw=source.read(item)
            if hashlib.sha256(raw).hexdigest()!=index[item.filename]:raise ValueError('Original member changed')
            target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
            restored[relative]=index[item.filename]
for name in ('config','historical-style','current-style','reader-preserved-style','templates'):
    shutil.copytree(p/name,out/name,dirs_exist_ok=True)
for file in p.glob('*.json'):shutil.copyfile(file,out/file.name)
for file in (p/'inherited-reports').glob('*.json'):shutil.copyfile(file,out/file.name)
(out/'run').mkdir(exist_ok=True)
shutil.copyfile(p/'english.json',out/'run/english.json')
shutil.copyfile(p/'site-intro.md',out/'site-intro.md')
(out/'run/facts').mkdir(parents=True,exist_ok=True)
(out/'run/facts/facts.json').write_bytes(gzip.decompress((p/'facts293.json.gz').read_bytes()))
manifest=json.loads((repo/'docs/site-manifest.json').read_text(encoding='utf-8'))
for name in manifest['outputs']:
    if name.endswith('.md'):
        target=out/'run/manuscripts'/name;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(repo/'docs'/name,target)
old='C:/Users/baboe/.codex/worktrees/'
maps=[
    (old+'cb18/camera-hal-sdd-generator/build/issue211-virtual/current-main-integration',out),
    (old+'cb18/camera-hal-sdd-generator/build/issue211-virtual/reader-verification.yaml',out/'selected-reader-verification.yaml'),
    (old+'cb18/camera-hal-sdd-generator/build/libcamera-source-issue211',root/'build/issue242-publication/source293'),
    (old+'cb18/camera-hal-sdd-generator/build/libcamera-sdd-issue211/docs/assets/mermaid',repo/'docs/assets/mermaid'),
    (old+'b199/camera-hal-sdd-generator/build/issue214/baseline/style',out/'historical-style'),
    (old+'b199/camera-hal-sdd-generator/build/issue214/baseline/templates',out/'templates'),
    (old+'cb18/camera-hal-sdd-generator/style',out/'current-style'),
    (old+'b199/camera-hal-sdd-generator',root),
    (old+'cb18/camera-hal-sdd-generator',root),
]
def relocate(value):
    if isinstance(value,dict):return {k:relocate(v) for k,v in value.items()}
    if isinstance(value,list):return [relocate(v) for v in value]
    if isinstance(value,str):
        path=value.replace('\\','/')
        for prefix,target in maps:
            if path==prefix or path.startswith(prefix+'/'):
                return str(target/path[len(prefix):].lstrip('/'))
    return value
for profile in (p/'profiles').glob('*.yaml'):
    data=relocate(yaml.safe_load(profile.read_bytes()))
    if 'publication' in data:data['publication']['operation_id']='issue242-public-release'
    (out/profile.name).write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
for path in (out/'config').glob('*.yaml'):
    data=relocate(yaml.safe_load(path.read_bytes()))
    path.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
# Exact old bytes remain under the original public package. Only the local
# configuration paths change; archived prompts/stdout/receipts never do.
facts=(out/'run/facts/facts.json').read_bytes()
review=out/'build/consistency-review.json'
result=dict(original_archived_files_restored=len(restored),
    facts_match_public_manifest=hashlib.sha256(facts).hexdigest()==manifest['inputs']['facts'],
    consistency_review_matches_public_manifest=review.exists() and hashlib.sha256(review.read_bytes()).hexdigest()==manifest['inputs']['consistency_review'],
    public_base=subprocess.run(['git','-C',str(repo),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip(),
    original_manifest=manifest['build_id'],restored_originals=restored,
    human_review='pending')
(out/'restoration.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='restored_originals'}),flush=True)
