def add_item(dict, obj):
    name1 = obj['name1']
    name2 = obj['name2']
    init_item(dict, name1)
    init_item(dict, name2)
    if obj['goal1'] > obj['goal2']:
        add_command_date(dict, name1, 'win')
        add_command_date(dict, name2, 'lose')
    elif obj['goal1'] < obj['goal2']:
        add_command_date(dict, name1, 'lose')
        add_command_date(dict, name2, 'win')
    else:
        add_command_date(dict, name1, 'non')
        add_command_date(dict, name2, 'non')

def add_command_date(dict, name, state):
    dict[name]['games'] += 1
    if state == 'win':
        dict[name]['wins'] += 1
        dict[name]['score'] += 3
    elif state == 'non':
        dict[name]['non'] += 1
        dict[name]['score'] += 1
    elif state == 'lose':
        dict[name]['lose'] += 1

def init_item(dict, name):
    if name not in dict:
        dict.update({name: {'games':0, 'wins':0, 'non':0, 'lose':0, 'score':0}})

def processing_list(list, dict):
    for elem in list:
        add_item(dict, elem)

def input_command(num):
    list = []
    for i in range(num):
        text_list = input().split(';')
        obj = {}
        obj['name1'] = text_list[0]
        obj['goal1'] = int(text_list[1])
        obj['name2'] = text_list[2]
        obj['goal2'] = int(text_list[3])
        list.append(obj.copy())
    return list

game_num = int(input())
game_list = input_command(game_num)
dictionary = {}

processing_list(game_list, dictionary)

for key, val in dictionary.items():
    print(key, end=':')
    print(*[score for score in val.values()])

# Красивое решение
# def command(c, res):
#     if not c in dct: dct[c] = [0, 0, 0, 0, 0]
#     dct[c] = [dct[c][0] + 1,
#                 dct[c][1] + 1 if res == 3 else dct[c][1],
#                 dct[c][2] + 1 if res == 1 else dct[c][2],
#                 dct[c][3] + 1 if res == 0 else dct[c][3],
#                 dct[c][4] + res,]
# dct = {}
# for i in range(int(input())):
#     c1, g1, c2, g2 = input().split(';')
#     command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
#     command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
# for c in dct:
#     print('{}:{} {} {} {} {}'.format(c, *dct[c]))