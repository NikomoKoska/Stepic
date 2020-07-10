import simplecrypt as sc

pwd = []
with open('passwords.txt') as f:
    pwd = [s.strip() for s in  f.readlines()]

with open('encrypted.bin', 'rb') as inp:
    secret_data = inp.read()
    for pas in pwd:
        try:
            print('Password = ', pas)
            print('Secret data = ', sc.decrypt(pas, secret_data))
        except:
            pass