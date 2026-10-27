"""Read-only readiness scan; current questions and selected CLI, no inference."""
import hashlib
import json
import subprocess
from pathlib import Path
from unittest.mock import patch

from sdd.config import load, section_output
from sdd.document_metadata import split_frontmatter
from sdd.evidence import collect
from sdd.facts.model import KnowledgeModel
from sdd.generated_design import _prepare_generation
from sdd.design_request import _design_units, _unit_tag
from sdd.trial_workspace import clone_config, write_snapshot

root = Path.cwd()
out = root / 'build/issue141/current-main-readiness'
out.mkdir()
cfg = clone_config(load(root / 'examples/libcamera/sdd.yaml'), out)
cfg.source_root = root / 'build/issue141/libcamera-full'
snapshot = write_snapshot(cfg, out / 'sdd.claude.yaml')
override = out / 'sdd.claude.local.yaml'
override.write_text('agent:\n  kind: cli\n  runner: claude\n  model: claude-haiku-5-5\n  args: [--effort, high]\n', encoding='utf-8')
cfg = load(snapshot)
assert (cfg.agent.kind, cfg.agent.runner, cfg.agent.model, cfg.agent.args) == ('cli', 'claude', 'claude-haiku-5-5', ['--effort', 'high'])
facts = root / 'build/issue141/merged-profile/facts/facts.json'
model = KnowledgeModel.load(facts)
old_evidence = json.dumps(model.evidence, sort_keys=True)
collect(cfg, model)
new_evidence = json.dumps(model.evidence, sort_keys=True)
published = load(root / 'build/issue141/fixed-public-latest/sdd.yaml')
rows = []
with patch('sdd.llm.Agent.chat', side_effect=AssertionError('Readiness scan cannot invoke a model')) as guard:
    for section in cfg.sections():
        manuscript = published.sdd_dir / section_output(section)
        previous = manuscript.read_text(encoding='utf-8') if manuscript.exists() else None
        meta, _ = split_frontmatter(previous) if previous else ({}, '')
        row = {'section': section['id'], 'previous_exists': bool(previous), 'previous_source': meta.get('source_commit'), 'previous_agent': meta.get('agent')}
        if section.get('design_generation') != 'llm':
            row.update(status='deterministic-generation-required', model_calls_required=False)
        else:
            row['total_topics'] = len(section['design_topics'])
            try:
                plan, retained, _ = _prepare_generation(cfg, model, section, previous)
                units = _design_units(section, retained)
                row.update(status='requires-cli-generation' if units else 'retained-topics-only', retained_topics=list(retained), required_units=[_unit_tag(section, unit) for unit in units])
            except (ValueError, KeyError, TypeError) as error:
                row.update(status='preflight-rejected', error=str(error))
        rows.append(row)
    assert guard.call_count == 0
report = {
    'schema': 1, 'purpose': 'Readiness only; no manuscript generation or publication',
    'generator_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'merged_dependency': 'a8972398ef29e8fd23fdc2b3464c552e07f81a20',
    'facts_generator': '350a9d344e6170d37124774f5f290ec13bc04d0b',
    'facts_sha256': hashlib.sha256(facts.read_bytes()).hexdigest(),
    'source_commit': model.meta['source_commit'], 'public_base': 'f57d9ec440254e9b1285c475f9fb7d70c94c259b',
    'questions': str(cfg.sections_file.relative_to(root)),
    'questions_sha256': hashlib.sha256(cfg.sections_file.read_bytes()).hexdigest(),
    'configuration': ['sdd.claude.yaml', 'sdd.claude.local.yaml'],
    'selected_agent': {'kind': cfg.agent.kind, 'runner': cfg.agent.runner, 'model': cfg.agent.model, 'args': cfg.agent.args, 'command': cfg.agent.command},
    'historical_agent_identity_substitution': False,
    'evidence_recollected_from_current_questions': True,
    'evidence_changed': old_evidence != new_evidence,
    'evidence_records': len(model.evidence),
    'evidence_needing_review': {key: value.get('reason') for key, value in model.evidence.items() if value.get('status') != 'available'},
    'new_model_calls': 0, 'blocked_call_attempts': 0,
    'manuscripts_written': 0, 'publishable': False, 'rows': rows,
}
(out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'sections': len(rows), 'status_counts': {status: sum(row['status'] == status for row in rows) for status in sorted({row['status'] for row in rows})}, 'required_units': sum(len(row.get('required_units', [])) for row in rows), 'retained_topics': sum(len(row.get('retained_topics', [])) for row in rows), 'evidence_needing_review': report['evidence_needing_review'], 'model_calls': 0}, ensure_ascii=False, indent=2))
