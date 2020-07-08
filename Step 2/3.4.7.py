import re
import requests as r

input_link = input()
input_html = r.get(input_link).text
pattern = r'''<a.*href\s*=[\S'"]((https?|ftp):?(//)?)?([^\.\.].*?)['":/]'''
res = re.findall(pattern, input_html)
full_list = [elem[3] for elem in res]
set = set(full_list)
result_list = sorted((list(set)))
print(*result_list, sep='\n')

# http://pastebin.com/raw/7543p0ns for tests