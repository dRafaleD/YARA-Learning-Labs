#!/usr/bin/env python3
from pathlib import Path

base = Path("samples")
base.mkdir(exist_ok=True)

samples = {
    "positive-contextual.txt": """YARA_LAB18_MARKER
training_component=parser
version=3.7
feature_alpha
feature_beta
feature_gamma
""",
    "negative-common-error.txt": """This ordinary application log contains an error message.
Nothing else belongs to the Day 18 training signature.
""",
    "negative-marker-only.txt": """YARA_LAB18_MARKER
This file intentionally lacks the other contextual indicators.
""",
    "threshold-positive.txt": """feature_alpha
feature_beta
feature_gamma
""",
    "threshold-negative.txt": """feature_alpha
feature_beta
""",
}

for name, content in samples.items():
    (base / name).write_text(content, encoding="utf-8")

# Create a small benign corpus to demonstrate why common strings can be noisy.
corpus = base / "benign-corpus"
corpus.mkdir(exist_ok=True)
for i in range(1, 31):
    text = f"sample={i}\nstatus=ok\n"
    if i % 3 == 0:
        text += "error=temporary training message\n"
    (corpus / f"benign-{i:02}.txt").write_text(text, encoding="utf-8")

print("Created Day 18 harmless samples and benign corpus.")
