from pathlib import Path
import json, yaml, shutil, gzip, zipfile, hashlib
W=Path(__file__).resolve().parent;R=W/'draft';P=W/'public/publication/issue214-unresolved';B=W/'public/publication/issue214'
def j(p):return json.loads(p.read_bytes())
def y(p):return yaml.safe_load(p.read_bytes())
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
record={'public_base':'d3d930b','preserved_document':'scenarios/queue_request.md','scope':'Preserve merged PR79 and its original provenance; unmerged PR78 is not a publication baseline.'}
shutil.copyfile(P/'manuscripts/scenarios/queue_request.md',R/'run/manuscripts/scenarios/queue_request.md')
f=R/'config/sections.yaml';data=y(f);latest={s['id']:s for s in y(P/'config/sections.yaml')['sections']};main={s['id']:s for s in y(Path('examples/libcamera/config/sections.yaml'))['sections']}
for i,s in enumerate(data['sections']):
 if s['id']=='scenario-queue_request':data['sections'][i]=latest[s['id']]
 if s['id']=='request-diagnosis':s['routes']=main[s['id']]['routes']
f.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
f=R/'run/english.json';ours=j(f);before=j(B/'english.json');latest=j(P/'english.json');changed={}
for k,v in latest.items():
 if isinstance(v,dict):
  n=0
  for key,value in v.items():
   if before.get(k,{}).get(key)!=value:
    assert ours.get(k,{}).get(key) in (None,before.get(k,{}).get(key),value),(k,key,'concurrent conflict')
    ours.setdefault(k,{})[key]=value;n+=1
  changed[k]=n
put(f,ours);record['catalog_imports']=changed
f=R/'run/facts/facts.json';ours=j(f);latest=json.loads(gzip.decompress((P/'facts293.json.gz').read_bytes()))
assert ours['meta']['source_commit']==latest['meta']['source_commit']
for k,v in latest.get('evidence',{}).items():
 if k in ours['evidence']:assert ours['evidence'][k]==v,k
 else:ours['evidence'][k]=v
put(f,ours)
with zipfile.ZipFile(P/'cli-evidence-delta.zip') as z:
 for name in z.namelist():
  target=(R/name).resolve();assert target.is_relative_to(R.resolve())
  if name.endswith('/'):continue
  raw=z.read(name)
  if target.exists():
   if target.read_bytes()!=raw:continue # Preserve our current mutable reports; receipts are unique.
  else:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
put(R/'concurrent-public-preservation.json',record)
print(record)
