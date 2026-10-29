<!-- system -->
Review this public repository diff for concrete correctness, evidence preservation, accessibility, archive validation and unintended scope regressions. Only the supplied diff and source are evidence. No tools are available. Return actionable findings with file and reason, or an empty findings list. Do not claim human approval or internal HAL validation.

<!-- user -->
diff --git a/AGENTS.md b/AGENTS.md
index af27bd8..a8d3af0 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -8,7 +8,8 @@
 - 사내 환경의 LLM, 네트워크와 정적 자산 제공 방식을 설정으로 교체할 수 있게 합니다. 공개 CDN이나 GitHub 서비스가 최종 운영의 필수 의존성이 되지 않도록 설계합니다.
 - 사내 환경 재현은 CLI 기반이며 기본 실행 주체는 Hermes입니다. 사용자가 선택하면 OpenCode, Claude Code 또는 Codex CLI로 바꿀 수 있으며 각 CLI는 독립적으로 실행합니다. Hermes가 다른 CLI를 호출한다고 가정하지 않습니다. 모델·제공자는 선택한 CLI의 설정 또는 명시적인 실행별 설정으로 정하고 Qwen에 고정하지 않습니다. Ollama는 CLI 뒤의 모델 제공 서버로 사용할 수 있지만 생성기나 작업 에이전트가 선택한 CLI를 건너뛰고 모델 API를 직접 호출하는 방식으로 대체하지 않습니다. 기존 직접 호출 예제·스크립트는 CLI 환경 재현 절차로 간주하지 않습니다. 선택한 CLI가 없거나 실패하면 원인과 미완료 단계를 보고하며, 다른 CLI·직접 호출·저장 응답·수동 원고로 대체하여 재현 성공으로 보고하지 않습니다. 직접 호출 비교 시험은 사용자가 별도로 요청한 범위에서만 수행하고 CLI 시험과 구분합니다.
 - 사내 HAL의 실제 구성과 소스가 제공되기 전에는 사내 적용이나 검증이 완료되었다고 표현하지 않습니다. libcamera 테스트 결과와 사내 HAL 검증 결과를 구분합니다.
-- 이 저장소의 공개 libcamera 입력을 Hermes와 Qwen으로 새로 생성·번역·검토할 때는 `qwen3.5:9b-ctx64k`와 `--reasoning high`를 사용합니다. 공개 기본 프로필은 `examples/libcamera/sdd.yaml`에서 관리하며 실행 전에 실제 모델·인자를 확인합니다. `agent.num_ctx`나 `agent.think`는 Hermes에 전달되지 않으므로 이 프로필을 대신하지 않습니다. 사내 환경은 별도 설정 또는 로컬 덮어쓰기로 모델·제공자·추론 강도를 바꿀 수 있게 유지합니다. 과거의 다른 모델·effort로 수행한 기록은 당시 값 그대로 보존합니다.
+- 이 저장소의 공개 libcamera 입력을 Hermes와 Qwen으로 새로 생성·번역할 때는 `qwen3.5:9b-ctx64k`와 `--reasoning high`를 사용합니다. 공개 생성·번역 기본 프로필은 `examples/libcamera/sdd.yaml`에서 관리하며 실행 전에 실제 모델·인자를 확인합니다. `agent.num_ctx`나 `agent.think`는 Hermes에 전달되지 않으므로 이 프로필을 대신하지 않습니다. 사내 환경은 별도 설정 또는 로컬 덮어쓰기로 모델·제공자·추론 강도를 바꿀 수 있게 유지합니다. 과거의 다른 모델·effort로 수행한 기록은 당시 값 그대로 보존합니다.
+- 이 프로젝트에서 LLM 검토가 필요하면 독립 Codex CLI의 `gpt-6.1-terra`와 reasoning effort `high`를 사용합니다. 검토 실행 설정은 `agent.kind: cli`, `agent.runner: codex`, `agent.model: gpt-6.1-terra`, `agent.args: [-c, 'model_reasoning_effort="high"']`로 명시합니다. 검토용 설정은 생성·번역 프로필과 별도로 관리하며 Hermes가 Codex를 호출하게 하지 않습니다. 선택한 CLI가 없거나 실패하면 검토 미완료를 보고하고 다른 CLI·직접 API·저장 응답으로 새 검토를 대체하지 않습니다. 기존 기록과 사람 검토 상태는 변경하지 않습니다.
 - 변경 시 반복 생성과 유지보수를 우선합니다. 문서 디자인은 `DESIGN.md`, 실행·검증 절차는 `docs/concepts/site.md`를 따릅니다.
 - 사용자의 상시 지시에 따라 이 프로젝트의 변경 작업에는 공개 libcamera SDD 갱신도 포함합니다. 생성기 변경을 리뷰·검증·병합하고, 공개 libcamera 입력으로 필요한 추출·원고 생성·사이트 빌드를 수행한 뒤 `TTolsun/libcamera-sdd`에 PR로 반영·병합하여 GitHub Pages 배포와 공개 URL을 확인합니다. 이 범위의 병합·공개 배포는 매번 다시 허락을 묻지 않습니다. 사내 데이터 배포 금지와 자동 검사·사람 승인 구분은 그대로 지킵니다.
 - 공개 libcamera 환경에는 매일 21시 등의 정기 예약을 설치하지 않습니다. 이 저장소에서 작업할 때 공식 upstream을 확인·동기화하고 문서를 갱신·배포합니다. 새 커밋이 없으면 기존 카테고리에서 근거가 있는 누락을 찾아 보완하며, 단순 재빌드나 좁은 범위의 no-gap 응답만으로 보완 작업을 완료했다고 하지 않습니다. 정기 예약·시간 변경 기능은 사내 운영을 위한 재사용 기능으로 유지합니다.
