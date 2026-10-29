"""Check saved CUA observations against immutable final HTML; no browser automation."""
from pathlib import Path
from html.parser import HTMLParser
import json, hashlib, datetime
import yaml

w = Path(__file__).resolve().parent
docs = w/'public-release-46235b02/docs'
report_path = w/'ui-public52/report.json'
report = json.loads(report_path.read_bytes())
assert report['public_commit'] == '46235b026626db49ef98ba3a5e23d1359dbe3d0a'
assert len(report['checks']) == 17 and all(c['passed'] for c in report['checks'])
assert len(report['legacy']) == 12 and all(c['passed'] for c in report['legacy'])

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids=set(); self.hrefs=[]; self.sources=[]; self.in_mermaid=False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if tag=='a' and 'href' in attrs:self.hrefs.append(attrs['href'])
        if tag=='pre' and 'mermaid' in attrs.get('class','').split():
            self.in_mermaid=True;self.sources.append('')
    def handle_endtag(self, tag):
        if tag=='pre':self.in_mermaid=False
    def handle_data(self,data):
        if self.in_mermaid:self.sources[-1]+=data

faults=report['faults']; assert {f['lang'] for f in faults}=={'ko','en'}
for f in faults:
    page=Page((docs/('en/index.html' if f['lang']=='en' else 'index.html')).read_text(encoding='utf-8'))
    assert [d['source'] for d in f['diagrams']]==page.sources
    assert len(f['notices'])==len(page.sources)==1
    assert all(d['svg']==0 and d['ready'] is None and d['display']!='none' for d in f['diagrams'])
    for d in f['diagrams']:d['source_sha256']=hashlib.sha256(d['source'].encode()).hexdigest()
    f['exact_original_sources_preserved']=True
server=json.loads((w/'ui-public52/fault-server.json').read_bytes())
assert server['passed'] and server['immutable_inputs_unchanged']
assert {x['path'] for x in server['requests'] if x['fault']}=={'/assets/mermaid/mermaid.esm.min.mjs'}
assert '/index.html' in {x['path'] for x in server['requests']}
assert '/en/index.html' in {x['path'] for x in server['requests']}

sections=yaml.safe_load((w/'public-release-46235b02/publication/goal-138-140/config/sections.yaml').read_text(encoding='utf-8'))['sections']
aliases=[]
for s in sections:
    for r in s.get('routes',[]):
        if not r.get('anchor'):continue
        for prefix in ('','en/'):
            src=docs/(prefix+s['output'].replace('.md','.html'))
            target,anchor=r['to'].split('#',1)
            dest=docs/(prefix+target.replace('.md','.html'))
            p=Page(src.read_text(encoding='utf-8'));q=Page(dest.read_text(encoding='utf-8'))
            assert r['anchor'] in p.ids,(src,r['anchor'])
            assert anchor in q.ids,(dest,anchor)
            aliases.append({'source':src.relative_to(docs).as_posix(),'old_anchor':r['anchor'],
                            'target':dest.relative_to(docs).as_posix(),'target_anchor':anchor})
assert aliases
report.update(passed=True,scope='CUA live representative interactions, 12 actual legacy clicks, all configured static aliases, local bilingual failure injection; not all60-page interactive or HAL/human approval',
              static_aliases=aliases,static_alias_count=len(aliases),fault_inputs_unchanged=True,
              verified_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
report['screenshots']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(report_path.parent.glob('*.png'))}
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'live_checks':len(report['checks']),'legacy_clicks':12,'static_aliases':len(aliases),'fault_languages':2,'screenshots':len(report['screenshots'])}))
