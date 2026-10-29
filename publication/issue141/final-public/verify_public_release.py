"""Verify an immutable libcamera-sdd release against its actual Pages artifacts.

This task-local helper never renders/edits output or calls a model. It verifies
all manifest-owned resources, not only a handful of representative URLs.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import threading
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument('--public-commit', required=True)
parser.add_argument('--source-commit', required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--expected-pages', type=Path,
                    help='Independently derived required bilingual HTML inventory JSON')
parser.add_argument('--repo', type=Path, default=Path('build/issue141/public-sdd'))
parser.add_argument('--generator-repo', type=Path, default=Path.cwd())
parser.add_argument('--base-url', default='https://ttolsun.github.io/libcamera-sdd/')
args = parser.parse_args()
report = dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              public_commit=args.public_commit, expected_source_commit=args.source_commit,
              base_url=args.base_url, passed=False, scope='All manifest-owned HTTP resources and immutable Git run/manifest identity; not LLM semantics, browser UI, human approval or internal HAL validation',
              network_phase_started=False, verified_live_resources=0, checked_resources=[])
results_lock = threading.Lock()


def blob(name):
    return subprocess.check_output(['git', '-C', str(args.repo), 'show',
                                    args.public_commit + ':' + name])


def fetch(name):
    req = urllib.request.Request(args.base_url + urllib.parse.quote(name, safe='/'),
        headers={'Cache-Control': 'no-cache', 'Accept-Encoding': 'identity',
                 'User-Agent': 'sdd-issue141-release-verification'})
    with urllib.request.urlopen(req, timeout=40) as response:
        if response.status != 200:
            raise ValueError(f'Unexpected HTTP status for {name}: {response.status}')
        return response.read(), response.status


try:
    assert re.fullmatch(r'[0-9a-f]{40}', args.public_commit)
    assert re.fullmatch(r'[0-9a-f]{40}', args.source_commit)
    assert args.base_url.startswith('https://') and args.base_url.endswith('/')
    report['stage'] = 'immutable Git metadata'
    manifest_bytes = blob('docs/site-manifest.json')
    manifest = json.loads(manifest_bytes)
    run = json.loads(blob('run.json'))
    assert run['source_commit'] == args.source_commit, 'run.json source differs'
    assert run['build_id'] == manifest['build_id'], 'run.json/site-manifest build_id differs'
    assert manifest['schema'] == 1 and manifest['outputs']
    build_data = {key: value for key, value in manifest.items() if key != 'build_id'}
    calculated_build_id = hashlib.sha256(json.dumps(build_data, sort_keys=True).encode()).hexdigest()
    assert calculated_build_id == manifest['build_id'], 'Manifest build_id does not bind its actual contents'
    report['manifest_build_id_recomputed'] = True
    if args.expected_pages:
        expected_raw = args.expected_pages.read_bytes()
        expected_pages = set(json.loads(expected_raw)['pages'])
        actual_pages = {name for name in manifest['outputs'] if name.endswith('.html')}
        assert actual_pages == expected_pages, ('HTML inventory differs',
            sorted(expected_pages - actual_pages), sorted(actual_pages - expected_pages))
        report.update(required_html_pages_verified=len(expected_pages),
                      expected_inventory_sha256=hashlib.sha256(expected_raw).hexdigest())
    report['stage'] = 'merged generator and recorded engine bytes'
    generator_commit = run['generator_commit']
    assert re.fullmatch(r'[0-9a-f]{40}', generator_commit), 'Invalid generator commit'
    subprocess.run(['git', '-C', str(args.generator_repo), 'merge-base', '--is-ancestor',
                    generator_commit, 'origin/main'], check=True, capture_output=True)
    subprocess.run(['git', '-C', str(args.generator_repo), 'merge-base', '--is-ancestor',
                    '0ed2a6e1b16a7500c1afb33c653316eed67f8044', generator_commit],
                   check=True, capture_output=True)
    engine_matches = {}
    assert manifest['engine'], 'Missing engine fingerprints'
    for name, expected in sorted(manifest['engine'].items()):
        assert re.fullmatch(r'[a-z_]+\.py', name), 'Unexpected engine module name'
        source = subprocess.check_output(['git', '-C', str(args.generator_repo),
            'show', generator_commit + ':src/sdd/' + name])
        forms = {'Git blob': source, 'LF checkout': source.replace(b'\r\n', b'\n')}
        forms['CRLF checkout'] = forms['LF checkout'].replace(b'\n', b'\r\n')
        matches = [label for label, raw in forms.items() if hashlib.sha256(raw).hexdigest() == expected]
        assert matches, f'Engine bytes do not match declared merged generator: {name}'
        engine_matches[name] = dict(sha256=expected, matching_checkout_forms=matches)
    report.update(declared_generator_is_merged=True, issue141_core_is_ancestor=True,
                  recorded_engine_matches_merged_source=engine_matches,
                  generator_byte_comparison_scope='Exact recorded hashes compared with immutable Git blob and explicit LF/CRLF checkout forms; no manifest, policy, receipt or production file changed')
    report.update(build_id=manifest['build_id'], generator_commit=run['generator_commit'],
                  run_manifest_build_id_matches=True,
                  human_approval_recorded=run.get('human_approval'),
                  human_review_recorded=run.get('human_review'),
                  inhouse_hal_verified_recorded=run.get('inhouse_hal_verified'),
                  internal_hal_validation_recorded=run.get('internal_hal_validation'),
                  device_validation_recorded=run.get('device_validation'))
    paths = sorted(manifest['outputs'])
    for path in paths:
        assert isinstance(path, str) and '\\' not in path and ':' not in path
        assert not PurePosixPath(path).is_absolute()
        assert all(part not in ('', '.', '..') for part in path.split('/'))
        assert re.fullmatch(r'[0-9a-f]{64}', manifest['outputs'][path])
        assert hashlib.sha256(blob('docs/' + path)).hexdigest() == manifest['outputs'][path], path
    report['committed_output_hashes_verified'] = len(paths)
    report['stage'] = 'live manifest'
    report['network_phase_started'] = True
    first, status = fetch('site-manifest.json')
    assert first == manifest_bytes, 'Live manifest does not match immutable Git release'

    def check(path):
        raw, status = fetch(path)
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == manifest['outputs'][path], f'Live artifact differs: {path}'
        row = dict(path=path, status=status, sha256=digest,
                   matches_committed_artifact=True)
        with results_lock:
            report['checked_resources'].append(row)
            report['verified_live_resources'] += 1
        return row

    report['stage'] = 'all live manifest-owned outputs'
    print(f'Verifying all {len(paths)} immutable release outputs', flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(check, paths))
    last, _ = fetch('site-manifest.json')
    assert last == first, 'Manifest changed while resources were checked'
    report.update(stable_manifest_during_check=True, passed=True, stage='complete')
except Exception as exc:
    report['error'] = dict(type=type(exc).__name__, message=str(exc))
finally:
    report['checked_resources'].sort(key=lambda row: row['path'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({key: report.get(key) for key in ('passed', 'stage', 'network_phase_started', 'verified_live_resources', 'error')}))
raise SystemExit(0 if report['passed'] else 1)
