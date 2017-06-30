# coding = utf-8

max_num = 1000


def sum_multiples(n):
    sum_num = 0
    for i in range(1, 1000):
        if i % n == 0:
            sum_num += i
    return sum_num

print sum_multiples(3)+sum_multiples(5)-sum_multiples(15)
