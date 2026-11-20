#!/usr/bin/env python3
"""Toy YARA stream: late event may revise an already finalized time bucket."""
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
WIDTH = 20
LATENESS = 10
# Producer, event ID, event-time seconds, synthetic content
ROWS = [
    ("a", "e1", 100, "BLUE-TOKEN GREEN-TOKEN"),
    ("a", "e2", 130, "BLUE-TOKEN"),
    ("a", "e3", 110, "GREEN-TOKEN"),    # After bucket [100,120) finalized.
    ("a", "e1", 100, "BLUE-TOKEN GREEN-TOKEN"), # Forwarded duplicate.
    ("b", "e1", 110, "ordinary training text"),
    ("a", "e4", 145, "BLUE-TOKEN GREEN-TOKEN"),
]

def scan(path: Path) -> set[str]:
    outcome = subprocess.run(["yara", str(RULES), str(path)],
                             capture_output=True, text=True, timeout=10)
    if outcome.returncode:
        raise RuntimeError(outcome.stderr.strip() or "YARA CLI failed")
    return {line.split(maxsplit=1)[0] for line in outcome.stdout.splitlines()
            if line.strip()}

def evaluate():
    if shutil.which("yara") is None:
        raise RuntimeError("Install the YARA CLI before running this lab")
    seen = set()
    max_time = {}
    count = dict(raw=0, accepted=0, flagged=0, late=0, duplicate=0, reconciled=0)
    with tempfile.TemporaryDirectory(prefix="yara-watermark-final-") as tmp:
        for index, (producer, event_id, second, content) in enumerate(ROWS):
            path = Path(tmp) / f"event-{index}.txt"
            path.write_text(content, encoding="utf-8")
            hits = scan(path)
            count["raw"] += len(hits)
            key = (producer, event_id)
            if key in seen:
                count["duplicate"] += 1
                verdict = "DUPLICATE"
            else:
                seen.add(key)
                prior_max = max_time.get(producer)
                prior_watermark = None if prior_max is None else prior_max - LATENESS
                late = prior_watermark is not None and second < prior_watermark
                bucket_end = (second // WIDTH + 1) * WIDTH
                correction = late and bucket_end <= prior_watermark
                count["accepted"] += 1
                count["flagged"] += bool(hits)
                count["late"] += late
                count["reconciled"] += correction
                max_time[producer] = max(prior_max or second, second)
                verdict = "RECONCILE" if correction else "LATE" if late else "ON_TIME"
            print(f"{producer}:{event_id} time={second} {verdict:10} {sorted(hits)}")
    return count

def main():
    actual = evaluate()
    expected = {"raw": 8, "accepted": 5, "flagged": 4,
                "late": 1, "duplicate": 1, "reconciled": 1}
    for field, value in expected.items():
        assert actual[field] == value, (field, actual[field], value)
    print("6/6 synthetic finalization/reconciliation checks passed")
    print("A late observation is retained; case counts can be revised.")

if __name__ == "__main__":
    main()
