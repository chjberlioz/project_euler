# coding = utf-8

import re
import itertools

sum_num = 0
for i in range(2, 7):
    for j in itertools.combinations_with_replacement('0123456789', i):
        if sorted(list(j)) == sorted(re.findall(r'\d', str(reduce(lambda x, y: x + y, map(lambda x: x ** 5, map(int, j)))))):
            sum_num += reduce(lambda x, y: x + y, map(lambda x: x ** 5, map(int, j)))
print sum_num
