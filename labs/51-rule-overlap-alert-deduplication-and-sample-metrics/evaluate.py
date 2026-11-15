#!/usr/bin/env python3
"""Differentiate per-rule alerts from per-sample detections using harmless YARA fixtures."""
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
CASES = [
    ("positive_both", True, "BLUE-TOKEN GREEN-TOKEN", 3),
    ("positive_blue", True, "BLUE-TOKEN", 2),
    ("negative_blue", False, "BLUE-TOKEN", 2),
    ("negative_green", False, "GREEN-TOKEN", 1),
    ("negative_plain", False, "ordinary training text", 0),
]

def scan(path: Path) -> set[str]:
    result = subprocess.run(
        ["yara", str(RULES), str(path)],
        text=True, capture_output=True, timeout=10, check=False
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "YARA failed")
    return {line.split(maxsplit=1)[0] for line in result.stdout.splitlines() if line.strip()}

def main():
    if not shutil.which("yara"):
        raise SystemExit("Install YARA CLI to run the exercise")
    rows = []
    with tempfile.TemporaryDirectory(prefix="yara-overlap-") as directory:
        for name, truth, content, expected_count in CASES:
            path = Path(directory) / f"{name}.txt"
            path.write_text(content, encoding="utf-8")
            names = scan(path)
            assert len(names) == expected_count, (name, names)
            rows.append((truth, names))
            print(f"{name:17} matches={sorted(names)}")
    raw_alerts = sum(len(names) for _, names in rows)
    tp = sum(truth and bool(names) for truth, names in rows)
    fp = sum(not truth and bool(names) for truth, names in rows)
    tn = sum(not truth and not names for truth, names in rows)
    fn = sum(truth and not names for truth, names in rows)
    assert raw_alerts == 8
    assert (tp, fp, tn, fn) == (2, 2, 1, 0)
    assert sum(bool(names) for _, names in rows) == 4
    print(f"raw rule alerts={raw_alerts}; unique flagged samples=4")
    print(f"sample metrics TP={tp} FP={fp} TN={tn} FN={fn}")
    print("8/8 fixture/count checks passed; detection quality remains unproven")

if __name__ == "__main__":
    main()
