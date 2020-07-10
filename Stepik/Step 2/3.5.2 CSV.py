import csv
from datetime import datetime as d

path = 'D:\Code\Python\Education\Stepic\Examples\Step 2\Crimes.csv'
crimes = {}
with open(path, 'r') as f:
    reader_list = csv.reader(f)
    # Пропускаем первую строку с шапкой
    next(reader_list)
    for str in reader_list:
        if str[2][6:10] != '2015': # str[2][6:10] - year
            continue

        if str[5] in crimes: # str[6] - Primary Type
            crimes[str[5]] += 1
        else:
            crimes[str[5]] = 1

f.close()
max_key = max(crimes, key=lambda x: crimes[x])
print(max_key)

# Right answer
# with open("Crimes.csv") as fi:
#     reader = csv.reader(fi)
#     next(reader)
#     crime_cnt = dict()
#     for row in reader:
#         year = row[2][6:10]
#         if year == "2015":
#             crime_type = row[5]
#             if crime_type not in crime_cnt:
#                 crime_cnt[crime_type] = 0
#             crime_cnt[crime_type] += 1
#
# a = list(map(lambda x: (crime_cnt[x], x), crime_cnt))
# a.sort(key=lambda x: -x[0])
#
# print(a[0][1])
