import base64
from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
marker=b"LAB39_HARMLESS_MARKER"
(p/"b64.txt").write_bytes(base64.b64encode(marker))
(p/"plain.txt").write_bytes(marker)
(p/"unrelated.txt").write_bytes(b"nothing to see here")
print("Prepared harmless samples")
