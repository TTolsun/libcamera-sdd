"""Prepare a new normal SDD workspace from this public release and Git baseline."""
import argparse
from hashlib import sha256
import io
import json
from pathlib import Path, PurePosixPath
import subprocess
from zipfile import ZipFile
import yaml


def git(repo, *args):
    return subprocess.check_output(['git','-C',str(repo),*args])


def write(root, path, data):
    rel=PurePosixPath(path)
    if rel.is_absolute() or '..' in rel.parts or '\\' in path or ':' in path:
        raise ValueError(f'Unsafe archived path: {path}')
    dest=root.joinpath(*rel.parts)
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():
        raise ValueError(f'Refusing to overwrite workspace input: {path}')
    dest.write_bytes(data)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generator',type=Path,required=True)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    record=Path(__file__).resolve().parent
    public=record.parents[1]
    info=json.loads((record/'release.json').read_bytes())
    expected=info['source_commit']
    if git(args.source,'rev-parse','HEAD').decode().strip()!=expected:
        parser.error(f'Check out public libcamera at {expected} before preparing the recorded release')
    if git(args.generator,'rev-parse','HEAD').decode().strip()!=info['build_generator_commit']:
        parser.error('Check out the generator revision in release.json')
    workspace=args.out.resolve()
    for protected in (public,args.source.resolve(),args.generator.resolve()):
        if workspace.is_relative_to(protected) or protected.is_relative_to(workspace):
            parser.error('Workspace must be separate from the public, generator and source checkouts')
    workspace.mkdir(parents=True)
    bundle=(record/'workspace-inputs.zip').read_bytes()
    if sha256(bundle).hexdigest()!=info['workspace_bundle_sha256']:
        raise ValueError('Portable workspace bundle has changed')
    with ZipFile(io.BytesIO(bundle)) as archive:
        for name in archive.namelist():
            write(workspace,name,archive.read(name))
    base=info['previous_public_commit']
    old_manifest=git(public,'show',f'{base}:docs/site-manifest.json')
    if sha256(old_manifest).hexdigest()!=info['previous_manifest_sha256']:
        raise ValueError('The prior published manifest no longer matches the pinned release')
    for row in json.loads((workspace/'published-input-references.json').read_bytes()):
        raw=git(public,'show',f"{base}:{row['git_path']}")
        if sha256(raw).hexdigest()!=row['sha256']:
            raise ValueError('Previously published observation does not match')
        write(workspace,row['workspace_path'],raw)
    sources=json.loads((record/'manuscript-provenance.json').read_bytes())
    for name,row in sources.items():
        if not name.endswith('.md') or row['intentionally_updated']:
            continue
        raw=git(public,'show',f'{base}:docs/{name}')
        if sha256(raw).hexdigest()!=row['release']:
            raise ValueError(f'The recorded baseline manuscript has changed: {name}')
        write(workspace,'manuscripts/'+name,raw)
    for name,expected_sha in json.loads(old_manifest)['outputs'].items():
        if name.startswith('assets/mermaid/'):
            raw=git(public,'show',f'{base}:docs/{name}')
            if sha256(raw).hexdigest()!=expected_sha:
                raise ValueError(f'The recorded Mermaid asset has changed: {name}')
            write(workspace,name,raw)
    for name in ('release.yaml','final-review.yaml'):
        path=workspace/name
        cfg=yaml.safe_load(path.read_bytes())
        cfg['source']['root']=str(args.source.resolve())
        path.write_text(yaml.safe_dump(cfg,allow_unicode=True,sort_keys=False),encoding='utf-8',newline='\n')
    print(workspace/'release.yaml')


if __name__=='__main__':
    main()
