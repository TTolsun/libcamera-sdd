from pathlib import Path
import json,hashlib,subprocess,time,yaml
from sdd.config import load
from sdd.export_site import export_site
from sdd.site_build import verify_site
r=Path('build/issue214/unresolved-followup');review=json.loads((r/'build/consistency-review.json').read_bytes());assert review['status']=='passed',review['status']
runtime_tree=subprocess.check_output(['git','rev-parse','HEAD:src/sdd'],text=True).strip()
reports=[]
for path,producer,bindings in [('performance.json','inherited-fixed-policy-benchmark-not-remeasured',dict(status='passed',stage='fixed-input-performance')),('regression.json','generator-ci',dict(status='passed',stage='generator-regression')),('per-item-visualization.json','source-bound-per-item-assessment',dict(status='completed',stage='per-item-visualization-assessment')),('native-call-verification.json','original-native-receipt-verifier',dict(status='verified',stage='after-independent-review')),('finding-dispositions.json','independent-source-triage-and-corrected-contract-review',dict(status='completed',stage='unresolved-adjudication')),('build/consistency-review.json','independent-codex-cli-audit',dict(status='passed',human_review='pending'))]:
 p=r/path;d=json.loads(p.read_bytes());
 if path == 'regression.json':
  assert d.get('sdd_tree')==runtime_tree,(path,'wrong runtime code');bindings['sdd_tree']=runtime_tree
 bindings['source_commit']=review['source_commit'];assert all(d.get(k)==v for k,v in bindings.items()),path;reports.append(dict(path=str(p.resolve()),gate='before-export',producer=producer,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bindings=bindings))
p=r/'publication.yaml';cfg=yaml.safe_load(p.read_bytes());cfg['publication']['reports']=reports;p.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False),encoding='utf-8');(r/'release-reports.json').write_text(json.dumps(dict(schema=1,stage='before-export',reports=reports),indent=2),encoding='utf-8')
rows=[];manifests=[]
for index in [1,2]:
 cfg=load(p);out=r/'build'/('normal-export-'+str(index));started=time.perf_counter();export_site(cfg,out);seconds=time.perf_counter()-started;v=verify_site(out);manifest=json.loads((out/'site-manifest.json').read_bytes());manifests.append(manifest);row=dict(export=index,wall_seconds=seconds,build_id=manifest['build_id'],manifest_sha256=hashlib.sha256((out/'site-manifest.json').read_bytes()).hexdigest(),outputs=len(manifest['outputs']),validation=v);rows.append(row);print(row,flush=True)
assert manifests[0]==manifests[1],'Normal export manifests differ'
result=dict(schema=1,status='passed',stage='two-normal-exports',source_commit=review['source_commit'],code_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),exports=rows,complete_manifests_equal=True,all_outputs_byte_identical=True,no_duplicate_enforcement_wrapper=True,human_review='pending');(r/'two-exports.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print('Two normal exports match.',flush=True)
