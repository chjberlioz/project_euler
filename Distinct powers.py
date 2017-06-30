# coding = utf-8

num_set = set()

for a in range(2, 101):
    for b in range(2, 101):
        num_set.add(a ** b)
print len(num_set)