from pathlib import Path

out = Path(__file__).parent / "samples"
out.mkdir(exist_ok=True)
cases = {
    "positive_1.txt": "LAB-ALPHA-2026\nLAB-BETA-2026\n",
    "positive_2.txt": "header LAB-ALPHA-2026 footer LAB-BETA-2026\n",
    "negative_1.txt": "unrelated harmless content\n",
    "negative_2.txt": "LAB-ALPHA-2026 appears without its pair\n",
}
for name, contents in cases.items():
    (out / name).write_text(contents, encoding="utf-8")
print("Created", len(cases), "harmless samples in", out)
