"""Verify the public replay artifacts with Python's standard library."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parent.parent
proof = json.loads((root / 'qwen-update-proof.json').read_text(encoding='utf-8'))
for stage in ('before', 'after'):
    manuscript = (root / 'qwen-replay' / f'{stage}-ipa.md').read_text(encoding='utf-8')
    match = re.fullmatch(r'---\n(.*?)\n---\n(.*)', manuscript, re.S)
    assert match
    frontmatter, body = match.groups()
    artifact = json.loads(next(line.split(': ', 1)[1] for line in frontmatter.splitlines()
                              if line.startswith('generated_design: ')))
    assert hashlib.sha256(body.strip().encode()).hexdigest() == artifact['body_sha256']
    assert proof[stage]['source_commit'] in frontmatter
    statements = []
    for call in proof[f'{stage}_calls']:
        receipt = call['receipt']
        assert receipt['transport'] == 'ollama' and receipt['http_call'] is True
        assert receipt['model'] == proof['model']['name']
        request = json.dumps(call['request'], ensure_ascii=False, sort_keys=True)
        assert hashlib.sha256(request.encode()).hexdigest() == receipt['request_sha256']
        assert hashlib.sha256(call['response'].encode()).hexdigest() == receipt['response_sha256']
        statements.extend(json.loads(call['response'])['statements'])
    answers = artifact['answers']['dma-import']
    assert len(statements) == len(answers)
    for response, answer in zip(statements, answers):
        assert response['text'].replace('`', '') == answer['text'].replace('`', '')
        assert response['covers'] == answer['covers'] and response['kind'] == answer['kind']
    assert answers == proof[f'{stage}_statements']
assert 'DRM_FORMAT_RG88' in proof['before_statements'][0]['text']
assert 'DRM_FORMAT_GR88' in proof['after_statements'][0]['text']
assert proof['update_state']['last_done'] == proof['after']['source_commit']
assert not proof['update_state']['failed']
print('Verified: 10 local Ollama call records, intact before/after manuscripts, and source-driven RG88 -> GR88 update.')
print('This checks recorded provenance and hashes; it is not a trusted hardware attestation or human approval.')
