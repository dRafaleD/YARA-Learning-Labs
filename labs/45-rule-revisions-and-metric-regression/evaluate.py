"""Compare two educational YARA rules on the same harmless, labeled corpus."""
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
CASES = {
    "positive_1.txt": (True, "DOC-ALPHA\nACTION-VERIFY\n"),
    "positive_2.txt": (True, "Header DOC-ALPHA; step ACTION-VERIFY\n"),
    "near_miss_negative.txt": (False, "This benign manual mentions DOC-ALPHA only.\n"),
    "negative_2.txt": (False, "General training notes with no matching markers.\n"),
}

def scan(rule: Path, sample: Path) -> bool:
    result = subprocess.run(["yara", str(rule), str(sample)], text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=10, check=False)
    if result.returncode != 0 or result.stderr.strip():
        raise RuntimeError(f"YARA failed: {result.stderr.strip()}")
    return bool(result.stdout.strip())

def score(rule: Path, folder: Path) -> dict:
    counts = {"TP": 0, "FP": 0, "TN": 0, "FN": 0}
    for name, (positive, _) in CASES.items():
        matched = scan(rule, folder / name)
        cell = "TP" if positive and matched else (
            "FN" if positive else ("FP" if matched else "TN"))
        counts[cell] += 1
        print(f"  {name}: expected_positive={positive}, matched={matched} -> {cell}")
    return counts

def safe_ratio(num: int, denominator: int):
    return num / denominator if denominator else None

def main():
    if shutil.which("yara") is None:
        raise SystemExit("YARA CLI missing; install 'yara' to run this practical.")
    with tempfile.TemporaryDirectory(prefix="yara-learning-") as directory:
        folder = Path(directory)
        for name, (_, body) in CASES.items():
            (folder / name).write_text(body, encoding="utf-8")
        expected = {
            "v1": {"TP": 2, "FP": 1, "TN": 1, "FN": 0},
            "v2": {"TP": 2, "FP": 0, "TN": 2, "FN": 0},
        }
        for version in ("v1", "v2"):
            print("\n" + version)
            counts = score(HERE / f"rules_{version}.yar", folder)
            print("Counts:", counts)
            print("Precision:", safe_ratio(counts["TP"], counts["TP"] + counts["FP"]))
            print("Recall:", safe_ratio(counts["TP"], counts["TP"] + counts["FN"]))
            assert counts == expected[version], "Regression result changed"
    print("\nAll labeled synthetic regression checks passed.")

if __name__ == "__main__":
    main()
