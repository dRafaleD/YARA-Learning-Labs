from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"match.bin").write_bytes(b"LAB27xyEND")
(p/"no_match.bin").write_bytes(b"LAB27xEND")
print("Created harmless training fixtures")
