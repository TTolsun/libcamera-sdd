"""Rebuild the revised published edition from pinned public inputs."""
import argparse
import gzip
from hashlib import sha256
from importlib.metadata import version
import json
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory, TemporaryFile
from zipfile import ZipFile


def git(repo, *args):
    return subprocess.check_output(['git','-C',str(repo),*args])


def digest(raw):
    return sha256(raw).hexdigest()


def restore_input(name, data):
    if not name.endswith('.html'):
        return data
    source = data.decode('utf-8')
    for pattern, expected in (
        (r'<nav class="download-nav"[^>]*><details class="language-selector download-menu".*?</details></nav>',1),
        (r'<details class="language-selector">.*?</details>',1),
        (r'<link rel="alternate" hreflang="(?:ko|en)"[^>]*>',2),
    ):
        source, found = re.subn(pattern,'',source,flags=re.S)
        if found != expected:
            raise ValueError(f'Unexpected generated navigation in seed page {name}')
    return source.encode('utf-8')


def rebuild(public, seed, profile, catalog, out, title, public_url, source_commit):
    from sdd.config import load
    from sdd.full_document import is_combined, publish as publish_downloads
    from sdd.reader_edition import publish
    from sdd.site_localization import localize_site
    from sdd.site_paths import owned_path

    original_bytes=git(public,'show',seed['commit']+':docs/site-manifest.json')
    original=json.loads(original_bytes)
    if digest(original_bytes)!=seed['manifest_sha256'] or original['build_id']!=seed['build_id']:
        raise ValueError('Seed edition manifest differs')
    out.mkdir(parents=True)
    with TemporaryFile() as archive_file:
        subprocess.run(['git','-C',str(public),'archive','--format=zip',seed['commit'],'docs'],
                       stdout=archive_file,check=True)
        archive_file.seek(0)
        with ZipFile(archive_file) as archive:
            for name, checksum in original['outputs'].items():
                data=archive.read('docs/'+name)
                if digest(data)!=checksum:
                    raise ValueError(f'Seed output differs from its manifest: {name}')
                if name.startswith('en/') or is_combined(name) or name.endswith('download/full.md') or name=='item-visual-audit.json':
                    continue
                path=owned_path(out,name)
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_bytes(restore_input(name,data))
    with TemporaryDirectory() as temporary:
        settings=Path(temporary)
        (settings/'reader-edition.yaml').write_bytes(profile)
        (settings/'english-release.json').write_bytes(catalog)
        config=settings/'sdd.yaml'
        config.write_text(json.dumps({'site':{'title':title,'public_url':public_url,
            'reader_edition':'reader-edition.yaml','english_catalog':'english-release.json'}},
            ensure_ascii=False),encoding='utf-8')
        cfg=load(config)
        localize_site(cfg,out)
        entries=publish(cfg,out)
        publish_downloads(out,entries,site_title=title,public_url=public_url,source_commit=source_commit,
                          pdf_downloads=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generator',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    record=Path(__file__).resolve().parent
    public=record.parents[1]
    producer=args.generator.resolve()
    out=args.out.resolve()
    if out.is_relative_to(public/'docs'):
        parser.error('Choose a new output directory outside the tracked site')
    meta=json.loads((record/'release.json').read_bytes())
    if git(producer,'rev-parse','HEAD').decode().strip()!=meta['build_generator_commit']:
        parser.error('Check out the exact generator commit recorded for this publication')
    if git(producer,'status','--porcelain','--untracked-files=no'):
        parser.error('The generator has tracked changes')
    prior=git(public,'show',meta['previous_public_commit']+':docs/site-manifest.json')
    if digest(prior)!=meta['previous_manifest_sha256']:
        raise ValueError('Preceding public manifest differs')
    raw=(public/'docs/site-manifest.json').read_bytes()
    expected=json.loads(raw)
    if digest(raw)!=meta['manifest_sha256']:
        parser.error('Check out this public release and its site manifest')
    for dependency, required in expected['dependencies'].items():
        if version(dependency)!=required:
            parser.error(f'{dependency} must be installed at version {required}')
    catalog_record=public/meta['catalog_record']
    profile=json.loads((public/meta['reader_profile_record']/'reader-edition-profile.json').read_bytes())['yaml'].encode('utf-8')
    catalog=gzip.decompress((catalog_record/'english-release.json.gz').read_bytes())
    for key,value in (('reader_edition',profile),('english_catalog',catalog)):
        if digest(value)!=expected['inputs'][key]:
            raise ValueError(f'Pinned input differs: {key}')
    sys.path.insert(0,str(producer/'src'))
    from sdd.site_build import verify_site
    rebuild(public,meta['projection_seed'],profile,catalog,out,meta['title'],meta['public_url'],meta['source_commit'])
    for name in ('item-visual-audit.json','site-manifest.json'):
        (out/name).write_bytes((public/'docs'/name).read_bytes())
    result=verify_site(out)
    observed={p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file()}
    if observed!=set(expected['outputs'])|{'site-manifest.json'}:
        raise ValueError('Reconstructed artifact inventory differs')
    print(json.dumps({'build_id':expected['build_id'],'outputs':len(expected['outputs']),**result}))


if __name__=='__main__':
    main()
