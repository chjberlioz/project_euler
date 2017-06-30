# coding = utf-8
import itertools


def to_num(l):
    return reduce(lambda x, y: x*10+y, l)

s = 0
p = [2, 3, 5, 7, 11, 13, 17]

for i in itertools.permutations(range(10), 10):
    if i[0] != 0:
        flag = 1
        for j in range(1, 8):
            if to_num(i[j: j+3]) % p[j-1] != 0:
                flag = 0
                break
        if flag == 1:
            s += to_num(i)

print s
