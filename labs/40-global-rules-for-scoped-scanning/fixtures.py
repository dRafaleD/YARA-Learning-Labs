from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"small_marker.txt").write_bytes(b"LAB40_HARMLESS_MARKER")
(p/"large_marker.txt").write_bytes(b"LAB40_HARMLESS_MARKER" + b"." * 4096)
print("Prepared harmless samples")
