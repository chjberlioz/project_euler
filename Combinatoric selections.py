# coding = utf-8


counter = 0
for n in range(23, 101):
    d = n
    r = 1
    while d < 1000000 and r <= int(n / 2):
        d = d * (n - r) / (r + 1)
        r += 1
    counter += n - 2 * r + 1
    print counter