import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b((\w)(\w))'
    line = re.sub(pattern, r'\3\2', line)
    print(line)