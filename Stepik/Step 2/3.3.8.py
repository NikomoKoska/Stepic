import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'.*\bcat\b'
    match = re.match(pattern, line)
    # print(match)
    if match is not None:
        print(line)