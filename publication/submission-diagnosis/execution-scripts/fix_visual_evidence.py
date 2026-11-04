from pathlib import Path
import yaml,json,copy
W=Path(__file__).resolve().parent;R=W/'draft';facts=json.loads((R/'run/facts/facts.json').read_bytes())['evidence'];sid='request-diagnosis'
paths=[Path('examples/libcamera/config/visuals.yaml'),R/'config/visuals.yaml']
for path in paths:
 d=yaml.safe_load(path.read_bytes());vs=d['sections'][sid]
 for v in vs:
  for item in v['nodes']+v['edges']:
   for e in item['evidence']:
    text=facts[sid+'/'+e['source']]['text'];q=e['quote']
    if text.count(q)==1:continue
    assert text.count(q)>1,(v['id'],q)
    if q=='return -EINVAL;':
     start=text.index('if (request->status()');end=text.index('\n\t}',start)+3;e['quote']=text[start:end]
    elif q=='This function shall be called from the CameraManager thread.':
     marker='\\context '+q;start=text.index(marker)
     if v['id']=='diagnosis-submission-order-completion':start=text.index(marker,start+1)
     end=text.index('\n{',start);e['quote']=text[start:end]
    else:raise ValueError(q)
    assert text.count(e['quote'])==1
 source='configuration-failure/configure';record=facts[sid+'/'+source];text=record['text']
 def proof(q):assert text.count(q)==1,q;return [dict(source=source,sha256=record['sha256'],quote=q)]
 def node(id,ko,en,q,shape='box'):return dict(id=id,label=ko,label_en=en,shape=shape,evidence=proof(q))
 def edge(a,b,ko,en,q):return {'from':a,'to':b,'label':ko,'label_en':en,'evidence':proof(q)}
 loop='for (const StreamConfiguration &cfg : *config)';null='if (!stream)';fail='LOG(Camera, Fatal)\n\t\t\t\t<< "Pipeline handler failed to update stream configuration";\n\t\t\td->activeStreams_.clear();\n\t\t\treturn -EINVAL;'
 v=dict(id='configuration-stream-link',topic='configuration-failure',kind='flow',title='구성 성공 뒤 스트림 연결을 확인하는 분기',question='상태 검사·검증과 PipelineHandler::configure 성공 뒤 cfg.stream()이 null인 경우 어떤 코드 위치를 관찰합니까?',nodes=[node('start','선행 검사·configure 성공 뒤','After checks and configure succeed','if (ret)\n\t\treturn ret;\n\n\td->activeStreams_.clear();'),node('stream','각 cfg.stream() 관찰','Observe each cfg.stream()',loop+' {\n\t\tStream *stream = cfg.stream();'),node('null','stream이 null인가?','Is stream null?',null,'decision'),node('failure','Fatal 로그 → activeStreams_ 비움 → -EINVAL','Fatal log → clear activeStreams_ → -EINVAL',fail),node('valid','configuration_ 연결·activeStreams_ 삽입','Assign configuration_ and insert active stream','stream->configuration_ = cfg;\n\t\td->activeStreams_.insert(stream);'),node('next','남은 스트림 반복 뒤 Configured·0','After remaining streams: Configured and 0','d->setState(Private::CameraConfigured);\n\n\treturn 0;')],edges=[edge('start','stream','각 항목','Each entry',loop),edge('stream','null','기존 결과 확인','Check original result',null),edge('null','failure','예: 실패 코드 위치','Yes: failure code locations',fail),edge('null','valid','아니요','No','stream->configuration_ = cfg;'),edge('valid','next','반복 후','After loop','d->setState(Private::CameraConfigured);\n\n\treturn 0;')])
 if not any(x['id']==v['id'] for x in vs):vs.insert(3,v)
 path.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.visuals import render
c=load(R/'publication.yaml');m=KnowledgeModel.load(c.facts_path);s=next(s for s in c.sections() if s['id']==sid);graphs=render(c,m,s);assert len(graphs)==10 and all(g[2] for g in graphs)
print('All 10 graphs have unique, current source evidence and emitted Mermaid.')
