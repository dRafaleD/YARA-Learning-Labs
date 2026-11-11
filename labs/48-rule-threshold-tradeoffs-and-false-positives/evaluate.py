#!/usr/bin/env python3
"""Test threshold tradeoffs on harmless text; requires YARA CLI."""
from pathlib import Path
import shutil
import subprocess
import tempfile

RULES = Path(__file__).with_name("rules.yar")
NAMES = ("Synthetic_Any", "Synthetic_Two", "Synthetic_All")
CASES = (
    ("positive_all", 1, "BLUE-TOKEN GREEN-TOKEN ORANGE-TOKEN"),
    ("positive_two", 1, "BLUE-TOKEN GREEN-TOKEN"),
    ("negative_one", 0, "BLUE-TOKEN"),
    ("negative_two", 0, "BLUE-TOKEN ORANGE-TOKEN"),
    ("negative_none", 0, "plain ordinary notes"),
)
EXPECTED = {
    "Synthetic_Any": (2, 2, 1, 0),
    "Synthetic_Two": (2, 1, 2, 0),
    "Synthetic_All": (1, 0, 3, 1),
}


def matches(filename: Path) -> set[str]:
    result = subprocess.run(
        ["yara", str(RULES), str(filename)], text=True,
        capture_output=True, timeout=10, check=False
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "YARA command failed")
    return {line.split(maxsplit=1)[0] for line in result.stdout.splitlines()
            if line.strip()}


def ratio(numerator: int, denominator: int) -> str:
    return f"{numerator / denominator:.2f}" if denominator else "undefined"


def main() -> None:
    if not shutil.which("yara"):
        raise SystemExit("Install YARA CLI to run this lab.")
    measured = {name: [] for name in NAMES}
    with tempfile.TemporaryDirectory(prefix="yara-thresholds-") as temp:
        for label, truth, content in CASES:
            path = Path(temp) / (label + ".txt")
            path.write_text(content, encoding="utf-8")
            observed = matches(path)
            for name in NAMES:
                measured[name].append((truth, name in observed))

    for name in NAMES:
        pairs = measured[name]
        tp = sum(t == 1 and p for t, p in pairs)
        fp = sum(t == 0 and p for t, p in pairs)
        tn = sum(t == 0 and not p for t, p in pairs)
        fn = sum(t == 1 and not p for t, p in pairs)
        counts = (tp, fp, tn, fn)
        print(f"{name:16} TP={tp} FP={fp} TN={tn} FN={fn} "
              f"precision={ratio(tp, tp + fp)} recall={ratio(tp, tp + fn)}")
        assert counts == EXPECTED[name], (name, counts)
    print("All synthetic threshold checks passed.")


if __name__ == "__main__":
    main()
