from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"positive.txt").write_text("LAB29_HEADER\nEVENT\nEVENT\n")
(p/"negative.txt").write_text("LAB29_HEADER\nEVENT\n")
print("Prepared harmless samples")
