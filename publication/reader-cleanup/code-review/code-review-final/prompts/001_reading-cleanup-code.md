<!-- system -->
Review the complete public diff for concrete correctness, provenance/information loss, accessibility, localization and custom-content regressions. Known generated table shapes are narrowly selected. Related references may move only after all cell HTML matches a unique unchanged index row. Publication keeps the original Markdown/facts and independently checks all old IDs, source inspectors, symbol rows and trace tables. Do not infer runtime or internal HAL approval. No tools. Return actionable findings with evidence, or an empty findings list. Avoid speculative scope expansion.

<!-- user -->
diff --git a/DESIGN.md b/DESIGN.md
index c3043de..d755088 100644
--- a/DESIGN.md
+++ b/DESIGN.md
@@ -31,6 +31,10 @@
 기준은 libcamera 공식 문서의 탐색 방식과 OMM `DESIGN.md`의 reading 규칙입니다. OMM 기준 커밋은 `12a704c603136308b87b26c4081bd6102d42395e`이며, OMM 실행기가 없어도 이 저장소만으로 같은 규칙을 적용할 수 있어야 합니다.
 ## 문서 분리와 이전 주소
 
+메뉴·목차와 중복되는 안내는 반복해서 표시하지 않습니다. 원고 끝의 `다음 단계`가 하단 이동 버튼과 같은 주소이면 하나의 버튼으로 합치며, 별도의 안내 문구는 버튼에 보존합니다. 다른 목적지·사용자 정의 내용은 유지합니다. 첫 화면의 문서별 검사 상태는 같은 검사 결과와 사람 검토 상태끼리 묶고, 상태·문서 수는 바로 보이며 문서 링크는 펼쳐 확인할 수 있게 합니다. 실패·미승인 상태를 통과·승인으로 합치지 않습니다.
+
+설계 질문 검증 정보는 질문·답변 위치·실행 확인 조건을 목록으로 표시하고 공통 확인 범위는 한 번만 적습니다. 한 행뿐인 호출 확인·경계 표는 열 이름과 모든 셀을 보존한 정의 목록으로 표시합니다. 관련 클래스 표는 모든 셀이 유일한 색인 행과 완전히 같은 경우에만 해당 행의 링크로 바꿉니다. 색인이 없거나 값이 다르면 원래 표를 유지합니다. 원고·facts·발췌·해시·기존 절 주소와 의미 검토 상태는 바꾸지 않습니다.
+
 모바일 메뉴는 현재 본문 위치를 바꾸지 않는 화면 내 패널로 엽니다. 닫기·배경 클릭·Escape와 키보드 초점 순환을 지원하고 닫으면 호출 버튼으로 초점을 돌립니다. 스크립트가 없으면 전체 메뉴를 문서 안에서 읽을 수 있어야 합니다.
 
 발췌로 이동한 뒤 뒤로 가기나 `설명으로 돌아가기`를 사용하면 원래 인용 링크와 스크롤 위치를 복원합니다. 색인은 원고를 바꾸지 않고 클래스·함수 행의 고유 주소와 검색 항목을 만들며, 페이지 내 이름·경로·패키지·종류 필터를 제공합니다. 필터를 지우거나 검색 결과로 진입하면 해당 행을 볼 수 있어야 합니다. 스크립트 없이도 전체 표와 원본 코드 링크를 보존합니다.
diff --git a/docs/concepts/site.md b/docs/concepts/site.md
index 77a042d..25c52c3 100644
--- a/docs/concepts/site.md
+++ b/docs/concepts/site.md
@@ -6,6 +6,8 @@
 
 문서 메뉴·페이지 목차와 중복되는 `지금 확인할 내용 / 이동할 절` 표는 사이트에서 제거합니다. 기존 원고는 보존하며 예전 표 행의 주소로 진입할 때만 해당 목적지 링크를 표시합니다. 생성기 형식과 다른 사용자 정의 셀 내용은 임의로 삭제하지 않습니다.
 
