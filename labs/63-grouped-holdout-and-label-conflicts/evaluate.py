"""Check split leakage and label conflicts before evaluating harmless YARA text."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT=Path(__file__).parent
ROWS=[
    ("d1","dev",True,b"BLUE-TOKEN"),
    ("d2","dev",False,b"ordinary text"),
    ("h1","holdout",True,b"BLUE-TOKEN example"),
    ("h2","holdout",False,b"color legend"),
    ("h3","holdout",True,b"GREEN-TOKEN"),
]

def audit(rows):
    groups={}
    for ident,split,label,data in rows:
        key=sha256(data).hexdigest()
        group=groups.setdefault(key,{"splits":set(),"labels":set(),"ids":[]})
        group["splits"].add(split)
        group["labels"].add(label)
        group["ids"].append(ident)
    issues=[]
    for group in groups.values():
        if len(group["splits"])>1:
            issues.append(("SPLIT_OVERLAP",sorted(group["ids"])))
        if len(group["labels"])>1:
            issues.append(("LABEL_CONFLICT",sorted(group["ids"])))
    return issues

def scan(data):
    with tempfile.TemporaryDirectory(prefix="toy-yara-") as tmp:
        path=Path(tmp)/"sample.txt"
        path.write_bytes(data)
        result=subprocess.run(["yara",str(ROOT/"rules.yar"),str(path)],
                              capture_output=True,text=True,timeout=10)
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or "YARA scan failed")
        return bool(result.stdout.strip())

def main():
    assert audit(ROWS)==[]
    assert audit(ROWS+[("copy","holdout",True,ROWS[0][3])])==[
        ("SPLIT_OVERLAP",["copy","d1"])]
    assert audit(ROWS+[("conflict","dev",False,ROWS[0][3])])==[
        ("LABEL_CONFLICT",["conflict","d1"])]
    assert len(audit(ROWS+[("both","holdout",False,ROWS[0][3])]))==2
    print("4/4 corpus integrity scenarios passed")
    if not shutil.which("yara"):
        raise SystemExit("YARA CLI required for scan portion")
    counts={"tp":0,"fp":0,"tn":0,"fn":0}
    for ident,split,label,data in ROWS:
        if split!="holdout":
            continue
        hit=scan(data)
        outcome=("tp" if hit else "fn") if label else ("fp" if hit else "tn")
        counts[outcome]+=1
        print(ident,outcome.upper())
    assert counts=={"tp":1,"fp":0,"tn":1,"fn":1}
    print("Holdout:",counts)

if __name__=="__main__":
    main()
