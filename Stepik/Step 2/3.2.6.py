# s = input('s = ')
# a = input('a = ')
# b = input('b = ')


def operations(s: str, a: str, b: str):
    counter = 0
    if s.count(a) == 0:
        return 0
    elif b.count(a) != 0:
        return 'Impossible'
    while counter < 1000 and s.count(a) != 0:
        s = s.replace(a, b)
        counter += 1

    if counter == 1000:
        return 'Impossible'
    else:
        return counter

s = 'abab'
b = 'ba'
a = 'ab'

print(operations(s, a, b))