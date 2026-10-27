import json
import hashlib
import os
import subprocess
import sys
from pathlib import Path
root=Path.cwd();folder=root/'build/issue141'/(sys.argv[1] if len(sys.argv)>1 else 'full-coverage-impact')
command=[str(Path(sys.executable).with_name('sdd.exe')),'--config',str(folder/'sdd.claude.yaml'),'impact','--base','2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f','--head','182307a772ebebf173ee84911906da707718485f','--base-facts',str(root/'build/issue141/public-sdd/qwen-full/publication/facts.json'),'--fail-on-coverage-gap']
result=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',env={**os.environ,'PYTHONIOENCODING':'utf-8'})
(folder/'execution.log').write_text(result.stdout+result.stderr,encoding='utf-8')
report=json.loads((folder/'build/impact.json').read_text(encoding='utf-8'))
data={'command':command,'facts_sha256':hashlib.sha256((folder/'facts/facts.json').read_bytes()).hexdigest(),'native_exit_code':result.returncode,'changed_files':len(report['changed_files']),'affected_sections':sorted(report['sections']),'coverage_status':report['coverage']['status'],'coverage_findings':len(report['coverage']['findings']),'model_calls':0,'human_acceptances_recorded':0,'passed_coverage_gate':False,'scope':'Deterministic source impact only; --fail-on-coverage-gap expected to stop. PowerShell outer exit1 from the first observation is not the native CLI exit code.'}
assert result.returncode==2 and report['coverage']['status']=='needs-review'
(folder/'execution.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(data,ensure_ascii=False,indent=2))
