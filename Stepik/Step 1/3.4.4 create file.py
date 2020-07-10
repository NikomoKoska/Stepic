directory = input('Enter full path to file:')

with open(directory) as f:
    rows = f.readlines()
    result_list = ([(int(math) + int(phys) + int(rus)) / 3 for fam, math, phys, rus in [str.strip().split(';') for str in rows]])
    avg_arr = [sum(int(math) for fam, math, phys, rus in [str.strip().split(';') for str in rows]) / len(rows), \
               sum(int(phys) for fam, math, phys, rus in [str.strip().split(';') for str in rows]) / len(rows), \
               sum(int(rus) for fam, math, phys, rus in [str.strip().split(';') for str in rows]) / len(rows)]

with open('answer_3.4.4.txt', 'w') as f:
    for row in result_list:
        f.write(str(row)+'\n')
    f.write(str(avg_arr[0]) + ' ' + str(avg_arr[1]) + ' '+ str(avg_arr[2]))