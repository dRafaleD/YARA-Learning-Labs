from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"lab4.bin").write_bytes(b"LAB4" + b"\x00" * 8)
(p/"short.bin").write_bytes(b"LA")
print("Prepared harmless samples")
