# coding = utf-8

longest_seq = 0
longest_num = 1
s = set()

for i in range(1, 1000000):
    if not (i in s):
        len_seq = 1
        s.add(i)
        num = i
        while i != 1:
            if i % 2 == 0:
                i /= 2
                s.add(i)
                len_seq += 1
            else:
                i = 3 * i + 1
                s.add(i)
                len_seq += 1
            if len_seq > longest_seq:
                longest_num = num
                longest_seq = len_seq

print longest_num