"""Compare declaration-name multiplicities only in unchanged tracked source files.

Usage: python compare_method_scope.py OLD_FACTS NEW_FACTS SOURCE_GIT OUTPUT
No parsing, model call, manuscript change, signature/ABI or runtime claim.
"""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

old_path, new_path, source_path, output_path = map(Path, sys.argv[1:])
old, new = [json.loads(path.read_text(encoding='utf-8')) for path in (old_path, new_path)]
before, after = old['meta']['source_commit'], new['meta']['source_commit']


def git_paths(*args):
    raw = subprocess.check_output(['git', '-C', str(source_path), *args, '-z'])
    return {name.decode('utf-8') for name in raw.split(b'\0') if name}


old_tracked = git_paths('ls-tree', '-r', '--name-only', before)
new_tracked = git_paths('ls-tree', '-r', '--name-only', after)
changed = git_paths('diff', '--no-renames', '--name-only', before, after)
unchanged = (old_tracked & new_tracked) - changed


def declarations(facts):
    selected, excluded = Counter(), Counter()
    for class_name, cls in facts['classes'].items():
        for method in cls.get('methods', []):
            file = (method.get('loc') or {}).get('file', '')
            if file in unchanged:
                selected[(class_name, method['name'], file)] += 1
            else:
                reason = 'changed_source' if file in changed else 'untracked_or_absent_source'
                excluded[reason] += 1
    return selected, excluded


old_entries, old_excluded = declarations(old)
new_entries, new_excluded = declarations(new)
missing = old_entries - new_entries
result = {
    'old_source': before, 'new_source': after,
    'scope': 'Method-name multiplicity within classes for declarations in Git-tracked files unchanged between these source commits. Not signature/ABI or runtime validation. Changed-source declarations and old untracked generated headers are excluded explicitly.',
    'old_facts_sha256': hashlib.sha256(old_path.read_bytes()).hexdigest(),
    'new_facts_sha256': hashlib.sha256(new_path.read_bytes()).hexdigest(),
    'old_method_entries_in_unchanged_source': old_entries.total(),
    'new_method_entries_in_unchanged_source': new_entries.total(),
    'excluded_old_entries': dict(old_excluded), 'excluded_new_entries': dict(new_excluded),
    'changed_paths': sorted(changed),
    'missing_entries': [dict(class_name=key[0], method_name=key[1], file=key[2], count=count)
                        for key, count in sorted(missing.items())],
    'passed': not missing,
}
output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({key: result[key] for key in ('old_method_entries_in_unchanged_source',
      'new_method_entries_in_unchanged_source', 'excluded_old_entries', 'excluded_new_entries', 'passed')}))
raise SystemExit(0 if result['passed'] else 1)
