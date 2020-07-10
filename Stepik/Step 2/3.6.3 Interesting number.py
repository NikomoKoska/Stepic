import requests as r

with open('numbers.txt') as f:
    adress = 'http://numbersapi.com/'
    params = {
        'json': True
    }
    numbers = f.readlines()
    for number in numbers:
        number = number.strip()
        api = f'{adress}{number}/math'
        res = r.get(api, params=params)
        ans = res.json()

        # print(number)
        if ans['found']:
            print('Interesting')
        else:
            print('Boring')
