"""Read-only audit of actual manifest-owned HTML source links against Git blobs."""
import datetime
import json
import re
import subprocess
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
from sdd.site_build import verify_site

site, source, expected, output = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
assert re.fullmatch(r'[0-9a-f]{40}', expected)
subprocess.run(['git', 'cat-file', '-e', f'{expected}^{{commit}}'], cwd=source, check=True, capture_output=True)
site_verification = verify_site(site)
manifest = json.loads((site / 'site-manifest.json').read_text(encoding='utf-8'))
prefix = '/TTolsun/libcamera-sdd/blob/'
links = {}
class Page(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag != 'a' or 'href' not in attrs:
            return
        href = attrs['href']
        parsed = urlsplit(href)
        if parsed.netloc.lower() == 'github.com' and parsed.path.startswith(prefix):
            links.setdefault(href, []).append(self.page)

pages = [rel for rel in manifest['outputs'] if rel.endswith('.html')]
for rel in pages:
    parser = Page()
    parser.page = rel
    parser.feed((site / rel).read_text(encoding='utf-8'))
failures, cache, commits = [], {}, Counter()
for href, origins in sorted(links.items()):
    parsed = urlsplit(href)
    commit, _, filename = unquote(parsed.path[len(prefix):]).partition('/')
    commits[commit] += len(origins)
    reason = ''
    if commit != expected:
        reason = 'source commit differs'
    elif not filename or '..' in PurePosixPath(filename).parts:
        reason = 'invalid source path'
    else:
        if filename not in cache:
            result = subprocess.run(['git', 'show', f'{expected}:{filename}'], cwd=source, capture_output=True)
            cache[filename] = len(result.stdout.decode('utf-8').splitlines()) if result.returncode == 0 else None
        line_count = cache[filename]
        anchor = re.fullmatch(r'L([1-9][0-9]*)(?:-L([1-9][0-9]*))?', parsed.fragment)
        if line_count is None:
            reason = 'source file absent from immutable Git tree'
        elif not anchor:
            reason = 'missing or invalid source line anchor'
        elif not (1 <= int(anchor[1]) <= int(anchor[2] or anchor[1]) <= line_count):
            reason = 'source line range outside immutable Git blob'
    if reason:
        failures.append({'url': href, 'reason': reason, 'pages': sorted(set(origins))})
report = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'site': str(site), 'build_id': manifest['build_id'], 'expected_source_commit': expected, 'scope': 'Actual HTML source-link commit, file existence and line bounds; not semantic review, actual GitHub UI navigation or remote byte verification', 'site_verification': site_verification, 'html_pages': len(pages), 'source_link_occurrences': sum(map(len, links.values())), 'unique_source_links': len(links), 'unique_source_files': len(cache), 'commits': dict(commits), 'failures': failures, 'passed': bool(links) and not failures}
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({key: report[key] for key in ('html_pages', 'source_link_occurrences', 'unique_source_links', 'unique_source_files', 'commits', 'passed')}))
if failures:
    print(json.dumps(failures[:5], ensure_ascii=False, indent=2))
raise SystemExit(0 if report['passed'] else 1)
