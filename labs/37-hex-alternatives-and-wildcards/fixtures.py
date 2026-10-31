from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"match_a.bin").write_bytes(b"LAB37A9_M")
(p/"match_b.bin").write_bytes(b"LAB37B?_M")
(p/"near_miss.bin").write_bytes(b"LAB37C9_M")
print("Prepared harmless samples")
