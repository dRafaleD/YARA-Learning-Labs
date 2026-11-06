from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"standalone.txt").write_bytes(b"see LAB43WORD here")
(p/"embedded.txt").write_bytes(b"xxLAB43WORDyy")
(p/"punctuated.txt").write_bytes(b"(LAB43WORD), end")
print("Prepared harmless samples")
