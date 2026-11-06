"""Run installed YARA CLI against labeled, synthetic files; no third-party target."""
from pathlib import Path
import subprocess
import shutil
from make_samples import out, cases

if not shutil.which("yara"):
    raise SystemExit("YARA CLI not found. Install it separately before running.")
root = Path(__file__).parent
tp = fp = tn = fn = 0
for filename in sorted(cases):
    expected = filename.startswith("positive_")
    proc = subprocess.run(["yara", str(root / "rules.yar"), str(out / filename)],
                          capture_output=True, text=True, check=False)
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"YARA failed for {filename}: {proc.stderr}")
    # YARA CLI exits 0 even if no rule matches.
    matched = any(line.startswith("Synthetic_Paired_Indicators ") for line in proc.stdout.splitlines())
    if expected and matched: tp += 1
    elif expected: fn += 1
    elif matched: fp += 1
    else: tn += 1
    print(f"{filename}: expected={expected}, matched={matched}")
print(f"TP={tp} FP={fp} TN={tn} FN={fn}")
print("precision:", tp/(tp+fp) if tp+fp else "undefined")
print("recall:", tp/(tp+fn) if tp+fn else "undefined")
