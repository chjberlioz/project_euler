# coding = utf-8

with open('names.txt') as name:
    name_list = [i.strip('"') for i in name.read().split(',')]
scores = 0


def re_ord(c):
    return ord(c) - 64

name_list = sorted(name_list)
for index, each_name in enumerate(name_list):
    print index+1, map(re_ord, each_name)
    scores += ((index + 1) * sum(map(re_ord, each_name)))
print scores
