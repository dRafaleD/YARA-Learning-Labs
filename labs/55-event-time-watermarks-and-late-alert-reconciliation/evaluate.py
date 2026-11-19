#!/usr/bin/env python3
"""Toy YARA event-time watermarking: preserve late evidence for investigation."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
ALLOWED_LATENESS = 10
# source, event_id, event_time, ingest_time, harmless file bytes
ROWS = [
    ("a", "e1", 100, 101, "BLUE-TOKEN GREEN-TOKEN"),
    ("a", "e2", 130, 132, "BLUE-TOKEN"),
    ("a", "e3", 115, 150, "BLUE-TOKEN GREEN-TOKEN"), # late, new ID
    ("a", "e2", 130, 151, "BLUE-TOKEN"),              # duplicate
    ("a", "e2", 130, 152, "BLUE-TOKEN GREEN-TOKEN"),  # conflicting ID
    ("b", "e1", 108, 160, "GREEN-TOKEN"),             # independent source
    ("a", "e4", 125, 180, "ordinary notes"),
]

def scan(path: Path) -> set[str]:
    p = subprocess.run(["yara", str(RULES), str(path)],
                       capture_output=True, text=True, timeout=10, check=False)
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or "YARA invocation failed")
    return {s.split(maxsplit=1)[0] for s in p.stdout.splitlines() if s.strip()}

def evaluate() -> dict:
    if not shutil.which("yara"):
        raise RuntimeError("YARA CLI required for Day 55")
    seen = {}
    max_event_time = {}
    totals = {key: 0 for key in ("raw", "accepted", "flagged", "late",
                                 "duplicate", "conflict")}
    with tempfile.TemporaryDirectory(prefix="yara-watermark-") as tmp:
        for i, (source, event_id, event_time, ingested, content) in enumerate(ROWS):
            path = Path(tmp) / f"sample-{i}.txt"
            path.write_text(content, encoding="utf-8")
            hits = scan(path)
            totals["raw"] += len(hits)
            identity = (source, event_id)
            facts = (event_time, sha256(content.encode()).hexdigest())
            previous = seen.get(identity)
            if previous is not None:
                label = "DUPLICATE" if previous == facts else "CONFLICT"
                totals[label.lower()] += 1
            else:
                watermark = max_event_time.get(source, event_time) - ALLOWED_LATENESS
                label = "LATE" if event_time < watermark else "ON_TIME"
                totals["late"] += label == "LATE"
                totals["accepted"] += 1
                totals["flagged"] += bool(hits)
                seen[identity] = facts
                max_event_time[source] = max(max_event_time.get(source, event_time),
                                             event_time)
            print(f"{source}:{event_id} event={event_time} ingest={ingested} "
                  f"{label:10} matches={sorted(hits)}")
    return totals

def main():
    found = evaluate()
    expected = {"raw": 9, "accepted": 5, "flagged": 4, "late": 1,
                "duplicate": 1, "conflict": 1}
    for key, value in expected.items():
        assert found[key] == value, (key, found[key], value)
    print("6/6 watermark aggregate assertions passed")
    print("Late events are retained and flagged, not silently discarded.")

if __name__ == "__main__":
    main()
