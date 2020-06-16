import datetime
date = datetime.date(*[int(s) for s in input().split()])
days = int(input())

delta = datetime.timedelta(days)
result_date = date + delta
print(result_date.year, result_date.month, result_date.day)