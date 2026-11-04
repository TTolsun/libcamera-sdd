"""Actual native Codex probe on two immutable public libcamera excerpts."""
import copy
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time
import yaml

from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.generate import Generator
from sdd.export_site import export_site
from sdd.site_build import verify_site
from sdd.llm import Agent
from sdd.call_records import load_record
from sdd.cli_provenance import verify_cli_receipt

root=Path.cwd()
out=root/'build/issue242-publication/actual-probe-01'
out.mkdir()
public=root/'build/issue242-publication/libcamera-sdd/publication/submission-diagnosis'
full=json.loads(gzip.decompress((public/'facts293.json.gz').read_bytes()))
commit=full['meta']['source_commit']
topics=[]; evidence={}
for tid,label in [('create','요청 생성'),('queue','요청 큐잉')]:
    name=tid+'-state'
    rec=copy.deepcopy(full['evidence']['camera-model/state/'+name])
    topics.append(dict(id=tid,title=label,
        question=('createRequest()를 호출할 수 있는 상태와 실패 반환값은 무엇입니까?' if tid=='create' else
                  'queueRequest()에 허용되는 상태와 오류 반환값은 무엇입니까?'),
        covers=[tid],sources=[rec['selector']]))
    evidence['probe/'+tid+'/'+name]=rec
section=dict(id='probe',title='요청 API의 상태와 반환값 검증 표본',kind='prose',
    lead='두 요청 API의 공개 소스 계약을 대조합니다.',show_evidence=True,design_generation='llm',
    design_requirements=[dict(id=t['id'],question=t['question']) for t in topics],design_topics=topics,
    next=dict(title='검증 표본',link='probe.md'))
source=out/'source'
target=source/'src/libcamera/camera.cpp';target.parent.mkdir(parents=True)
raw=subprocess.run(['git','-C',str(root/'build/issue242-publication/libcamera-sdd'),
                    'show',commit+':src/libcamera/camera.cpp'],capture_output=True,check=True).stdout
target.write_bytes(raw)
for rec in evidence.values():
    selected='\n'.join(raw.decode('utf-8').splitlines()[rec['line']-1:rec['end_line']])
    if selected!=rec['text']:raise ValueError('Public literal source window mismatch')
(out/'sections.yaml').write_text(yaml.safe_dump(dict(sections=[section]),allow_unicode=True),encoding='utf-8')
(out/'scenarios.yaml').write_text('scenarios: []\n',encoding='utf-8')
profile=yaml.safe_load((root/'examples/libcamera/sdd.yaml').read_bytes())
data=dict(source=dict(root=str(source),compile_commands=str(source/'not-used.json')),
    output=dict(facts_dir='build/facts',sdd_dir='manuscripts',diagrams_dir='manuscripts/diagrams'),
    paths=dict(sections_file='sections.yaml',scenarios_file='scenarios.yaml',
               prompts=str(root/'examples/libcamera/prompts'),templates=str(root/'templates'),style=str(root/'style')),
    agent=profile['agent'],review={**profile['review']},site=dict(title='Public CLI validation probe',
        source_url='https://github.com/TTolsun/libcamera-sdd'))
(out/'sdd.yaml').write_text(yaml.safe_dump(data,allow_unicode=True),encoding='utf-8')
cfg=load(out/'sdd.yaml')
model=KnowledgeModel(meta=dict(source_commit=commit,source_root=str(source)),evidence=evidence)
model.save(cfg.facts_path)
plan=dict(public_source_commit=commit,source_file_sha256=hashlib.sha256(raw).hexdigest(),
    source_windows={k:{f:v[f] for f in ('file','line','end_line','sha256')} for k,v in evidence.items()},
    selected_profile=data['agent'],review_separate_from_generation=True,
    planned_cases=[dict(case='baseline',new_generation=2,new_grounding=2),
                   dict(case='same',new_generation=0,new_grounding=0),
                   dict(case='question',new_generation=1,new_grounding=1)],
    timing='wall and summed process time are separate; retries/failures remain visible',
    visual_assessment='Short individual API-contract paragraphs in a validation-only probe; no public article is replaced. Full published item checks remain separate.',
    human_review='pending')
(out/'representative-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
results=[]
def run(case):
    start=time.perf_counter()
    before=set((cfg.build_dir/'generation-runs').glob('*.json'))
    try:
        Generator(cfg,model,Agent(cfg.agent,cfg.build_dir/'prompts')).run()
        site=export_site(cfg)
        quality=verify_site(site)
        runs=[json.loads(p.read_bytes()) for p in set((cfg.build_dir/'generation-runs').glob('*.json'))-before]
        calls=[c for r in runs for c in r['calls']]
        row=dict(case=case,status='passed',wall_seconds=time.perf_counter()-start,
                 call_seconds_sum=sum(c['seconds'] for c in calls),calls=calls,quality=quality,
                 decisions=[d for r in runs for d in r.get('decisions',[])])
        results.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ('decisions','calls')},ensure_ascii=False),flush=True)
    except BaseException as exc:
        results.append(dict(case=case,status='failed',wall_seconds=time.perf_counter()-start,error=str(exc)))
        raise
    finally:
        (out/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')

run('baseline')
shutil.copytree(cfg.sdd_dir,out/'previous-good-manuscripts')
shutil.copytree(cfg.build_dir/'site',out/'previous-good-site')
archives={p:hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('calls','cli')
          for p in (cfg.build_dir/'prompts'/folder).rglob('*') if p.is_file()}
run('same')
section['design_topics'][0]['question']+=' 스레드 안전성도 포함하세요.'
(out/'sections.yaml').write_text(yaml.safe_dump(dict(sections=[section]),allow_unicode=True),encoding='utf-8')
run('question')
for p,sha in archives.items():
    if hashlib.sha256(p.read_bytes()).hexdigest()!=sha:raise ValueError('Original archive changed')
verified=[]
for path in (cfg.build_dir/'prompts/calls').rglob('*.receipt.json'):
    record=load_record(path,root=cfg.build_dir/'prompts/calls')
    verify_cli_receipt(record.request,record.raw,record.receipt,cfg.build_dir/'prompts/calls',cfg.agent)
    verified.append(dict(path=str(path.relative_to(out)),tag=record.receipt['tag'],model=record.receipt['model'],
                         provider=record.receipt['provider']))
(out/'native-receipts-verified.json').write_text(json.dumps(dict(original_archive_files_preserved=len(archives),
    receipts=verified),ensure_ascii=False,indent=2),encoding='utf-8')
