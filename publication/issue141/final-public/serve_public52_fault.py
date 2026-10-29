"""Serve immutable committed HTML with only Mermaid requests faulted; stop via stdin."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
import hashlib, json, sys

root = Path(__file__).resolve().parent
docs = root / 'public-release-46235b02/docs'
log = root / 'ui-public52/fault-server.json'
before = {p.relative_to(docs).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
          for p in docs.rglob('*') if p.is_file()}
requests = []
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(docs), **kwargs)
    def do_GET(self):
        fault = self.path.startswith('/assets/mermaid/')
        requests.append({'path': self.path, 'fault': fault})
        if fault:
            self.send_error(503, 'Intentional local Mermaid loading fault')
        else:
            super().do_GET()
    def log_message(self, *args):
        pass

server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
Thread(target=server.serve_forever, daemon=True).start()
print(json.dumps({'port': server.server_port, 'root': str(docs)}), flush=True)
try:
    for line in sys.stdin:
        if line.strip() == 'stop':
            break
finally:
    server.shutdown()
    server.server_close()
    after = {p.relative_to(docs).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in docs.rglob('*') if p.is_file()}
    result = {'passed': before == after, 'input_files': len(before),
              'immutable_inputs_unchanged': before == after, 'requests': requests,
              'scope': 'Local HTTP fault injection only; no public site or source mutation'}
    log.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    assert result['passed']
    print(json.dumps({'stopped': True, 'inputs_unchanged': True}), flush=True)
