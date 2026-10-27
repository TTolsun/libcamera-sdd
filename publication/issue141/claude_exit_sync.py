import sys,subprocess,time
from pathlib import Path
native=Path(r'C:\Users\baboe\.local\bin\claude.exe')
result=subprocess.run([str(native),*sys.argv[1:]],stdin=sys.stdin.buffer,stdout=sys.stdout.buffer,stderr=sys.stderr.buffer)
# The standard runner already received exit0. Give native Windows child handles
# time to close before its caller removes the empty working directory.
time.sleep(1.0)
raise SystemExit(result.returncode)
