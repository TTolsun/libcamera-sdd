from pathlib import Path
import hashlib,json,os,subprocess,sys
import yaml
root=Path.cwd();w=root/'build/issue241/public-case-02'
folder=w/'changed-inputs';folder.mkdir(exist_ok=False)
sections=w/'sections.yaml';facts=w/'facts/facts.json';manuscript=w/'manuscripts/camera-requests.md'
original=sections.read_bytes();old_facts=facts.read_bytes();old_output=manuscript.read_bytes()
(folder/'sections-before.yaml').write_bytes(original)
(folder/'facts-before.json').write_bytes(old_facts)
values=yaml.safe_load(original);values['sections'][0]['design_topics'][0]['question']+=' 검사 순서를 다시 확인하세요.'
modified=yaml.safe_dump(values,allow_unicode=True,sort_keys=False).encode()
sections.write_bytes(modified);(folder/'sections-unrecorded.yaml').write_bytes(modified)
before=set((w/'build/generation-runs').glob('*.json'))
try:
    code=subprocess.run([sys.executable,str(root/'build/issue241/invoke_case.py'),'03-unrecorded-input','generate'],check=False).returncode
    (folder/'facts-after-refusal.json').write_bytes(facts.read_bytes())
    paths=set((w/'build/generation-runs').glob('*.json'))-before
    assert code!=0 and len(paths)==1
    run=json.loads(next(iter(paths)).read_bytes())
    assert run['calls']==[] and 'new revision' in run['phases'][-1]['error']
    assert manuscript.read_bytes()==old_output
    report=dict(status='expected-refusal',calls=0,run=str(next(iter(paths)).relative_to(w)),manuscript_sha256=hashlib.sha256(old_output).hexdigest(),previous_output_preserved=True,reason=run['phases'][-1]['error'])
    (folder/'result.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))
finally:
    if sections.read_bytes()!=modified:raise RuntimeError('External section edit preserved; manual reconciliation required')
    sections.write_bytes(original)
    facts.write_bytes(old_facts)
