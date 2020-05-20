str = input()
result_string = ''

start_num = 0
end_num = 0
num = 1

for i in len(str):
    if str[start_num] == str[end_num]:
        result_string += str[start_num] + str(num)
        start_num = i
    else:
        num = 1
    end_num = i

print(result_string)
