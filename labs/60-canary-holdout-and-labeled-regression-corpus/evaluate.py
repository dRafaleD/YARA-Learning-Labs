"""Compare two harmless YARA rules on fixed labeled development and holdout sets."""
from pathlib import Path
from hashlib import sha256
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).parent
CORPUS = [
    ("d1", "development", "BLUE-TOKEN", True),
    ("d2", "development", "GREEN-TOKEN", True),
    ("d3", "development", "ordinary notes", False),
    ("h1", "holdout", "BLUE-TOKEN example", True),
    ("h2", "holdout", "GREEN-TOKEN color legend", False),
    ("h3", "holdout", "other notes", False),
]

def scan(rule, sample):
    proc = subprocess.run(["yara", str(rule), str(sample)],
                          capture_output=True, text=True, timeout=10)
    if proc.returncode:
        raise RuntimeError(proc.stderr.strip() or "YARA failed")
    return bool(proc.stdout.strip())

def evaluate(rule):
    counts = {split: dict(tp=0, fp=0, tn=0, fn=0)
              for split in ("development", "holdout")}
    with tempfile.TemporaryDirectory(prefix="yara-holdout-") as tmp:
        for ident, split, text, expected in CORPUS:
            path = Path(tmp) / (ident + ".txt")
            path.write_text(text, encoding="utf-8")
            hit = scan(rule, path)
            outcome = ("tp" if hit else "fn") if expected else ("fp" if hit else "tn")
            counts[split][outcome] += 1
    print(rule.name, sha256(rule.read_bytes()).hexdigest(), counts)
    return counts

def main():
    if shutil.which("yara") is None:
        raise SystemExit("Install the YARA CLI before running this lab")
    first = evaluate(ROOT / "rules_v1.yar")
    second = evaluate(ROOT / "rules_v2.yar")
    assert first["development"] == dict(tp=1,fp=0,tn=1,fn=1)
    assert second["development"] == dict(tp=2,fp=0,tn=1,fn=0)
    assert first["holdout"] == dict(tp=1,fp=0,tn=2,fn=0)
    assert second["holdout"] == dict(tp=1,fp=1,tn=1,fn=0)
    assert second["holdout"]["fp"] > first["holdout"]["fp"]
    print("5/5 toy checks passed; holdout regression requires review")

if __name__ == "__main__":
    main()
