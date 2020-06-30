
class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # Сразу обрабатываем всю последовательность и уже готовый результат передаём в итератор
        self.result_list = []
        for elem in iterable:
            pos = 0
            neg = 0
            for func in funcs:
                if func(elem):
                    pos += 1
                else:
                    neg += 1
            if judge(pos, neg):
                self.result_list.append(elem)

    def __iter__(self):
        for elem in self.result_list:
            yield elem

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))

# Test iterator
# class MyIterator:
#     def __init__(self, iterable):
#         self.index = 0
#         self.iterable = iterable
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             return self.iterable[self.index]
#         raise StopIteration
#
# class MyList:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __iter__(self):
#         return MyIterator(self.lst)

# Correct 

# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg

#     def judge_any(pos, neg):
#         return pos > 0

#     def judge_all(pos, neg):
#         return neg == 0

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterator = iter(iterable)
#         self.funcs = funcs
#         self.judge = judge

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while (True):
#             elem = next(self.iterator)
#             pos, neg = 0, 0
#             for func in self.funcs:
#                 if func(elem):
#                     pos += 1
#                 else:
#                     neg += 1

#             if self.judge(pos, neg):
#                 return elem