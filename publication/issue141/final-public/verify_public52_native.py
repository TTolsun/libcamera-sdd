"""Independently restore immutable public evidence and verify current native calls.

No writer/model is invoked; protocol integrity is not manuscript acceptance.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import time
import yaml
from sdd.call_records import load_record
from sdd.cli_provenance import verify_cli_receipt
from sdd.config import AgentConfig

w = Path('build/issue141').resolve()
release = w/'public-release-46235b02'
package = release/'publication/goal-138-140'
evidence = package/'original-evidence'
out = w/'restored-public52-evidence'
assert not out.exists(), 'Keep previous evidence runs intact'
index = json.loads((evidence/'original-cli-evidence-index.json').read_bytes())
names = [r['path'] for r in index['files']]
assert len(names) == len(set(names))
for row in index['files']:
    path = PurePosixPath(row['path'])
    assert not path.is_absolute() and '..' not in path.parts
    assert ':' not in row['path'] and '\\' not in row['path']
    assert re.fullmatch(r'[0-9a-f]{64}', row['sha256']) and row['bytes'] >= 0
started = time.monotonic()
report = dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    public_commit='46235b026626db49ef98ba3a5e23d1359dbe3d0a',passed=False,
    stage='original evidence restoration',new_model_calls=0,
    scope='All original indexed file paths/bytes/SHA and all current root-ledger completed native CLI receipts; not fresh CLI inference, manuscript semantics, human approval or internal HAL/device validation',
    expected_original_files=len(names),original_files_verified=0,original_bytes_verified=0,
    current_native_receipts_verified=0,native_failures=[])
try:
    archive = evidence/index['archive']
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == index['archive_sha256']
    report['archive_sha256'] = index['archive_sha256']
    result = subprocess.run([sys.executable,'-X','utf8',str(evidence/'restore-evidence.py'),'--out',str(out)],capture_output=True)
    (w/'public52-evidence-restoration.stdout.log').write_bytes(result.stdout)
    (w/'public52-evidence-restoration.stderr.log').write_bytes(result.stderr)
    report['restoration_exit_code'] = result.returncode
    assert result.returncode == 0, 'Original evidence restore failed; preserved stdout/stderr'
    # Read long paths under the same explicit Windows convention as the public
    # restore tool. This changes no logical names, payload bytes or receipts.
    native_root = Path('\\\\?\\'+str(out)) if os.name == 'nt' else out
    report['stage'] = 'all restored original bytes and exact file count'
    for i,row in enumerate(index['files'],1):
        path = native_root/row['path']
        data = path.read_bytes()
        assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
        report['original_files_verified'] += 1
        report['original_bytes_verified'] += len(data)
        if i % 10000 == 0:
            print(f'Verified {i}/{len(names)} original indexed files',flush=True)
    actual_files = sum(path.is_file() for path in native_root.rglob('*'))
    assert actual_files == len(names)
    report['exact_restored_file_count'] = actual_files
    ledger = json.loads((release/'generation-receipts.json').read_bytes())
    assert ledger['source_commit']=='e117198c015057761bb0bbaa85f963c41ce412d7'
    assert ledger['human_review']=='pending'
    rows = ledger['receipts']
    assert len(rows)==len({r['receipt_sha256'] for r in rows})==1127
    expected = AgentConfig(**yaml.safe_load((package/'executed-sdd.codex.local.yaml').read_text(encoding='utf-8'))['agent'])
    assert expected.kind=='cli' and expected.runner=='codex' and expected.model=='gpt-6.1-terra'
    assert expected.args==['-c','model_reasoning_effort="high"']
    report['stage'] = 'all current selected native CLI receipts'
    index_by_path = {r['path']:r for r in index['files']}
    for number,row in enumerate(rows,1):
        try:
            name = row['archive_entry']
            assert index_by_path[name]['sha256']==row['receipt_sha256']
            path = native_root/name
            assert hashlib.sha256(path.read_bytes()).hexdigest()==row['receipt_sha256']
            record = load_record(path,root=native_root)
            calls = next(p for p in path.parents if p.name=='calls')
            checked = verify_cli_receipt(record.request,record.raw,record.receipt,calls,expected)
            assert checked['arguments_verified']
            for key in ('tag','model','transport','request_sha256','response_sha256'):
                assert row[key]==record.receipt[key],key
            assert row['stdout_sha256']==record.receipt['provider']['stdout_sha256']
            assert row['arguments']==record.receipt['provider']['arguments']
            assert row['human_review']=='pending'
            report['current_native_receipts_verified'] += 1
        except Exception as exc:
            report['native_failures'].append(dict(archive_entry=row.get('archive_entry'),error=type(exc).__name__,message=str(exc)))
        if number % 200 == 0:
            print(f'Checked {number}/{len(rows)} current native receipts',flush=True)
    assert not report['native_failures'], 'Current native receipt failures; inspect full report'
    report.update(passed=True,stage='complete',selected_profile=dict(kind=expected.kind,runner=expected.runner,model=expected.model,args=expected.args),
                  archive_copies_are_new_calls=False,backend_canonical_model_independently_attested=False)
except Exception as exc:
    report['error']=dict(type=type(exc).__name__,message=str(exc))
finally:
    report['seconds']=round(time.monotonic()-started,3)
    (w/'public52-native-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report.get(k) for k in ('passed','stage','original_files_verified','original_bytes_verified','current_native_receipts_verified','error','seconds')},ensure_ascii=False))
raise SystemExit(0 if report['passed'] else 1)
