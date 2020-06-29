import webvtt
import sys

try:
    filename = sys.argv[1]
except:
    print("vtt2txt.py FILENAME")
    sys.exit()

vtt = webvtt.read(filename)
transcript = ""

lines = []
for line in vtt:
    lines.extend(line.text.strip().splitlines())

previous = None
for line in lines:
    if line == previous:
       continue
    transcript += " " + line + "\n"
    previous = line

print(transcript)
