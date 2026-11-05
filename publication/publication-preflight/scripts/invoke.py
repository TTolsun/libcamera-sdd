from pathlib import Path
import hashlib,json,os,subprocess,sys,time
root=Path.cwd();w=root/'build/preflight-native';kind,name,action=sys.argv[1:4];case=w/('native-bad-02' if kind=='bad2' else 'native-'+kind+'-01')
command=[sys.executable,'-m','sdd.cli','--config',str(case/'sdd.yaml')]
if action=='generate':command+=['generate','--sections','camera-requests']
elif action=='translate':command=[sys.executable,'-m','sdd.localization_cli','--config',str(case/'sdd.yaml'),'--out',str(case/'english.json'),'--translate']
elif action=='audit':command+=['audit-consistency']
elif action=='export':command+=['export-site','--out',str(case/'site')]
elif action=='verify':command+=['verify-site','--out',str(case/'site')]
elif action=='diagram':command=[sys.executable,str(w/'review_diagram.py')]
elif action=='finalize':command=[sys.executable,str(w/'finalize.py')]
elif action=='adopt':command=[sys.executable,str(w/'adopt_merged.py')]
else:raise ValueError(action)
folder=case/'invocations';folder.mkdir(exist_ok=True);log=folder/(name+'.log');out=folder/(name+'.json');assert not log.exists() and not out.exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
tracked=[case/'english.json',case/'manuscripts/camera-requests.md']
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
declared=json.loads((case/'operation.json').read_bytes())['integration']['commit']
if action=='adopt':subprocess.run(['git','diff','--quiet',declared,head],check=True)
else:assert head==declared, (head,declared)
row=dict(schema=1,command=command,generator_commit=head,started_at=time.time(),status='running',before={str(p.relative_to(case)):sha(p) for p in tracked},inputs={p:sha(case/p) for p in ['operation.json','sdd.yaml','sections.yaml','visuals.yaml','contracts.yaml','review.yaml']})
out.write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');started=time.monotonic()
with log.open('wb') as stream:
    code=subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONPATH':str(root/'src'),'PYTHONDONTWRITEBYTECODE':'1','PYTHONIOENCODING':'utf-8'}).returncode
row.update(exit_code=code,finished_at=time.time(),wall_seconds=time.monotonic()-started,status='passed' if code==0 else 'failed',after={str(p.relative_to(case)):sha(p) for p in tracked})
out.write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(row,ensure_ascii=False));print(log.read_text(encoding='utf-8',errors='replace')[-2500:]);raise SystemExit(code)
