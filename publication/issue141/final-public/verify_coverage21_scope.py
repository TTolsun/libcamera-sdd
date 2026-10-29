"""Explain each unresolved coverage item without changing classification or approval."""
from pathlib import Path
import subprocess,json,hashlib,datetime
w=Path(__file__).resolve().parent
repo=w/'libcamera-full'; proof=w/'public-sdd/publication/issue141'
old=json.loads((proof/'full-scope-tagged/impact/impact.json').read_bytes())
current=json.loads((w/'e117-impact-main160-verified/build/impact.json').read_bytes())
base='182307a772ebebf173ee84911906da707718485f';head='e117198c015057761bb0bbaa85f963c41ce412d7'
assert old['head']==base and current['head']==head
oldkeys={(r['reason'],r['kind'],r['name']) for r in old['coverage']['findings']}
newkeys={(r['reason'],r['kind'],r['name']) for r in current['coverage']['findings']}
assert oldkeys==newkeys and len(newkeys)==21
published=w/'public-release-547fdf05/publication/goal-138-140'
facts=json.loads((published/'facts/facts.json').read_bytes())
assert facts['meta']['source_commit']==head
files={r['file']:r for r in current['coverage']['files']}
rows=[]
for r in current['coverage']['findings']:
    p=r['name'];a=subprocess.check_output(['git','-C',str(repo),'show',base+':'+p]);b=subprocess.check_output(['git','-C',str(repo),'show',head+':'+p])
    assert a==b,p
    if '/data/' in p and ('/rpi/' in p or 'mira220' in p):
        category='sensor tuning values (real calibration changes before182; not declared harmless)'
    elif p.endswith('meson.build'):
        category='install new sensor tuning file (build configuration; not a C++ entity)'
    elif '/virtual/' in p:
        category='virtual camera location configuration names (real input contract change before182)'
    else:
        category='control/property enumerator names and bindings/code-generation templates (real source change before182)'
    rows.append({'finding':r,'source_sha256_at182_and_e117':hashlib.sha256(b).hexdigest(),
        'unchanged_182_to_e117':True,'category':category,'watch_sections':files[p]['watch_sections'],
        'coverage_status':files[p]['status'],'approval':'not recorded',
        'documentation_adequacy':'Unresolved file-to-entity coverage; full e117 rebuild is not proof of complete prose coverage for this file'})
changed=subprocess.check_output(['git','-C',str(repo),'diff','--name-only',base,head],text=True).splitlines()
incremental=json.loads((published/'impact.json').read_bytes())
assert incremental['base']==base and incremental['head']==head and not incremental['coverage']['findings']
assert set(changed)==set(incremental['changed_files'])
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,
 'scope':'Per-file immutable source and coverage provenance; no policy/classification/approval/output mutation or content-completeness claim',
 'unresolved_count':21,'same_finding_keys_as_recorded182_run':True,'all21_source_files_unchanged182_to_e117':True,
 'new_upstream_changed_files':changed,'published_incremental_coverage_findings':0,
 'published_facts_source':head,'rows':rows,
 'completion_boundary':'The #141 acceptance condition requires impact analysis and preservation of refusal/approval contracts, not automatic acceptance of every project coverage item. The full-range coverage gate remains failed and all21 unresolved; latest upstream3changedC++files have a separate actual incremental report. Whole current-source extraction/generation/translation/audit and publication are independently verified, but do not prove prose completeness for these21files.',
 'semantic90_cases_are_separate':True,'human_acceptances_recorded':0,'sdd_accept_executed':False}
(w/'coverage21-scope.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('passed','unresolved_count','same_finding_keys_as_recorded182_run','all21_source_files_unchanged182_to_e117','new_upstream_changed_files')}))
