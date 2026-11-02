from pathlib import Path
import json,yaml,gzip,shutil,hashlib,subprocess,zipfile,argparse
from sdd.site_build import verify_site
from sdd.publication import copy_site
from sdd.config import load
from sdd.publication_plan import check_reports
W=Path(__file__).resolve().parent;R=W/'draft';P=W/'public';D=P/'publication/submission-diagnosis'
def j(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
ap=argparse.ArgumentParser();ap.add_argument('--merge',required=True);a=ap.parse_args()
site=R/'build/normal-export-1';validation=verify_site(site);manifest=j(site/'site-manifest.json');review=j(R/'build/consistency-review.json');native=j(R/'native-call-verification.json');exports=j(R/'two-exports.json')
assert review['status']=='passed' and native['status']=='verified' and exports['status']=='passed'
assert subprocess.check_output(['git','rev-parse',a.merge+':src/sdd'],text=True).strip()==j(R/'regression.json')['sdd_tree']
assert all(x['build_id']==manifest['build_id'] for x in exports['exports'])
check_reports(load(R/'publication.yaml'),'before-export')
baseline=P/'publication/issue214-unresolved/manuscripts';unchanged=[]
for p in (R/'run/manuscripts').rglob('*.md'):
 rel=p.relative_to(R/'run/manuscripts')
 if str(rel)=='request-diagnosis.md':continue
 assert p.read_bytes()==(baseline/rel).read_bytes(),rel;unchanged.append(rel.as_posix())
assert len(unchanged)==28
D.mkdir(parents=True,exist_ok=True)
for p in R.glob('*.yaml'):
 if p.name!='package.yaml':cp(p,D/'profiles'/p.name)
package=yaml.safe_load((R/'publication.yaml').read_bytes())
for name,stage in [('two-exports.json','two-normal-exports'),('ui-verification.json',None)]:
 bindings=dict(status='passed',source_commit=review['source_commit'])
 if stage:bindings['stage']=stage
 package['publication']['reports'].append(dict(path=str((R/name).resolve()),gate='before-package',producer=name.removesuffix('.json'),sha256=sha(R/name),bindings=bindings))
p=R/'package-current.yaml';p.write_text(yaml.safe_dump(package,allow_unicode=True,sort_keys=False),encoding='utf-8');check_reports(load(p),'before-package');cp(p,D/'profiles/package.yaml')
for name,dest in [('config','config'),('run/manuscripts','manuscripts'),('historical-style','historical-style'),('current-style','current-style'),('reader-preserved-style','reader-preserved-style'),('templates','templates'),('prior-reviews','prior-reviews')]:
 if (R/name).exists():shutil.copytree(R/name,D/dest,dirs_exist_ok=True)
shutil.copytree(Path('examples/libcamera/prompts'),D/'prompts',dirs_exist_ok=True)
shutil.copytree(site/'assets/mermaid',D/'site-assets/mermaid',dirs_exist_ok=True)
(D/'facts293.json.gz').write_bytes(gzip.compress((R/'run/facts/facts.json').read_bytes(),mtime=0));cp(R/'run/english.json',D/'english.json');cp(R/'build/consistency-review.json',D/'consistency-review.json');cp(site/'site-manifest.json',D/'site-manifest.json')
for name in ['scope.json','regression.json','performance.json','per-item-visualization.json','native-call-verification.json','two-exports.json','release-reports.json','concurrent-public-preservation.json','site-intro.md','ui-verification.json']:
 cp(R/name,D/name)
for p in R.glob('independent-window-review.request-diagnosis*.json'):cp(p,D/'reviews'/p.name)
for p in W.glob('*.py'):cp(p,D/'execution-scripts'/p.name)
for p in W.glob('*.log'):cp(p,D/'attempts'/p.name)
for name in ['prior-reviews','gap-review']:
 if (W/name).exists():shutil.copytree(W/name,D/name,dirs_exist_ok=True)
cp(W/'gap-review.json',D/'gap-review.json')
cp(R/'access-default-review.json',D/'access-default-review.json')
cp(P/'publication/issue214-unresolved/finding-dispositions.json',D/'historical-finding-dispositions.json')
entries=[]
with zipfile.ZipFile(D/'cli-evidence.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for role in ['prompts','translation-prompts','independent-window-review','cli-checkpoints','generation-runs','execution-locks']:
  for p in sorted((R/'build'/role).rglob('*')):
   if p.is_file() and p.suffix not in ['.lock','.tmp']:
    rel=p.relative_to(R).as_posix();z.write(p,rel);entries.append(dict(path=rel,bytes=p.stat().st_size,sha256=sha(p)))
paths={e['path']:e for e in entries};assert all(paths[c['receipt']]['sha256']==c['receipt_sha256'] for c in native['calls'])
put(D/'archive-index.json',dict(schema=1,archive=dict(path='cli-evidence.zip',sha256=sha(D/'cli-evidence.zip')),entries=entries,human_review='pending'))
merge=dict(pr='https://github.com/TTolsun/camera-hal-sdd-generator/pull/229',sha=a.merge,sdd_tree=j(R/'regression.json')['sdd_tree']);put(D/'generator-merge.json',merge)
run=dict(schema=1,source_repository='https://gitlab.freedesktop.org/camera/libcamera.git',source_commit=review['source_commit'],upstream_head='df8e348d64b4932a0676256ed24f0da3ee9438bc',generator_merge=merge,modified_manuscripts=['request-diagnosis.md'],unchanged_manuscripts=unchanged,preserved_public_base='d3d930b',build_id=manifest['build_id'],manifest_sha256=sha(site/'site-manifest.json'),manifest_outputs=len(manifest['outputs']),validation=validation,independent_review=dict(status=review['status'],fresh_batches=review['fresh_batches'],reused_batches=review['reused_batches'],unresolved=len(review['unresolved'])),human_review='pending',deployment='Pages and live artifact proof recorded after merge in publication PR.',scope='Public source-window follow-up only; original293facts/runtime retained; no new hardware/internal HAL validation.')
for name in ['run.json','generation-receipts.json']:
 if not (D/'prior-root'/name).exists():cp(P/name,D/'prior-root'/name)
put(D/'run.json',run);put(P/'run.json',run)
receipts=dict(schema=1,source_commit=review['source_commit'],new_writer=dict(runner='codex',model='gpt-6.1-terra',args=['-c','model_reasoning_effort="high"']),reviewer=dict(runner='codex',model='gpt-6.1-terra',args=['-c','model_reasoning_effort="high"']),historical_profiles='Preserved; old Claude calls are not new Codex generation.',counts=native['counts'],verification='publication/submission-diagnosis/native-call-verification.json',interpretation='Completed invocations include rejected drafts. Not human approval.',human_review='pending');put(D/'generation-receipts.json',receipts);put(P/'generation-receipts.json',receipts)
copy_site(site,P/'docs',P/'.git/submission-copy')
p=P/'.gitattributes';text=p.read_text(encoding='utf-8');line='publication/submission-diagnosis/** -text -whitespace'
if line not in text:p.write_text(text.rstrip()+'\n'+line+'\n',encoding='utf-8')
(D/'README.md').write_text('''# Request submission diagnosis follow-up

Public libcamera only. One existing document gains source-bound submission checks and ten question-specific diagrams. The other 28 manuscripts exactly preserve merged public PR79. Unmerged PR78 is outside this baseline. The original 293 structural facts/runtime remain; upstream df8 changes only the release version. This is not hardware/internal HAL validation or completion of #215/#163.

`scope.json` records reviewed literal windows and exclusions. `reviews`, `per-item-visualization.json` and `consistency-review.json` retain automatic findings and per-question omission reasons. Human approval remains pending; unresolved informational/insufficient-evidence findings are not erased. `attempts` and the native archive retain rejected and interrupted attempts, including stale visual excerpts fixed after browser inspection. The inherited `performance.json` is historical, not a newly measured benchmark.

`profiles`, `config`, `manuscripts`, `facts293.json.gz`, `english.json`, styles/templates/prompts and `cli-evidence.zip` reproduce the inputs with the generator merge and locked dependencies. Restore facts to run/facts/facts.json, manuscripts to run/manuscripts, english.json to run/english.json, and extract the indexed archive at the work root. Relocate paths in all profiles consistently, retain authentication profiles and historical identity, and use a 293 source checkout. Historical compile database paths document the original extraction; re-export is not a new build or extraction. Path relocation changes the configuration hash/build ID. Verify the relocated manifest separately.

Fresh execution uses independent native Codex CLI gpt-6.1-terra with model_reasoning_effort="high". Missing or failed selected CLI execution must be reported; saved responses, another CLI, direct APIs or manual manuscripts do not substitute for a new successful run. Existing checkpoint revalidation is explicitly counted as reuse.

`native-call-verification.json` checks original request/response/stdout and selected arguments. `two-exports.json` records two normal exports with identical complete manifests; `ui-verification.json` records the actually inspected browser views. Live manifest and all output hashes are checked after Pages deployment and recorded in the publication PR.
''',encoding='utf-8')
p=P/'README.md';text=p.read_text(encoding='utf-8');link='- [Request submission diagnosis evidence](publication/submission-diagnosis/README.md)'
if link not in text:p.write_text(text.rstrip()+'\n\n'+link+'\n',encoding='utf-8')
put(D/'package-file-index.json',dict(schema=1,build_id=manifest['build_id'],files={p.relative_to(D).as_posix():dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file() and p.name!='package-file-index.json'}))
print(dict(status='prepared',build_id=manifest['build_id'],files=len(list(D.rglob('*'))),archive_entries=len(entries)))
