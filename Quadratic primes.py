# coding = utf-8
import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    p = 2
    while p <= math.sqrt(n):
        if n % p == 0:
            return False
        p += 1
    return True


set_prime = set()
set_non_prime = set()

len_prime = 0

a = -999
prod = 0
while a <= 999:
    b = -1000
    while b <= 1000:
        i = 0
        l = 0
        while True:
            t = i ** 2 + a * i + b
            if t in set_prime:
                i += 1
                l += 1
            if t in set_non_prime:
                break
            if is_prime(t):
                set_prime.add(t)
                i += 1
                l += 1
            else:
                set_non_prime.add(t)
                break
        if l > len_prime:
            len_prime = l
            prod = a * b
        b += 1
    a += 1
print prod
