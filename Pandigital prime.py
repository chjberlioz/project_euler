# coding = utf-8
import itertools
import math


def to_num(l):
    return reduce(lambda x, y: 10*x+y, l)


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return False
    m = 3
    while m <= math.sqrt(n):
        if n % m == 0:
            return False
        else:
            m += 2
    return True

large_num = 0
for i in range(1,10):
    for j in itertools.permutations(range(1, i+1), i):
        if to_num(j) > large_num and is_prime(to_num(j)):
            large_num = to_num(j)
print large_num