lst = []
while True:
    input_num = int(input())
    lst.append(input_num)
    if sum(lst) == 0:
        break
num_sum = 0
for i in lst:
    num_sum += i * i
print(num_sum)