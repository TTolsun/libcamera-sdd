from pathlib import Path
import json,subprocess
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.publication_plan import prepare
root=Path.cwd();w=root/'build/preflight-native/native-good-01';path=w/'operation.json';op=json.loads(path.read_bytes());assert op['revision']==2
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
subprocess.run(['git','diff','--quiet',op['integration']['commit'],head],check=True)
(w/'before-merged-operation.json').write_bytes(path.read_bytes())
op.update(revision=3,reason='Adopt the actual generator merge after a byte-identical candidate-tree check.',change=dict(kind='integration',reason='Generator PR272 merged; the tested tree is identical. Preserve completed native work and original reports.',affected_sections=['camera-requests'],recheck='Current source/receipt/report checks and post-merge export/site verification; no manuscript regeneration.'))
op['integration']['commit']=head
path.write_text(json.dumps(op,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
cfg=load(w/'sdd.yaml');prepare(cfg,KnowledgeModel.load(cfg.facts_path));print('Merged tree adopted explicitly; original native records retained.')
