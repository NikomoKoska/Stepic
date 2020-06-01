alf1 = input()
alf2 = input()
code1 = input()
code2 = input()

voc1 = {}
voc2 = {}

for i in range(len(alf1)):
    voc1[alf1[i]] = alf2[i]
    voc2[alf2[i]] = alf1[i]

str1 = ''
str2 = ''

for c in code1:
    str1 += voc1[c]

for c in code2:
    str2 += voc2[c]

print(str1)
print(str2)

