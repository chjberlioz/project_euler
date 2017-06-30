# coding = utf-8

def is_right(n):
    count = 0
    for a in range(1, n/2):
        for b in range(a, n/2):
            c = n - a - b
            if c <= b:
                break
            if a**2+b**2 == c**2:
                count += 1
    return count
large_value = 0
max_solution = 0
for i in range(1, 1001):
    if is_right(i) >= max_solution:
        max_solution = is_right(i)
        large_value = i
print large_value
