# coding = utf-8
import math
from datetime import datetime


def main():
    start = datetime.now()
    primes = [2, 3, 5, 7]
    start_num = 9
    flag = 0
    while flag != 4:
        factor_num = 0
        for p in primes:
            if start_num % p == 0:
                factor_num += 1
            if factor_num > 4:
                start_num += 1
                flag = 0
                break
        if factor_num == 0:
            primes.append(start_num)
            flag = 0
            start_num += 1
            continue
        if factor_num == 4:
            flag += 1
            start_num += 1
        if factor_num < 4:
            flag = 0
            start_num += 1
    print start_num-4
    runtime = datetime.now() - start
    print runtime

if __name__ == '__main__':
    main()
