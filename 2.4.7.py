input_string = input()
str_len = len(input_string)
result_string = ''
num = 1

for i in range(str_len):
    symbol = input_string[i]
    if i == str_len - 1:
        result_string += symbol + str(num)
        break

    if symbol == input_string[i + 1]:
        num += 1
    else:
        result_string += symbol + str(num)
        num = 1

print(result_string)

#  решение на курсе

# genome = input()+' '
# s = 0
# n=genome[0]
# for i in genome:
#     if n!=i:
#         print(n + str(s), end = '')
#         s=0
#         n=i
#     s+=1