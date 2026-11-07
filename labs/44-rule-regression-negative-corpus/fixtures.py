"""Create harmless local fixtures for YARA rule regression."""
from pathlib import Path
out=Path(__file__).parent / "samples"
out.mkdir(exist_ok=True)
for name,text in {
 "positive.txt":"COURSE:ALPHA and COURSE:OMEGA\n",
 "near_miss.txt":"COURSE:ALPHA only\n",
 "negative.txt":"Unrelated training text\n"
}.items():
 (out/name).write_text(text,encoding="utf-8")
print("Synthetic fixtures created.")
