from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
marker=b"LAB35_HARMLESS_MARKER"
(p/"plain.txt").write_bytes(marker)
(p/"xor_0x41.bin").write_bytes(bytes(b^0x41 for b in marker))
(p/"unrelated.txt").write_bytes(b"nothing to see here")
print("Prepared harmless samples")
