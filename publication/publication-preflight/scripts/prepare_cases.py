from pathlib import Path
import copy,hashlib,json,shutil,subprocess,yaml
root=Path.cwd();w=root/'build/preflight-native';old=root/'build/issue241/public-case-02'
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
question=('Request::addBuffer()에서 세 거절 검사를 통과한 뒤 전달받은 fence를 어떤 조건에서 버퍼로 이동합니까? '
          'fence && fence->isValid()와 setFence(std::move(fence))를 연결하고 null 또는 유효하지 않은 전달 fence에서는 '
          '이 분기를 실행하지 않는다는 점을 설명하세요. 앞선 거절 조건의 전체 설명과 실패 시 소유권·기기 동작은 제외하세요.')
for kind in ['bad','good']:
    case=w/('native-'+kind+'-01');assert not case.exists();case.mkdir()
    for name in ['facts','templates']:
        shutil.copytree(old/name,case/name)
    for name in ['review.yaml','scenarios.yaml']:
        shutil.copyfile(old/name,case/name)
    cfg=yaml.safe_load((old/'sdd.yaml').read_bytes())
    cfg['agent']=copy.deepcopy(yaml.safe_load((root/'examples/libcamera/sdd.yaml').read_bytes())['agent'])
    (case/'review.yaml').write_text(yaml.safe_dump(dict(agent=copy.deepcopy(cfg['agent'])),sort_keys=False),encoding='utf-8')
    cfg['publication']=dict(operation_id='publication-preflight-'+kind+'-01',operation_file='operation.json')
    sections=yaml.safe_load((old/'sections.yaml').read_bytes());section=sections['sections'][0]
    visual=yaml.safe_load((old/'visuals.yaml').read_bytes())
    contracts=yaml.safe_load((old/'contracts.yaml').read_bytes())
    if kind=='bad':
        shutil.copytree(old/'manuscripts',case/'manuscripts')
        shutil.copyfile(old/'english.json',case/'english.json')
        cfg['paths']['templates']=str(root/'templates')
        section['next']=dict(title='Missing',link='absent.md')
        manuscript=case/'manuscripts/camera-requests.md'
        manuscript.write_bytes(manuscript.read_bytes()+b'\n\n'+ '다음 단계: [Missing](absent.md)\n'.encode())
    else:
        section.update(title='addBuffer의 전달 fence 조건',lead='전달 fence가 버퍼로 이동하는 조건을 확인합니다.',
                       answers=['어떤 전달 fence에서 setFence 호출을 실행합니까?'])
        topic=section['design_topics'][0]
        topic.update(title='전달 fence의 이동 조건',question=question,
                     answer_contract=dict(basis='implementation',required_terms=[[x] for x in ['addBuffer','fence','isValid','setFence','move']]))
        section['design_requirements'][0]['question']=question
        contracts['contracts'][0].update(id='fence-transfer',question=question,match='addBuffer|fence|isValid|setFence')
        model=json.loads((case/'facts/facts.json').read_bytes());record=model['evidence']['camera-requests/request/buffer-code']
        def proof(quote):
            assert record['text'].count(quote)==1
            return [dict(source='request/buffer-code',sha256=record['sha256'],quote=quote)]
        condition='if (fence && fence->isValid())';move='buffer->_d()->setFence(std::move(fence));'
        block=record['text'][record['text'].index(condition):]
        def node(ident,ko,en,quote,decision=False):
            v=dict(id=ident,label=ko,label_en=en,evidence=proof(quote))
            if decision:v['shape']='decision'
            return v
        def edge(a,b,ko,en,quote):return dict(**{'from':a,'to':b},label=ko,label_en=en,evidence=proof(quote))
        diagram=dict(id='fence-transfer',topic='request',kind='decision',title='전달 fence의 조건부 이동',question=question,
            nodes=[node('linked','앞선 검사와 버퍼 연결 통과','Earlier checks and buffer linking passed','buffer->_d()->setRequest(this);'),
                   node('valid','전달 fence가 있고 isValid()인가?','Is a supplied fence present and valid?',condition,True),
                   node('move','setFence(std::move(fence)) 호출','Call setFence(std::move(fence))',move),
                   node('done','0 반환','Return 0','return 0;')],
            edges=[edge('linked','valid','조건 검사','Check condition',record['text'][record['text'].index('buffer->_d()->setRequest(this);'):]),
                   edge('valid','move','예','Yes',block),edge('valid','done','아니요','No',block),edge('move','done','반환','Return',block)])
        # Keep the project-owned document/diagram schema from the original fixture.
        visual['sections']['camera-requests']=[diagram]
        cfg['publication']['reports']=[dict(path='build/consistency-review.json',gate='before-export',producer='consistency.audit',sha256='0'*64,bindings=dict(status='passed',source_commit=model['meta']['source_commit'])),
            dict(path='build/diagram-review.json',gate='before-export',producer='independent-diagram-review',sha256='0'*64,bindings=dict(status='passed',source_commit=model['meta']['source_commit']))]
    operation=json.loads((old/'operation.json').read_bytes())
    operation.update(revision=1,reason='Preregister pretranslation refusal and the first-merge native integration sample.',prerequisites=[],discoveries=[])
    operation.pop('change',None)
    operation['integration']=dict(root='../../..',ref='refs/heads/codex/publication-preflight-integration',commit=head)
    for name,data in [('sdd.yaml',cfg),('sections.yaml',sections),('visuals.yaml',visual),('contracts.yaml',contracts)]:
        (case/name).write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
    (case/'operation.json').write_text(json.dumps(operation,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    files={p.relative_to(case).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in case.rglob('*') if p.is_file()}
    (case/'preregistered-inputs.json').write_text(json.dumps(dict(generator_commit=head,kind=kind,question=question if kind=='good' else 'Deliberate archival fixture mutation, not fresh generation.',files=files),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(case)
