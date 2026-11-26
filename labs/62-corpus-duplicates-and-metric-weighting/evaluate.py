"""Compare observation-weighted and unique-content metrics on harmless samples."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

RULE = Path(__file__).resolve().with_name("rules.yar")
ROWS = [
    ("a","BLUE-TOKEN",True),
    ("b","BLUE-TOKEN",True),
    ("c","BLUE-TOKEN",True),
    ("d","GREEN-TOKEN",True),
    ("e","BLUE-TOKEN legend",False),
    ("f","ordinary notes",False),
    ("g","ordinary notes",False),
]

def count(rows):
    out = dict(tp=0,fp=0,tn=0,fn=0)
    for truth,hit in rows:
        out[("tp" if hit else "fn") if truth else ("fp" if hit else "tn")]+=1
    return out

def dedup(rows):
    unique = {}
    for digest,truth,hit in rows:
        value=(truth,hit)
        if digest in unique and unique[digest]!=value:
            raise ValueError("conflicting label or result for identical bytes")
        unique[digest]=value
    return list(unique.values())

def main():
    if not shutil.which("yara"):
        raise SystemExit("Install the YARA CLI before running")
    results=[]
    with tempfile.TemporaryDirectory(prefix="yara-duplicate-") as tmp:
        for ident,content,truth in ROWS:
            data=content.encode()
            p=Path(tmp)/(ident+".txt")
            p.write_bytes(data)
            run=subprocess.run(["yara",str(RULE),str(p)],
                               capture_output=True,text=True,timeout=10)
            if run.returncode:
                raise RuntimeError(run.stderr or "YARA failed")
            results.append((sha256(data).hexdigest(),truth,bool(run.stdout.strip())))
    raw=count([(truth,hit) for _,truth,hit in results])
    unique=count(dedup(results))
    assert raw==dict(tp=3,fp=1,tn=2,fn=1)
    assert unique==dict(tp=1,fp=1,tn=1,fn=1)
    assert len(dedup(results))==4
    assert dedup([])==[]
    assert count([])==dict(tp=0,fp=0,tn=0,fn=0)
    try:
        dedup([("same",True,True),("same",False,True)])
    except ValueError:
        pass
    else:
        raise AssertionError("conflicting labels accepted")
    print("Observation weighted:",raw)
    print("Unique content:",unique)
    print("7 scans + 6 checks passed")

if __name__=="__main__":
    main()
