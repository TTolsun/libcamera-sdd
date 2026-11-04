"""Preserve every indexed ZIP entry in GitHub-sized archive parts."""
from pathlib import Path
import json,zipfile,hashlib,shutil
from sdd.runtime_evidence import sha256
r=Path(__file__).resolve().parent.parent;w=r/'build/issue211-virtual';repo=r/'build/libcamera-sdd-issue211';p=repo/'publication/issue211-virtual';extra=p/'integration';original=extra/'cli-evidence.zip';backup=w/'oversized-integration-archive';backup.mkdir()
assert original.resolve().is_relative_to(r.resolve()) and backup.resolve().is_relative_to(r.resolve())
old_sha=sha256(original);expected=json.loads((extra/'archive-index.json').read_bytes());parts=[];seen=set();limit=60_000_000
for rel in ['evidence-index.json','generation-receipts.json','run.json']:shutil.copy2(p/rel,backup/rel)
with zipfile.ZipFile(original) as source:
 assert set(source.namelist())==set(expected)
 groups=[];group=[];size=0
 for info in source.infolist():
  if group and size+info.compress_size+len(info.filename.encode())*2+256>limit:groups.append(group);group=[];size=0
  assert info.compress_size<limit
  group.append(info);size+=info.compress_size+len(info.filename.encode())*2+256
 if group:groups.append(group)
 for number,group in enumerate(groups,1):
  target=extra/f'cli-evidence-{number:02}.zip';assert not target.exists()
  with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as output:
   for info in group:
    data=source.read(info);assert hashlib.sha256(data).hexdigest()==expected[info.filename];assert info.filename not in seen;seen.add(info.filename)
    output.writestr(info,data,compresslevel=9)
  assert target.stat().st_size<100_000_000
  with zipfile.ZipFile(target) as check:
   for name in check.namelist():assert hashlib.sha256(check.read(name)).hexdigest()==expected[name]
  parts.append({'path':target.name,'sha256':sha256(target),'bytes':target.stat().st_size,'entries':[info.filename for info in group]})
assert seen==set(expected)
shutil.move(str(original),str(backup/original.name))
manifest={'schema':1,'format':'indexed-zip-parts-v1','original_archive_sha256':old_sha,'original_archive_bytes':(backup/original.name).stat().st_size,'archive_index_sha256':sha256(extra/'archive-index.json'),'entry_count':len(expected),'parts':parts,'all_entries_preserved_and_verified':True}
(extra/'archive-parts.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
for name in ['generation-receipts.json','run.json']:
 value=json.loads((p/name).read_bytes())
 if name=='generation-receipts.json':
  value['integration_archive']='publication/issue211-virtual/integration/archive-parts.json';value['integration_archive_format']=manifest['format'];value['integration_archives']=['publication/issue211-virtual/integration/'+x['path'] for x in parts]
 else:value['integration']['archive_manifest']='publication/issue211-virtual/integration/archive-parts.json'
 for target in [p/name,repo/name]:target.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
operators=extra/'operators';operators.mkdir();shutil.copy2(Path(__file__),operators/Path(__file__).name)
print(json.dumps({'parts':len(parts),'entries':len(expected),'bytes':[x['bytes'] for x in parts],'original_preserved_locally':True}))
