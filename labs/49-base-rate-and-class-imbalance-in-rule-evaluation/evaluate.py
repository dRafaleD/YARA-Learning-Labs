#!/usr/bin/env python3
"""Measure rule precision at two synthetic class prevalences; requires YARA CLI."""
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
NAMES = ("Training_Any_Token", "Training_Both_Tokens")
POSITIVE = [("positive_both", "BLUE-TOKEN GREEN-TOKEN"),
            ("positive_blue", "BLUE-TOKEN")]
NEGATIVE = [(f"negative_{i:02}", "BLUE-TOKEN" if i < 3 else "plain notes")
            for i in range(18)]

def match_file(filename: Path) -> set[str]:
    run = subprocess.run(["yara", str(RULES), str(filename)],
                         text=True, capture_output=True, timeout=10, check=False)
    if run.returncode:
        raise RuntimeError(run.stderr.strip() or "YARA failed")
    return {line.split(maxsplit=1)[0] for line in run.stdout.splitlines() if line.strip()}

def counts(rows, name):
    tp = sum(truth and name in matches for truth, matches in rows)
    fp = sum(not truth and name in matches for truth, matches in rows)
    tn = sum(not truth and name not in matches for truth, matches in rows)
    fn = sum(truth and name not in matches for truth, matches in rows)
    return tp, fp, tn, fn

def ratio(n, d):
    return f"{n / d:.3f}" if d else "undefined"

def main():
    if not shutil.which("yara"):
        raise SystemExit("Install the YARA CLI before running this lab.")
    cases = [(name, True, body) for name, body in POSITIVE] + [
        (name, False, body) for name, body in NEGATIVE
    ]
    observed = []
    with tempfile.TemporaryDirectory(prefix="yara-base-rate-") as directory:
        for name, truth, body in cases:
            path = Path(directory) / (name + ".txt")
            path.write_text(body, encoding="utf-8")
            observed.append((truth, match_file(path)))
    # Balanced: 2 positive, first 2 negative. Low prevalence: 2 vs 18.
    populations = {
        "balanced": observed[:4],
        "rare-positive": observed,
    }
    expected = {
        ("balanced", "Training_Any_Token"): (2, 2, 0, 0),
        ("balanced", "Training_Both_Tokens"): (1, 0, 2, 1),
        ("rare-positive", "Training_Any_Token"): (2, 3, 15, 0),
        ("rare-positive", "Training_Both_Tokens"): (1, 0, 18, 1),
    }
    for label, rows in populations.items():
        for rule in NAMES:
            tp, fp, tn, fn = counts(rows, rule)
            actual = (tp, fp, tn, fn)
            assert actual == expected[(label, rule)], (label, rule, actual)
            print(f"{label:13} {rule:21} TP={tp} FP={fp} TN={tn} FN={fn} "
                  f"precision={ratio(tp, tp + fp)} recall={ratio(tp, tp + fn)} "
                  f"FPR={ratio(fp, fp + tn)}")
    print("4/4 synthetic confusion matrices passed; these are not field detection rates.")

if __name__ == "__main__":
    main()
