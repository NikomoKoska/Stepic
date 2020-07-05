s = input()
t = input()

def find_count(s: str, t: str):
    counter = 0
    for i in range(len(s)):
        if s.startswith(t, i):
            counter += 1
    return counter

print(find_count(s, t))