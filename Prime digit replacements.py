# coding = utf-8
import itertools
import math
from datetime import datetime


def is_prime(n):
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor += 2
    return True


def to_num(n):
    return reduce(lambda x, y: x*10 + y, map(int, n))


def count_prime(n, l):
    count = 0
    for i in '0123456789':
        for j in l:
            n[j] = i
        if n[0] == '0':
            continue
        if is_prime(to_num(n)):
            count += 1
    if count >= 8:
        return True
    return False


def template_test(n):
    strlist = list(str(n))
    for mask in itertools.combinations(range(len(strlist)-1), 3):
        if strlist[mask[0]] == strlist[mask[1]] and strlist[mask[1]] == strlist[mask[2]]:
            if count_prime(strlist, mask):
                return True
    return False


num = 1000
while True:
    if not is_prime(num):
        pass
    elif not (list(str(num)).count('0') >= 3 or list(str(num)).count('1') >= 3 or list(str(num)).count('2') >= 3):
        pass
    elif not num % 10 in [1, 3, 7, 9]:
        pass
    elif template_test(num):
        print num
        break
    num += 1
