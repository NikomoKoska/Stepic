str = input()

list_str = str.lower().split()
set_str = set(str.lower().split())

def print_count(set):
    for symbol in set:
        print(symbol, list_str.count(symbol))

print_count(set_str)