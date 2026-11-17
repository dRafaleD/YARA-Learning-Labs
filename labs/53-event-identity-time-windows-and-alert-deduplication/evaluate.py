#!/usr/bin/env python3
"""Synthetic YARA alerts: compare raw, event, hash and time-window counts."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
BOTH = "BLUE-TOKEN GREEN-TOKEN"
BLUE = "BLUE-TOKEN"
EVENTS = [
    ("e1", "host-a", 100, BOTH),
    ("e1", "host-a", 100, BOTH),  # forwarded copy of the same event
    ("e2", "host-a", 110, BOTH),  # separate event, same host/content/window
    ("e3", "host-b", 110, BOTH),  # another host
    ("e4", "host-a", 240, BOTH),  # later observation window
    ("e5", "host-a", 111, BLUE),
    ("e6", "host-b", 250, "plain training notes"),
]
WINDOW_SECONDS = 60

def scan(path: Path) -> set[str]:
    r = subprocess.run(["yara", str(RULES), str(path)],
                       capture_output=True, text=True, timeout=10, check=False)
    if r.returncode:
        raise RuntimeError(r.stderr.strip() or "YARA failed")
    return {line.split(maxsplit=1)[0] for line in r.stdout.splitlines()
            if line.strip()}

def main():
    if shutil.which("yara") is None:
        raise SystemExit("Install YARA CLI to run this lab")
    raw = 0
    event_ids = set()
    content_hashes = set()
    incident_keys = set()
    received = {}
    with tempfile.TemporaryDirectory(prefix="yara-event-dedup-") as temp:
        for index, (event_id, host, second, content) in enumerate(EVENTS):
            path = Path(temp) / f"sample-{index}.txt"
            path.write_text(content, encoding="utf-8")
            rule_names = scan(path)
            digest = sha256(content.encode()).hexdigest()
            recorded = (host, second, digest)
            if event_id in received and received[event_id] != recorded:
                raise AssertionError("conflicting data under same event ID")
            received[event_id] = recorded
            raw += len(rule_names)
            if rule_names:
                event_ids.add(event_id)
                content_hashes.add(digest)
                # Illustrative bucketing, NOT a true incident identifier.
                incident_keys.add((host, digest, second // WINDOW_SECONDS))
            print(f"{event_id} {host:7} t={second:3} rules={sorted(rule_names)}")
    assert raw == 11, raw
    assert len(event_ids) == 5, event_ids
    assert len(content_hashes) == 2, content_hashes
    assert len(incident_keys) == 4, incident_keys
    assert len(received) == 6
    print(f"raw rule matches={raw}; unique flagged event IDs={len(event_ids)}")
    print(f"unique matching contents={len(content_hashes)}")
    print(f"toy time-bucket groups={len(incident_keys)}")
    print("5/5 aggregate checks passed; these groups are not confirmed incidents")

if __name__ == "__main__":
    main()
