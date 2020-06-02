# n = int(input())
#
# def init_mas(n):
#     mas = [[0 for j in range(n)] for i in range(n)]
#     return mas
#
# main_mas = init_mas(n)
#
# iterator = 1
# start_x = 0
# start_y = 0
# end_x = n - 1
# end_y = n - 1
#
# while True:
#     for val in range(stop_num):
#         main_mas[start_x][val] = iterator
#         iterator += 1
#
#     stop_num -= 1
#
#     for val in range(stop_num):
#         main_mas[val][end_y] = iterator
#         iterator += 1
#

# Сдался. Решение из интернета
n = int(input())
i, j = 0, -1
max_j, max_i = n - 1, n - 1
min_j, min_i = 0, 1
count = 1
mtrx = [[0 for j in range(n)] for i in range(n)]
while True:

    while j < max_j:
        j += 1
        mtrx[i][j] = count
        count += 1
    max_j -= 1
    while i < max_i:
        i += 1
        mtrx[i][j] = count
        count += 1
    max_i -= 1
    while j > min_j:
        j -= 1
        mtrx[i][j] = count
        count += 1
    min_j += 1
    while i > min_i:
        i -= 1
        mtrx[i][j] = count
        count += 1
    min_i += 1

    if j == (n - 1) // 2 and i == n // 2:
        break

print()
print()
for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end=' ')
    print()