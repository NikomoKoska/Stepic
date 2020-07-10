import requests as r

def return_url(file_adress):
    with open(file_adress) as f:
        url = f.readline().strip()
        return url

def get_text_file(url):
    response = r.get(url)
    if response.status_code == 200:
        return response.text

def numbers_of_lines(text):
    lines = text.splitlines()
    return len(lines)

adress = 'D:\Code\Python\Education\Stepic\Examples\dataset_for_3.6.2.txt'
url = return_url(adress)
text = get_text_file(url)
print(numbers_of_lines(text))
