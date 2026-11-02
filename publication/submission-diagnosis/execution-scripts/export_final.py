from pathlib import Path
import json,hashlib,subprocess,time,yaml
from sdd.config import load
from sdd.export_site import export_site
from sdd.site_build import verify_site
from sdd.document_metadata import split_frontmatter
R=Path(__file__).resolve().parent/'draft'
def j(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
review=j(R/'build/consistency-review.json');item=j(R/'independent-window-review.request-diagnosis.json')
assert review['status']=='passed'
assert len(item['units'])==19 and all(u['status']=='pass' for u in item['units']),item
assert item['body_sha256']==hashlib.sha256(split_frontmatter((R/'run/manuscripts/request-diagnosis.md').read_text(encoding='utf-8'))[1].encode()).hexdigest()
assert item['visuals_sha256']==sha(R/'config/visuals.yaml')
put(R/'regression.json',j(R/'final-ci.json'))
assert j(R/'regression.json')['status']=='passed'
assert j(R/'regression.json')['code_commit']==subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
assert j(R/'access-default-review.json')['status']=='source-supported'
put(R/'per-item-visualization.json',dict(schema=1,status='completed',stage='per-item-visualization-assessment',source_commit=review['source_commit'],human_review='pending',document='request-diagnosis.md',diagrams=10,units=item['units'],review_sha256=sha(R/'independent-window-review.request-diagnosis.json'),scope='19 individual questions only; not whole-site #215/#163 completion.'))
reports=[]
for name,producer,bindings in [('performance.json','inherited-historical-fixed-policy-benchmark-not-remeasured',dict(status='passed',stage='fixed-input-performance')),('regression.json','generator-ci',dict(status='passed',stage='generator-regression')),('per-item-visualization.json','source-bound-per-item-assessment',dict(status='completed',stage='per-item-visualization-assessment')),('native-call-verification.json','original-native-receipt-verifier',dict(status='verified',stage='after-independent-review')),('build/consistency-review.json','independent-codex-cli-audit',dict(status='passed',human_review='pending'))]:
 p=R/name;d=j(p);bindings['source_commit']=review['source_commit'];assert all(d.get(k)==v for k,v in bindings.items()),name;reports.append(dict(path=str(p.resolve()),gate='before-export',producer=producer,sha256=sha(p),bindings=bindings))
reports.append(dict(path=str((R/'access-default-review.json').resolve()),gate='before-export',producer='independent-codex-header-default-review',sha256=sha(R/'access-default-review.json'),bindings=dict(status='source-supported',source_commit=review['source_commit'],human_review='pending')))
p=R/'publication.yaml';cfg=yaml.safe_load(p.read_bytes());cfg['publication']['reports']=reports;p.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False),encoding='utf-8');put(R/'release-reports.json',dict(reports=reports))
manifests=[];rows=[]
for number in [1,2]:
 out=R/'build'/f'normal-export-{number}';start=time.perf_counter();export_site(load(p),out);duration=time.perf_counter()-start;v=verify_site(out);manifest=j(out/'site-manifest.json');manifests.append(manifest)
 for lang in ['', 'en/']:
  text=(out/(lang+'request-diagnosis.html')).read_text(encoding='utf-8')
  assert '소스 근거가 달라져' not in text and 'evidence has changed' not in text.lower()
 assert len(list(out.glob('request-diagnosis.*.mmd')))==10
 row=dict(export=number,wall_seconds=duration,build_id=manifest['build_id'],manifest_sha256=sha(out/'site-manifest.json'),outputs=len(manifest['outputs']),validation=v);rows.append(row);print(row,flush=True)
assert manifests[0]==manifests[1]
put(R/'two-exports.json',dict(schema=1,status='passed',stage='two-normal-exports',source_commit=review['source_commit'],code_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),exports=rows,complete_manifests_equal=True,all_outputs_byte_identical=True,human_review='pending'))
