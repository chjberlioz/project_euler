# coding = utf-8
import itertools


def comp(x, y):
    s_x = str(x)
    s_y = str(y)
    for each in itertools.permutations(s_x):
        s_each = ''.join(each)
        if s_y == s_each:
            return True
    return False


def is_permuted(num):
    for i in range(2, 7):
        if not comp(num, i * num):
            return False
    return True

print comp(125874, 251748)
num = 1
while 1:
    if is_permuted(num):
        break
    else:
        num += 1
print num
