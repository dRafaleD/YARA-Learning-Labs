#!/usr/bin/env python3
"""Run the Lab 19 YARA rules against deterministic fixtures."""
from pathlib import Path
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
EXPECTED = {
    "low-entropy.bin": {"Lab19_LowEntropyFirstWindow"},
    "high-entropy.bin": {"Lab19_HighEntropyFirstWindow"},
    "mixed-entropy.bin": {
        "Lab19_LowEntropyFirstWindow",
        "Lab19_HighEntropySecondWindow",
    },
}

if shutil.which("yara") is None:
    sys.exit("YARA CLI not found. Install YARA, then rerun this test.")

subprocess.run([sys.executable, str(BASE / "generate_samples.py")], check=True)

failure = False
for name, expected in EXPECTED.items():
    proc = subprocess.run(
        ["yara", str(BASE / "test_rules.yar"), str(BASE / "samples" / name)],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.exit(f"YARA returned {proc.returncode} for {name}:\n{proc.stderr}")
    actual = {line.split(maxsplit=1)[0]
              for line in proc.stdout.splitlines() if line.strip()}
    ok = actual == expected
    print(f"{'PASS' if ok else 'FAIL'} {name}: {sorted(actual)}")
    if not ok:
        print(f"  expected: {sorted(expected)}")
        failure = True

sys.exit(1 if failure else 0)
