#!/usr/bin/env python3
"""Generate harmless, deterministic binary fixtures for YARA entropy exercises."""
from collections import Counter
from hashlib import sha256
from math import log2
from pathlib import Path

BASE = Path(__file__).resolve().parent
SAMPLES = BASE / "samples"
SAMPLES.mkdir(exist_ok=True)

MARKER = b"LAB19_DEMO"
PREFIX = MARKER + bytes(256 - len(MARKER))
LOW = b"A" * 4096
# Deterministic pseudorandom-looking bytes; NOT a key or cryptographic secret.
HIGH = b"".join(sha256(i.to_bytes(4, "little")).digest() for i in range(128))

FILES = {
    "low-entropy.bin": PREFIX + LOW,
    "high-entropy.bin": PREFIX + HIGH,
    "mixed-entropy.bin": PREFIX + LOW + HIGH,
}


def entropy(data: bytes) -> float:
    """Shannon entropy (bits per byte) for a finite byte sample."""
    if not data:
        return 0.0
    frequencies = Counter(data)
    total = len(data)
    return -sum((count / total) * log2(count / total)
                for count in frequencies.values())


for name, content in FILES.items():
    (SAMPLES / name).write_bytes(content)
    first = entropy(content[256:4352])
    second = entropy(content[4352:8448]) if len(content) >= 8448 else None
    second_str = f"{second:.3f}" if second is not None else "N/A"
    print(f"{name:19} size={len(content):5} "
          f"window1={first:.3f} window2={second_str}")
