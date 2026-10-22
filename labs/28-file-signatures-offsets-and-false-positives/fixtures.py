from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"positive.bin").write_bytes(b"LAB28 safe_document")
(p/"negative.bin").write_bytes(b"XXXXLAB28 safe_document")
print("Created two harmless binary fixtures")
