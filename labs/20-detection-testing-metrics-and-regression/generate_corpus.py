#!/usr/bin/env python3
"""Generate labeled, harmless positive and negative samples."""
from pathlib import Path
import json

base = Path(__file__).resolve().parent
samples = base / "samples"
samples.mkdir(exist_ok=True)
data = {
    "positive-01.txt": (True, "LAB20_SIGNAL\ncomponent=widget\nmode=active\n"),
    "positive-02.txt": (True, "component=widget\nmode=active\nLAB20_SIGNAL\nbuild=2\n"),
    "positive-03.txt": (True, "LAB20_SIGNAL\nnotes=harmless\nmode=active\ncomponent=widget\n"),
    "negative-marker.txt": (False, "LAB20_SIGNAL\nordinary document about a marker\n"),
    "negative-component.txt": (False, "component=widget\nmode=active\nno family marker\n"),
    "negative-mode.txt": (False, "LAB20_SIGNAL\ncomponent=widget\nmode=inactive\n"),
    "negative-unrelated.txt": (False, "normal benign application text\n"),
    "negative-mentions-marker.txt": (False, "This is a harmless note: LAB20_SIGNAL is a training name.\n"),
}
for name,(positive,text) in data.items():
    (samples/name).write_text(text,encoding="utf-8")
(base/"labels.json").write_text(
    json.dumps({name:positive for name,(positive,_) in data.items()},indent=2)+"\n",
    encoding="utf-8")
print("Generated",len(data),"labeled, harmless samples.")
