from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,tarfile
root=Path.cwd();w=root/'build/preflight-native';good=w/'native-good-01';public=root/'build/issue241/public'
dest=public/'publication/publication-preflight';site=public/'docs/validation/publication-preflight'
assert not dest.exists() and not site.exists();dest.mkdir(parents=True);shutil.copytree(good/'site',site)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
qa=dict(schema=1,checked_at=datetime.now(timezone.utc).isoformat(),method='Actual IAB browser, local HTTP server.',
    checks=['Korean and English prose and four-node supplied-fence condition graph rendered.',
            'Korean graph enlargement, fit and fence element search worked (two matches).',
            'Language menu navigated to the English page. Human review remained pending.'],
    build_id=json.loads((site/'site-manifest.json').read_bytes())['build_id'],
    limits=['Desktop sample only; not full-book, mobile, hardware or internal HAL validation.',
            'Screenshots inspected in tool output; no separately saved screenshot file claimed.'])
(w/'browser-verification.json').write_text(json.dumps(qa,indent=2)+'\n',encoding='utf-8')
with tarfile.open(dest/'native-originals.tar.gz','w:gz') as archive:
    for case in [w/'native-bad-01',w/'native-bad-02',good]:
        for p in sorted(case.rglob('*')):
            if p.is_file() and 'site' not in p.relative_to(case).parts:
                archive.add(p,arcname=p.relative_to(w).as_posix(),recursive=False)
with tarfile.open(dest/'generator-checks.tar.gz','w:gz') as archive:
    for p in sorted((w/'code-review-01').rglob('*')):
        if p.is_file():archive.add(p,arcname=p.relative_to(w).as_posix(),recursive=False)
    for p in sorted((root/'build').glob('preflight-*.log')):
        archive.add(p,arcname='focused-tests/'+p.name,recursive=False)
for name in ['comparison.json','ci-pr-final.json','ci-pr-full.log','generator-merge.json','code-review-result-01.json',
             'official-head-final.log','mirror-head-final.log','browser-verification.json']:
    shutil.copyfile(w/name,dest/name)
scripts=dest/'scripts';scripts.mkdir()
for name in ['prepare_cases.py','invoke.py','review_code.py','review_diagram.py','finalize.py','adopt_merged.py','collect_evidence.py','package.py']:
    shutil.copyfile(w/name,scripts/name)
manifest=json.loads((site/'site-manifest.json').read_bytes())
assert all(sha(p)==sha(site/p.relative_to(good/'site')) for p in (good/'site').rglob('*') if p.is_file())
record=dict(schema=1,public_base_commit=subprocess.check_output(['git','-C',str(public),'rev-parse','HEAD'],text=True).strip(),
    generator_candidate='825e261c8aaf25e924659b623b97e414fb68d899',generator_merge='3023f5c95eb6b1347a0597bb8bad46d96f30ea5e',
    candidate_merge_file_tree='identical',source_commit='293d751a814e0d4c34e85ad457ccd9d5eefd1a61',
    official_and_public_mirror='be7e83e91348250c015aad6d6f59f1468555bae8',
    site_build_id=manifest['build_id'],site_outputs=len(manifest['outputs']),
    files={p.relative_to(dest).as_posix():dict(sha256=sha(p),bytes=p.stat().st_size) for p in sorted(dest.rglob('*')) if p.is_file()})
(dest/'evidence-manifest.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8');print({k:v for k,v in record.items() if k!='files'})
