input_numbers = [int(i) for i in input().split()]
input_len = len(input_numbers)

if input_len == 1:
    print(input_numbers[0])
else:
    for i in range(input_len):
        end_num = i + 1
        if i == input_len - 1:
            end_num = 0
        sum = input_numbers[i-1] + input_numbers[end_num]
        print(sum, end= ' ')