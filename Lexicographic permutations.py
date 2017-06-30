# coding = utf-8

from itertools import permutations

l = [map(str, i) for i in list(permutations(range(10), 10))]
ll = [''.join(i) for i in l]
ll.sort()
print ll[999999]