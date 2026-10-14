#!/usr/bin/env python3
"""YARA CLI regression tester: per-rule confusion matrix and quality metrics."""
import json
from pathlib import Path
import shutil
import subprocess
import sys

BASE=Path(__file__).resolve().parent
RULE_FILE=BASE/"test_rules.yar"
STRICT="Lab20_Contextual_Detection"
BROAD="Lab20_Broad_Marker"

if shutil.which("yara") is None:
    sys.exit("Install YARA CLI before running the detection regression test.")
subprocess.run([sys.executable,str(BASE/"generate_corpus.py")],check=True)
labels=json.loads((BASE/"labels.json").read_text(encoding="utf-8"))
results={name:{"TP":0,"FP":0,"TN":0,"FN":0} for name in [BROAD,STRICT]}
for filename,positive in sorted(labels.items()):
    proc=subprocess.run(
        ["yara",str(RULE_FILE),str(BASE/"samples"/filename)],
        text=True,capture_output=True)
    if proc.returncode:
        sys.exit(f"YARA error for {filename}: {proc.stderr}")
    matched={line.split(maxsplit=1)[0] for line in proc.stdout.splitlines() if line.strip()}
    for name in results:
        key=("TP" if positive else "FP") if name in matched else ("FN" if positive else "TN")
        results[name][key]+=1
    print(f"{filename:30} label={positive!s:5} matches={','.join(sorted(matched)) or '-'}")

for name,m in results.items():
    denom=m["TP"]+m["FP"]
    precision=m["TP"]/denom if denom else None
    denom=m["TP"]+m["FN"]
    recall=m["TP"]/denom if denom else None
    def fmt(v): return f"{v:.2%}" if v is not None else "undefined"
    print(f"\n{name} {m} precision={fmt(precision)} recall={fmt(recall)}")

strict=results[STRICT]
assert strict=={"TP":3,"FP":0,"TN":5,"FN":0},f"Regression failed: {strict}"
assert results[BROAD]["FP"]>0,"Expected broad marker false positives"
print("\nPASS: expected synthetic-corpus regression results.")
