from pathlib import Path
import subprocess
root=Path(__file__).parent
expected={"positive.txt":True,"late-header.txt":False,"missing-marker.txt":False,"truncated.txt":False}
for name,want in expected.items():
 result=subprocess.run(["yara",str(root/"test_rules.yar"),str(root/"samples"/name)],capture_output=True,text=True,check=True)
 got=bool(result.stdout.strip())
 print(name,got,"expected",want)
 assert got==want,name
print("PASS all four fixtures")