+`reading_cleanup.py`는 검증 범위 표의 반복 열을 공통 안내와 질문별 목록으로 바꾸고, 한 행 호출 표는 열 이름이 있는 정의 목록으로 표시합니다. 첫 화면의 문서 상태는 검사·사람 검토 결과가 정확히 같은 항목끼리 묶습니다. 각 문서 링크와 실패·미승인 상태는 유지합니다. 관련 클래스는 전체 행이 유일한 색인 행과 일치할 때만 해당 행으로 연결하며, 다르거나 색인이 없으면 표를 보존합니다. 본문의 마지막 `다음 단계`와 하단 이동 버튼은 같은 주소일 때만 합치고 별도의 안내 문구도 유지합니다. 원고 파일은 감사용 원본으로 보존합니다.
+
 `site.overview_visual: {section: <섹션 ID>, visual: <그림 ID>}`를 지정하면 해당 문서의 검증된 질문 그림을 인덱스의 첫 문단 뒤에서도 보여 줍니다. 원래 문서의 현재 소스·원고·그림 검사를 통과한 정의를 인덱스 경로로 다시 렌더링하며 새 설명을 작성하거나 HTML을 복사하지 않습니다. 근거 링크는 원래 문서의 검증된 발췌로 연결합니다. 그림이나 섹션을 찾지 못하거나 근거가 달라졌으면 빌드를 실패시키고 기존 출력을 보존합니다. 프로젝트별 계층·그림 선택은 예제 설정에 둡니다.
 
 `paths.consistency_file`을 지정하면 [문서 간 계약 대조](contract-consistency.md)의 현재 검토와 원본 CLI 영수증을 확인한 뒤 빌드합니다. 확정 모순·오래된 입력·손상 기록은 게시를 막고, 자동 미판정 목록과 사람 검토 전 상태를 보존합니다. 통과한 보고서는 `contract-consistency.json`으로 동봉하여 같은 manifest에서 대조할 수 있게 합니다.
diff --git a/examples/libcamera/english.json b/examples/libcamera/english.json
index 9df019b..718c583 100644
--- a/examples/libcamera/english.json
+++ b/examples/libcamera/english.json
@@ -1898,6 +1898,11 @@
   "문서·절·용어·코드 요소 검색": "Search documents, sections, terms and symbols",
   "그림 요소·함수 이름": "Diagram element or function name",
   "그림이 화면보다 크면 가로·세로로 밀어 보세요. 전체 모양은 화면에 맞춤으로 확인합니다.": "Scroll horizontally or vertically when the diagram is larger than the screen. Use Fit to see the whole diagram.",
-  "이전 링크의 목적지": "Destination of the previous link"
+  "이전 링크의 목적지": "Destination of the previous link",
+  "문서 검증 현황": "Document validation status",
+  "선언·상속·주석은 각 클래스 링크에서 확인하세요.": "Follow each class link for its declaration, inheritance and source comment.",
+  "실행 확인 항목 별도": "Runtime checks are separate",
+  "페이지 첫 문장과 목차에서 지금 확인할 내용을 고릅니다.": "Use the opening sentence and page contents to choose what to read.",
+  "절 전체 근거의 {{1}}를 누르면 이 문서 안의 원문이 펼쳐집니다. {{3}}는 해당 커밋의 코드 저장소로 이동합니다.": "Select {{1}} under the section evidence to expand the original text in this document. {{3}} opens the source repository at the analyzed commit."
  }
 }
diff --git a/examples/libcamera/site-intro.md b/examples/libcamera/site-intro.md
index 229047e..9ee33ab 100644
--- a/examples/libcamera/site-intro.md
+++ b/examples/libcamera/site-intro.md
@@ -2,8 +2,6 @@
 
 **기능·강점·연동 조건을 판단하려면 For Vendor에서, 처음 구조를 배우거나 다른 팀의 코드를 수정하려면 For Developer에서 시작하세요.**
 
-왼쪽 메뉴는 **독자 → 수행할 작업 → 문서** 순서입니다. For Vendor에서는 도입 판단·연동 구현·장치별 기능 구현을, For Developer에서는 구조 이해·동작 추적과 문제 진단·코드 탐색을 선택하세요.
-
 ## Vendor가 먼저 확인할 내용
 
 1. [libcamera 제품 개요](vendor-overview.md)에서 해결하는 문제, 제공 기능과 공통 설계의 강점을 확인합니다.
@@ -34,11 +32,9 @@ For Developer는 신입·타팀 개발자를 위한 경로입니다. 클래스 
 | 처음 구조를 배우고 수정할 코드를 찾습니다. | [시스템 개요](overview.md) |
 | 객체 수명과 상태 전이를 확인합니다. | [카메라와 요청 모델](camera-model.md) |
 
-하드웨어 지원을 추가하거나 파이프라인·알고리즘을 수정한다면 **[libcamera 제품 개요](vendor-overview.md)**부터 읽으세요. 구현할 경계와 계약을 확인한 뒤 작업별 상세 문서로 이동할 수 있습니다.
-
 ## 기준 설명 찾기
 
