import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'.*z...z'
    if re.match(pattern, line):
        print(line)

# Var 2

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"z...z", line):
#         print(line)