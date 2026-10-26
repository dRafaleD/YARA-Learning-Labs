from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"suspicious.txt").write_text("LAB32_SUSPICIOUS\n")
(p/"suspicious_with_benign.txt").write_text("LAB32_SUSPICIOUS\nLAB32_BENIGN_VENDOR\n")
(p/"benign_only.txt").write_text("LAB32_BENIGN_VENDOR\n")
print("Prepared harmless samples")
