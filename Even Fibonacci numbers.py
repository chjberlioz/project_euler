# coding = utf-8

maxnum = 4000000
sumnum = 2
n1 = 2
n2 = 8
while n2 <= maxnum:
    sumnum += n2
    n1, n2 = n2, 4 * n2 + n1
print sumnum
