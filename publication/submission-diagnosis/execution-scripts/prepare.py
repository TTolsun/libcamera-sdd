from pathlib import Path
import copy,gzip,json,shutil,zipfile,yaml

root=Path(__file__).resolve().parents[2]
w=Path(__file__).resolve().parent
p=w/'public/publication/issue214'
out=w/'draft'
if out.exists(): raise SystemExit('Draft already exists; resume it.')
out.mkdir()
for source,target in [('config','config'),('manuscripts','run/manuscripts'),('historical-style','historical-style'),('reader-preserved-style','reader-preserved-style'),('templates','templates')]:
 shutil.copytree(p/source,out/target)
shutil.copytree(root/'style',out/'current-style')
for source,target in [('english.json','run/english.json'),('site-intro.md','site-intro.md'),('consistency-review.json','build/consistency-review.json')]:
 dest=out/target;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p/source,dest)
for f in p.glob('*.json'): shutil.copyfile(f,out/f.name)
(out/'run/facts').mkdir(parents=True)
(out/'run/facts/facts.json').write_bytes(gzip.decompress((p/'facts293.json.gz').read_bytes()))
with zipfile.ZipFile(p/'cli-evidence.zip') as z:
 for entry in z.infolist():
  dest=(out/entry.filename).resolve()
  if not dest.is_relative_to(out.resolve()): raise ValueError('Unsafe archive path')
  if not entry.is_dir():
   dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(entry))
old='C:/Users/baboe/.codex/worktrees/b199/camera-hal-sdd-generator'
mappings=[(old+'/build/issue214/draft-v1',out),(old+'/build/issue214/baseline/style',out/'historical-style'),(old+'/build/issue214/baseline/templates',out/'templates'),(old+'/build/issue214/public',w/'public'),(old+'/build/issue214/source',w/'source'),(old,root)]
def relocate(x):
 if isinstance(x,dict):return {k:relocate(v) for k,v in x.items()}
 if isinstance(x,list):return [relocate(v) for v in x]
 if isinstance(x,str):
  path=x.replace('\\','/')
  for prefix,target in mappings:
   if path==prefix or path.startswith(prefix+'/'):return str(target/path[len(prefix):].lstrip('/'))
 return x
profiles={f.name:relocate(yaml.safe_load(f.read_text(encoding='utf-8'))) for f in (p/'profiles').glob('*.yaml')}
for name,d in profiles.items():
 if 'publication' in d:d['publication']['operation_id']='libcamera-submission-diagnosis'
 if name in ['publication.yaml','independent-review.yaml','generation.yaml']:
  d['site']['manuscript_profiles']['request-diagnosis.md']=str(out/'diagnosis-authentication.yaml')
 if name=='generation.yaml':
  d['agent'].update(kind='cli',runner='codex',model='gpt-6.1-terra',command=[],args=['-c','model_reasoning_effort="high"'])
  d['paths']['style']=str(out/'current-style')
 if name=='independent-review.yaml':d['agent']['command']=[]
 if name=='translation-agent.yaml':
  d['agent'].update(kind='cli',runner='codex',model='gpt-6.1-terra',command=[],args=['-c','model_reasoning_effort="high"'])
 (out/name).write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
auth={'agent':copy.deepcopy(profiles['generation.yaml']['agent']),'paths':{'style':str(out/'current-style')}}
(out/'diagnosis-authentication.yaml').write_text(yaml.safe_dump(auth,allow_unicode=True,sort_keys=False),encoding='utf-8')
print('Restored public inputs and original receipts; fresh generation/translation/review use independent Codex CLI/Terra High.')
