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

n = 1
m = 3
while n < 10001:
    if is_prime(m):
        n += 1
    m += 2

print m - 2
