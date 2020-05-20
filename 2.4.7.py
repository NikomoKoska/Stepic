# num = 1
# prev_symbol = ''

# for c in str:
#     if c == prev_symbol:
#         num += 1
#     else
#         result_string += c
#     prev_symbol = c
input_string = input('Enter string ')
result_string = ''

start_num = 0
end_num = 0
num = 1

for i in range(len(input_string)):
    if str[start_num] == str[end_num]:
        result_string += str[start_num] + str(num)
        start_num = i
    else:
        num = 1
    end_num = i

print(result_string)

# str = 'a'
# print(str[0:])