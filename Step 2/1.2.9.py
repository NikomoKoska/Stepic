objects = [1, 2, 1, 2, 3, True, True, False]
total_list = []
for obj in objects:
    if obj not in total_list:
        total_list.append(obj)
    elif total_list.count(obj) == 1:
        item = total_list[total_list.index(obj)]
        if obj is not item:
            total_list.append(obj)
    else:
        num = total_list.count(obj)
        l = len(total_list)
        for i in range(num):
            elem = total_list[total_list.index(obj, i + 1 - l)]
            if elem is not obj:
                total_list.append(obj)
                break

print(len(total_list))

# Вариант 2
total_set = set()
for obj in objects:
    total_set.add(id(obj))

print(len(total_set))
