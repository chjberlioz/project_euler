# coding = utf-8
import math
from datetime import datetime


def is_pentagona(num):
    return int((1+math.sqrt(1+24*num))/6) == (1+math.sqrt(1+24*num))/6


def is_hexagonal(num):
    return int((1+math.sqrt(1+8*num))/4) == (1+math.sqrt(1+8*num))/4


t = lambda n: n*(n+1)/2


def main():
    start = datetime.now()
    index = 286
    while 1:
        if is_hexagonal(t(index)) and is_pentagona(t(index)):
            print t(index)
            break
        index += 1
    runtime = datetime.now() - start
    print runtime.microseconds

if __name__ == '__main__':
    main()