from pathlib import Path
import yaml,json,shutil
root=Path.cwd(); w=root/'build/issue241/public-case-02'
backup=w/'pre-integration-inputs'; backup.mkdir(exist_ok=False)
for n in ['sdd.yaml','sections.yaml','comparison-plan.json','operation.json']:
    shutil.copyfile(w/n,backup/n)
sections=yaml.safe_load((w/'sections.yaml').read_text(encoding='utf-8'))
s=sections['sections'][0]
s['answers']=['세 거절 검사의 순서와 반환값은 무엇입니까?', '어느 검사까지 통과해야 요청과 버퍼가 연결됩니까?']
s['next']={'title':'발행 검증 표본의 시작','link':'index.md'}
q=s['design_topics'][0]['question']; q=q[:q.index('전달받은 fence')]+'전달받은 fence의 이동과 실패 시 소유권은 이 표본 범위에서 제외하세요.'
s['design_topics'][0]['question']=s['design_requirements'][0]['question']=q
(w/'sections.yaml').write_text(yaml.safe_dump(sections,allow_unicode=True,sort_keys=False),encoding='utf-8')
contracts={'contracts':[dict(id='buffer-rejection',question=q,primary='camera-requests.md',documents=['camera-requests.md'],match='addBuffer|EINVAL|EEXIST|setRequest|pending_',evidence=['camera-requests/request/buffer-code'])]}
(w/'contracts.yaml').write_text(yaml.safe_dump(contracts,allow_unicode=True,sort_keys=False),encoding='utf-8')
cfg=yaml.safe_load((w/'sdd.yaml').read_text(encoding='utf-8'))
cfg['paths']['consistency_file']='contracts.yaml'
cfg['site'].update(translation_batch_size=12,mermaid_dir=str(root/'build/issue241/public/docs/assets/mermaid'),mermaid='assets/mermaid/mermaid.esm.min.mjs')
(w/'sdd.yaml').write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False),encoding='utf-8')
plan=json.loads((w/'comparison-plan.json').read_bytes())
plan.update(question=q,deployment='Dedicated source-bound validation site under docs/validation/issue241; main handbook and its review claims retained.',pre_inference_adjustment='Before successful adoption/native drafting: remove dangling separate-topic reference, retain rejection/linking scope, bind bilingual contract and local Mermaid assets.',excluded=['Main handbook-wide regeneration and review.','Whole #215/#163 audit.','Passed-fence failure ownership.'],measurement='Compare preregistered plan with actual first execution and identical resume. Prerequisite/mutation refusals count actual calls only. No unobserved baseline time or prevented call total inferred.')
(w/'comparison-plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Pre-inference integration complete; originals:',backup)
