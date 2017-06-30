# coding = utf-8


def triangular_num(tri_n):
    return tri_n * (tri_n + 1) / 2


def factor_num(num, p):
    f_n = 0
    while num % p == 0:
        f_n += 1
        num /= p
    return num, f_n


def div_num(num):
    d_n = 1
    num, f_2 = factor_num(num, 2)
    d_n *= (f_2 + 1)
    p = 3
    while num != 1:
        num, f_n = factor_num(num, p)
        d_n *= (f_n + 1)
        p += 2
    return d_n


s_n = 1
t_n = triangular_num(s_n)

while div_num(t_n) <= 500:
    s_n += 1
    t_n = triangular_num(s_n)

print triangular_num(s_n)