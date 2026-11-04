from pathlib import Path
import json,hashlib,urllib.request
from sdd.runtime_evidence import sha256
r=Path(__file__).resolve().parent.parent;w=r/'build/issue211-virtual';repo=r/'build/libcamera-sdd-issue211';merge=json.loads((w/'public-virtual-merge.json').read_bytes());assert merge['merged'];commit=merge['sha']
out=w/'public-evidence-artifacts';out.mkdir();rows=[]
parts=json.loads((repo/'publication/issue211-virtual/integration/archive-parts.json').read_bytes())
for rel in ['cli-evidence.zip','archive-index.json','evidence-index.json','integration/archive-index.json','integration/archive-parts.json',*['integration/'+p['path'] for p in parts['parts']]]:
 path='publication/issue211-virtual/'+rel;url='https://raw.githubusercontent.com/TTolsun/libcamera-sdd/'+commit+'/'+path
 digest=hashlib.sha256();size=0
 with urllib.request.urlopen(urllib.request.Request(url,headers={'Cache-Control':'no-cache'}),timeout=90) as response:
  assert response.status==200;headers=dict(response.headers)
  while chunk:=response.read(1024*1024):digest.update(chunk);size+=len(chunk)
 expected=sha256(repo/path);assert digest.hexdigest()==expected,(path,digest.hexdigest(),expected)
 rows.append({'url':url,'path':path,'status':200,'bytes':size,'sha256':expected,'headers':headers});print(path,'verified',flush=True)
(out/'report.json').write_text(json.dumps({'schema':1,'public_merge':commit,'artifacts':rows,'all_verified':True},indent=2)+'\n',encoding='utf-8')
