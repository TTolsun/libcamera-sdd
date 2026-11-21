"""Rebuild the published reader layout from manifest-pinned public material."""
from __future__ import annotations

import argparse
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
    return subprocess.check_output(['git', '-C', str(repo), *args])


def digest(data):
    return sha256(data).hexdigest()


def restore_input(name, data):
    if not name.endswith('.html'):
        return data
    # The former whole-document exporter inserted one download menu after
    # rendering each original page. The new exporter reinserts it for the
    # canonical reader pages after layout and archived links are resolved.
    legacy_menu = (r'<nav class="download-nav"[^>]*><details class="language-selector download-menu"'
                   r'.*?</details></nav>')
    source, removed = re.subn(legacy_menu, '', data.decode('utf-8'), flags=re.S)
    if removed != 1:
        raise ValueError(f'Unexpected baseline download menu count at {name}: {removed}')
    return source.encode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generator', type=Path, required=True, help='Clean generator checkout at the release SHA')
    parser.add_argument('--out', type=Path, required=True, help='New output directory')
    args = parser.parse_args()
    records = Path(__file__).resolve().parent
    public = records.parents[1]
    generator = args.generator.resolve()
    out = args.out.resolve()
    if out.is_relative_to(public/'docs'):
        parser.error('Choose an output directory outside the tracked site')
    release = json.loads((records/'release.json').read_bytes())
    baseline_release = git(public, 'show', release['previous_public_commit']+':docs/site-manifest.json')
    if digest(baseline_release) != release['previous_manifest_sha256']:
        raise ValueError('The preceding public release manifest differs')
    source = release['projection_seed']
    previous = source['commit']
    generator_sha = release['generator_merge']['sha']
    if git(generator, 'rev-parse', 'HEAD').decode('ascii').strip() != generator_sha:
        parser.error(f'The generator must be checked out at {generator_sha}')
    if git(generator, 'status', '--porcelain', '--untracked-files=no'):
        parser.error('The generator checkout has tracked changes')
    manifest_bytes = (public/'docs/site-manifest.json').read_bytes()
    if digest(manifest_bytes) != release['manifest_sha256']:
        parser.error('Check out the public repository commit containing this release and its manifest')
    expected = json.loads(manifest_bytes)
    for dependency, required in expected['dependencies'].items():
        if version(dependency) != required:
            parser.error(f'{dependency} must be installed at version {required}')
    source_manifest_bytes = git(public, 'show', f'{previous}:docs/site-manifest.json')
    if digest(source_manifest_bytes) != source['manifest_sha256']:
        raise ValueError('The baseline Git manifest digest differs from the release record')
    original = json.loads(source_manifest_bytes)
    if original['build_id'] != source['build_id']:
        raise ValueError('The baseline build differs from the release record')
    profile = json.loads((records/'reader-edition-profile.json').read_bytes())['yaml'].encode('utf-8')
    if digest(profile) != expected['inputs']['reader_edition']:
        raise ValueError('The reader edition profile differs from the published input')
    sys.path.insert(0, str(generator/'src'))
    from sdd.config import load
    from sdd.full_document import is_combined, publish as publish_downloads
    from sdd.reader_edition import publish as publish_reader_edition
    from sdd.site_build import verify_site
    from sdd.site_paths import owned_path

    out.mkdir(parents=True)
    with TemporaryFile() as temporary:
        subprocess.run(['git', '-C', str(public), 'archive', '--format=zip', previous, 'docs'],
                       stdout=temporary, check=True)
        temporary.seek(0)
        with ZipFile(temporary) as archive:
            for name, checksum in original['outputs'].items():
                data = archive.read('docs/'+name)
                if digest(data) != checksum:
                    raise ValueError(f'Baseline output differs from its Git manifest: {name}')
                if is_combined(name) or name.endswith('download/full.md') or name == 'item-visual-audit.json':
                    continue
                target = owned_path(out, name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(restore_input(name, data))
    with TemporaryDirectory() as temporary:
        cfg_root = Path(temporary)
        (cfg_root/'reader-edition.yaml').write_bytes(profile)
        cfg_path = cfg_root/'sdd.yaml'
        site = release['reader_site']
        cfg_path.write_text(json.dumps({'site': {**site, 'reader_edition': 'reader-edition.yaml'}},
                                      ensure_ascii=False), encoding='utf-8')
        entries = publish_reader_edition(load(cfg_path), out)
        publish_downloads(out, entries, site_title=site['title'], public_url=site['public_url'],
                          source_commit=release['source_commit'])

    # The independent verdict was already published. Verify its manifest
    # bytes and resolved item fingerprints through the ordinary site checker.
    for name in ('item-visual-audit.json', 'site-manifest.json'):
        (out/name).write_bytes((public/'docs'/name).read_bytes())
    result = verify_site(out)
    generated = {p.relative_to(out).as_posix() for p in out.rglob('*') if p.is_file()}
    if generated != set(expected['outputs']) | {'site-manifest.json'}:
        raise ValueError('Reconstructed file set differs from the published manifest')
    print(json.dumps({'build_id': expected['build_id'], 'outputs': len(expected['outputs']), **result}))


if __name__ == '__main__':
    main()
