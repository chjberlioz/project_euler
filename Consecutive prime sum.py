# coding = utf-8
import math
from datetime import datetime

start = datetime.now()
primes = [2, 3, 5, 7]
max_num = 1000000
for num in range(11, max_num, 2):
    for p in primes:
        if p <= math.sqrt(num):
            if num % p == 0:
                break
        if p > math.sqrt(num):
            primes.append(num)
            break

step = 1
low = 0
high = 0
s = 0
for first in range(len(primes)):
    for last in range(first+step, len(primes)):
        if sum(primes[first: last]) in primes:
            low = first
            high = last
            s = last - first
        if sum(primes[first: last]) >= max_num:
            break
    step = s
print sum(primes[low: high])
runtime = datetime.now() - start
print runtime
