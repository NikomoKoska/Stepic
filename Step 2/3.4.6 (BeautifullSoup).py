import requests as r
# Stepik doesnt have BeautifulSoup
# from bs4 import BeautifulSoup
import re

A = input()
B = input()

# def find_links_in_page(page):
#     result = []
#     soup = BeautifulSoup(page.text, 'html.parser')
#     for link in soup.find_all('a'):
#         result.append(link.get('href'))
#     return result
#
# page = r.get(A)
# links = find_links_in_page(page)
# flag = False
# for link in links:
#     links2 = find_links_in_page(r.get(link))
#     if B in links2:
#         print('Yes')
#         flag = True
#         break
#
# if not flag:
#     print('No')

# lets use regular expression
def find_all_href(page):
    pattern = r'''href=['"](.*)['"]'''
    all = re.findall(pattern, page)
    list = [re.sub(pattern, r'\1', href) for href in all]
    return list

page1 = r.get(A)
links = find_all_href(page1.text)
list2 = []
for link in links:
    list2 += find_all_href(r.get(link).text)

if B in list2:
    print('Yes')
else:
    print('No')