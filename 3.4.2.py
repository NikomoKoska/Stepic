import os

def uncode_string(str):
    str_len = len(str)
    result = ''
    symbol = ''
    num = 0
    for i in range(str_len):
        isEnd = i == (str_len - 1) and str[i].isdigit() and symbol != ''
        isDigit = str[i].isdigit()
        isAlpha = str[i].isalpha()

        if num != 0 and symbol != '' and isAlpha: # Вывод и обнуление локальных счётчиков
            result += symbol * num
            symbol = ''
            num = 0

        if num == 0 and isDigit: # Когда мы первый раз попадаем на число
            num = int(str[i])
        elif num != 0 and isDigit: # Когда число дву- или более значное
            num *= 10
            num += int(str[i])
        elif isAlpha: # Когда встречаем символ, тут же пишем его в память
            symbol = str[i]

        if isEnd: # Если это последний элемент, то у нас полюбас должны быть заполнены локальные значения
            result += symbol * num


    return result

directory = input()

with open(directory) as file:
    str = file.readline()
    print(uncode_string(str))
