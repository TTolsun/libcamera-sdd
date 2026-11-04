import hashlib,json,time
from pathlib import Path
from sdd.config import load
from sdd.export_site import export_site
from sdd.site_build import verify_site
root=Path.cwd();out=root/'build/issue242-publication/release-01';cfg=load(out/'publication.yaml')
original=json.loads((out/'final-input-audit.json').read_bytes())['original_native_hashes']
previous=set((cfg.build_dir/'generation-runs').glob('*.json'))
results=[];first=None
for number in (1,2):
 start=time.perf_counter();site=export_site(cfg);quality=verify_site(site)
 raw=(site/'site-manifest.json').read_bytes();manifest=json.loads(raw)
 signatures={name:hashlib.sha256((site/name).read_bytes()).hexdigest() for name in manifest['outputs']}
 assert signatures==manifest['outputs']
 if first is None:first=raw,signatures
 else:assert first==(raw,signatures)
 results.append(dict(export=number,wall_seconds=time.perf_counter()-start,quality=quality,build_id=manifest['build_id'],manifest_sha256=hashlib.sha256(raw).hexdigest(),outputs=len(signatures)))
 print(json.dumps(results[-1]),flush=True)
actual={p.relative_to(out).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (cfg.build_dir/'prompts').rglob('*') if p.is_file()}
assert actual==original
runs=[json.loads(p.read_bytes()) for p in set((cfg.build_dir/'generation-runs').glob('*.json'))-previous]
assert not any(r['calls'] for r in runs)
old=json.loads((root/'build/issue242-publication/libcamera-sdd/docs/site-manifest.json').read_bytes())
assert old['outputs']==manifest['outputs'], 'Unexpected public output changes'
result=dict(status='passed',exports=results,all_manifests_equal=True,all_output_bytes_equal=True,original_native_file_set_identical=True,original_native_files_preserved=len(original),new_model_calls=0,generation_runs=runs,public_base=original and json.loads((out/'final-input-audit.json').read_bytes())['public_base'],outputs_equal_latest_public=True,human_review='pending')
(out/'two-exports-final.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
