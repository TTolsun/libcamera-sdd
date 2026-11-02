"""Index original public native calls; retain failed/rejected lineage separately."""
from collections import Counter
from pathlib import Path
import hashlib
import json
from sdd.call_records import iter_records
from sdd.cli_provenance import verify_cli_receipt
from sdd.config import load

RUN = Path(__file__).resolve().parent/'draft'


def verify():
    profiles = {name: load(RUN/(name+'.yaml')).agent for name in ('reader-authentication', 'independent-review')}
    rows = []
    for name in ('prompts', 'translation-prompts', 'independent-window-review'):
        calls = RUN/'build'/name/'calls'
        for record in iter_records(calls):
            receipt = record.receipt
            cfg = profiles['reader-authentication' if receipt['provider']['runner']=='claude' else 'independent-review']
            verified = verify_cli_receipt(record.request, record.raw, receipt, calls, cfg)
            native = receipt['provider']
            stdout = calls.parent/native['stdout_path']
            data = json.loads(stdout.read_text(encoding='utf-8')) if cfg.runner=='claude' else None
            row = dict(receipt=record.receipt_path.relative_to(RUN).as_posix(),
                receipt_sha256=hashlib.sha256(record.receipt_path.read_bytes()).hexdigest(),
                request_sha256=receipt['request_sha256'], response_sha256=receipt['response_sha256'],
                stdout_sha256=verified['stdout_sha256'], tag=receipt['tag'],
                runner=cfg.runner, model=cfg.model, selected_args=cfg.args,
                cli_version=native['cli_version'], arguments_verified=verified['arguments_verified'],
                completed_at=receipt['completed_at'], human_review='pending')
            if data is not None:
                row['native_model_usage'] = list(data.get('modelUsage', {}))
                row['native_duration_ms'] = data.get('duration_ms')
                assert row['native_model_usage']==['claude-haiku-5-5']
            rows.append(row)
    counts = Counter((row['runner'], 'translation' if row['tag'].startswith('translation_') else
        'independent-review' if row['tag'].startswith('consistency_') or 'independent' in row['tag'] else 'generation-and-grounding') for row in rows)
    result = dict(schema=1, source_commit='293d751a814e0d4c34e85ad457ccd9d5eefd1a61',
        stage='after-independent-review', status='verified', human_review='pending',
        interpretation='Completed native CLI invocations include rejected drafts and retries; not a count of successful manuscripts. Failed preflight/execution attempts remain in generation-runs and raw failure logs.',
        counts=[dict(runner=runner,purpose=purpose,calls=count) for (runner,purpose),count in sorted(counts.items())],
        calls=rows)
    (RUN/'native-call-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(result['counts'], flush=True)


if __name__=='__main__':
    verify()