diff --git a/DESIGN.md b/DESIGN.md
index abb8626..d36e95e 100644
--- a/DESIGN.md
+++ b/DESIGN.md
@@ -31,6 +31,8 @@
 기준은 libcamera 공식 문서의 탐색 방식과 OMM `DESIGN.md`의 reading 규칙입니다. OMM 기준 커밋은 `12a704c603136308b87b26c4081bd6102d42395e`이며, OMM 실행기가 없어도 이 저장소만으로 같은 규칙을 적용할 수 있어야 합니다.
 ## 문서 분리와 이전 주소
 
+`소스 근거` 절의 발췌 목록 전체는 `소스 발췌 N개` 한 줄로 접습니다. 펼친 목록에서 개별 발췌를 다시 열 수 있으며, 본문의 발췌 링크로 이동하면 바깥 목록과 해당 발췌를 모두 펼치고 해당 요약에 초점을 옮깁니다. 기존 절·발췌 주소와 원문·해시는 보존하며 스크립트 없이도 두 단계 접기를 조작할 수 있어야 합니다.
+
 긴 문서의 질문·근거를 다른 페이지로 옮기면 기존 절 주소도 유지합니다.
 `routes[].anchor`에 정규화된 이전 제목 ID를 선언하면 이동 안내 표의 정적 앵커에서
 새 페이지로 연결합니다. 제목과 앵커 ID가 충돌하거나 같은 ID를 두 번 선언하면 실패합니다.
diff --git a/docs/concepts/site.md b/docs/concepts/site.md
index 6559269..5d4b5e2 100644
--- a/docs/concepts/site.md
+++ b/docs/concepts/site.md
@@ -187,6 +187,10 @@ site:
 
 변경 후에는 Vendor·Developer 페이지에서 다음을 확인하세요.
 
+`소스 근거` 절에서는 발췌 목록 전체를 `소스 발췌 N개` 한 줄로 접습니다. 목록을 펼친 뒤 개별 원문을 열 수 있고, 본문의 발췌 링크로 이동하면 두 단계가 함께 열립니다. 원고를 재생성하지 않아도 기존 발췌·해시·주소를 보존하여 적용합니다. 스크립트를 끈 상태에서도 목록과 개별 발췌를 키보드로 열 수 있는지 확인하세요.
+
+기존 CLI 감사 영수증을 읽는 사이트 빌드는 과거 실행 파일의 설치 여부를 요구하지 않습니다. 기록된 요청·응답·stdout·실행 인자와 현재 검사 정책은 그대로 대조합니다. 새 CLI 실행은 별도로 설치된 실행 파일을 확인합니다.
+
 1. 기본 화면에서 설명이 보이고 근거 목록은 접혀 있습니다.
 2. `문단 근거`를 Enter와 Space로 펼쳐 해당 문단의 위치를 찾습니다. `절 전체 근거`에서도 같은 발췌에 도달합니다.
 3. 문단 근거에 유일한 로컬 발췌가 있으면 **발췌**를 먼저 표시합니다. 누르면 도착한 원문을 펼치고 요약에 초점을 둡니다. **전체 소스**는 원래 코드 호스트의 커밋·파일·줄을 유지합니다. 발췌가 모호하면 임의로 고르지 않습니다. 스크립트가 없으면 해당 위치에서 기본 `summary`로 직접 펼칠 수 있습니다.
