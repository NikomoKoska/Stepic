import requests as r

def get_text_from_url(url):
    response = r.get(url)
    if response.status_code == 200:
        return response.text.strip()

def text_is_url(text):
    list = text.split()
    if list[0] == 'We':
        return False
    else:
        return True

main_adress = 'https://stepic.org/media/attachments/course67/3.6.3/'
file_name = ''

with open('filename_for_3.6.3.txt') as f:
    file_name = f.readline().strip()

local_adress = file_name
result = ''
counter = 1
while True:
    text = get_text_from_url(local_adress)
    if not text_is_url(text):
        result = text
        break
    print('File number:', counter, 'Name:', local_adress, 'Content:', text)
    local_adress = main_adress + text
    counter += 1

print(result)