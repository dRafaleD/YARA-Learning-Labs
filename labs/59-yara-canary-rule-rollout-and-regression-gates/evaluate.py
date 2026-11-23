#!/usr/bin/env python3
"""Toy YARA canary gate: compare exact event IDs, not just alert totals."""
from hashlib import sha256
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).parent
RULESETS = {name: HERE / f"rules_{name}.yar" for name in ("v1", "v2", "v3")}
EVENTS = [
    ("e1", "BLUE-TOKEN"),
    ("e2", "GREEN-TOKEN"),
    ("e3", "BLUE-TOKEN GREEN-TOKEN"),
    ("e4", "TRAINING-NOTE only"),
]

def matched(rule: Path, path: Path) -> bool:
    proc = subprocess.run(["yara", str(rule), str(path)],
                          capture_output=True, text=True, timeout=10)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "YARA scan failed")
    return bool(proc.stdout.strip())

def gate(baseline: set[str], candidate: set[str]) -> str:
    added = candidate - baseline
    removed = baseline - candidate
    # Host-controlled acceptance contract for THIS harmless canary corpus.
    return "PROMOTE_CANDIDATE" if added == {"e2"} and not removed else "QUARANTINE"

def main():
    if not shutil.which("yara"):
        raise SystemExit("Install the YARA command-line tool first")
    results = {}
    with tempfile.TemporaryDirectory(prefix="yara-canary-") as tmp:
        corpus = {}
        for event_id, content in EVENTS:
            sample = Path(tmp) / f"{event_id}.txt"
            sample.write_text(content, encoding="utf-8")
            corpus[event_id] = sample
        for version, rule in RULESETS.items():
            results[version] = {
                event_id for event_id, path in corpus.items() if matched(rule, path)}
            rule_hash = sha256(rule.read_bytes()).hexdigest()[:16]
            print(f"{version} sha256[:16]={rule_hash} matched={sorted(results[version])}")
    good = gate(results["v1"], results["v2"])
    bad = gate(results["v1"], results["v3"])
    checks = [
        ("baseline alerts", len(results["v1"]) == 2),
        ("expected candidate alerts", len(results["v2"]) == 3),
        ("overbroad candidate alerts", len(results["v3"]) == 4),
        ("only expected canary addition", results["v2"]-results["v1"] == {"e2"}),
        ("unexpected canary addition", "e4" in results["v3"]-results["v1"]),
        ("promote expected change", good == "PROMOTE_CANDIDATE"),
        ("quarantine regression", bad == "QUARANTINE"),
        ("same four events", len(EVENTS) == 4),
    ]
    for name, passed in checks:
        assert passed, name
        print(f"{name:31} PASS")
    print("8/8 synthetic rollout-gate assertions passed")

if __name__ == "__main__":
    main()
