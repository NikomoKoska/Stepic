lst = [int(num) for num in input().split()]

# Этот вариант ищет уникальные числа в массиве чисел. А в задании требовалось иное.
def findUniqNum(lst):
    uniq_lst = []
    for num in lst:
        if num not in uniq_lst:
            uniq_lst.append(num)
    for i in uniq_lst:
        print(i, end=' ')

# пиздец уродство(
lst.sort()
uniq_lst = []
if len(lst) <= 1:
    print()
else:
    i = -1
    for num in lst:
        i += 1
        if num in uniq_lst:
            continue
        if lst[i-1] == num:
            uniq_lst.append(num)
            print(num, end=' ')


# a, b = [int(i) for i in input().split()], []
# for i in a:
#     if a.count(i) > 1 and b.count(i) == 0:
#         b.append(i)
# for i in b:
#     print(i, end=" ")