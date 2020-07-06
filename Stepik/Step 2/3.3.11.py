import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(.+)\1\b'
    if re.search(pattern, line):
        print(line)