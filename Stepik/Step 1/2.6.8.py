num = int(input())
counter = 0
for i in range(1, num + 1):
    j = 0
    while counter < num:
        if j == i:
            break
        j += 1
        print(i, end=' ')
        counter += 1

def dont_understend(n):
    count = 0
    curr = 1
    for i in range(n):
        print(curr, end=' ')
        count += 1
        if count == curr:
            curr += 1
            count = 0

dont_understend(num)