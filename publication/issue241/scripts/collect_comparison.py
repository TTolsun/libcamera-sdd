"""Read this fixed case's existing journals; never infer missing work or time."""
from pathlib import Path
from datetime import datetime
import hashlib,json
w=Path.cwd()/'build/issue241/public-case-02'
runs=[]
for path in (w/'build/generation-runs').glob('*.json'):
    run=json.loads(path.read_bytes());runs.append((path,run))
receipts=[];seen={}
for path in (w/'build').rglob('*.receipt.json'):
    receipt=json.loads(path.read_bytes())
    if receipt.get('cli_call') is True:
        identity=hashlib.sha256(json.dumps(receipt,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        if identity in seen:
            seen[identity].append(str(path.relative_to(w)))
            continue
        seen[identity]=[str(path.relative_to(w))]
        receipts.append((path,receipt,datetime.fromisoformat(receipt['completed_at']).timestamp()))
rows=[]
for path in sorted((w/'invocations').glob('*.json')):
    inv=json.loads(path.read_bytes())
    if 'command' not in inv or 'finished_at' not in inv:continue
    selected=[(p,r) for p,r in runs if inv['started_at']<=r.get('started_at',0)<=inv['finished_at']]
    calls=[c for _,r in selected for c in r['calls']]
    native=[p for p,_,at in receipts if inv['started_at']<=at<=inv['finished_at']]
    rows.append(dict(invocation=path.stem,status='no-op-preparation-error' if path.stem=='06-translation' else inv['status'],
        exit_code=inv['exit_code'],generator_commit=inv['generator_commit'],
        wall_seconds=inv['wall_seconds'],transport_attempts=len(calls),
        completed_attempts=sum(c['status']=='completed' for c in calls),
        failed_attempts=sum(c['status']=='failed' for c in calls),
        cli_seconds_sum=sum(c.get('seconds',0) for c in calls),
        successful_native_receipts=[str(p.relative_to(w)) for p in native],
        runs=[dict(path=str(p.relative_to(w)),publication=r.get('publication'),
                   counts=r['counts'],phases=r['phases'],plans=r.get('publication_plans',[]),
                   decisions=r.get('decisions',[])) for p,r in selected]))
revisions=[]
for path in sorted((w/'build/publication-operations').glob('*/revisions/*.json')):
    record=json.loads(path.read_bytes());c=record['payload']['contract']
    revisions.append(dict(path=str(path.relative_to(w)),revision=c['revision'],reason=c['reason'],
        change=c.get('change'),source_commit=c['source_commit'],discoveries=c['discoveries'],
        contract_sha256=record['payload']['contract_sha256'],basis_sha256=record['payload']['basis_sha256']))
first=json.loads((w/'after-first-output.json').read_bytes())
result=dict(schema=1,scope='Preregistered single public addBuffer rejection/linking question, not the whole handbook or internal HAL.',
    measurements=rows,revisions=revisions,first_plans_preserved=all((w/p).is_file() and hashlib.sha256((w/p).read_bytes()).hexdigest()==sha for p,sha in first['plans'].items()),
    receipts_total=len(receipts),receipt_copies=list(seen.values()),limits=[
        'Byte-equivalent receipt copies in original call directories and checkpoints count as the same call, not fresh inference.',
        'Native receipts are distinguished from transport attempts and controlled test doubles.',
        'Native drafting/translation/review calls here exclude separate generator code-review calls.',
        'Invocation wall time is measured separately. Parent preparation and nested translation records overlap; their seconds are not a wall-clock sum.',
        'Human work, source investigation, approval/CI/network waiting outside these invocations and causal critical paths were not measured.',
        'No same-input native old-generator baseline was run. General call/time savings and all 79 historical reviews being preventable are not established.',
        'A no-op module entrypoint invocation is retained as preparation error, not successful translation or CLI/model failure.'])
(w/'comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(receipts_total=len(receipts),first_plans_preserved=result['first_plans_preserved'],rows=[{k:r[k] for k in ('invocation','status','transport_attempts','wall_seconds')} for r in rows]),ensure_ascii=False))
