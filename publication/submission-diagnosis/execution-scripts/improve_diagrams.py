from pathlib import Path
import copy,json,yaml
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.visuals import render
root=Path(__file__).resolve().parents[2];w=Path(__file__).resolve().parent;o=w/'draft'
cfg=load(o/'publication.yaml');m=KnowledgeModel.load(cfg.facts_path)
data=yaml.safe_load((o/'config/visuals.yaml').read_text(encoding='utf-8'))
graphs=data['sections']['request-diagnosis'];new=[]
def transplant(sid,id,topic,newid=None):
 g=copy.deepcopy(next(g for g in data['sections'][sid] if g['id']==id));assert 'producer' not in g
 g['topic']=topic;g['id']=newid or 'diagnosis-'+id
 for item in g['nodes']+g['edges']:
  for e in item['evidence']:
   candidates=[(k,r) for k,r in m.evidence.items() if k.startswith('request-diagnosis/'+topic+'/') and e['quote'] in r.get('text','')]
   assert candidates,(id,e['quote'])
   key,r=min(candidates,key=lambda kv:len(kv[1]['text']))
   e.update(source=key.split('/',1)[1],sha256=r['sha256'])
 return g
replacement=transplant('request-lifecycle','waiting-queue-conditions','diagnosis','queue-gates')
graphs[graphs.index(next(g for g in graphs if g['id']=='queue-gates'))]=replacement
for sid,id in [('camera-requests','add-buffer-rejections'),('request-lifecycle','dispatch-cancel-or-device'),('request-lifecycle','buffer-and-request-completion'),('request-lifecycle','submission-order-completion')]:
 new.append(transplant(sid,id,'diagnosis'))
def proof(s,q):
 r=m.evidence['request-diagnosis/configuration-failure/'+s];assert q in r['text'],q
 return [dict(source='configuration-failure/'+s,sha256=r['sha256'],quote=q)]
def node(id,ko,en,s,q,decision=False):
 d=dict(id=id,label=ko,label_en=en,evidence=proof(s,q))
 if decision:d['shape']='decision'
 return d
def edge(a,b,ko,en,s,q):return dict(**{'from':a,'to':b},label=ko,label_en=en,evidence=proof(s,q))
new.append(dict(id='configuration-access-branches',topic='configuration-failure',kind='decision',title='구성 접근 검사에서 관찰할 분기',question='연결 해제를 먼저 확인한 뒤 상태 범위를 검사합니다. 단언과 로그 뒤의 코드는 실제 실행 결과로 단정하지 않습니다.',nodes=[
 node('disconnected','연결 해제 금지이며 disconnected_인가?','Disconnection disallowed and disconnected_?','access','if (!allowDisconnected && disconnected_)',True),
 node('removed','-ENODEV 반환','Return -ENODEV','access','return -ENODEV;'),
 node('range','low ≤ currentState ≤ high인가?','low ≤ currentState ≤ high?','access','if (currentState >= low && currentState <= high)',True),
 node('allowed','0 반환','Return 0','access','return 0;'),
 node('denied','ASSERT·로그·-EACCES 코드 위치','ASSERT, log and -EACCES code locations','access','return -EACCES;')],edges=[
 edge('disconnected','removed','예','Yes','access','if (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;'),
 edge('disconnected','range','아니요','No','access','State currentState = state_.load(std::memory_order_acquire);'),
 edge('range','allowed','예','Yes','access','if (currentState >= low && currentState <= high)\n\t\treturn 0;'),
 edge('range','denied','아니요: 후속 코드 관찰','No: observe following code','access','ASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));')]))
new.append(dict(id='configuration-implementation-observation',topic='configuration-failure',kind='flow',title='구성 호출의 실제 구현을 확인하는 조사 계획',question='상태 검사를 통과한 기존 호출에서 타입·구현·반환값을 관찰하는 계획입니다. 검증이나 구성을 다시 호출하지 않습니다.',nodes=[
 node('validate','계획: config 동적 타입·validate 구현 기록','Plan: record config type and validate implementation','configure-code','if (config->validate() != CameraConfiguration::Valid)'),
 node('result','기존 validate 결과와 Valid 비교','Compare existing validate result with Valid','configure-code','if (config->validate() != CameraConfiguration::Valid)',True),
 node('invalid','-EINVAL 코드 위치','-EINVAL code location','validation-check','return -EINVAL;'),
 node('handler','계획: 실제 configure 구현 기록','Plan: record actual configure implementation','configure-code','ret = d->pipe_->invokeMethod(&PipelineHandler::configure,\n\t\t\t\t     ConnectionTypeBlocking, this, config);'),
 node('return','ret 관찰: 비영이면 그대로 반환','Observe ret: return unchanged if nonzero','configure-code','if (ret)\n\t\treturn ret;')],edges=[
 edge('validate','result','기존 호출 결과 관찰','Observe existing call result','configure-code','if (config->validate() != CameraConfiguration::Valid)'),
 edge('result','invalid','Valid 아님','Not Valid','validation-check','if (config->validate() != CameraConfiguration::Valid)'),
 edge('result','handler','Valid: 원래 configure 호출에서 관찰','Valid: observe original configure call','configure-code','ret = d->pipe_->invokeMethod(&PipelineHandler::configure,\n\t\t\t\t     ConnectionTypeBlocking, this, config);'),
 edge('handler','return','원래 호출의 ret 기록','Record original call ret','configure-code','if (ret)\n\t\treturn ret;')]))
graphs.extend(new)
assert len({g['id'] for g in graphs})==len(graphs)
for p in [o/'config/visuals.yaml',root/'examples/libcamera/config/visuals.yaml']:
 d=yaml.safe_load(p.read_text(encoding='utf-8'));d['sections']['request-diagnosis']=graphs
 p.write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
render(cfg,m,next(s for s in cfg.sections() if s['id']=='request-diagnosis'))
(w/'diagram-lineage.json').write_text(json.dumps({'adapted_source_bound_diagrams':new,'replaced_queue_gates':replacement,'note':'Authored graph definitions adapted and pinned to this page source windows; original diagrams and historical review records retained.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Replaced ambiguous queue gates; added six question-specific diagrams, all source-bound.')
