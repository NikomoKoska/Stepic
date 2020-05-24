lst = [int(i) for i in input().split()]
x = int(input())
num_list = []
if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i] == x:
            num_list.append(i)
    print(*num_list)
