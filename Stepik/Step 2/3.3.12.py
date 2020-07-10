import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'human'
    line = re.sub(pattern, 'computer', line)
    print(line)