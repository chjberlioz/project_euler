# coding = utf-8
import math


def sum_divisors(n):
    sum_d = 1
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            sum_d += (i + n / i)
        i += 1
    if int(math.sqrt(n)) == math.sqrt(n):
        sum_d += math.sqrt(n)
    return sum_d

num_set = set()
sum_amicable = 0
for i in range(2, 10000):
    if not (i in num_set):
        num_set.add(i)
        s1 = i
        s2 = sum_divisors(s1)
        s3 = sum_divisors(s2)
        while (not (s2 in num_set)) and s2 < 10000 and s2 > 1:
            num_set.add(s2)
            if s1 == s3:
                sum_amicable += (s1 + s2)
            s1 = s2
            s2 = s3
            s3 = sum_divisors(s2)

print sum_amicable
