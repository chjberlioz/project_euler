# coding = utf-8


def is_triangle_num(n):
    for i in range(n+1):
        if n == i*(i+1)/2:
            return True
    return False


def to_num(w):
    return sum([ord(i)-64 for i in w])
count = 0
with open('words.txt') as ws:
    words = ws.read()
    wl = [i.strip('"') for i in words.split(',')]
    for i in wl:
        if is_triangle_num(to_num(i)):
            count += 1
print count
