#!/usr/bin/env python3
"""Offline YARA ruleset migration: pin the version before comparing alert counts."""
from pathlib import Path
from hashlib import sha256
import shutil
import subprocess
import tempfile

BASE = Path(__file__).parent
RULESETS = {
    "v1": BASE / "rules_v1.yar",
    "v2": BASE / "rules_v2.yar",
}
SAMPLES = [
    ("e1", "BLUE-TOKEN"),
    ("e2", "GREEN-TOKEN"),
    ("e3", "BLUE-TOKEN GREEN-TOKEN"),
    ("e4", "normal harmless training notes"),
]

def match(path: Path, rule: Path) -> bool:
    result = subprocess.run(["yara", str(rule), str(path)],
                            capture_output=True, text=True, timeout=10,
                            check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "YARA CLI scan failed")
    return bool(result.stdout.strip())

def evaluate() -> dict:
    if shutil.which("yara") is None:
        raise RuntimeError("YARA CLI is required for this lab")
    versions: dict[str, dict[str, bool]] = {}
    with tempfile.TemporaryDirectory(prefix="yara-versioned-alerts-") as tmp:
        for version, rule in RULESETS.items():
            observations = {}
            for event_id, content in SAMPLES:
                path = Path(tmp) / f"{event_id}.txt"
                path.write_text(content, encoding="utf-8")
                observations[event_id] = match(path, rule)
            versions[version] = observations
    batch_digest = sha256("\n".join(
        f"{eid}:{content}" for eid, content in SAMPLES).encode()).hexdigest()
    totals = {version: sum(flags.values()) for version, flags in versions.items()}
    changed = [eid for eid, _ in SAMPLES if versions["v1"][eid] != versions["v2"][eid]]
    print("batch sha256:", batch_digest)
    for version, flags in versions.items():
        print(f"{version}: {totals[version]} flagged unique events: {flags}")
    print("changed event IDs:", changed)
    return {"v1": totals["v1"], "v2": totals["v2"], "changed": changed,
            "same_events": len(SAMPLES), "batch_digest": batch_digest}

def main():
    results = evaluate()
    assert results["v1"] == 2
    assert results["v2"] == 3
    assert results["changed"] == ["e2"]
    assert results["same_events"] == 4
    assert len(results["batch_digest"]) == 64
    print("5/5 pinned-rule-version assertions passed")

if __name__ == "__main__":
    main()
