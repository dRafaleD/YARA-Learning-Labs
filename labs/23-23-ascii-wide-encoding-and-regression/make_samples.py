from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"ascii.txt").write_bytes(b"LAB23_MARKER training_context")
(p/"wide.bin").write_bytes("LAB23_MARKER training_context".encode("utf-16le"))
(p/"negative.txt").write_bytes(b"ordinary benign training file")
print("Created 3 safe test files")
