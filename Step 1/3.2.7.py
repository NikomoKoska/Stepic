num = int(input())
dictionary = {}
for i in range(num):
    xi = int(input())
    if xi in dictionary:
        print(dictionary[xi])
    else:
        val = f(xi)
        print(val)
        dictionary[xi] = val
