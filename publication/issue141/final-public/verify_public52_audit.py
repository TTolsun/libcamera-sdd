"""Bind all current claims and verdicts to restored native calls; no inference.

Reconstruct the independently documented publisher checkout identity for an
archive comparison only. No policy function, cache, manuscript or report changes.
"""
import collections
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import yaml
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.call_records import canonical_request_hash,load_record
from sdd.cli_checkpoint import checksum,UnitStore
from sdd.cli_agent import arguments
from sdd.cli_provenance import verify_cli_receipt
from sdd import consistency

w=Path('build/issue141').resolve();release=w/'public-release-46235b02';package=release/'publication/goal-138-140'
restored=w/'restored-public52-evidence'
native_root=Path('\\\\?\\'+str(restored)) if os.name=='nt' else restored
report=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),public_commit='46235b026626db49ef98ba3a5e23d1359dbe3d0a',passed=False,new_model_calls=0,
    scope='Exact current five-group payloads, all native batch requests/responses and386 assembled verdicts; not fresh LLM inference, exhaustive secondary all-pairs proof, natural current-environment export/reuse or human approval',
    policy_function_modified=False,production_cache_or_export_invoked=False,batches=0,receipts=0,contracts=[])
try:
    cfg=load(package/'executed-sdd.codex.local.yaml')
    cfg.sdd_dir=package/'manuscripts';cfg.facts_dir=package/'facts';cfg.source_root=w/'current-e117/source'
    for name,file in [('consistency_file','contracts.yaml'),('sections_file','sections.yaml'),('scenarios_file','scenarios.yaml')]:
        cfg.paths[name]=package/'config'/file
    cfg.raw['site']['english_catalog']=str(package/'english.json')
    model=KnowledgeModel.load(cfg.facts_path)
    saved=json.loads((package/'consistency-review.json').read_bytes())
    summary=json.loads((package/'merged-main-verification.json').read_bytes())
    parts={}
    for name in ('consistency.py','consistency_sources.py','consistency_analysis.py'):
        data=subprocess.check_output(['git','show',summary['generator_commit']+':src/sdd/'+name])
        if name=='consistency.py':data=data.replace(b'\n',b'\r\n')
        parts[name]=hashlib.sha256(data).hexdigest()
    policy=canonical_request_hash(parts)
    assert policy==summary['consistency_policy']=='19eb352e6730b1eab46255a4a4b4384e9c097ff75ef601efbaacbf39d7718b2c'
    report.update(recorded_runtime_policy_reconstructed_from_git=policy,
        policy_reconstruction_basis='Exact a403 Git source with the LF/CRLF layout independently documented and cross-checked in merged PR159; archive comparison only, not a compatibility exception')
    configured=consistency.groups(cfg);assert len(configured)==len(saved['contracts'])==5
    for group,stored in zip(configured,saved['contracts'],strict=True):
        assert group['id']==stored['id']
        payload=consistency.request(cfg,model,group)
        assert canonical_request_hash(dict(payload=payload,policy=policy))==stored['input_sha256'],group['id']
        for field in ('claims','sources','source_aliases'):assert payload[field]==stored[field],(group['id'],field)
        findings=[];n=0
        for batch in consistency.batches(payload,max_input_chars=cfg.agent.max_input_chars):
            request=dict(system=consistency.SYSTEM,user=json.dumps(consistency.wire_payload(batch),ensure_ascii=False,separators=(',',':')),response_schema=consistency.schema(batch))
            identity=dict(purpose='cross-document-consistency',policy=policy,source_commit=payload['source_commit'],request=request,
                execution=dict(runner=cfg.agent.runner,model=cfg.agent.model,command=cfg.agent.command,arguments=arguments(cfg.agent,request['response_schema'])))
            key=checksum(UnitStore.draft_identity(identity))
            state=json.loads((native_root/'publication-e117/build/cli-checkpoints'/f'{key}.json').read_bytes())
            body=state['payload'];assert state['sha256']==checksum(body) and body['identity']==identity
            calls=native_root/'publication-e117/build/prompts/calls'
            records=[load_record(calls/name,root=calls) for name in body['receipts']]
            assert records
            for record in records:verify_cli_receipt(record.request,record.raw,record.receipt,calls,cfg.agent)
            assert any(record.request==request and record.raw==body['raw'] for record in records)
            checked=consistency.validate(batch,body['raw'])
            assert checked==body['statements']
            findings+=checked;n+=1;report['batches']+=1;report['receipts']+=len(records)
        assert findings==stored['findings'],group['id']
        report['contracts'].append(dict(id=group['id'],claims=len(payload['claims']),batches=n,counts=dict(collections.Counter(f['status'] for f in findings))))
    all_findings=[f for c in saved['contracts'] for f in c['findings']]
    assert len(all_findings)==386 and report['batches']==report['receipts']==88
    assert saved['status']=='passed' and saved['human_review']=='pending'
    assert len(saved['unresolved'])==1 and saved['unresolved'][0]['status']=='insufficient-evidence'
    assert saved['unresolved'][0]['claim_id']=='scenarios/queue_request.md/paragraph/28'
    report.update(passed=True,findings=len(all_findings),counts=dict(collections.Counter(f['status'] for f in all_findings)),
        unresolved=saved['unresolved'],comparison_scope=saved['comparison_scope'],human_review='pending')
except Exception as exc:report['error']=dict(type=type(exc).__name__,message=str(exc))
finally:(w/'public52-audit-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report.get(k) for k in ('passed','batches','receipts','findings','counts','error')},ensure_ascii=False))
raise SystemExit(0 if report['passed'] else 1)
