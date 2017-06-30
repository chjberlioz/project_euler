# coding = utf-8
import math
import itertools


def is_prime(n):
    if n % 2 == 0 or n == 1:
        return False
    d = 3
    while d <= math.sqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True

already_test = set()
prime_set = set()
for i in range(2, 7):
    for j in itertools.combinations_with_replacement('1379', i):
        for k in itertools.permutations(j):
            if not (k in already_test):
                flag = 1
                for l in range(i):
                    nk = k[l:]+k[:l]
                    already_test.add(nk)
                    num_nk = reduce(lambda x, y: 10*x+y, map(int, nk))
                    if not is_prime(num_nk):
                        flag = 0
                if flag == 1:
                    for l in range(i):
                        nk = k[l:] + k[:l]
                        prime_set.add(nk)
print len(prime_set)+4


