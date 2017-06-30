# coding = utf-8

sum_spiral = 1
num = 1
i = 2
while i <= 1001:
    if i % 2 == 0:
        sum_spiral += 2 * num + 3 * i
        num += 2 * i
    else:
        sum_spiral += 2 * num + 3 * (i - 1)
        num += 2 * (i - 1)
    i += 1
print sum_spiral
