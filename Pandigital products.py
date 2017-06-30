# coding = utf-8

import itertools
s = 0
ss = set()
for equ in itertools.permutations('123456789', 9):
    for (i, j) in [(1, 5), (2, 5)]:
        x = reduce(lambda x, y: 10*x+y, map(int, equ[:i]))
        y = reduce(lambda x, y: 10*x+y, map(int, equ[i:j]))
        z = reduce(lambda x, y: 10*x+y, map(int, equ[j:]))
        if x*y == z and not (z in ss):
            s += z
            ss.add(z)
print s