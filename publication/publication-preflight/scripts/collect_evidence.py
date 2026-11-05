from pathlib import Path
from datetime import datetime
import hashlib,json
root=Path.cwd();w=root/'build/preflight-native';good=w/'native-good-01';bad=w/'native-bad-02';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def runs(case):return [json.loads(p.read_bytes()) for p in (case/'build/generation-runs').glob('*.json')]
bad_inv=json.loads((bad/'invocations/01-missing-target.json').read_bytes());bad_runs=runs(bad)
assert bad_inv['exit_code']!=0 and bad_inv['before']==bad_inv['after'] and not any(r['calls'] for r in bad_runs)
assert any(p['name']=='translation-preflight' and p['status']=='failed' and 'next-step target missing' in p['error'] for r in bad_runs for p in r['phases'])
invocations=[json.loads(p.read_bytes())|{'name':p.stem} for p in sorted((good/'invocations').glob('*.json'))]
assert all(i['status']=='passed' for i in invocations)
merge=json.loads((w/'generator-merge.json').read_bytes());merged_at=datetime.fromisoformat(merge['mergedAt'].replace('Z','+00:00')).timestamp()
before=[i for i in invocations if int(i['name'][:2])<=7];assert len(before)==7 and all(i['finished_at']<merged_at for i in before)
records={}
for p in (good/'build').rglob('*.receipt.json'):
    r=json.loads(p.read_bytes())
    if r.get('cli_call'):
        identity=hashlib.sha256(json.dumps(r,sort_keys=True).encode()).hexdigest();records.setdefault(identity,dict(path=str(p.relative_to(good)),tag=r['tag'],model=r['model'],completed_at=r['completed_at']))
reviewed=json.loads((good/'reviewed-before-export.json').read_bytes());assert all(sha(good/p)==h for p,h in reviewed.items())
ci=json.loads((w/'ci-pr-final.json').read_bytes());assert ci['conclusion']=='success' and all(j['conclusion']=='success' for j in ci['jobs'])
manifest=json.loads((good/'site/site-manifest.json').read_bytes())
result=dict(schema=1,scope='Pretranslation missing-target refusal plus a newly generated public supplied-fence condition; not a same-content speed benchmark.',
    missing_target=dict(model_calls=0,translation_preflight='failed-as-required',previous_manuscript_catalog_sha256_preserved=True,invocation=bad_inv),
    earlier_fixture='bad01 used an extra paragraph separator and reached the existing body-integrity rejection. Its original attempt is retained and not credited as the intended missing-target check.',
    premerge_native_pipeline=dict(passed=True,all_seven_stages_finished_before_merge=True,merge=merge),
    native_document_calls=len(records),receipts=list(records.values()),invocations=invocations,
    translation=dict(completed_transport_attempts=9,initial_batches=8,response_validation_retries=1,
        retry_tag='translation_batch_0_1',reason='The first response repeated {{0}} in string12; existing exact-placeholder validation rejected it.',
        source_input_correction_retranslation=0,assessment='Required response correction is retained; preflight does not remove this validation.'),
    independent_content=json.loads((good/'build/consistency-review.json').read_bytes())['status'],
    independent_diagram=json.loads((good/'build/diagram-review.json').read_bytes())['status'],
    reviewed_manuscript_catalog_preserved=True,site_build_id=manifest['build_id'],site_outputs=len(manifest['outputs']),
    ci_url=ci['url'],human_review='pending',limits=['Original/checkpoint receipt copies count once.',
      'Code review is separate from native document calls; CI transports are explicit test doubles.',
      'Parent/nested journal seconds overlap; invocation wall times are separate.',
      'Historical #241 extra translation batch had four strings; this refusal does not establish a general time saving or all its first eight legitimate translation calls being avoidable.',
      'The new healthy reader question and public profile differ from the historical sample. No same-input old-generator native baseline or external-wait critical path was measured.',
      'The earlier bad01 preparation correction cost work and is not hidden as prevented rework.'])
(w/'comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['native_document_calls','reviewed_manuscript_catalog_preserved','site_build_id','site_outputs']},ensure_ascii=False))
