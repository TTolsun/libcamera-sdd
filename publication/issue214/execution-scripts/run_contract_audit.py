from pathlib import Path
from sdd.config import load
from sdd.consistency import audit
from sdd.facts.model import KnowledgeModel
from sdd.llm import Agent
r=Path('build/issue214/draft-v1');cfg=load(r/'independent-review.yaml');assert cfg.agent.runner=='codex' and cfg.agent.model=='gpt-6.1-terra' and cfg.agent.args==['-c','model_reasoning_effort="high"']
model=KnowledgeModel.load(cfg.facts_path)
report=audit(cfg,model,Agent(cfg.agent,cfg.build_dir/'prompts'))
print({k:report.get(k) for k in ['status','fresh_batches','reused_batches','source_commit']},'unresolved',len(report.get('unresolved',[])),flush=True)
