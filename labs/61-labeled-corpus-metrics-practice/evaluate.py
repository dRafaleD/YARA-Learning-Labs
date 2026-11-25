"""Measure toy YARA classification on a labeled harmless corpus."""
from pathlib import Path
import subprocess
import tempfile
import shutil

ROOT = Path(__file__).resolve().parent
CORPUS = [
    ("p1","BLUE-TOKEN",True),
    ("p2","BLUE-TOKEN note",True),
    ("p3","GREEN-TOKEN",True),
    ("p4","GREEN-TOKEN memo",True),
    ("p5","BLUE-TOKEN GREEN-TOKEN",True),
    ("p6","ORANGE-TOKEN",True),
    ("n1","ordinary report",False),
    ("n2","GREEN-TOKEN color legend",False),
    ("n3","BLUE-TOKEN classroom example",False),
    ("n4","plain document",False),
    ("n5","",False),
    ("n6","another training note",False),
]

def scan(rule, path):
    result = subprocess.run(["yara",str(rule),str(path)],
                            capture_output=True,text=True,timeout=10)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "YARA failed")
    return bool(result.stdout.strip())

def ratio(a,b):
    return a/b if b else None

def measure(c):
    p=ratio(c["tp"],c["tp"]+c["fp"])
    r=ratio(c["tp"],c["tp"]+c["fn"])
    f1=2*p*r/(p+r) if p is not None and r is not None and p+r else None
    return {"precision":p,"recall":r,"f1":f1,
            "fpr":ratio(c["fp"],c["fp"]+c["tn"])}

def evaluate(rule):
    counts=dict(tp=0,fp=0,tn=0,fn=0)
    with tempfile.TemporaryDirectory(prefix="yara-metrics-") as directory:
        for ident,text,truth in CORPUS:
            sample=Path(directory)/(ident+".txt")
            sample.write_text(text,encoding="utf-8")
            hit=scan(rule,sample)
            tag=("tp" if hit else "fn") if truth else ("fp" if hit else "tn")
            counts[tag]+=1
            print(f"{rule.name:14} {ident} {tag.upper()}")
    metrics=measure(counts)
    print(counts,metrics)
    return counts,metrics

def main():
    if not shutil.which("yara"):
        raise SystemExit("Install the YARA command-line tool first")
    a,ma=evaluate(ROOT/"rules_v1.yar")
    b,mb=evaluate(ROOT/"rules_v2.yar")
    assert a==dict(tp=3,fp=1,tn=5,fn=3)
    assert b==dict(tp=5,fp=2,tn=4,fn=1)
    assert ma["precision"]==.75 and ma["recall"]==.5
    assert abs(ma["f1"]-.6)<1e-9
    assert mb["recall"]>ma["recall"]
    assert mb["fpr"]>ma["fpr"]
    assert ratio(0,0) is None
    print("24 sample evaluations + 7 metric checks passed")

if __name__=="__main__":
    main()
