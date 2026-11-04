import hashlib,json,time
from pathlib import Path
from sdd.config import load
from sdd.export_site import export_site
from sdd.site_build import verify_site
root=Path.cwd();out=root/'build/issue242-publication/release-01'
cfg=load(out/'publication.yaml')
before_receipts={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in (cfg.build_dir/'prompts').rglob('*') if p.is_file()}
results=[];first=None
for number in (1,2):
    start=time.perf_counter();site=export_site(cfg);quality=verify_site(site)
    raw=(site/'site-manifest.json').read_bytes();manifest=json.loads(raw)
    signatures={name:hashlib.sha256((site/name).read_bytes()).hexdigest() for name in manifest['outputs']}
    if signatures!=manifest['outputs']:raise ValueError('Output hashes differ from manifest')
    if first is None:first=raw,signatures
    elif first!=(raw,signatures):raise ValueError('Repeated exports differ')
    results.append(dict(export=number,wall_seconds=time.perf_counter()-start,quality=quality,
        build_id=manifest['build_id'],manifest_sha256=hashlib.sha256(raw).hexdigest(),outputs=len(signatures)))
    print(json.dumps(results[-1]),flush=True)
if any(hashlib.sha256(p.read_bytes()).hexdigest()!=sha for p,sha in before_receipts.items()):
    raise ValueError('Original native archives changed')
result=dict(status='passed',exports=results,all_manifests_equal=True,all_output_bytes_equal=True,
    original_native_files_preserved=len(before_receipts),new_model_calls=0,human_review='pending')
(out/'two-exports-issue242.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
