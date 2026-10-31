from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"early.txt").write_bytes(b"LAB38_ITEM" + b"." * 40)
(p/"late.txt").write_bytes(b"." * 40 + b"LAB38_ITEM")
(p/"both.txt").write_bytes(b"LAB38_ITEM" + b"." * 40 + b"LAB38_ITEM")
print("Prepared harmless samples")
