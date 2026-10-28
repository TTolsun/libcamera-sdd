"""Restore original evidence paths and verify every byte; no model is invoked."""
from pathlib import Path
import argparse,hashlib,json,zipfile,os
def native_path(path):
    """Use Windows extended paths without changing logical evidence names."""
    value=str(path)
    if os.name=='nt' and not value.startswith('\\\\?\\'):
        value=('\\\\?\\UNC\\'+value[2:]) if value.startswith('\\\\') else '\\\\?\\'+value
    return Path(value)
parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
base=Path(__file__).resolve().parent;index=json.loads((base/'original-cli-evidence-index.json').read_text(encoding='utf-8'))
archive=base/index['archive'];assert hashlib.sha256(archive.read_bytes()).hexdigest()==index['archive_sha256']
root=args.out.resolve();native_path(root).mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(archive) as source:
    for row in index['files']:
        target=(root/row['path']).resolve();assert target.is_relative_to(root)
        data=source.read('blobs/'+row['sha256']);assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
        target=native_path(target)
        if target.exists():assert target.is_file() and target.read_bytes()==data,'Existing different file: '+str(target)
        else:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
print('Restored and verified',len(index['files']),'original file paths. Copies are not new CLI calls.')
