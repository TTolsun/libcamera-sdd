"""Check the committed inputs and pure contracts without rendering or inference."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import yaml
from sdd.document_metadata import split_frontmatter
from sdd.design_response import validate_answers
from sdd.evidence import fingerprint
from sdd.facts.model import KnowledgeModel
from sdd.site_localization import KOREAN,display_strings,selector,source_hash
from sdd.translation import _validate_text

w=Path('build/issue141');release=w/'public-release-46235b02';package=release/'publication/goal-138-140'
manifest=json.loads((release/'docs/site-manifest.json').read_bytes())
run=json.loads((release/'run.json').read_bytes())
result=dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),public_commit='46235b026626db49ef98ba3a5e23d1359dbe3d0a',passed=False,new_model_calls=0,
    scope='All committed manifest input hashes, source/body identities, pure answer contracts and bilingual catalog completeness; not rerunning the environment-specific publication/reuse policy gate, human review or internal HAL/device validation')
def digest(data):return hashlib.sha256(data).hexdigest()
try:
    raw=yaml.safe_load((package/'executed-sdd.codex.local.yaml').read_text(encoding='utf-8'))
    assert digest(json.dumps(raw,sort_keys=True,default=str).encode())==manifest['inputs']['configuration']
    files={'facts':'facts/facts.json','sections':'sections.yaml','consistency_configuration':'config/contracts.yaml',
           'consistency_review':'consistency-review.json','english_catalog':'english.json','visuals':'config/visuals.yaml'}
    checked={'configuration':'Exact effective YAML object hash'}
    for key,name in files.items():
        assert digest((package/name).read_bytes())==manifest['inputs'][key],key
        checked[key]=name
    intro=subprocess.check_output(['git','show',run['generator_commit']+':examples/libcamera/site-intro.md'])
    assert manifest['inputs']['intro'] in {digest(intro),digest(intro.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'))}
    checked['intro']='Merged generator example, exact Git/LF-or-CRLF checkout bytes'
    for key,expected in manifest['inputs'].items():
        if key.startswith('markdown/'):
            assert digest((package/'manuscripts'/key[len('markdown/'):]).read_bytes())==expected,key
            checked[key]='Committed original manuscript bytes'
    assert set(checked)==set(manifest['inputs'])
    result['manifest_inputs_verified']=len(checked)
    model=KnowledgeModel.load(package/'facts/facts.json')
    assert model.meta['source_commit']==run['source_commit']=='e117198c015057761bb0bbaa85f963c41ce412d7'
    sections=yaml.safe_load((package/'sections.yaml').read_text(encoding='utf-8'))['sections']
    assert len(sections)==22
    docs=list((package/'manuscripts').rglob('*.md'))
    assert len(docs)==28
    section_by_output={s['output']:s for s in sections}
    answer_pages=[];all_meta={}
    for path in docs:
        name=path.relative_to(package/'manuscripts').as_posix()
        meta,body=split_frontmatter(path.read_text(encoding='utf-8'))
        assert meta['source_commit']==run['source_commit'],name
        all_meta[name]=meta
        artifact=meta.get('generated_design')
        if not artifact:continue
        section=section_by_output[name]
        assert meta['agent']=='cli/codex/gpt-6.1-terra',name
        assert all(agent=='cli/codex/gpt-6.1-terra' for agent in artifact['topic_agents'].values()),name
        assert artifact['body_sha256']==digest(body.strip().encode()),name
        assert artifact['input_fingerprint']==fingerprint(model,section),name
        _,resolved,report=validate_answers(model,section,artifact['answers'])
        assert report['human_review']=='pending',name
        answer_pages.append(dict(path=name,topics=len(artifact['answers']),pure_contract_status=report['status'],body_sha256=artifact['body_sha256'],validation_policy=artifact['validation_policy']))
    assert len(answer_pages)==19 and sum(p['topics'] for p in answer_pages)==69
    result.update(manuscripts_source_verified=len(docs),answer_pages=answer_pages,deterministic_pages=9)
    catalog=json.loads((package/'english.json').read_bytes());assert catalog['schema']==1 and catalog['review_status']=='human-review-pending'
    units=set();page_hashes={};english_korean=[]
    def remove_selector(document,rel,english):
        sample=selector('<head></head><div class="header-actions">END',rel,english)
        alts=sample.split('<head>')[1].split('</head>')[0]
        control=sample.split('<div class="header-actions">')[1].removesuffix('END')
        assert document.count(alts)==document.count(control)==1,rel
        return document.replace(alts,'',1).replace(control,'',1)
    for rel,expected in catalog['pages'].items():
        ko=remove_selector((release/'docs'/rel).read_text(encoding='utf-8'),rel,False)
        assert source_hash(ko)==expected,rel
        page_hashes[rel]=expected;units.update(display_strings(ko))
        en=remove_selector((release/'docs/en'/rel).read_text(encoding='utf-8'),rel,True)
        if display_strings(en):english_korean.append(rel)
    for entry in json.loads((release/'docs/assets/search.json').read_bytes()):
        units.update(entry[k].strip() for k in ('title','page') if KOREAN.search(entry[k]))
    for item in json.loads((release/'docs/assets/glossary.json').read_bytes()):
        units.update(v.strip() for v in [item['term'],item['definition'],*item['names']] if KOREAN.search(v))
    assert set(catalog['strings'])==units
    for source,text in catalog['strings'].items():_validate_text(source,text)
    assert len(page_hashes)==30 and len(units)==1733 and not english_korean
    result.update(catalog_source_pages_verified=len(page_hashes),catalog_strings_verified=len(units),unprotected_korean_english_pages=english_korean,
        selector_hash_scope='Known language controls reversed in memory for pre-localization source hashes; no HTML edited')
    summary=json.loads((package/'merged-main-verification.json').read_bytes())
    generation=json.loads((package/'generation-runs'/summary['generation_record']).read_bytes())
    assert generation['calls']==[] and len(generation['documents'])==19
    assert all(d['status']=='passed' for d in generation['documents'])
    assert summary['generator_commit']==run['generator_commit'] and summary['source_commit']==run['source_commit']
    assert summary['manifest_build_id']==run['build_id']==manifest['build_id']
    assert summary['unit_counts']=={'manuscript-reused':313} and summary['repeat_identical']
    assert summary['audit_fresh_batches']==0 and summary['audit_reused_batches']==88 and summary['new_cli_receipts']==0
    assert summary['human_review']==run['human_review']=='pending' and run['inhouse_hal_verified'] is False
    result.update(passed=True,recorded_final_generation=dict(documents=19,reused_units=313,new_calls=0),
        recorded_final_audit=dict(reused_batches=88,new_calls=0),recorded_repeat_build=True,
        production_repeat_procedure='Reviewed actual final_main_verify.py: exact main and runtime-byte assertions, two complete manifest comparisons, verify_site and before/after native-receipt set equality. This check does not rerun that script.',
        published_runtime=summary['python'],current_verification_runtime=sys.version,publication_policy_gate_rerun_by_this_check=False)
except Exception as exc:
    result['error']=dict(type=type(exc).__name__,message=str(exc))
finally:
    (w/'public52-input-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result.get(k) for k in ('passed','manifest_inputs_verified','manuscripts_source_verified','catalog_source_pages_verified','catalog_strings_verified','error')},ensure_ascii=False))
raise SystemExit(0 if result['passed'] else 1)
