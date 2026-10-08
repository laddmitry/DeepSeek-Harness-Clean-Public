"""Read-only verification of a prepared source tree and all available Git history."""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--commit');args=p.parse_args()
root=Path.cwd();manifest=json.loads((root/'FILES.sha256.json').read_text(encoding='utf-8'))
expected=manifest['files'];errors=[]
def digest(b): return hashlib.sha256(b).hexdigest()
def git(*a): return subprocess.check_output(['git',*a],cwd=root)
if not args.commit:
 actual={f.relative_to(root).as_posix():digest(f.read_bytes()) for f in root.rglob('*') if f.is_file() and '.git' not in f.relative_to(root).parts and f.name!='FILES.sha256.json'}
 if actual!=expected: errors.append('Working tree differs from prepared manifest')
else:
 expected=dict(expected);expected['FILES.sha256.json']=digest((root/'FILES.sha256.json').read_bytes())
 commits=git('rev-list','--all').decode().splitlines()
 target=git('rev-parse',args.commit+'^{commit}').decode().strip()
 commits=list(dict.fromkeys(commits+[target]))
 for commit in commits:
  entries=git('ls-tree','-rz','--full-tree',commit).split(b'\0');actual={}
  for entry in entries:
   if not entry: continue
   metadata,name=entry.split(b'\t',1);mode,kind,oid=metadata.split()
   name=name.decode('utf-8')
   if kind!=b'blob' or mode not in (b'100644',b'100755'): errors.append('Unexpected entry '+name);continue
   actual[name]=digest(git('cat-file','blob',oid.decode()))
  if (commit==target and actual!=expected) or any(expected.get(n)!=h for n,h in actual.items()): errors.append('Commit tree contains unprepared bytes or target is incomplete: '+commit)
 if git('status','--porcelain'): errors.append('Working tree has uncommitted changes')
 print('COMMIT',target,'HISTORY_COMMITS',len(commits))
if errors:
 print('\n'.join('FAIL '+e for e in errors));sys.exit(1)
print('PASS: exact prepared bytes. Secret/author review and runtime limits remain applicable.')
