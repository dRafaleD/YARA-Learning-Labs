#!/usr/bin/env python3
"""YARA alert accounting: duplicate IDs, late delivery and contradictory records."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
# producer, event ID, event time, ingestion time, harmless file contents
EVENTS = [
    ("a", "e1", 100, 101, "BLUE-TOKEN GREEN-TOKEN"),
    ("a", "e1", 100, 103, "BLUE-TOKEN GREEN-TOKEN"),  # forwarded duplicate
    ("a", "e2", 102, 140, "BLUE-TOKEN"),              # delivered late
    ("b", "e1", 105, 106, "GREEN-TOKEN"),             # same ID, other sensor
    ("a", "e3", 115, 116, "ordinary notes"),
    ("a", "e4", 110, 111, "BLUE-TOKEN GREEN-TOKEN"),
    ("a", "e4", 110, 119, "BLUE-TOKEN"),              # conflicting same ID
]
LATENCY_LIMIT = 20

def matches(path: Path) -> set[str]:
    p = subprocess.run(["yara", str(RULES), str(path)],
                       text=True, capture_output=True, timeout=10, check=False)
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or "YARA exited with an error")
    return {line.split(maxsplit=1)[0] for line in p.stdout.splitlines() if line}

def main():
    if shutil.which("yara") is None:
        raise SystemExit("Install YARA CLI before running the evaluation")
    seen = {}
    raw_alerts = duplicate = conflicts = late = timely = 0
    with tempfile.TemporaryDirectory(prefix="yara-late-events-") as temp:
        for index, (producer, event_id, when, received, content) in enumerate(EVENTS):
            path = Path(temp) / f"item-{index}.txt"
            path.write_text(content, encoding="utf-8")
            hits = matches(path)
            raw_alerts += len(hits)
            identity = (producer, event_id)
            facts = (when, sha256(content.encode()).hexdigest())
            if identity in seen:
                if seen[identity] == facts:
                    duplicate += 1
                    label = "DUPLICATE"
                else:
                    conflicts += 1
                    label = "CONFLICT"
            else:
                seen[identity] = facts
                label = "LATE" if received - when > LATENCY_LIMIT else "ON_TIME"
                if hits:
                    if label == "LATE":
                        late += 1
                    else:
                        timely += 1
            print(f"{producer}:{event_id} {label:10} matches={sorted(hits)}")
    assert raw_alerts == 9
    assert duplicate == 1 and conflicts == 1
    assert len(seen) == 5
    assert late == 1 and timely == 3
    print("raw rule alerts=9; deduplicated flagged events=4")
    print("late flagged events=1; timely flagged events=3")
    print("5/5 aggregate checks passed; no incident attribution")

if __name__ == "__main__":
    main()
