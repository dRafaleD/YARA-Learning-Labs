from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
for name, size in {"small.bin": 512, "target.bin": 2048, "large.bin": 8192}.items():
    (p/name).write_bytes(b"LAB42" + b"A" * (size - 5))
print("Prepared harmless samples")
