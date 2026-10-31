from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"mz_with_marker.bin").write_bytes(b"MZ"+b"\x00"*8+b"LAB36_HARMLESS_MARKER")
(p/"text_with_marker.txt").write_bytes(b"LAB36_HARMLESS_MARKER")
(p/"mz_without_marker.bin").write_bytes(b"MZ"+b"\x00"*30)
print("Prepared harmless samples")
