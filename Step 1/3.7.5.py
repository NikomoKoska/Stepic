with open('dataset_for_3.7.5.tsv') as f:
    f_list = f.readlines()
    jornal_list = [[s for s in str.split('\t')] for str in f_list]

class_list = {}
for i in range(1,12):
    class_list.update({i:{'kol':0, 'sum':0}})

for str in jornal_list:
    class_num = int(str[0])
    degree = int(str[2])

    class_list[class_num]['kol'] += 1
    class_list[class_num]['sum'] += degree

# Обработаем словарик для вывода
for key, val in class_list.items():
    if val['kol'] == 0:
        print(key, '-')
    else:
        print(key, val['sum'] / val['kol'])

