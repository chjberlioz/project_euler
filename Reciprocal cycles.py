# coding = utf-8


def len_cycle_fun(d):
    m = 10
    l = []
    while not (m in l) and m != 0:
        l.append(m)
        m = m % d * 10
    if m == 0:
        return 0
    return len(l) - l.index(m)

len_cycle = 0
digit = 1
for i in range(1, 1000):
    if len_cycle_fun(i) > len_cycle:
        digit = i
        len_cycle = len_cycle_fun(i)
print digit