import pathlib,json,hashlib,tarfile
from sdd.config import load
from sdd.call_records import load_record
from sdd.cli_provenance import verify_cli_receipt
r=pathlib.Path(__file__).resolve().parents[2];out=r/'build/issue253/publication-final/publication/issue253-reader-followup';restore=r/'build/q253rf1';assert not restore.exists();restore.mkdir();meta=json.loads((out/'package.json').read_bytes());index=json.loads((out/'archive-index.json').read_bytes());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();archive=out/meta['archive'];assert sha(archive)==meta['archive_sha256'] and sha(out/'archive-index.json')==meta['index_sha256'];seen=set();size=0
with tarfile.open(archive,'r:gz') as tar:
 for member in tar:
  p=pathlib.PurePosixPath(member.name);assert member.isfile() and not p.is_absolute() and '..' not in p.parts and ':' not in member.name and '\\' not in member.name and member.name in index and member.name not in seen
  q=restore.joinpath(*p.parts).resolve();assert q.is_relative_to(restore.resolve());data=tar.extractfile(member).read();assert hashlib.sha256(data).hexdigest()==index[member.name]['sha256'];q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data);seen.add(member.name);size+=len(data)
assert seen==set(index);v=json.loads((restore/'run-05/native-call-verification-final.json').read_bytes());expected=load(r/'build/issue253/reader-current249/run-05/review-v11.yaml').agent
for row in v['records']:
 p=restore/'run-05'/row['path'];record=load_record(p,root=p.parent);calls=next(p for p in p.parents if p.name=='calls');verify_cli_receipt(record.request,record.raw,record.receipt,calls,expected)
report=dict(status='verified',files_verified=len(seen),bytes_restored=size,new_original_native_chains_verified=len(v['records']),explicitly_inherited_native_receipts=len(v['inherited_original_receipts']),archive_sha256=meta['archive_sha256'],scope='Safe restore, every file hash and91 current original native request/response/stdout/argv chains. No archived script executed, no inference rerun, no human approval.',human_review='pending');(out/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(report)
