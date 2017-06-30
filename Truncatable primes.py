# coding = utf-8

import math
import itertools


def is_prime(n):
    n = reduce(lambda x, y: 10*x+y, map(int, n))
    if n % 2 == 0 or n == 1:
        return False
    d = 3
    while d <= math.sqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


i = 2
lt_good = set([('2',), ('3',), ('5',), ('7',)])
lt_bad = set([('1',), ('9',)])
rt_good = set([('2',), ('3',), ('5',), ('7',)])
rt_bad = set([('1',), ('9',)])
while 1:
    lflag = 0
    rflag = 0
    for l in itertools.product('123579', repeat=i):
        pflag = 0
        if l[1:] in lt_good:
            if is_prime(l):
                pflag = 1
                lflag = 1
                lt_good.add(l)
            else:
                lt_bad.add(l)
        if l[:-1] in rt_good:
            if pflag == 1 or is_prime(l):
                rflag = 1
                rt_good.add(l)
            else:
                lt_bad.add(l)
    if lflag == 1 and rflag == 1:
        i += 1
    else:
        break

t_good = lt_good & rt_good - set([('2',), ('3',), ('5',), ('7',)])
sum_good = 0
for i in t_good:
    sum_good += reduce(lambda x, y: 10*x+y, map(int, i))
print t_good
print sum_good
