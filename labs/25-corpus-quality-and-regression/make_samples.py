from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"positive.txt").write_text("LAB25_DOCUMENT\ncomponent=parser\nversion=5\n")
(p/"near_miss.txt").write_text("LAB25_DOCUMENT\ncomponent=parser\n")
(p/"benign.txt").write_text("ordinary harmless text\n")
print("Created three fixtures")
