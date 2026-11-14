#!/usr/bin/env python3
"""Stratified evaluation on synthetic harmless text; needs YARA CLI."""
from collections import defaultdict
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
RULE_NAMES = ("Training_Any", "Training_Both")
SAMPLES = [
    ("alpha", True, "BLUE-TOKEN GREEN-TOKEN"),
    ("alpha", True, "BLUE-TOKEN"),
    ("alpha", False, "BLUE-TOKEN"),
    ("alpha", False, "ordinary notes"),
    ("beta", True, "GREEN-TOKEN BLUE-TOKEN"),
    ("beta", True, "GREEN-TOKEN"),
    ("beta", False, "GREEN-TOKEN"),
    ("beta", False, "GREEN-TOKEN"),
    ("beta", False, "GREEN-TOKEN"),
    ("beta", False, "ordinary notes"),
]
EXPECTED = {
    ("alpha", "Training_Any"): (2, 1, 1, 0),
    ("alpha", "Training_Both"): (1, 0, 2, 1),
    ("beta", "Training_Any"): (2, 3, 1, 0),
    ("beta", "Training_Both"): (1, 0, 4, 1),
}

def matches(path: Path) -> set[str]:
    r = subprocess.run(["yara", str(RULES), str(path)], capture_output=True,
                       text=True, timeout=10, check=False)
    if r.returncode:
        raise RuntimeError(r.stderr or "YARA failed")
    return {line.split(maxsplit=1)[0] for line in r.stdout.splitlines() if line}

def main():
    if not shutil.which("yara"):
        raise SystemExit("YARA CLI is required to run this exercise")
    observed = defaultdict(list)
    with tempfile.TemporaryDirectory(prefix="yara-strata-") as tmp:
        for i, (group, positive, content) in enumerate(SAMPLES):
            path = Path(tmp) / f"sample-{i}.txt"
            path.write_text(content, encoding="utf-8")
            result = matches(path)
            observed[group].append((positive, result))
    for group, rows in observed.items():
        for name in RULE_NAMES:
            tp = sum(y and name in hits for y, hits in rows)
            fp = sum(not y and name in hits for y, hits in rows)
            tn = sum(not y and name not in hits for y, hits in rows)
            fn = sum(y and name not in hits for y, hits in rows)
            assert (tp, fp, tn, fn) == EXPECTED[(group, name)]
            print(f"{group} {name} TP={tp} FP={fp} TN={tn} FN={fn}")
    print("4/4 stratified confusion matrices checked")

if __name__ == "__main__":
    main()
