#!/usr/bin/env python3
"""Harmless YARA event stream with versioned, correctable alert snapshots."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
WIDTH = 20
LATENESS = 10
# Producer, unique event ID, event time, text
EVENTS = [
    ("a", "e1", 100, "BLUE-TOKEN GREEN-TOKEN"),
    ("a", "e2", 130, "BLUE-TOKEN"),             # Finalizes [100,120).
    ("a", "e3", 110, "GREEN-TOKEN"),            # Legitimate late correction.
    ("a", "e4", 145, "BLUE-TOKEN GREEN-TOKEN"),
    ("a", "e1", 100, "BLUE-TOKEN GREEN-TOKEN"), # Forwarded duplicate.
    ("a", "e1", 100, "BLUE-TOKEN"),             # Contradictory same ID.
    ("b", "e1", 105, "ordinary training notes"),
]

def scan(path: Path) -> set[str]:
    process = subprocess.run(["yara", str(RULES), str(path)],
                             capture_output=True, text=True, timeout=10)
    if process.returncode:
        raise RuntimeError(process.stderr.strip() or "YARA invocation failed")
    return {line.split(maxsplit=1)[0] for line in process.stdout.splitlines()
            if line.strip()}

def evaluate():
    if shutil.which("yara") is None:
        raise RuntimeError("YARA CLI required to execute this lab")
    seen = {}
    maximum_time = {}
    buckets = {}
    counts = {k: 0 for k in ("raw", "accepted", "flagged", "late",
                            "duplicate", "conflict", "corrections")}
    with tempfile.TemporaryDirectory(prefix="yara-versioned-snapshots-") as tmp:
        for index, (source, event_id, second, content) in enumerate(EVENTS):
            path = Path(tmp) / f"event-{index}.txt"
            path.write_text(content, encoding="utf-8")
            hits = scan(path)
            counts["raw"] += len(hits)
            identity = (source, event_id)
            facts = (second, sha256(content.encode()).hexdigest())
            if identity in seen:
                label = "DUPLICATE" if seen[identity] == facts else "CONFLICT"
                counts[label.lower()] += 1
            else:
                seen[identity] = facts
                counts["accepted"] += 1
                counts["flagged"] += bool(hits)
                start = (second // WIDTH) * WIDTH
                key = (source, start)
                record = buckets.setdefault(
                    key, {"alerts": 0, "revision": 1, "finalized": False})
                before = maximum_time.get(source)
                prior_watermark = before - LATENESS if before is not None else None
                late = prior_watermark is not None and second < prior_watermark
                counts["late"] += bool(late)
                if hits:
                    if record["finalized"]:
                        record["revision"] += 1
                        counts["corrections"] += 1
                    record["alerts"] += 1
                maximum_time[source] = max(second, before if before is not None else second)
                watermark = maximum_time[source] - LATENESS
                for (origin, bucket_start), snapshot in buckets.items():
                    if origin == source and bucket_start + WIDTH <= watermark:
                        snapshot["finalized"] = True
                label = "CORRECTION" if late and hits else "ACCEPTED"
            print(f"{source}:{event_id} time={second} {label:11} hits={sorted(hits)}")
    return counts, buckets

def main():
    counts, buckets = evaluate()
    expected = {"raw": 9, "accepted": 5, "flagged": 4, "late": 1,
                "duplicate": 1, "conflict": 1, "corrections": 1}
    for field, expected_value in expected.items():
        assert counts[field] == expected_value, (field, counts[field], expected_value)
    assert buckets[("a", 100)] == {
        "alerts": 2, "revision": 2, "finalized": True}
    print("8/8 synthetic snapshot assertions passed")
    print("Bucket a:[100,120) corrected from revision 1 to 2.")

if __name__ == "__main__":
    main()
