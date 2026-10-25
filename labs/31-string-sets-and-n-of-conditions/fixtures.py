from pathlib import Path
p=Path("samples");p.mkdir(exist_ok=True)
(p/"two_of_three.txt").write_text("LAB31_ALPHA\nLAB31_BETA\n")
(p/"one_of_three.txt").write_text("LAB31_ALPHA\n")
(p/"all_three.txt").write_text("LAB31_ALPHA\nLAB31_BETA\nLAB31_GAMMA\n")
print("Prepared harmless samples")
