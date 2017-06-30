# coding = utf-8
import itertools


def to_num(l):
    return reduce(lambda x, y: x*10+y, map(int, l))
large_num = 0
for i in range(1, 5):
    for j in itertools.permutations('123456789', i):
        num = to_num(j)
        s = set('123456789')
        digit = []
        d = 1
        flag = 1
        while set(digit) != s:
            if set(digit) & set(str(num*d)):
                flag = 0
                break
            digit.extend(list(str(num*d)))
            d += 1
        if flag == 1 and to_num(digit) > large_num:
            large_num = to_num(digit)
print large_num