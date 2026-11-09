#!/usr/bin/env python3
"""Offline, synthetic YARA train/holdout experiment."""
from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

RULES = Path(__file__).with_name("rules.yar")
RULE_NAMES = ("Synthetic_Broad", "Synthetic_Strict")
# (split, label: 1=positive/0=negative, harmless content)
CASES = (
    ("train", 1, "TEST-CANARY\nACTION-CHECK\ncase A\n"),
    ("train", 1, "case B\nTEST-CANARY\nACTION-CHECK\n"),
    ("train", 0, "USER-GUIDE\nTEST-CANARY is a fictional label\n"),
    ("train", 0, "NORMAL-TEXT\nno markers\n"),
    ("holdout", 1, "case C\nTEST-CANARY\nACTION-CHECK\n"),
    ("holdout", 1, "case D\nTEST-CANARY\nACTION-REVIEW\n"),
    ("holdout", 0, "Guide: TEST-CANARY is a sample name\n"),
    ("holdout", 0, "Ordinary harmless document\n"),
)


def yara_matches(path: Path) -> set[str]:
    completed = subprocess.run(
        ["yara", str(RULES), str(path)],
        capture_output=True, text=True, check=False, timeout=10
    )
    if completed.returncode != 0:
        raise RuntimeError("YARA failed: " + completed.stderr.strip())
    # Each output line is '<rule name> <file path>'.
    return {line.split(maxsplit=1)[0] for line in completed.stdout.splitlines()
            if line.strip()}


def counts(predictions: list[tuple[int, bool]]) -> tuple[int, int, int, int]:
    tp = sum(label == 1 and matched for label, matched in predictions)
    fp = sum(label == 0 and matched for label, matched in predictions)
    tn = sum(label == 0 and not matched for label, matched in predictions)
    fn = sum(label == 1 and not matched for label, matched in predictions)
    return tp, fp, tn, fn


def metric(numerator: int, denominator: int) -> str:
    return f"{numerator / denominator:.2f}" if denominator else "undefined"


def main() -> int:
    if shutil.which("yara") is None:
        print("YARA CLI not found. Install YARA, then run python3 evaluate.py.")
        return 2
    if not RULES.is_file():
        print("Missing rules.yar")
        return 2

    results: dict[tuple[str, str], list[tuple[int, bool]]] = {
        (split, rule): [] for split in ("train", "holdout") for rule in RULE_NAMES
    }
    with tempfile.TemporaryDirectory(prefix="yara-holdout-") as folder:
        for index, (split, label, content) in enumerate(CASES):
            path = Path(folder) / f"case_{index:02d}.txt"
            path.write_text(content, encoding="utf-8")
            found = yara_matches(path)
            for rule in RULE_NAMES:
                results[(split, rule)].append((label, rule in found))

    for split in ("train", "holdout"):
        for rule in RULE_NAMES:
            tp, fp, tn, fn = counts(results[(split, rule)])
            print(f"{split:7} {rule:16} TP={tp} FP={fp} TN={tn} FN={fn} "
                  f"precision={metric(tp, tp + fp)} recall={metric(tp, tp + fn)}")

    assert counts(results[("train", "Synthetic_Strict")]) == (2, 0, 2, 0)
    assert counts(results[("holdout", "Synthetic_Strict")]) == (1, 0, 2, 1)
    print("Assertions passed for this deliberately curated corpus.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"Evaluation error: {error}", file=sys.stderr)
        sys.exit(1)
