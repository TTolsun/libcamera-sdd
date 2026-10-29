"""Validate source line bounds and excerpt bytes against immutable Git blobs."""
from pathlib import Path
import json,subprocess,io,hashlib,sys
root=Path.cwd();folder=root/'build/issue141'/(sys.argv[1] if len(sys.argv)>1 else 'tracked-native');data=json.loads((folder/'facts/facts.json').read_text(encoding='utf-8'));sha=data['meta']['source_commit'];positions=[]
def visit(value,where=''):
 if isinstance(value,dict):
  if isinstance(value.get('file'),str) and isinstance(value.get('line'),int):positions.append((where,value['file'],value['line']))
  for key,item in value.items():visit(item,where+'/'+key)
 elif isinstance(value,list):
  for index,item in enumerate(value):visit(item,where+'/'+str(index))
visit(data);files=sorted({file for _,file,_ in positions});requests=''.join(f'{sha}:{file}\n' for file in files).encode()
raw=subprocess.check_output(['git','-C',str(root/'build/issue141/libcamera-full'),'cat-file','--batch'],input=requests);stream=io.BytesIO(raw);texts={}
for file in files:
 header=stream.readline().split();assert len(header)==3 and header[1]==b'blob',file
 body=stream.read(int(header[2]));assert stream.read(1)==b'\n';texts[file]=body.decode('utf-8').replace('\r\n','\n')
invalid_bounds=[position for position in positions if not 1<=position[2]<=len(texts[position[1]].splitlines())]
assert not invalid_bounds,invalid_bounds[:5]
def verify_excerpt(file,record):
 text=texts[file];line=record['line'];excerpt=record['text'];start=0
 for _ in range(line-1):start=text.index('\n',start)+1
 end=text.find('\n',start);end=len(text) if end<0 else end
 found=text.find(excerpt,start)
 assert start<=found<=end,(file,line,'excerpt not at pinned line')
 assert record['end_line']==line+excerpt.count('\n'),(file,line,'end line')
 assert record['sha256']==hashlib.sha256(excerpt.encode()).hexdigest(),(file,line,'hash')
 assert record['end_line']<=len(text.splitlines()),(file,line,'end bounds')
contexts=0
for key,record in data['evidence'].items():
 assert record['status']=='available' and record['commit']==sha,key
 verify_excerpt(record['file'],record)
 if 'context' in record:verify_excerpt(record['file'],record['context']);contexts+=1
result={'source_commit':sha,'facts_sha256':hashlib.sha256((folder/'facts/facts.json').read_bytes()).hexdigest(),'translation_units':data['meta']['translation_units'],'parse_errors':data['meta']['comments']['errors'],'classes':len(data['classes']),'functions':len(data['functions']),'scenarios':len(data['scenarios']),'immutable_Git_blobs':len(files),'source_positions_within_real_file_bounds':len(positions),'invalid_positions':invalid_bounds,'source_excerpts_at_pinned_lines':len(data['evidence']),'excerpt_hashes_match_Git':len(data['evidence']),'context_ranges_and_hashes_match_Git':contexts,'text_contract':'UTF-8 Git content with existing universal-newline normalization; no facts or source edits','model_calls':0}
output=Path(sys.argv[2]) if len(sys.argv)>2 else folder/'git-span-verification.json'
output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
