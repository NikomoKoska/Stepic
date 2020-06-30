def primes():
    n = 2

    while True:
        isSimple = True
        d = n - 1
        while d > 1:
            if n % d == 0:
                isSimple = False
                break
            d -= 1

        if isSimple:
            yield n
        n += 1

# Correct
# def primes():
#     i = 2
#     while True:
#         is_prime = True
#         divisor = 2
#         while divisor ** 2 <= i:
#             if i % divisor == 0:
#                 is_prime = False # non-trivial divisor
#                 break
#
#             divisor += 1
#
#         if is_prime:
#             yield i
#
#         i += 1

print(primes())
print(primes())
print(primes())
print(primes())
print(primes())
print(primes())