import os

directories = set()

for current_dir, dirs, files in os.walk('main'):
    for file in files:
        if '.py' in file:
            directories.add(current_dir.strip())
            print(current_dir)

lst = list(directories)
lst.sort()
with open('2.4.6 answer.txt', 'w') as f:
    f.writelines('\n'.join(lst))