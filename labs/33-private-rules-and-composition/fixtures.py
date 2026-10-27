from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"both.txt").write_text("LAB32_HEADER\nLAB32_BODY\n")
(p/"header_only.txt").write_text("LAB32_HEADER\n")
(p/"body_only.txt").write_text("LAB32_BODY\n")
print("Prepared harmless samples")
