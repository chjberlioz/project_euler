# coding = utf-8

import re
import itertools
import math
s = 0
for i in range(2, 9):
    for j in itertools.combinations_with_replacement('1234567890', i):
        num = reduce(lambda x, y: x + y, map(math.factorial, map(int, j)))
        if sorted(list(j)) == sorted(re.findall(r'\d', str(num))):
            s += num
print s