diff --git a/docs/inhouse/cli-agents.md b/docs/inhouse/cli-agents.md
index 261134c..8d41f30 100644
--- a/docs/inhouse/cli-agents.md
+++ b/docs/inhouse/cli-agents.md
@@ -33,6 +33,18 @@ OpenCode에서는 `runner: opencode`와 해당 CLI의 `provider/model` ID를, Cl
 
 공개 libcamera의 기본 프로필은 [예제 설정](../../examples/libcamera/sdd.yaml)에 저장합니다. 같은 환경에서 새 Qwen 시험을 실행할 때는 이 모델과 `high`를 사용합니다. 기존 HTTP·CLI 시험 기록의 모델이나 추론 설정은 바꾸지 않습니다.
 
+이 프로젝트의 LLM 검토는 별도 실행 설정에서 독립 Codex CLI의 `gpt-6.1-terra`와 reasoning effort `high`를 사용합니다. 생성·번역용 Hermes 프로필은 유지하고, 검토 명령에는 검토용 설정 경로를 명시합니다. 과거 실행 기록은 당시 모델·인자를 그대로 보존합니다.
+
+```yaml
+agent:
+  kind: cli
+  runner: codex
+  model: gpt-6.1-terra
+  args: [-c, 'model_reasoning_effort="high"']
+```
+
+위 블록은 전체 실행 설정에서 교체할 `agent` 항목입니다. 소스·facts·원고·검토 정책을 포함한 별도 전체 설정에 적용하고 해당 파일을 `--config`로 지정합니다. 실행에 실패하면 검토 미완료를 보고하며 직접 API나 다른 CLI로 대체하지 않습니다. 자동 검토 결과는 사람 승인이 아닙니다.
+
 사내에서는 자체 `sdd.yaml`을 사용하거나 `sdd.local.yaml`로 모델·제공자·추론 강도를 교체할 수 있습니다. 예를 들어 다음 값은 공개 예제의 `model`과 `args`를 대체합니다. `args`는 목록 전체가 교체되므로 사용할 실행기의 인자를 모두 적으세요.
 
 ```yaml
diff --git a/examples/libcamera/english.json b/examples/libcamera/english.json
index 23298d9..b240b61 100644
--- a/examples/libcamera/english.json
+++ b/examples/libcamera/english.json
@@ -1186,6 +1186,7 @@
   "선택한 시나리오의 코드 읽기 순서": "Code reading order for the selected scenario",
   "설계 질문": "Design question",
   "설계 질문과 검증 범위": "Design questions and validation scope",
+  "소스 발췌 {{1}}개": "Source excerpts · {{1}}",
   "설명": "Explanation",
   "설명 (주석)": "Description (comment)",
   "설명 위치": "Explanation location",
diff --git a/src/sdd/cli_checkpoint.py b/src/sdd/cli_checkpoint.py
index eb0ee51..778352e 100644
--- a/src/sdd/cli_checkpoint.py
+++ b/src/sdd/cli_checkpoint.py
@@ -145,8 +145,10 @@ class UnitStore:
             arguments = record.receipt['provider'].get('arguments')
             # A historical receipt without actual CLI arguments is insufficient
             # for this optimization; ordinary manuscript provenance is separate.
-            from .cli_agent import command, arguments as invocation_arguments
-            expected = command(self.cfg.agent)[1:] + invocation_arguments(self.cfg.agent, record.request['response_schema'])
+            from .cli_agent import arguments as invocation_arguments
+            # Validating an archived call does not execute its historical binary.
+            # Keep the exact configured prefix arguments without resolving PATH.
+            expected = self.cfg.agent.command[1:] + invocation_arguments(self.cfg.agent, record.request['response_schema'])
             if arguments != expected:
                 raise ValueError('CLI checkpoint arguments mismatch')
             rows.append(record)
diff --git a/src/sdd/evidence_navigation.py b/src/sdd/evidence_navigation.py
index 56715c5..e2f3076 100644
--- a/src/sdd/evidence_navigation.py
+++ b/src/sdd/evidence_navigation.py
@@ -17,6 +17,22 @@ _ITEMS = re.compile(_ITEM)
 _LOCAL = re.compile(r'<a href="(#source-[0-9a-f]{16})">([^<>]+:\d+)</a>')
 
 
+def fold_source_details(document: str) -> str:
+    """Collapse the generated excerpt collection, preserving each inner inspector."""
+    def section(match):
+        heading, body = match.groups()
+        count = len(re.findall(r'<a id="source-[0-9a-f]{16}"></a>', body))
+        return (heading + '\n<details class="source-excerpts"><summary>소스 발췌 '
+                + f'<span>{count}</span>개</summary>\n' + body + '\n</details>\n')
+
+    # SourceDetails emits an introduction followed by anchor/inspector pairs.
+    # Stop at the last pair so trailing review metadata stays outside the fold.
+    intro = re.escape('<p>같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.</p>')
+    inspector = r'<p><a id="source-[0-9a-f]{16}"></a></p>\s*<details class="note">.*?</details>'
+    return re.sub(r'(<h2 id="소스-근거">소스 근거</h2>)\s*('
+                  + intro + r'(?:\s*' + inspector + r')+)\s*', section, document, flags=re.S)
+
+
 def _panel(refs: list[tuple[str, str]], scope: str, destinations=None) -> str:
     groups = defaultdict(list)
     for cite, element in refs:
diff --git a/src/sdd/site_assets/reading.css b/src/sdd/site_assets/reading.css
index a2b9228..0210825 100644
--- a/src/sdd/site_assets/reading.css
+++ b/src/sdd/site_assets/reading.css
@@ -70,6 +70,7 @@ button.term{display:inline;font:inherit;color:inherit;background:none;border:0;b
 .state-help{font-size:12px;color:var(--muted)}.state-help:hover{color:var(--accent)}
 
 /* Evidence belongs to the preceding paragraph; native disclosure works offline. */
+details.source-excerpts{margin:16px 0;overflow-wrap:anywhere}.source-excerpts>details{margin:12px 0}.source-excerpts>summary{min-height:28px}
 details.evidence-links{border:0;border-left:2px solid var(--line);border-radius:0;padding:0 12px;margin:-7px 0 20px;font-size:12px;color:var(--muted)}
 .evidence-links>summary{font-weight:400;padding:4px 0;min-height:28px;width:fit-content}
 .evidence-links>summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
diff --git a/src/sdd/site_assets/site.js b/src/sdd/site_assets/site.js
index 1ac5717..e5572fd 100644
--- a/src/sdd/site_assets/site.js
+++ b/src/sdd/site_assets/site.js
@@ -11,8 +11,12 @@
     const anchor = target?.parentElement?.tagName === 'P' ? target.parentElement : target;
     const panel = anchor?.nextElementSibling;
     if (panel?.tagName === 'DETAILS') {
+      for (let parent = panel.parentElement; parent; parent = parent.parentElement) {
+        if (parent.tagName === 'DETAILS') parent.open = true;
+      }
       panel.open = true;
       panel.querySelector('summary')?.focus({preventScroll: true});
+      panel.scrollIntoView({block: 'start'});
     }
   }
   window.addEventListener('hashchange', revealEvidence);
diff --git a/src/sdd/site_markdown.py b/src/sdd/site_markdown.py
index d1cddd6..30615ed 100644
--- a/src/sdd/site_markdown.py
+++ b/src/sdd/site_markdown.py
@@ -6,7 +6,7 @@ import re
 from pathlib import PurePosixPath
 from urllib.parse import quote,urlsplit
 import markdown
-from .evidence_navigation import compact_evidence
+from .evidence_navigation import compact_evidence, fold_source_details
 from .export_html import _mermaid_fence
 from .facts.model import KnowledgeModel
 SOURCE_LINK_TEMPLATES = {
@@ -64,6 +64,7 @@ def _render(body: str, rel: str, known: set[str], model: KnowledgeModel | None,
         rendered = re.sub(r"<code>([^<>]+:\d+)</code>", citation, rendered)
     valid = model.citations() if model and commit == model.meta.get("source_commit") else set()
     rendered = compact_evidence(rendered, valid)
+    rendered = fold_source_details(rendered)
 
     def table_wrapper(match: re.Match) -> str:
         table = match[0]
diff --git a/tests/test_consistency.py b/tests/test_consistency.py
index 66bd63a..d2cf5ed 100644
--- a/tests/test_consistency.py
+++ b/tests/test_consistency.py
@@ -202,6 +202,12 @@ def test_audit_requires_real_archives_and_rejects_stale_or_tampered_report(tmp_c
     report = audit(tmp_cfg, model, agent())
     assert report['status']=='passed' and report['human_review']=='pending'
     enforce(tmp_cfg, model)
+    with monkeypatch.context() as missing_cli:
+        def unavailable(cfg):
+            raise RuntimeError('Historical CLI binary was removed by an app update')
+        missing_cli.setattr('sdd.cli_agent.command', unavailable)
+        enforce(tmp_cfg, model)
+        assert len(calls) == 1  # Archive validation never needs to launch a CLI.
     for field in ('claims', 'sources', 'source_aliases'):
         altered = copy.deepcopy(report)
         altered['contracts'][0][field] = {}
diff --git a/tests/test_evidence_navigation.py b/tests/test_evidence_navigation.py
index 02b353e..04c5fc7 100644
--- a/tests/test_evidence_navigation.py
+++ b/tests/test_evidence_navigation.py
@@ -2,7 +2,7 @@
 import re
 from collections import Counter
 
-from sdd.evidence_navigation import compact_evidence
+from sdd.evidence_navigation import compact_evidence, fold_source_details
 from sdd.export_site import _render
 from sdd.site_localization import DisplayText, display_strings
 
@@ -79,3 +79,39 @@ def test_english_ui_keeps_evidence_identifiers_and_destinations():
     translated = ''.join(parser.output)
     assert 'Paragraph evidence · <span>1</span>' in translated
     assert 'title="a.cpp:1"' in translated
+
+
+def test_source_collection_folds_without_changing_excerpts_or_adjacent_sections():
+    from sdd.contract_render import SourceDetails
+    sources = SourceDetails()
+    sources.records = {
+        'source-' + digit * 16: ({}, dict(file=f'src/{digit}.cpp', line=1,
+                                        end_line=3, sha256=digit * 64,
+                                        text='// Preserve <condition>\nreturn 0;'))
+        for digit in ('1', '2')
+    }
+    review = '\n\n??? note "근거와 검토 정보"\n    사람 검토 전입니다.\n'
+    body = '## 설명\n\n설명입니다.\n\n' + sources.render() + review + '\n\n## 다음 절\n\n다음 설명입니다.'
+    rendered, toc, _ = _render(body, 'test.md', set(), None, '', '')
+    assert '<summary>소스 발췌 <span>2</span>개</summary>' in rendered
+    assert '<details class="source-excerpts">' in rendered
+    assert '소스-근거' in toc
+    assert '</details>\n<details class="note">\n<summary>근거와 검토 정보</summary>' in rendered
+    assert rendered.index('근거와 검토 정보') < rendered.index('<h2 id="다음-절">')
+    assert 'open' not in rendered
+    for digit in ('1', '2'):
+        assert rendered.count(f'id="source-{digit * 16}"') == 1
+        assert digit * 64 in rendered
+    assert rendered.count('Preserve &lt;condition&gt;') == 2
+    assert fold_source_details(rendered) == rendered
+    assert '소스 발췌 {{1}}개' in display_strings(rendered)
+    parser = DisplayText(lambda value: value.replace('소스 발췌 {{1}}개', 'Source excerpts · {{1}}'))
+    parser.feed(rendered)
+    assert '<summary>Source excerpts · <span>2</span></summary>' in ''.join(parser.output)
+
+
+def test_ordinary_source_heading_and_example_markup_are_not_folded():
+    source = '<h2 id="소스-근거">소스 근거</h2><p>Ordinary explanation.</p>'
+    assert fold_source_details(source) == source
+    example = '<pre><code>' + source.replace('<', '&lt;').replace('>', '&gt;') + '</code></pre>'
+    assert fold_source_details(example) == example

Context:
"""Atomic, receipt-bound checkpoints for completed CLI design units.

Only fully validated answers enter this store. Loading verifies original CLI
archives and reruns current deterministic checks and exact grounding verdicts.
It never turns an imported response into a new call or a human approval.
"""
from __future__ import annotations

import hashlib
import ast
import json
from pathlib import Path

from .call_records import canonical_request_hash, load_record
from .cli_provenance import verify_cli_receipt
from .state_io import save
from .trial_workspace import contained_path, reject_symlinks
from .llm import AgentError


def checksum(value):
    return canonical_request_hash(value)


def execution_identity(agent_config, schema):
    """Keep invocation details at the receipt/checkpoint boundary, byte-exact."""
    from .cli_agent import arguments
    return dict(runner=agent_config.runner, model=agent_config.model,
                command=agent_config.command, args=agent_config.args,
                arguments=arguments(agent_config, schema))


def validation_policy():
    # Lexical/source/contract checks are distinct from model entailment policy.
    # Content hashes change with code; no compatibility aliases are added here.
    root = Path(__file__).parent
    policy = {name: hashlib.sha256((root / (name + '.py')).read_bytes()).hexdigest()
              for name in ('manuscript', 'semantic', 'duplicates', 'design_contracts', 'validate',
                           'reader_profiles', 'contract_schema', 'answer_contracts')}
    # All pure response helpers participate, including quote resolution and
    # normalization called transitively by the selected validation functions.
    policy['design_response'] = hashlib.sha256((root/'design_response.py').read_bytes()).hexdigest()
    selected = {'materialize', 'validate_answers', 'decode_unit', 'normalize_answer', '_validate_unit_response'}
    nodes = []
    for module in ('design_response', 'design_execution'):
        tree = ast.parse((root/(module+'.py')).read_text(encoding='utf-8'))
        nodes.extend(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in selected)
    if {node.name for node in nodes} != selected:
        raise ValueError('Design validation policy functions are missing')
    policy['design_validation'] = hashlib.sha256(ast.dump(ast.Module(body=nodes, type_ignores=[]),
                                                         include_attributes=False).encode()).hexdigest()
    return policy


def validation_model(model):
    """Bind validator inputs without redrafting source-identical answers."""
    return checksum(dict(classes={name: item.bases for name, item in model.classes.items()},
                         functions=sorted(model.functions),
                         relations=sorted((r.source, r.target, r.type) for r in model.relations),
                         citations=sorted(model.citations())))


def style_policy(cfg):
    return {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(cfg.style_dir.glob('*.md'))}


def same_request_context(expected, actual):
    if actual.startswith(expected):
        return True  # Standard retries append the error after the full request.
    prefix, marker, suffix = expected.rpartition('\n출력:')
    if '\nDraft to check (untrusted, not evidence):\n' in actual:
        actual = actual.rpartition('\nDraft to check (untrusted, not evidence):\n')[0]
    return bool(marker and actual.startswith(prefix + '\n작성 조건: ')
                and actual.endswith(marker + suffix))  # Focused retries insert diagnostics before output.


class Capture:
    def __init__(self, agent):
        self.agent, self.receipts = agent, []

    def __getattr__(self, name):
        return getattr(self.agent, name)

    def chat(self, system, user, **kwargs):
        raw = self.agent.chat(system, user, **kwargs)
        path = getattr(self.agent, 'last_receipt', None)
        if path is not None:
            self.receipts.append(Path(path))
        return raw


class UnitStore:
    _indexes = {}

    def __init__(self, cfg, identity):
        self.cfg, self.identity = cfg, identity
        self.path = cfg.build_dir / 'cli-checkpoints' / (checksum(self.draft_identity(identity)) + '.json')
        self.canonical_path = self.path
        self.calls = cfg.build_dir / 'prompts' / 'calls'
        if not self.path.exists() and self.path.parent.exists():
            directory = reject_symlinks(self.path.parent).resolve()
            if directory not in self._indexes:
                index = {}
                for candidate in directory.glob('*.json'):
                    reject_symlinks(candidate)
                    try:
                        data = json.loads(candidate.read_text(encoding='utf-8'))
                        payload = data['payload']
                        if data['sha256'] != checksum(payload):
                            raise ValueError('checkpoint checksum mismatch')
                        key = checksum(self.compatible_identity(payload['identity']))
                        index.setdefault(key, candidate)
                    except (ValueError, KeyError, TypeError, OSError) as exc:
                        raise ValueError(f'CLI checkpoint is damaged: {candidate}: {exc}') from exc
                self._indexes[directory] = index
            compatible = self._indexes[directory].get(checksum(self.compatible_identity(identity)))
            if compatible is not None:
                self.path = compatible

    @staticmethod
    def draft_identity(identity):
        return {key: value for key, value in identity.items()
                if key not in ('validation_policy', 'validation_model', 'validation_answers', 'grounding_policy')}

    @classmethod
    def compatible_identity(cls, identity):
        result = cls.draft_identity(identity)
        if isinstance(result.get('topic'), dict):
            result['topic'] = {key: value for key, value in result['topic'].items() if key != 'title'}
            if isinstance(result['topic'].get('answer_contract'), dict):
                result['topic']['answer_contract'] = {key: value for key, value in result['topic']['answer_contract'].items()
                                                       if key != 'reject_patterns'}
        # Actual system/user/schema, source revision and execution identity must
        # STILL match. Only a layout title and checks absent from the model's
        # input can use this path, always under current deterministic validation.
        return result

    def _records(self, paths):
        rows = []
        for name in paths:
            path = contained_path(self.calls, name)
            record = load_record(path, root=self.calls)
            verify_cli_receipt(record.request, record.raw, record.receipt, self.calls, self.cfg.agent)
            arguments = record.receipt['provider'].get('arguments')
            # A historical receipt without actual CLI arguments is insufficient
            # for this optimization; ordinary manuscript provenance is separate.
            from .cli_agent import arguments as invocation_arguments
            # Validating an archived call does not execute its historical binary.
            # Keep the exact configured prefix arguments without resolving PATH.
            expected = self.cfg.agent.command[1:] + invocation_arguments(self.cfg.agent, record.request['response_schema'])
            if arguments != expected:
                raise ValueError('CLI checkpoint arguments mismatch')
            rows.append(record)
        return rows

    def read(self):
        if not self.path.exists():
            return None
        try:
            reject_symlinks(self.path)
            data = json.loads(self.path.read_text(encoding='utf-8'))
            payload = data['payload']
            if (data['sha256'] != checksum(payload)
                    or self.compatible_identity(payload['identity']) != self.compatible_identity(self.identity)
                    or not isinstance(payload['receipts'], list) or not payload['receipts']):
                raise ValueError('checkpoint identity or checksum mismatch')
            records = self._records(payload['receipts'])
            request = self.identity['request']
            if not any(row.raw == payload['raw'] and row.request['system'] == request['system']
                       and same_request_context(request['user'], row.request['user'])
                       and row.request.get('response_schema') == request['response_schema'] for row in records):
                raise ValueError('validated response has no completed CLI receipt')
            return payload, Reviewer(records)
        except (ValueError, OSError, KeyError, TypeError) as exc:
            raise ValueError(f'CLI checkpoint is damaged; previous output preserved: {self.path}: {exc}') from exc

    def write(self, raw, statements, capture):
        if not capture.receipts:
            # A custom ChatPort without an archive is allowed, but cannot certify
            # a durable checkpoint as a real CLI call.
            return
        try:
            paths = [path.resolve().relative_to(self.calls.resolve()).as_posix() for path in capture.receipts]
            self._records(paths)
            payload = dict(identity=self.identity, raw=raw, statements=statements, receipts=paths)
            save(self.canonical_path, dict(schema=1, payload=payload, sha256=checksum(payload)), newline='\n')
            self.path = self.canonical_path
            directory = self.path.parent.resolve()
            if directory in self._indexes:
                self._indexes[directory][checksum(self.compatible_identity(self.identity))] = self.path
        except (ValueError, OSError) as exc:
            raise AgentError(f'CLI checkpoint persistence failed; previous output preserved: {exc}') from exc


class Reviewer:
    def __init__(self, records):
        self.records = {canonical_request_hash(row.request): row.raw for row in records}

    def chat(self, system, user, **kwargs):
        key = canonical_request_hash(dict(system=system, user=user, response_schema=kwargs.get('response_schema')))
        if key not in self.records:
            raise ValueError('CLI checkpoint lacks the exact current grounding review receipt')
        return self.records[key]

"""Validate CLI call archives without executing a runner or changing manuscripts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any, Callable

from .config import AgentConfig
from .cli_agent import RUNNERS, build_prompt as assemble_prompt, decode_response, arguments as invocation_arguments
from .cli_schema import schema_hash, validate_original
from .trial_workspace import is_link

PromptBuilder = Callable[[str, str, dict | None], str]
StdoutDecoder = Callable[[str, str], tuple[str, dict]]


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def _stdout_file(calls: Path, name: Any) -> Path:
    # cli_agent stores POSIX paths relative to dump_dir, the parent of calls/.
    # Reject traversal before resolution and links even when their target is inside.
    if not isinstance(name, str) or '\\' in name or ':' in name:
        raise ValueError('Unsafe CLI stdout path')
    parts = name.split('/')
    if len(parts) < 2 or parts[0] != 'cli' or any(p in ('', '.', '..') for p in parts):
        raise ValueError('Unsafe CLI stdout path')
    if PurePosixPath(name).is_absolute():
        raise ValueError('Unsafe CLI stdout path')
    if is_link(calls):
        raise ValueError('Linked CLI calls directory is not allowed')
    try:
        if not calls.is_dir():
            raise ValueError('CLI calls archive is not a directory')
        base = calls.resolve(strict=True).parent
        path = base.joinpath(*parts)
        current = path
        while current != base:
            if is_link(current):
                raise ValueError('Linked CLI stdout path is not allowed')
            current = current.parent
        resolved = path.resolve(strict=True)
        if not resolved.is_relative_to(base / 'cli') or not resolved.is_file():
            raise ValueError('Unsafe CLI stdout path')
        return resolved
    except OSError as exc:
        raise ValueError('CLI stdout archive is missing or unreadable') from exc


def verify_cli_receipt(request: dict, response: str, receipt: dict, calls: Path,
                       expected: AgentConfig, *, build_prompt: PromptBuilder = assemble_prompt,
                       decode_stdout: StdoutDecoder = decode_response) -> dict:
    """Bind a saved response to the selected CLI's prompt and completed raw output.

    Pass the same prompt builder and decoder used by cli_agent.chat. Callbacks
    keep transport formatting in that module rather than duplicating it here.
    This checks archive integrity, not semantic correctness or human approval.
    A CLI's default model remains an unverified runtime selection.
    """
    if expected.kind != 'cli' or expected.runner not in RUNNERS:
        raise ValueError('CLI provenance requires an explicitly selected CLI runner')
    if not isinstance(receipt, dict):
        raise ValueError('Invalid CLI receipt archive')
    metadata = receipt.get('provider')
    selection = 'explicit' if expected.model else 'cli-default'
    if (type(receipt.get('schema')) is not int or receipt['schema'] != 1
            or receipt.get('transport') != 'cli' or receipt.get('cli_call') is not True
            or receipt.get('http_call') is not False or receipt.get('model') != expected.model
            or not isinstance(metadata, dict) or metadata.get('runner') != expected.runner
            or metadata.get('model_selection') != selection
            or type(metadata.get('exit_code')) is not int or metadata['exit_code'] != 0):
        raise ValueError('CLI receipt identity or completion mismatch')
    if (not isinstance(request, dict) or set(request) != {'system', 'user', 'response_schema'}
            or not isinstance(request['system'], str) or not isinstance(request['user'], str)
            or not (request['response_schema'] is None or isinstance(request['response_schema'], dict))
            or not isinstance(response, str) or not response.strip()):
        raise ValueError('Invalid CLI request or response archive')
    arguments_verified = bool(expected.command or expected.args)
    if arguments_verified:
        recorded = metadata.get('arguments')
        native = invocation_arguments(expected, request['response_schema'])
        if (not isinstance(recorded, list) or any(not isinstance(value, str) for value in recorded)
                or (recorded != expected.command[1:] + native if expected.command
                    else recorded[-len(native):] != native)):
            raise ValueError('CLI arguments differ from the expected configuration')
    request_hash = _digest(json.dumps(request, ensure_ascii=False, sort_keys=True))
    if (receipt.get('request_sha256') != request_hash
            or receipt.get('response_sha256') != _digest(response)):
        raise ValueError('CLI request or response hash mismatch')
    prompt = build_prompt(request['system'], request['user'], request['response_schema'])
    if not isinstance(prompt, str) or metadata.get('prompt_sha256') != _digest(prompt):
        raise ValueError('CLI prompt hash mismatch')
    path = _stdout_file(calls, metadata.get('stdout_path'))
    try:
        stdout = path.read_bytes().decode('utf-8')
    except (OSError, UnicodeError) as exc:
        raise ValueError('CLI stdout archive is missing or unreadable') from exc
    if metadata.get('stdout_sha256') != _digest(stdout):
        raise ValueError('CLI stdout hash mismatch')
    try:
        decoded, provider = decode_stdout(expected.runner, stdout)
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        raise ValueError('CLI stdout does not contain a completed response') from exc
    if (not isinstance(decoded, str) or decoded != response
            or _digest(decoded) != receipt.get('response_sha256')
            or provider != metadata.get('provider')):
        raise ValueError('CLI decoded response or provider metadata mismatch')
    if expected.runner == 'codex':
        if metadata.get('native_schema_sha256') != schema_hash(request['response_schema']):
            raise ValueError('Codex native schema hash mismatch')
        validate_original(decoded, request['response_schema'])
    return {'runner': expected.runner, 'model': expected.model, 'model_selection': selection,
            'producer': expected.label, 'stdout_sha256': metadata['stdout_sha256'],
            'arguments_verified': arguments_verified}

