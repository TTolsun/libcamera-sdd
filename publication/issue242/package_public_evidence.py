import hashlib,json,shutil,zipfile
from pathlib import Path
root=Path.cwd();repo=root/'build/issue242-publication/libcamera-sdd';release=root/'build/issue242-publication/release-01';evidence=repo/'publication/issue242';evidence.mkdir(parents=True,exist_ok=True)
index={}
with zipfile.ZipFile(evidence/'native-and-regression-evidence.zip','w',zipfile.ZIP_DEFLATED) as z:
 for base in [root/'build/issue242-publication/actual-probe-02',root/'build/issue242-investigation/benchmark-05']+[p for p in (root/'build/issue242-investigation').glob('implementation-review-*') if p.is_dir()]:
  for p in sorted(base.rglob('*')):
   if not p.is_file() or any(s in p.parts for s in ['__pycache__','.pytest_cache','baseline-code']):continue
   name=p.relative_to(root/'build').as_posix();raw=p.read_bytes();index[name]=hashlib.sha256(raw).hexdigest();z.writestr(name,raw)
(evidence/'archive-index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding='utf-8')
for n in ['comparison.json']:
 shutil.copy2(root/'build/issue242-investigation/benchmark-05'/n,evidence/('matrix-'+n))
for n in ['final-input-audit.json','two-exports-final.json','publication.yaml','restoration.json']:
 p=release/n
 if p.exists():shutil.copy2(p,evidence/n)
shutil.copy2(repo/'docs/site-manifest.json',evidence/'previous-good-site-manifest.json')
for folder in ['config','historical-style','current-style','reader-preserved-style','templates']:
 if (release/folder).exists():shutil.copytree(release/folder,evidence/'release-inputs'/folder,dirs_exist_ok=True)
for p in release.glob('*.yaml'):shutil.copy2(p,evidence/'release-inputs'/p.name)
for p in (root/'build/issue242-investigation').glob('*.py'):
 shutil.copy2(p,evidence/p.name)
for pattern in ['typed-before.*','final-regressions-10.*','ci-fixes-09.*','review-final-delta.log','public-exports-final.log','resume-public-final.log']:
 for p in (root/'build/issue242-investigation').glob(pattern):shutil.copy2(p,evidence/p.name)
for p in (root/'build/issue242-investigation').glob('issue*.json'):shutil.copy2(p,evidence/p.name)
shutil.copy2(root/'docs/records/issue242.md',evidence/'generator-record.md')
summary=dict(archive_files=len(index),archive_sha256=hashlib.sha256((evidence/'native-and-regression-evidence.zip').read_bytes()).hexdigest(),archive_bytes=(evidence/'native-and-regression-evidence.zip').stat().st_size,public_data_only=True,human_review='pending',actual_cli='Codex CLI / gpt-6.1-terra / high',matrix_transport='controlled CLI double; not actual inference')
(evidence/'evidence-package.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary))
