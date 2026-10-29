from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"match.txt").write_text("id=LAB34-2026-AB\n")
(p/"near_miss.txt").write_text("id=LAB34-26-AB\n")
(p/"no_marker.txt").write_text("id=OTHER-2026-AB\n")
print("Prepared harmless samples")
