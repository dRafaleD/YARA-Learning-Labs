"""Compare per-group detection metrics on harmless labeled text."""
from fractions import Fraction
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT=Path(__file__).parent
ROWS=[
    ("a","BLUE-TOKEN",True),("a","BLUE-TOKEN memo",True),
    ("a","ordinary text",False),("a","plain report",False),
    ("b","GREEN-TOKEN",True),("b","BLUE-TOKEN legend",False),
]

def metrics(rows):
    c=dict(tp=0,fp=0,tn=0,fn=0)
    for truth,hit in rows:
        c[("tp" if hit else "fn") if truth else ("fp" if hit else "tn")]+=1
    def ratio(a,b):
        return Fraction(a,b) if b else None
    return c,ratio(c["tp"],c["tp"]+c["fn"]),ratio(c["fp"],c["fp"]+c["tn"])

def main():
    assert metrics([])==(dict(tp=0,fp=0,tn=0,fn=0),None,None)
    assert metrics([(True,False)])[1:]==(Fraction(0),None)
    assert metrics([(False,True)])[1:]==(None,Fraction(1))
    if not shutil.which("yara"):
        raise SystemExit("Install YARA CLI for the scan portion")
    groups={"a":[],"b":[]}
    with tempfile.TemporaryDirectory() as tmp:
        for i,(group,content,truth) in enumerate(ROWS):
            path=Path(tmp)/f"sample-{i}.txt"
            path.write_text(content,encoding="utf-8")
            result=subprocess.run(["yara",str(ROOT/"rules.yar"),str(path)],
                                  capture_output=True,text=True,timeout=10)
            if result.returncode:
                raise RuntimeError(result.stderr or "YARA scan failed")
            groups[group].append((truth,bool(result.stdout.strip())))
    a,b=metrics(groups["a"]),metrics(groups["b"])
    overall=metrics(groups["a"]+groups["b"])
    assert a==(dict(tp=2,fp=0,tn=2,fn=0),Fraction(1),Fraction(0))
    assert b==(dict(tp=0,fp=1,tn=0,fn=1),Fraction(0),Fraction(1))
    assert overall[1:]==(Fraction(2,3),Fraction(1,3))
    print("Group A:",a)
    print("Group B:",b)
    print("Overall:",overall)
    print("6 scans + 6 metric assertions completed")

if __name__=="__main__":
    main()