-요청·버퍼의 소유권과 재사용 규칙은 **카메라와 요청 모델**, 장치 큐와 완료 순서의 구현 규칙은 **Pipeline Handler**에서 관리합니다. 진단 문서는 이 계약을 연결하여 증상별 확인 순서를 안내합니다.
+요청·버퍼의 소유권과 재사용 규칙은 **[요청 객체와 버퍼 수명](camera-requests.md)**, 장치 큐와 완료 순서의 구현 규칙은 **[Pipeline 요청 제출과 완료](pipeline-requests.md)**에서 관리합니다. 진단 문서는 이 계약을 연결하여 증상별 확인 순서를 안내합니다.
 
 알고리즘을 따라가려면 [IPU3 LSC의 설정과 프레임 처리](ipu3-lsc-flow.md)를 여세요. 카메라별 튜닝과 커널 지원 조건은 [RKISP1 카메라별 왜곡 보정](rkisp1-dewarp.md)에서 확인합니다.
 
@@ -46,7 +42,7 @@ For Developer는 신입·타팀 개발자를 위한 경로입니다. 클래스 
 
 ## 문서를 읽는 방법
 
-1. 페이지 첫 문장과 이동 안내에서 지금 확인할 항목을 고릅니다.
+1. 페이지 첫 문장과 목차에서 지금 확인할 내용을 고릅니다.
 2. 절 전체 근거의 **발췌**를 누르면 이 문서 안의 원문이 펼쳐집니다. **전체 소스**는 해당 커밋의 코드 저장소로 이동합니다.
 3. 실행 확인 항목은 대상 기기의 검증 계획에 옮깁니다.
 
