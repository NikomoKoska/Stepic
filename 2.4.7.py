# num = 1
# prev_symbol = ''

# for c in str:
#     if c == prev_symbol:
#         num += 1
#     else
#         result_string += c
#     prev_symbol = c
input_string = input('Enter string ')
str_len = len(input_string)
result_string = ''

start_num = 0
num = 1

for i in range(str_len+1):
    for j in input_string[i+1:]:
        

    # end_num = start_num + 1
    # if start_num + 1 >= str_len:
    #     end_num = start_num

    # if input_string[start_num] == input_string[end_num:end_num]:
    #     num += 1
    # else:
    #     result_string += input_string[start_num] + str(num)
    #     num = 1
    # start_num = i


print(result_string)

# str = 'a'
# print(str[0:])