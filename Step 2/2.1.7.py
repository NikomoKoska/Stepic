
# Функция поиска значения в графе
def search_child(graph, child, parent, ):
    if child == parent:
        return True

    searched = []
    search_list = deque()
    search_list += graph[child]
    while search_list:
        next_parent = search_list.popleft()
        if next_parent not in searched:
            if next_parent == parent:
                return True
            else:
                search_list += graph[next_parent]
                searched.append(next_parent)
    return False

# Ввод начальных данных
num = int(input())
graph = {}
for _ in range(num):
    all_str = input().split()
    if len(all_str) == 1: # Если ввели только один класс, то родители - пустой массив
        graph[all_str[0]] = []
    else: # Ввели родителя и предков через :
        child = all_str[0]
        parents = all_str[2:] # 0 - ребёнок, 1 - разделитель :, а начиная с 2 - предки
        graph[child] = parents

# Ввод данных для поиска и сам поиск предка
num = int(input())
exception_list = []
for _ in range(num):
    next_exception = input().split()
    if search_child(graph, child, parent):
        print('Yes')
    else:
        print('No')