diff --git a/src/sdd/export_site.py b/src/sdd/export_site.py
index 5910211..fc44966 100644
--- a/src/sdd/export_site.py
+++ b/src/sdd/export_site.py
@@ -201,11 +201,16 @@ def _prepare_site_pages(cfg, settings, sections, entries, *, check_consistency=T
             texts["index.md"] = (cfg.root / str(intro)).read_text(encoding="utf-8")
         else:
             texts["index.md"] = "# 문서 안내\n\n코드에서 추출한 구조와 문장별 근거를 함께 확인하세요.\n"
-        texts["index.md"] += "\n## 문서 목록\n\n| 문서 | 검사 결과 | 검토 상태 |\n|---|---|---|\n"
+        texts["index.md"] += "\n## 문서 검증 현황 {#문서-목록}\n\n"
+        status_groups = {}
         for _, name, rel in entries:
             check_name, result, _ = _check(split_frontmatter(texts[rel])[0])
             label = _approval_label(approval_states.get(rel, "unreviewed"), ledger["pages"].get(rel))
-            texts["index.md"] += f"| [{name}]({rel}) | {check_name} {result} | {label} |\n"
+            status_groups.setdefault((f'{check_name} {result}', label), []).append((name, rel))
+        for (check, approval), pages in status_groups.items():
+            summary = (f'<span>{html.escape(check)}</span> · <span>{html.escape(approval)}</span> '
+                       f'(<span>{len(pages)}</span>)')
+            texts['index.md'] += f'??? note "{summary}"\n' + ''.join(f'    - [{name}]({rel})\n' for name, rel in pages) + '\n'
         entries.insert(0, ("시작하기", "문서 안내", "index.md"))
         approval_states["index.md"] = "unreviewed"
     # 용어집은 표시용이다. 원고를 바꾸지 않고, 뜻이 없는 약어가 있으면 게시 전에 멈춘다.
@@ -353,6 +358,12 @@ def _render_pages(cfg, entries, sections, texts, terms, model, source_url, link_
         search.append({"title": page_title, "page": page_title, "url": _html_path(rel)})
 
         search.extend(_heading_search(tokens, page_title, rel))
+    from .reading_cleanup import class_targets, link_related_classes
+    targets = class_targets({_html_path(rel): page[2] for rel, page in rendered_pages.items()
+                             if sections.get(rel, {}).get('kind') == 'per-package'})
+    for rel, (page_title, meta, content, toc) in rendered_pages.items():
+        if sections.get(rel, {}).get('kind', 'prose') == 'prose':
+            rendered_pages[rel] = (page_title, meta, link_related_classes(content, _html_path(rel), targets), toc)
     return rendered_pages, search, diagram_sources, visual_sources
 
 
@@ -454,6 +465,10 @@ def _write_pages(cfg, out, entries, sections, rendered_pages, approval_states, l
         page_title, meta, content, toc = rendered_pages[rel]
         nav = _navigation_html(entries, sections, rel, current)
         previous_next = _pagination_html(entries, sections, index, rel, current)
+        from .reading_cleanup import merge_next_step
+        for i, following in enumerate(previous_next):
+            if following.startswith('<a class="next"'):
+                content, previous_next[i] = merge_next_step(content, following)
         info = []
         method_label, method_scope = generation_info(str(meta.get("generation_method", "")))
         if meta:
diff --git a/src/sdd/reading_cleanup.py b/src/sdd/reading_cleanup.py
new file mode 100644
index 0000000..7b3ca98
--- /dev/null
+++ b/src/sdd/reading_cleanup.py
@@ -0,0 +1,115 @@
+"""Compact generated reading aids while preserving their unique information."""
+from __future__ import annotations
+
+import html
+import posixpath
+import re
+from urllib.parse import quote
+
+
+def cells(row: str, tag: str = 'td') -> tuple[str, ...]:
+    return tuple(cell.strip() for cell in re.findall(rf'<{tag}\b[^>]*>(.*?)</{tag}>', row, re.S))
+
+
+def reference_cells(row: str) -> tuple[str, ...]:
+    return tuple(re.findall(r'<td\b[^>]*>.*?</td>', row, re.S))
+
+
+def compact_tables(document: str) -> str:
+    """Only recognized coverage blocks and one-row call tables change form."""
+    intro = '질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.'
+    common = '코드 근거와 설명 연결'
+
+    def coverage(match):
+        prefix, table, suffix = match.groups()
+        if re.search(r'<(?:table|thead|tbody|tr|th|td)\s', table):
+            return match[0]
+        if cells(table, 'th') != ('설계 질문', '설명 위치', '확인 범위'):
+            return match[0]
+        items = []
+        for row in re.findall(r'<tr>(.*?)</tr>', table, re.S):
+            values = cells(row)
+            if not values:
+                continue
+            if len(values) != 3 or values[2] not in (common, common + ' · 실행 확인 항목 별도'):
+                return match[0]
+            question, links, scope = values
+            qualifier = '<p>실행 확인 항목 별도</p>' if scope != common else ''
+            items.append('<li><p>' + question + '</p><p>' + links + '</p>' + qualifier + '</li>')
+        if not items or re.search(r'\bid=', table):
+            return match[0]
+        return (prefix + '<ul class="coverage-links">' + ''.join(items) + '</ul>'
+                + '<p><span>확인 범위</span>: <span>' + common + '</span></p>' + suffix)
+
+    # Full generated context keeps unrelated/custom tables untouched.
+    coverage_pattern = (r'(<details class="note">\s*<summary>설계 질문과 검증 범위</summary>\s*<p>'
+                        + re.escape(intro) + r'</p>\s*)(<table>.*?</table>)(\s*</details>)')
+    headers = {('확인할 내용', '호출 측과 대상', '구분', '근거'),
+               ('호출 지점', '후보 또는 예약 대상', '확인할 경계', '근거')}
+
+    def single_call(match):
+        table = match[0]
+        if re.search(r'<(?:table|thead|tbody|tr|th|td)\s', table):
+            return table
+        labels = cells(table, 'th')
+        rows = [cells(row) for row in re.findall(r'<tr>(.*?)</tr>', table, re.S)]
+        rows = [row for row in rows if row]
+        if labels not in headers or len(rows) != 1 or len(rows[0]) != len(labels) or re.search(r'\bid=', table):
+            return table
+        return '<dl class="call-checkpoint">' + ''.join('<dt>' + key + '</dt><dd>' + value + '</dd>'
+                                                       for key, value in zip(labels, rows[0])) + '</dl>'
+
+    chunks = re.split(r'(<pre\b[^>]*>.*?</pre>)', document, flags=re.S)
+    return ''.join(chunk if i % 2 else re.sub(r'<table>.*?</table>', single_call,
+                                             re.sub(coverage_pattern, coverage, chunk, flags=re.S), flags=re.S)
+                   for i, chunk in enumerate(chunks))
+
+
+def class_targets(indexes: dict[str, str]) -> dict[tuple[str, ...], str]:
+    """Only an unambiguous, byte-equal index row can replace a local reference."""
+    targets = {}
+    for page, document in indexes.items():
+        for anchor, row in re.findall(r'<tr id="(symbol-[0-9a-f]{16}(?:-\d+)?)" tabindex="-1" data-symbol-kind="class">(.*?)</tr>', document, re.S):
+            key = reference_cells(row)
+            targets.setdefault(key, []).append(page + '#' + anchor)
+    return {key: values[0] for key, values in targets.items() if len(values) == 1}
+
+
+def link_related_classes(document: str, page: str, targets: dict[tuple[str, ...], str]) -> str:
+    def related(match):
+        heading, table = match.groups()
+        if cells(table, 'th') != ('클래스', '선언 위치', '상속', '책임 (주석)') or re.search(r'\bid=', table):
+            return match[0]
+        if re.search(r'<(?:table|thead|tbody|tr|th)\s', table):
+            return match[0]
+        if any(not re.fullmatch(r'<td(?: data-label="[^"]*")?>', tag) for tag in re.findall(r'<td\b[^>]*>', table)):
+            return match[0]
+        rows = [reference_cells(row) for row in re.findall(r'<tr>(.*?)</tr>', table, re.S)]
+        rows = [row for row in rows if row]
+        if not rows or any(row not in targets for row in rows):
+            return match[0]
+        links = []
+        for row in rows:
+            label = cells(row[0])[0]
+            if re.search(r'<a\b', label):
+                return match[0]
+            path, anchor = targets[row].split('#', 1)
+            target = quote(posixpath.relpath(path, posixpath.dirname(page) or '.'), safe='/.-') + '#' + anchor
+            links.append('<li><a href="' + html.escape(target, quote=True) + '">' + label + '</a></li>')
+        return (heading + '<p>선언·상속·주석은 각 클래스 링크에서 확인하세요.</p>'
+                + '<ul class="related-symbols">' + ''.join(links) + '</ul>')
+
+    return re.sub(r'(<h2 id="관련-클래스">관련 클래스</h2>\s*)<div class="table-scroll stack" tabindex="0" role="region" aria-label="표">(<table>.*?</table>)</div>',
+                  related, document, flags=re.S)
+
+
+def merge_next_step(document: str, following: str) -> tuple[str, str]:
+    """Merge the exact generated tail only; retain different destinations/hints."""
+    tail = re.search(r'<p>다음 단계: <a href="([^"]+)">([^<>]+)</a></p>\s*$', document)
+    control = re.fullmatch(r'(<a class="next" href="([^"]+)">)<small>다음</small>([^<>]+) →</a>', following)
+    if not tail or not control or html.unescape(tail[1]) != html.unescape(control[2]):
+        return document, following
+    if tail[2] != control[3]:
+        following = (control[1] + '<small><span>다음</span> · <span>' + control[3] + '</span></small>'
+                     + '<span>' + tail[2] + '</span> →</a>')
+    return document[:tail.start()], following
diff --git a/src/sdd/site_assets/reading.css b/src/sdd/site_assets/reading.css
index 5a269ef..059eced 100644
--- a/src/sdd/site_assets/reading.css
+++ b/src/sdd/site_assets/reading.css
@@ -81,6 +81,9 @@ details.evidence-section{border-top:1px solid var(--line);border-left:0;margin:8
 
 /* Mobile navigation is a viewport drawer; static navigation remains available without scripts. */
 .menu-backdrop,.sidebar-close{display:none}
+.coverage-links li{margin-bottom:14px}.coverage-links p{margin:3px 0}.related-symbols li{overflow-wrap:anywhere}
+.call-checkpoint{display:grid;grid-template-columns:minmax(100px,140px) minmax(0,1fr);gap:8px 16px}.call-checkpoint dt{font-weight:600}.call-checkpoint dd{margin:0;overflow-wrap:anywhere}
+@media(max-width:760px){.call-checkpoint{grid-template-columns:1fr;gap:3px}.call-checkpoint dd{margin-bottom:10px}}
 html{scrollbar-gutter:stable}
 .previous-route:not(:target){display:none}.previous-route{scroll-margin-top:calc(var(--site-header-height,68px) + 16px);padding:12px;border:1px solid var(--line);margin:12px 0}.previous-route p{margin:0 0 4px;font-size:12px;color:var(--muted)}
 html.menu-open,html.menu-open body{overflow:hidden}
diff --git a/src/sdd/site_build.py b/src/sdd/site_build.py
index 1a05c87..029cdd1 100644
--- a/src/sdd/site_build.py
+++ b/src/sdd/site_build.py
@@ -117,7 +117,7 @@ def build_site(cfg: Config, out: Path, render, mermaid_src: str | None) -> Path:
         engine = {p.name: digest(p) for p in [code_root / "diagrams.py", code_root / "visuals.py", code_root / "export_site.py",
                                             code_root / "document_health.py", code_root / "evidence_navigation.py",
                                             code_root / "site_localization.py", code_root / "site_markdown.py",
-                                            code_root / "index_navigation.py",
+                                            code_root / "index_navigation.py", code_root / "reading_cleanup.py",
                                             code_root / "document_metadata.py", code_root / "scenario_document.py",
                                             code_root / "design_contracts.py", code_root / "evidence.py",
                                             code_root / "contract_schema.py", code_root / "reader_profiles.py",
diff --git a/src/sdd/site_markdown.py b/src/sdd/site_markdown.py
index d9e500e..c0e2c77 100644
--- a/src/sdd/site_markdown.py
+++ b/src/sdd/site_markdown.py
@@ -110,6 +110,8 @@ def _render(body: str, rel: str, known: set[str], model: KnowledgeModel | None,
     rendered = compact_evidence(rendered, valid)
     rendered = fold_source_details(rendered)
     rendered = _remove_route_tables(rendered)
+    from .reading_cleanup import compact_tables
+    rendered = compact_tables(rendered)
 
     def table_wrapper(match: re.Match) -> str:
         table = match[0]
diff --git a/tests/test_export_site.py b/tests/test_export_site.py
index cfcc548..55992da 100644
--- a/tests/test_export_site.py
+++ b/tests/test_export_site.py
@@ -536,4 +536,4 @@ def test_page_state_uses_plain_words_and_keeps_status_code_in_evidence(tmp_cfg,
     assert '소스 발췌에 연결한 설계 설명' in evidence
     index = (out / 'index.html').read_text(encoding='utf-8')
     assert '<code>ok</code>' not in index and '<code>needs-review</code>' not in index
-    assert '>인용 검사 확인 필요</td>' in index
+    assert '>인용 검사 확인 필요</span>' in index
diff --git a/tests/test_reading_cleanup.py b/tests/test_reading_cleanup.py
new file mode 100644
index 0000000..a99ea10
--- /dev/null
+++ b/tests/test_reading_cleanup.py
@@ -0,0 +1,134 @@
+import re
+
+import pytest
+
+from sdd.reading_cleanup import compact_tables, class_targets, link_related_classes, merge_next_step
+
+
+def table(headers, rows):
+    return ('<table><thead><tr>' + ''.join('<th>' + h + '</th>' for h in headers)
+            + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + c + '</td>' for c in row) + '</tr>' for row in rows)
+            + '</tbody></table>')
+
+
+def coverage(scope='코드 근거와 설명 연결'):
+    return ('<details class="note"><summary>설계 질문과 검증 범위</summary>'
+            '<p>질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.</p>'
+            + table(['설계 질문', '설명 위치', '확인 범위'], [
+                ['<code>Request</code>의 수명은?', '<a href="#life">수명</a>', scope],
+                ['실행 검증은?', '<a href="#verify">검증</a>', '코드 근거와 설명 연결 · 실행 확인 항목 별도']]) + '</details>')
+
+
+def test_coverage_list_keeps_questions_links_scope_and_human_review_boundary():
+    source = coverage()
+    result = compact_tables(source)
+    assert '<table' not in result and '<ul class="coverage-links">' in result
+    assert '<code>Request</code>의 수명은?' in result and '실행 검증은?' in result
+    assert re.findall(r'href="([^"]+)"', result) == re.findall(r'href="([^"]+)"', source)
+    assert result.count('코드 근거와 설명 연결') == 1
+    assert '실행 확인 항목 별도' in result and '의미와 실행 결과는 사람 검토가 필요합니다.' in result
+    assert compact_tables(result) == result
+
+
+def test_custom_coverage_scope_and_example_html_stay_intact():
+    source = coverage('사용자 정의 검증 조건')
+    assert compact_tables(source) == source
+    source = coverage().replace('<td>', '<td title="context">', 1)
+    assert compact_tables(source) == source
+    source = '<pre>' + coverage() + '</pre>'
+    assert compact_tables(source) == source
+
+
+def test_single_call_becomes_labeled_record_without_losing_boundary_or_citations():
+    headers = ['호출 지점', '후보 또는 예약 대상', '확인할 경계', '근거']
+    row = ['Camera', '<code>Pipe::queue()</code>', '메서드 전달이며 비동기 보장이 아닙니다.', '<a href="code#L9">src/a.cpp:9</a>']
+    result = compact_tables(table(headers, [row]))
+    assert '<table' not in result and '<dl class="call-checkpoint">' in result
+    assert all('<dt>' + header + '</dt>' in result for header in headers)
+    assert all('<dd>' + cell + '</dd>' in result for cell in row)
+    source = table(headers, [row, row])
+    assert compact_tables(source) == source
+
+
+def test_one_row_code_index_and_anchored_table_are_not_changed():
+    source = table(['클래스', '선언 위치', '상속', '책임 (주석)'], [['Camera', 'a.h:1', 'Base', 'Camera']])
+    assert compact_tables(source) == source
+    for tag in ('th', 'td', 'tr'):
+        custom = source.replace('<' + tag + '>', '<' + tag + ' aria-label="context">', 1)
+        assert compact_tables(custom) == custom
+    source = table(['확인할 내용', '호출 측과 대상', '구분', '근거'], [['<a id="keep"></a>check', 'call', 'note', 'a:1']])
+    assert compact_tables(source) == source
+
+
+CLASS_HEADERS = ['클래스', '선언 위치', '상속', '책임 (주석)']
+ROW = ['<code>Camera</code>', '<a href="https://host/blob/hash/a.h#L1"><code>a.h:1</code></a>', '<code>Base</code>', 'A camera']
+
+
+def index(row=ROW, anchor='symbol-1111111111111111'):
+    return table(CLASS_HEADERS, [row]).replace('<tbody><tr>', '<tbody><tr id="' + anchor + '" tabindex="-1" data-symbol-kind="class">')
+
+
+def related(row=ROW):
+    return ('<h2 id="관련-클래스">관련 클래스</h2>\n'
+            '<div class="table-scroll stack" tabindex="0" role="region" aria-label="표">'
+            + table(CLASS_HEADERS, [row]) + '</div>')
+
+
+def test_reference_links_require_exact_unique_full_row_and_use_relative_destination():
+    targets = class_targets({'reference/index.html': index()})
+    result = link_related_classes(related(), 'guides/camera.html', targets)
+    assert '<table' not in result and 'id="관련-클래스"' in result
+    assert '<a href="../reference/index.html#symbol-1111111111111111"><code>Camera</code></a>' in result
+    assert link_related_classes(related([*ROW[:3], 'Different responsibility']), 'camera.html', targets) == related([*ROW[:3], 'Different responsibility'])
+    assert link_related_classes(related(), 'camera.html', class_targets({'a.html': index(), 'b.html': index()})) == related()
+    assert link_related_classes(related(), 'camera.html', {}) == related()
+
+
+def test_partial_reference_matches_do_not_drop_unmatched_rows():
+    source = related().replace('</tbody>', '<tr><td>Missing</td><td>m.h:2</td><td>–</td><td>Unique</td></tr></tbody>')
+    assert link_related_classes(source, 'camera.html', class_targets({'index.html': index()})) == source
+
+
+def test_custom_reference_attributes_and_linked_names_remain_intact():
+    for tag in ('th', 'td', 'tr'):
+        source = related().replace('<' + tag + '>', '<' + tag + ' title="context">', 1)
+        assert link_related_classes(source, 'camera.html', class_targets({'index.html': index()})) == source
+    row = ['<a href="other.html">Camera</a>', *ROW[1:]]
+    assert link_related_classes(related(row), 'camera.html', class_targets({'index.html': index(row)})) == related(row)
+    assert class_targets({'index.html': index().replace('<td>', '<td title="context">', 1)}) != class_targets({'index.html': index()})
+
+
+def test_matching_next_link_is_one_control_and_distinct_hint_survives():
+    control = '<a class="next" href="request.html#life"><small>다음</small>요청 수명 →</a>'
+    source = '<h2 id="keep">내용</h2><p>다음 단계: <a href="request.html#life">요청 수명</a></p>'
+    content, result = merge_next_step(source, control)
+    assert content == '<h2 id="keep">내용</h2>' and result == control
+    content, result = merge_next_step(source.replace('>요청 수명</a>', '>실패 후 복구 확인</a>'), control)
+    assert content == '<h2 id="keep">내용</h2>'
+    assert '실패 후 복구 확인' in result and '요청 수명' in result and result.count('href=') == 1
+
+
+@pytest.mark.parametrize('tail', [
+    '<p>다음 단계: <a href="request.html#different">요청 수명</a></p>',
+    '<p>다음 단계: <a id="legacy" href="request.html#life">요청 수명</a></p>',
+    '<pre><p>다음 단계: <a href="request.html#life">요청 수명</a></p></pre>',
+    '<p>다음 단계: <a href="request.html#life">요청 수명</a>과 추가 지시</p>',
+])
+def test_distinct_targets_custom_attributes_examples_and_extra_instructions_are_retained(tail):
+    control = '<a class="next" href="request.html#life"><small>다음</small>요청 수명 →</a>'
+    assert merge_next_step(tail, control) == (tail, control)
+
+
+def test_generated_status_groups_preserve_all_pages_and_nonpassing_states(tmp_cfg, sample_model):
+    from test_export_site import prepare
+    from sdd.export_site import export_site
+    prepare(tmp_cfg, sample_model)
+    path = tmp_cfg.sdd_dir / 'nested/detail.md'
+    path.write_text(path.read_text(encoding='utf-8').replace('needs-review', 'ok'), encoding='utf-8')
+    out = export_site(tmp_cfg)
+    page = (out / 'index.html').read_text(encoding='utf-8')
+    assert '<h2 id="문서-목록">문서 검증 현황</h2>' in page
+    assert '<th>검사 결과</th>' not in page
+    assert '<span>인용 검사 확인 필요</span>' in page and '<span>인용 검사 통과</span>' in page
+    assert page.count('<span>사람 검토 전</span>') >= 2
+    assert 'href="device.html"' in page and 'href="nested/detail.html"' in page

Existing context:
def _pagination_html(entries, sections, index, rel, current):
    previous_next = []
    for offset, label in [(-1, "이전"), (1, "다음")]:
        other = index + offset
        fragment = ''
        if offset == 1 and sections.get(rel, {}).get('next', {}).get('link'):
            destination, _, requested_fragment = sections[rel]['next']['link'].partition('#')
            selected = next((i for i, entry in enumerate(entries) if entry[2] == (destination or rel)), None)
            if selected is not None:
                other, fragment = selected, requested_fragment
        if 0 <= other < len(entries):
            _, dest_title, dest_rel = entries[other]
            destination_href = _href(_html_path(dest_rel), current) + ('#' + quote(fragment) if fragment else '')
            previous_next.append(f'<a class="{"previous" if offset < 0 else "next"}" href="{destination_href}"><small>{label}</small>{html.escape(dest_title)} {"←" if offset < 0 else "→"}</a>')
    return previous_next



"""Stable links to rendered index rows, without changing extracted manuscripts."""
from __future__ import annotations

import hashlib
import html
import re


def _text(value: str) -> str:
    return html.unescape(re.sub(r'<[^>]*>', '', value)).strip()


def index_navigation(document: str, page: str, title: str) -> tuple[str, list[dict]]:
    """Only generated class/function tables become searchable symbol entries."""
    entries = []
    seen = {}
    package = ''
    parts = re.split(r'(<h2\b[^>]*>.*?</h2>|<table>.*?</table>)', document, flags=re.S)
    for index, part in enumerate(parts):
        if part.startswith('<h2'):
            package = _text(part)
            continue
        if not part.startswith('<table>'):
            continue
        headers = re.findall(r'<th\b[^>]*>(.*?)</th>', part, re.S)
        if not headers or _text(headers[0]) not in ('클래스', '함수'):
            continue
        kind = 'class' if _text(headers[0]) == '클래스' else 'function'

        def row(match):
            cells = re.findall(r'<td\b[^>]*>(.*?)</td>', match[1], re.S)
            if len(cells) < 2:
                return match[0]
            name, location = _text(cells[0]), _text(cells[1])
            location = re.sub(r':\d+(?:-\d+)?(?=\s|$)', '', location)
            key = '\0'.join((package, name, location))
            seen[key] = seen.get(key, 0) + 1
            suffix = '' if seen[key] == 1 else f'-{seen[key]}'
            anchor = 'symbol-' + hashlib.sha256(key.encode()).hexdigest()[:16] + suffix
            entries.append(dict(title=name, page=title, url=page + '#' + anchor, kind='symbol'))
            return (f'<tr id="{anchor}" tabindex="-1" data-symbol-kind="{kind}">'
                    + match[1] + '</tr>')

        parts[index] = re.sub(r'<tr>(.*?)</tr>', row, part, flags=re.S)
    return ''.join(parts), entries

Follow-up: prior findings about dropped table/cell attributes and nested class-name links were addressed with conservative attribute guards, full-cell matching and linked-name rejection. Added regressions cover those cases. The homepage copy removes repeated menu/product-entry instructions and corrects stale reading guidance; it makes no new source behavior claims.

