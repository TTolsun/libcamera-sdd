from pathlib import Path
import hashlib,json,yaml
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.publication_plan import prepare
root=Path.cwd();w=root/'build/preflight-native/native-good-01';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cfgpath=w/'sdd.yaml';opfile=w/'operation.json'
cfg=yaml.safe_load(cfgpath.read_bytes());op=json.loads(opfile.read_bytes());assert op['revision']==1
for report in cfg['publication']['reports']:
    path=w/report['path'];data=json.loads(path.read_bytes());assert data['status']=='passed' and not data.get('unresolved') and not data.get('findings')
    report['sha256']=sha(path)
(w/'before-final-config.yaml').write_bytes(cfgpath.read_bytes());(w/'before-final-operation.json').write_bytes(opfile.read_bytes())
op.update(revision=2,reason='Bind actual independent pre-merge native reviews before final export.',
          change=dict(kind='policy',reason='Fill preregistered independent report hashes; preserve reviewed manuscript/catalog bytes.',affected_sections=['camera-requests'],recheck='Existing prepare and export gates, local site verification, browser and public manifest/output hashes.'))
op['discoveries']=[dict(id='metadata-llm-glossary',kind='follow-up',status='deferred',reason='Retain the known nonblocking metadata LLM abbreviation warning; no change to source claims or human review pending.')]
cfgpath.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False),encoding='utf-8');opfile.write_text(json.dumps(op,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
record={str(p.relative_to(w)):sha(p) for p in [w/'manuscripts/camera-requests.md',w/'english.json']}
(w/'reviewed-before-export.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
loaded=load(cfgpath);prepare(loaded,KnowledgeModel.load(loaded.facts_path));print('Final report hashes adopted; reviewed manuscript/catalog unchanged.')
