# coding = utf-8
p = 0
for a in range(1000):
    for b in range(a, 1000):
        if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
            p = a * b * (1000 - a - b)
            break
    if p != 0:
        break

print p