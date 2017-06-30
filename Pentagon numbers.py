# coding = utf-8
import math


s = [i*(3*i-1)/2 for i in range(1, 3000)]

for i in range(2999):
    for j in range(2998):
        if (s[i]+s[j]) in s and (s[i]+2*s[j]) in s:
            print i
            print j
            break
        if s[i] < s[j+1]-s[j]:
            break
# def seq(n):
#     return n * (3 * n - 1) / 2
#
#
# def is_in_seq(n):
#     return (1 + math.sqrt(1 + 24 * n)) / 6 == int((1 + math.sqrt(1 + 24 * n)) / 6)
#
#
# def is_good(index):
#     n = seq(index)
#     s = 1
#     while 1:
#         if is_in_seq(seq(s)+n) and is_in_seq(2*seq(s)+n):
#             return True
#         if n < seq(s+1)-seq(s):
#             return False
#         s += 1
#
# s_index = 1
# while not (is_good(s_index)):
#     s_index += 1
#
# print seq(s_index)
