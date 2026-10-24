from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"ascii_upper.txt").write_text("LAB30_MARKER\n")
(p/"wide.bin").write_bytes("lab30_marker".encode("utf-16-le"))
(p/"near_miss.txt").write_text("LAB30-MARKER\n")
print("Prepared harmless samples")
