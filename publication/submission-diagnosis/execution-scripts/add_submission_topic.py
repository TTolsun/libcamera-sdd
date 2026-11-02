from pathlib import Path
import copy,json,yaml
from sdd.config import load
from sdd.evidence import collect
from sdd.facts.model import KnowledgeModel
from sdd.visuals import render

root=Path(__file__).resolve().parents[2]; w=Path(__file__).resolve().parent; out=w/'draft'
topic=dict(id='submission-checks',title='요청 제출 오류 코드와 검사 순서',question='Camera::queueRequest()가 요청을 거부하는 조건을 반환값과 실제 검사 순서로 구분하세요.',covers=['submission-checks'],design_prompt='focused',sources=[
 dict(id='queue',file='src/libcamera/camera.cpp',start='\\brief Queue a request to the camera',end='\\brief Start capture from camera'),
 dict(id='access',file='src/libcamera/camera.cpp',start='int Camera::Private::isAccessAllowed(State state, bool allowDisconnected,',end='int Camera::Private::isAccessAllowed(State low, State high,')],parts=[])
def part(id,q,sources,terms,basis='implementation'):
 return dict(id=id,question=q,sources=sources,max_statements=1,answer_contract=dict(basis=basis,required_terms=[[x] for x in terms]))
topic['parts']=[
 part('access','queueRequest의 첫 검사는 isAccessAllowed(CameraRunning)입니다. 연결 해제와 Running 상태가 아닌 경우를 -ENODEV 및 -EACCES에 연결하고, 음수이면 요청 내용 검사 전에 그대로 반환한다는 순서를 세 문장 이내로 설명하세요. 이 항목은 조사 명령이나 실행 결과가 아니라 구현 설명입니다.',['queue','access'],['isAccessAllowed','CameraRunning','-ENODEV','-EACCES']),
 part('request','접근 검사를 통과한 뒤 요청 생성 카메라, RequestPending 상태, controls().infoMap() 비교를 순서대로 설명하세요. 생성 카메라 불일치는 -EXDEV, 나머지 두 실패는 -EINVAL이며 controls 목록을 다른 목록으로 덮어쓰지 못하게 검사한다는 의미를 보존하세요. 네 문장 이내로 답하세요.',['queue'],['-EXDEV','-EINVAL','RequestPending','infoMap']),
 part('buffers','버퍼 맵이 비어 있으면 -EINVAL을 반환하고, 그 다음 각 버퍼의 스트림이 activeStreams_에 있는지 검사하여 없는 스트림에도 -EINVAL을 반환함을 두 문장으로 설명하세요. 같은 오류 코드가 서로 다른 실패 원인을 뜻하므로 검사 지점을 함께 구분하세요.',['queue'],['버퍼','activeStreams_','-EINVAL']),
 part('handoff','모든 앞선 검사를 통과한 경우 patchControlList로 AeEnable을 전처리한 뒤 PipelineHandler::queueRequest를 ConnectionTypeQueued로 예약하고 0을 반환하는 구현을 두 문장 이내로 설명하세요. 0이 요청 완료를 뜻한다고 쓰지 마세요. 완료·준비 대기 상세는 다음 진단 절에서 다루므로 반복하지 마세요.',['queue'],['patchControlList','AeEnable','ConnectionTypeQueued','0']),
 part('allocation','queueRequest API 주석의 -ENOMEM 반환 설명과 제공된 queueRequest 구현의 명시적 반환 분기를 구분하세요. 주석에는 메모리 할당 실패가 나열되지만 이 발췌 함수 본문에 -ENOMEM을 직접 반환하는 분기가 없으므로 어느 할당이 실패했다고 단정하지 마세요. 두 문장 이내로 설명하세요.',['queue'],['-ENOMEM','주석','구현'],basis='description')]
for path in [out/'config/sections.yaml',root/'examples/libcamera/config/sections.yaml']:
 data=yaml.safe_load(path.read_text(encoding='utf-8'));s=next(s for s in data['sections'] if s['id']=='request-diagnosis')
 if any(t['id']=='submission-checks' for t in s['design_topics']):raise SystemExit('Already prepared')
 s['design_topics'].insert(1,copy.deepcopy(topic))
 s['design_requirements'].append(dict(id='submission-checks',question='요청 제출 실패의 반환값을 어느 입력과 검사 순서에 연결합니까?',aspects=['failure']))
 path.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
