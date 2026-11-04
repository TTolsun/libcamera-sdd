from pathlib import Path
import hashlib,json,re,yaml
w=Path.cwd()/'build/issue241/public-case-02'
content=json.loads((w/'build/consistency-review.json').read_bytes())
diagram=json.loads((w/'build/diagram-review.json').read_bytes())
assert content['status']=='passed' and not content['unresolved']
assert diagram['status']=='passed' and not diagram['findings']
for name,digest in diagram['inputs'].items():
    assert hashlib.sha256((w/name).read_bytes()).hexdigest()==digest,name
assert not re.search(r'(?m)^다음 단계:',(w/'manuscripts/camera-requests.md').read_text(encoding='utf-8'))
cfgpath=w/'sdd.yaml'
(w/'input-corrections/sdd-before-final-report-bindings.yaml').write_bytes(cfgpath.read_bytes())
cfg=yaml.safe_load(cfgpath.read_bytes())
for row in cfg['publication']['reports']:
    row['sha256']=hashlib.sha256((w/row['path']).read_bytes()).hexdigest()
cfgpath.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False),encoding='utf-8')
op=w/'operation.json';old=op.read_bytes()
c=json.loads(old);assert c['revision']==5
(w/'contract-inputs/revision-05.json').write_bytes(old)
c['revision']=6;c['reason']='Bind completed independent evidence and final standalone input checks without rewriting reviewed manuscripts.'
c['change']=dict(kind='policy',reason='Fill predeclared final report hashes after actual independent CLI reviews; preserve reviewed Markdown/catalog bytes and prior failures.',affected_sections=['camera-requests'],recheck='Prepare a new immutable plan only, enforce report hashes and current source/receipts during export, then verify generated files, browser behavior and public deployment. Do not rewrite the reviewed manuscript just to update its timestamp.')
for row in c['discoveries']:
    if row['id']=='independent-content-review':
        row.update(status='resolved',reason='Fresh separate Codex/Terra High content review passed with zero unresolved findings and diagram review passed with zero findings; exact report hashes are bound before export. Human review remains pending.')
    if row['id']=='sample-next-step':
        row.update(status='resolved',reason='Revision4 did not resolve the default-footer behavior. Revision5 standalone template produced actual Markdown without the next-task footer and both independent entry/review paths passed; final links still require site verification.')
c['discoveries'].append(dict(id='metadata-llm-glossary',kind='follow-up',status='deferred',reason='Standalone metadata reports the undefined LLM abbreviation warning. It does not change the fixed addBuffer source claims or conditions; common metadata/glossary polish stays outside this bounded operation. The warning is retained, not relabeled as fixed.'))
op.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(w/'reviewed-artifacts-before-export.json').write_text(json.dumps(dict(manuscript=hashlib.sha256((w/'manuscripts/camera-requests.md').read_bytes()).hexdigest(),catalog=hashlib.sha256((w/'english.json').read_bytes()).hexdigest()),indent=2)+'\n',encoding='utf-8')
print('Revision6 binds actual evidence; reviewed artifact bytes retained.')
