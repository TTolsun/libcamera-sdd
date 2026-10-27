import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

root = Path.cwd() / 'build/issue141'
old_path = root / 'public-sdd/qwen-full/publication/facts.json'
new_path = root / (sys.argv[1] if len(sys.argv)>1 else 'merged-profile') / 'facts/facts.json'
old, new = [json.loads(path.read_text(encoding='utf-8')) for path in (old_path, new_path)]
tracked = set(subprocess.check_output(['git', '-C', str(root / 'libcamera-full'), 'ls-tree', '-r', '--name-only', new['meta']['source_commit']], text=True).splitlines())
def group(filename):
    parts = filename.split('/')
    return '/'.join(parts[:4] if filename.startswith(('src/ipa/', 'src/libcamera/pipeline/')) else parts[:2])
missing = []
for name in sorted(old['classes'].keys() - new['classes'].keys()):
    file = old['classes'][name]['loc']['file']
    missing.append({'name': name, 'previous_file': file, 'file_exists_in_new_source': file in tracked, 'group': group(file)})
missing_functions = []
for name in sorted(old['functions'].keys() - new['functions'].keys()):
    previous = old['functions'][name]
    location = previous.get('loc') or previous.get('def_loc') or {}
    filename = location.get('file', '')
    missing_functions.append({'name': name, 'previous_file': filename, 'file_exists_in_new_source': filename in tracked, 'group': group(filename)})
result = {'old_source_commit': old['meta']['source_commit'], 'new_source_commit': new['meta']['source_commit'], 'old_facts_sha256': hashlib.sha256(old_path.read_bytes()).hexdigest(), 'new_facts_sha256': hashlib.sha256(new_path.read_bytes()).hexdigest(), 'old_tus': old['meta']['translation_units'], 'new_tus': new['meta']['translation_units'], 'old_classes': len(old['classes']), 'new_classes': len(new['classes']), 'new_class_names': sorted(new['classes'].keys() - old['classes'].keys()), 'missing_class_names': len(missing), 'missing_in_still_present_source_files': sum(row['file_exists_in_new_source'] for row in missing), 'missing_by_group': dict(Counter(row['group'] for row in missing).most_common()), 'scope': 'Extraction coverage comparison; file existence alone is not proof that every previous declaration still exists or parses under current configuration.', 'missing': missing}
result.update(old_functions=len(old['functions']), new_functions=len(new['functions']), missing_functions=missing_functions, missing_functions_in_still_present_source_files=sum(row['file_exists_in_new_source'] for row in missing_functions), new_function_names=sorted(new['functions'].keys()-old['functions'].keys()), old_flag_names=sorted(old['defines']), new_flag_names=sorted(new['defines']), all_missing_declarations_are_previous_generated_files=all(row['previous_file'].startswith('build-full/') for row in missing+missing_functions))
(root / (sys.argv[2] if len(sys.argv)>2 else 'extraction-scope-comparison.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({key: value for key, value in result.items() if key not in ('missing', 'missing_functions', 'new_class_names')}, ensure_ascii=False, indent=2))
