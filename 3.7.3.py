num = int(input())
vocabulary = {}
for i in range(num):
    word = input().lower()
    vocabulary[word] = word

l = int(input())
mistakes = {}
for i in range(l):
    str = input().lower().split()
    for word in str:
        if word not in vocabulary:
            mistakes[word] = word

print(*mistakes, sep='\n')
