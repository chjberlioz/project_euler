# coding = utf-8
sum_count = 0
for i in range(1000000):
    i2 = bin(i)[2:]
    if str(i) == str(i)[::-1] and i2 == i2[::-1]:
        sum_count += i
print sum_count
