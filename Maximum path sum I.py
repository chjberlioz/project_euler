# coding = utf-8

with open('Maximum path sum I.txt') as tri:
    tri_list = [map(int, i.split()) for i in tri.readlines()]

r = len(tri_list) - 2

while r >= 0:
    for i in range(len(tri_list[r])):
        tri_list[r][i] += max(tri_list[r + 1][i], tri_list[r + 1][i + 1])
    r -= 1
print tri_list[0][0]