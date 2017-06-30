# coding = utf-8
import math


def is_prime(n):
    if n % 2 == 0:
        return False
    m = 3
    while m <= math.sqrt(n):
        if n % m == 0:
            return False
        else:
            m += 2
    return True

n = 2000000
sum_primes = 2

p = 3
while p <= n:
    if is_prime(p):
        sum_primes += p
    p += 2

print sum_primes