from pathlib import Path
p=Path(__file__).parent/"samples";p.mkdir(exist_ok=True)
cases={"positive.txt":"YL21SECTION=LAB\nVERSION=1\nOK\n","late-header.txt":"xxYL21SECTION=LAB\nVERSION=1\nOK\n","missing-marker.txt":"YL21VERSION=1\nExtra content that exceeds min size\n","truncated.txt":"YL21"}
for name,content in cases.items():(p/name).write_text(content,encoding="utf-8")
print("Generated",len(cases),"synthetic files")
