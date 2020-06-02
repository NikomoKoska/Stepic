s = 'abcdefghijk'
mas = []
mas.append(s[3:6])
mas.append(s[:6])
mas.append(s[3:])
mas.append(s[::-1])
mas.append(s[-3:])
mas.append(s[:-6])
mas.append(s[-1:-10:-2])

for i in mas:
    print('s' + str(mas.index(i)) + ' =', i)