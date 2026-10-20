from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"positive.txt").write_text("LAB26_HEADER\ncomponent=sample\n")
(p/"negative.txt").write_text("component=sample\n")
print("Generated two harmless fixtures.")
