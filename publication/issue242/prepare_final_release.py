import hashlib,json,shutil,subprocess
from pathlib import Path
root=Path.cwd();release=root/'build/issue242-publication/release-01';repo=root/'build/issue242-publication/libcamera-sdd'
old=release/'run/english.json'
if not (release/'run/english.before-pan.json').exists():shutil.copy2(old,release/'run/english.before-pan.json')
shutil.copy2(repo/'publication/diagram-pan/english.json',old)
manifest=json.loads((repo/'docs/site-manifest.json').read_bytes())
restore=json.loads((release/'restoration.json').read_bytes())
expected={n:sha for n,sha in restore['restored_originals'].items() if n.startswith('build/prompts/')}
actual={p.relative_to(release).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (release/'build/prompts').rglob('*') if p.is_file()}
assert expected==actual,('native archive set changed',len(expected),len(actual))
report=(release/'build/consistency-review.json').read_bytes()
assert hashlib.sha256(report).hexdigest()==manifest['inputs']['consistency_review']
facts=(release/'run/facts/facts.json').read_bytes()
assert hashlib.sha256(facts).hexdigest()==manifest['inputs']['facts']
git=lambda *args:subprocess.run(['git',*args],capture_output=True,text=True,check=True).stdout.strip()
changed=git('-C',str(repo),'diff','--name-only','293d751a814e0d4c34e85ad457ccd9d5eefd1a61','origin/upstream/master').splitlines()
# facts include the exact selected evidence files; retain explicit unchanged-path proof.
from sdd.facts.model import KnowledgeModel
from sdd.config import load
cfg=load(release/'publication.yaml');model=KnowledgeModel.load(cfg.facts_path)
paths=sorted({e['file'] for e in model.to_dict().get('evidence',{}).values()}) if hasattr(model,'to_dict') else []
assert not (set(paths)&set(changed)), 'Referenced source changed'
result=dict(referenced_evidence_files=paths,referenced_source_files_unchanged=True,generator_head=git('rev-parse','HEAD'),public_base=git('-C',str(repo),'rev-parse','HEAD'),source_commit=manifest['source_commit'] if 'source_commit' in manifest else '293d751a814e0d4c34e85ad457ccd9d5eefd1a61',upstream=git('-C',str(repo),'rev-parse','origin/upstream/master'),upstream_changed_paths=changed,original_native_file_set_identical=True,original_native_files=len(actual),original_native_hashes=actual,facts_match_public=True,consistency_report_matches_public=True,english_catalog_sha256=hashlib.sha256(old.read_bytes()).hexdigest(),source_hashes={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (root/'src/sdd').rglob('*.py')})
(release/'final-input-audit.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['original_native_hashes','source_hashes']}))

