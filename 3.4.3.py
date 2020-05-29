directory = input('Inpute full path to the file:')

with open(directory) as file:
    list = [] # Здесь будет список всех слов, которые встречаются в файле
    while True:
        str = file.readline().strip().lower()
        if len(str) == 0:
            break
        list += str.split()
    set_list = set(list)

    min_word = 'z'
    num = 0
    for word in set_list:
        count_word = list.count(word)
        if count_word > num:
            min_word = word
            num = count_word
        elif count_word == num:
            if word < min_word:
                min_word = word
    print(min_word, num)
