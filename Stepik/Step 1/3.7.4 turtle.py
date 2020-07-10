n = int(input())
struct ={'север':0, "запад":0, "юг":0, "восток":0}
for i in range(n):
    str = input().lower().split()
    struct[str[0]] += int(str[1]) # str[0] - направление, str[1] - расстояние

print(struct["восток"] - struct["запад"], struct["север"] - struct['юг'])