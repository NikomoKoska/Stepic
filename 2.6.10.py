new_str = input()
matrix = []
while new_str != 'end':
    matrix.append([int(i) for i in new_str.split()])
    new_str = input()
len_i = len(matrix)
for i in range(len_i):

    for j in range(len(matrix[i])):
        sum = matrix[i-1][j] + matrix[i+1-len_i][j] + matrix[i][j-1] + matrix[i][j+1-len(matrix[i])]
        print(sum, end=' ')
    print()

