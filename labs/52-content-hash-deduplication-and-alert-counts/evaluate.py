#!/usr/bin/env python3
"""Compare rule alerts, flagged files and unique-content alerts with YARA CLI."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
# name, independent toy label, text, expected matching rules
CASES = [
    ("positive_both_a", True, "BLUE-TOKEN GREEN-TOKEN",
     {"Training_Any", "Training_Both"}),
    ("positive_both_copy", True, "BLUE-TOKEN GREEN-TOKEN",
     {"Training_Any", "Training_Both"}),
    ("positive_blue", True, "BLUE-TOKEN", {"Training_Any"}),
    ("negative_blue", False, "BLUE-TOKEN ", {"Training_Any"}),
    ("negative_green", False, "GREEN-TOKEN", {"Training_Any"}),
    ("negative_plain", False, "ordinary training notes", set()),
]

def scan(path: Path) -> set[str]:
    completed = subprocess.run(
        ["yara", str(RULES), str(path)], text=True,
        capture_output=True, timeout=10, check=False,
    )
    if completed.returncode:
        raise RuntimeError(completed.stderr.strip() or "YARA failed")
    return {line.split(maxsplit=1)[0]
            for line in completed.stdout.splitlines() if line.strip()}

def confusion(rows):
    tp = sum(truth and flagged for truth, flagged in rows)
    fp = sum(not truth and flagged for truth, flagged in rows)
    tn = sum(not truth and not flagged for truth, flagged in rows)
    fn = sum(truth and not flagged for truth, flagged in rows)
    return tp, fp, tn, fn

def main():
    if not shutil.which("yara"):
        raise SystemExit("Install YARA CLI to run this lab.")
    file_rows = []
    by_hash = {}
    raw_alerts = 0
    with tempfile.TemporaryDirectory(prefix="yara-hash-dedup-") as tmp:
        for name, truth, body, expected_rules in CASES:
            file = Path(tmp) / (name + ".txt")
            file.write_text(body, encoding="utf-8")
            matched = scan(file)
            assert matched == expected_rules, (name, matched)
            raw_alerts += len(matched)
            flagged = bool(matched)
            file_rows.append((truth, flagged))
            digest = sha256(body.encode("utf-8")).hexdigest()
            if digest in by_hash:
                assert by_hash[digest] == (truth, flagged), "conflicting labels"
            else:
                by_hash[digest] = (truth, flagged)
            print(f"{name:21} rule_matches={sorted(matched)} sha256={digest[:10]}")

    assert raw_alerts == 7
    assert sum(flagged for _, flagged in file_rows) == 5
    assert len(by_hash) == 5
    assert sum(flagged for _, flagged in by_hash.values()) == 4
    assert confusion(file_rows) == (3, 2, 1, 0)
    assert confusion(list(by_hash.values())) == (2, 2, 1, 0)
    print("rule alerts=7, flagged files=5, flagged distinct contents=4")
    print("file TP/FP/TN/FN=3/2/1/0; unique-content=2/2/1/0")
    print("6 corpus metrics assertions passed; not real detection performance")

if __name__ == "__main__":
    main()
