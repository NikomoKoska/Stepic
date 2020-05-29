n = int(input())

def init_mas(n):
    mas = [[0] * n for i in range(n)]
    return mas

main_mas = init_mas(n)

start_x = 0
start_y = 0
edn_x = n - 1
end_y = n - 1
horizontal = True