cfg=load(out/'generation.yaml');m=KnowledgeModel.load(cfg.facts_path)
before={k:v.get('sha256') for k,v in m.evidence.items()};collect(cfg,m)
assert all(m.evidence[k].get('sha256')==v for k,v in before.items() if k in m.evidence)
m.save(cfg.facts_path)
records={k.rsplit('/',1)[-1]:v for k,v in m.evidence.items() if k.startswith('request-diagnosis/submission-checks/')}
assert all(v['status']=='available' for v in records.values()),records
def proof(source,quote):
 r=records[source];assert quote in r['text'],quote
 return [dict(source='submission-checks/'+source,sha256=r['sha256'],quote=quote)]
def node(id,ko,en,quote,source='queue',decision=False):
 d=dict(id=id,label=ko,label_en=en,evidence=proof(source,quote))
 if decision:d['shape']='decision'
 return d
nodes=[
 node('access','접근 검사: CameraRunning','Access check: CameraRunning','int ret = d->isAccessAllowed(Private::CameraRunning);',decision=True),
 node('access-error','-ENODEV 또는 -EACCES','-ENODEV or -EACCES','if (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;','access'),
 node('owner','생성한 카메라와 같은가?','Same camera that created the request?','if (request->_d()->camera() != this)',decision=True),
 node('other-camera','-EXDEV','-EXDEV','return -EXDEV;'),
 node('pending','RequestPending인가?','Is status RequestPending?','if (request->status() != Request::RequestPending)',decision=True),
 node('controls','원래 controls 정보 맵인가?','Original controls info map?','if (request->controls().infoMap() != &controls())',decision=True),
 node('buffers','버퍼가 하나 이상 있는가?','At least one buffer?','if (request->buffers().empty())',decision=True),
 node('streams','모든 스트림이 활성 상태인가?','Every stream active?','if (d->activeStreams_.find(stream) == d->activeStreams_.end())',decision=True),
 node('invalid','-EINVAL: 실패 검사 구분','-EINVAL: identify the failed check','return -EINVAL;'),
 node('queued','AeEnable 전처리 후 queued 호출','Preprocess AeEnable; queue the call','patchControlList(request->controls());'),
 node('success','0 반환','Return 0','return 0;')]
edges=[]
def edge(a,b,ko,en,q,source='queue'):edges.append(dict(**{'from':a,'to':b},label=ko,label_en=en,evidence=proof(source,q)))
edge('access','access-error','ret < 0','ret < 0','if (ret < 0)\n\t\treturn ret;')
edge('access','owner','접근 검사 통과','Access check passes','/* Requests can only be queued to the camera that created them. */')
edge('owner','other-camera','아니요','No','if (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << "Request was not created by this camera";\n\t\treturn -EXDEV;\n\t}')
edge('owner','pending','예','Yes','if (request->status() != Request::RequestPending)')
edge('pending','invalid','아니요','No','if (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << " is not valid";\n\t\treturn -EINVAL;\n\t}')
edge('pending','controls','예','Yes','/* Make sure the Request has a valid control list. */')
edge('controls','invalid','아니요','No','if (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << "Overwriting Request::controls() is not allowed";\n\t\treturn -EINVAL;\n\t}')
edge('controls','buffers','예','Yes','if (request->buffers().empty())')
edge('buffers','invalid','아니요','No','if (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << "Request contains no buffers";\n\t\treturn -EINVAL;\n\t}')
edge('buffers','streams','예','Yes','for (const auto &[stream, buffer] : request->buffers())')
edge('streams','invalid','아니요','No','if (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << "Invalid request";\n\t\t\treturn -EINVAL;\n\t\t}')
edge('streams','queued','예','Yes','/* Pre-process AeEnable. */')
edge('queued','success','예약 후 반환','Return after scheduling','d->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;')
visual=dict(id='submission-checks',topic='submission-checks',kind='decision',title='요청 제출 검사 순서',question='반환 오류를 실제 검사 조건과 연결합니다. 성공 반환 뒤의 준비와 완료는 다음 절에서 확인합니다.',nodes=nodes,edges=edges)
for path in [out/'config/visuals.yaml',root/'examples/libcamera/config/visuals.yaml']:
 data=yaml.safe_load(path.read_text(encoding='utf-8'));data['sections'].setdefault('request-diagnosis',[]).append(visual)
 path.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
s=next(s for s in cfg.sections() if s['id']=='request-diagnosis');render(cfg,m,s)
print('Added five source-bound submission questions and 11-node diagram; existing evidence hashes preserved.')
