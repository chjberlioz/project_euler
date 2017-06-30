# coding = utf-8
import math
from datetime import datetime


def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    if n == 2:
        return True
    p = 3
    while p <= math.sqrt(n):
        if n % p == 0:
            return False
        p += 2
    return True


def is_square(n):
    return int(math.sqrt(n)) == math.sqrt(n)


def main():
    start = datetime.now()
    primes = [3, 5, 7]
    start_num = 9
    while 1:
        flag = 0
        if is_prime(start_num):
            primes.append(start_num)
            start_num += 2
            continue
        for p in primes:
            if is_square((start_num-p)/2):
                start_num += 2
                flag = 1
                break
        if flag == 0:
            print start_num
            break
    runtime = datetime.now() - start
    print runtime.microseconds

if __name__ == '__main__':
    main()
