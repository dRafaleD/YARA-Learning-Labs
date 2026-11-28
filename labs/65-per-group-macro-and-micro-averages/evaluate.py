"""Offline YARA metrics on harmless synthetic groups."""
from fractions import Fraction
from pathlib import Path
import subprocess
import tempfile
import shutil

ROOT=Path(__file__).parent
ROWS=[
    ("a1","a",True,"BLUE-TOKEN"),
    ("a2","a",False,"ordinary report"),
    ("b1","b",True,"BLUE-TOKEN example"),
    ("b2","b",True,"GREEN-TOKEN"),
    ("b3","b",True,"ORANGE-TOKEN"),
    ("b4","b",False,"BLUE-TOKEN color legend"),
]

def recall(counts):
    tp,fn=counts["tp"],counts["fn"]
    return Fraction(tp,tp+fn) if tp+fn else None

def averages(groups):
    values=[value for c in groups.values() if (value:=recall(c)) is not None]
    total_tp=sum(c["tp"] for c in groups.values())
    total_fn=sum(c["fn"] for c in groups.values())
    return (sum(values,Fraction(0))/len(values) if values else None,
            Fraction(total_tp,total_tp+total_fn) if total_tp+total_fn else None)

def scan(path):
    result=subprocess.run(["yara",str(ROOT/"rules.yar"),str(path)],
                          capture_output=True,text=True,timeout=10)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "YARA failed")
    return bool(result.stdout.strip())

def main():
    expected={"a":{"tp":1,"fn":0,"fp":0,"tn":1},
              "b":{"tp":1,"fn":2,"fp":1,"tn":0}}
    assert recall(expected["a"])==1
    assert recall(expected["b"])==Fraction(1,3)
    assert averages(expected)==(Fraction(2,3),Fraction(1,2))
    assert averages({})==(None,None)
    assert averages({"empty":{"tp":0,"fn":0}})==(None,None)
    assert averages({**expected,"empty":{"tp":0,"fn":0}})==averages(expected)
    print("6 arithmetic checks passed")
    if not shutil.which("yara"):
        raise SystemExit("Install YARA CLI for scan portion")
    groups={}
    with tempfile.TemporaryDirectory(prefix="yara-groups-") as temp:
        for ident,group,truth,text in ROWS:
            p=Path(temp)/(ident+".txt")
            p.write_text(text,encoding="utf-8")
            hit=scan(p)
            label=("tp" if hit else "fn") if truth else ("fp" if hit else "tn")
            c=groups.setdefault(group,dict(tp=0,fn=0,fp=0,tn=0))
            c[label]+=1
            print(ident,group,label.upper())
    assert groups==expected
    print("Macro recall, micro recall:",averages(groups))

if __name__=="__main__":
    main()
