import sys
import re

for line in sys.stdin:
    line = line.rstrip()

    pattern = r'(.*cat.*){2,}'
    match = re.match(pattern, line)
    if match is not None:
        print(match.group())