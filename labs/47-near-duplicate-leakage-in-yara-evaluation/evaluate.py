#!/usr/bin/env python3
"""Synthetic YARA experiment demonstrating near-duplicate train/test leakage."""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

RULES = Path(__file__).with_name("rules.yar")
CASES = [
    ("train", 1, "case=train-a\nDOC-CANARY\nACTION-CHECK\n"),
    ("train", 1, "case=train-b\nDOC-CANARY\nACTION-CHECK\nnote=extra\n"),
    ("train", 0, "case=train-c\nDOC-CANARY\nREFERENCE\n"),
    ("train", 0, "case=train-d\nGUIDE-NO-MARKER\n"),
    ("holdout", 1, "case=clone\nDOC-CANARY\nACTION-CHECK\n"),
    ("holdout", 1, "case=unseen-a\nDOC-CANARY\nACTION-CHECK\nnote=holdout\n"),
    ("holdout", 1, "case=unseen-b\nDOC-CANARY\nACTION-REVIEW\n"),
    ("holdout", 0, "case=unseen-c\nDOC-CANARY\nNO-ACTION\n"),
    ("holdout", 0, "case=unseen-d\nORDINARY DOCUMENT\n"),
]


def fingerprint(content: str) -> str:
    """Demo-only canonicalization. Do not use blindly on real samples."""
    meaningful = [line.strip() for line in content.splitlines()
                  if line.strip() and not line.startswith("case=")]
    return sha256("\n".join(meaningful).encode("utf-8")).hexdigest()


def yara_match(path: Path) -> bool:
    completed = subprocess.run(
        ["yara", str(RULES), str(path)],
        capture_output=True, text=True, check=False, timeout=10
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "YARA command failed")
    return any(line.startswith("Synthetic_Document_Pair ")
               for line in completed.stdout.splitlines())


def confusion(rows: list[tuple[int, bool]]) -> tuple[int, int, int, int]:
    tp = sum(label == 1 and match for label, match in rows)
    fp = sum(label == 0 and match for label, match in rows)
    tn = sum(label == 0 and not match for label, match in rows)
    fn = sum(label == 1 and not match for label, match in rows)
    return tp, fp, tn, fn


def report(title: str, rows: list[tuple[int, bool]]) -> tuple[int, int, int, int]:
    tp, fp, tn, fn = confusion(rows)
    precision = f"{tp / (tp + fp):.3f}" if tp + fp else "undefined"
    recall = f"{tp / (tp + fn):.3f}" if tp + fn else "undefined"
    print(f"{title}: TP={tp} FP={fp} TN={tn} FN={fn} "
          f"precision={precision} recall={recall}")
    return tp, fp, tn, fn


def main() -> int:
    if shutil.which("yara") is None:
        print("YARA CLI missing. Install it before running this lab.")
        return 2
    train_fingerprints = {fingerprint(content)
                          for split, _, content in CASES if split == "train"}
    train_exact_hashes = {sha256(content.encode()).hexdigest()
                          for split, _, content in CASES if split == "train"}
    rows = {"train": [], "holdout": [], "deduplicated_holdout": []}
    overlap = 0
    with tempfile.TemporaryDirectory(prefix="yara-leakage-") as folder:
        for index, (split, label, content) in enumerate(CASES):
            sample = Path(folder) / f"case-{index}.txt"
            sample.write_text(content, encoding="utf-8")
            matched = yara_match(sample)
            rows[split].append((label, matched))
            if split == "holdout":
                exact = sha256(content.encode()).hexdigest() in train_exact_hashes
                near = fingerprint(content) in train_fingerprints
                if near:
                    overlap += 1
                    print(f"EXCLUDE holdout case-{index}: "
                          f"training overlap (exact={exact}, normalized={near})")
                else:
                    rows["deduplicated_holdout"].append((label, matched))

    report("training", rows["train"])
    raw = report("raw holdout", rows["holdout"])
    clean = report("overlap-filtered holdout", rows["deduplicated_holdout"])
    assert overlap == 1
    assert raw == (2, 0, 2, 1)
    assert clean == (1, 0, 2, 1)
    print("Synthetic assertions passed; evaluate independent corpora in practice.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
