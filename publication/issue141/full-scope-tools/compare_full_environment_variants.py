"""Enumerate every observed data change after restoring official Git tags."""
import copy
import hashlib
import json
from pathlib import Path

root=Path.cwd()/'build/issue141'
before_path=root/'full-coverage/facts/facts.json'
after_path=root/'full-coverage-tagged/facts/facts.json'
before,after=[json.loads(path.read_text(encoding='utf-8')) for path in (before_path,after_path)]
changes=[]
def compare(a,b,path=''):
    if type(a)!=type(b):
        changes.append({'path':path,'before':a,'after':b})
    elif isinstance(a,dict):
        for key in sorted(a.keys()|b.keys()):
            child=path+'/'+key.replace('~','~0').replace('/','~1')
            if key not in a:changes.append({'path':child,'added':b[key]})
            elif key not in b:changes.append({'path':child,'removed':a[key]})
            else:compare(a[key],b[key],child)
    elif isinstance(a,list):
        if len(a)!=len(b):changes.append({'path':path,'before':a,'after':b})
        else:
            for index,(left,right) in enumerate(zip(a,b)):compare(left,right,path+'/'+str(index))
    elif a!=b:changes.append({'path':path,'before':a,'after':b})
compare(before,after)
same={key:before[key]==after[key] for key in ('classes','functions','relations','packages','scenarios','includes','evidence')}
old_flags,new_flags=copy.deepcopy(before['defines']),copy.deepcopy(after['defines'])
old_version=old_flags.pop('VERSION');new_version=new_flags.pop('VERSION')
report={'source_commit':after['meta']['source_commit'],'before_sha256':hashlib.sha256(before_path.read_bytes()).hexdigest(),'after_sha256':hashlib.sha256(after_path.read_bytes()).hexdigest(),'scope':'Same generator and source/build options; official history/tags restored and actual rebuild/re-extraction performed. No facts editing or model calls.','identical_source_sections':same,'other_flag_records_identical':old_flags==new_flags,'version_before':old_version,'version_after':new_version,'all_differences':changes,'new_model_calls':0}
(root/'full-coverage-tagged/environment-comparison.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'identical_source_sections':same,'other_flag_records_identical':old_flags==new_flags,'changed_paths':[item['path'] for item in changes],'version_before':old_version['value'],'version_after':new_version['value']},ensure_ascii=False,indent=2))
assert before['meta']['source_commit']==after['meta']['source_commit']
assert all(same.values()) and old_flags==new_flags
assert '-nvm' not in new_version['value']
