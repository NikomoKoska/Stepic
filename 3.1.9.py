def modify_list(list):
    del_list = []
    for i in range(len(list)):
        if list[i] % 2 != 0:
            del_list.append(i)
        else:
            list[i] //= 2
    del_list.reverse()
    for counter in del_list:
        del list[counter]

lst = [1]
print(modify_list(lst))  # None
print(lst)