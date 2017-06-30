# coding = utf-8
import math
max_num = 28124
set_non_abundant_sums = set(range(1, max_num))
set_abundant = set()


def abundant(n):
    sum_factor = 1
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            sum_factor += (i + n / i)
        i += 1
    if int(math.sqrt(n)) == math.sqrt(n):
        sum_factor += math.sqrt(n)
    if sum_factor > n:
        return True
    return False

for i in range(2, max_num):
    if abundant(i):
        set_abundant.add(i)

for i in set_abundant:
    for j in set_abundant:
        if i + j in set_non_abundant_sums:
            set_non_abundant_sums.remove(i + j)
s = 0
for i in set_non_abundant_sums:
    s += i
print s
