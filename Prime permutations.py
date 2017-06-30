# coding = utf-8
from datetime import datetime
import math
import itertools


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p <= math.sqrt(n):
        if n % p == 0:
            return False
        p += 2
    return True


def str_to_num(s):
    return reduce(lambda x, y: 10 * x + y, map(int, s))

primes = []
for num in range(1001, 10000, 2):
    if is_prime(num):
        primes.append(num)

for prime in primes:
    prime_set = set()

    for str_p in itertools.permutations(str(prime)):
        num_p = str_to_num(str_p)
        if num_p in primes:
            prime_set.add(num_p)
            primes.remove(num_p)
    if len(prime_set) >= 3:
        for num_list in itertools.combinations(prime_set, 3):
            if sum(num_list) == 3 * num_list[0] or sum(num_list) == 3 * num_list[1] or sum(num_list) == 3 * num_list[2]:
                print num_list
