# coding = utf-8


with open('grid.txt','r') as grid:
    g_li = grid.read()
    l = [map(int, h.split()) for h in g_li.split('\n')]

index = len(l)
largest_pro = 1
for i in range(20):
    for j in range(20):
        if i + 3 < 20:
            pro = l[i][j] * l[i+1][j] * l[i+2][j] * l[i+3][j]
            if pro > largest_pro:
                largest_pro = pro
        if j + 3 < 20:
            pro = l[i][j] * l[i][j+1] * l[i][j+2] * l[i][j+3]
            if pro > largest_pro:
                largest_pro = pro
        if i + 3 < 20 and j + 3 < 20:
            pro = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3]
            if pro > largest_pro:
                largest_pro = pro
        if i + 3 < 20 and j - 3 > 0:
                pro = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3]
                if pro > largest_pro:
                    largest_pro = pro

print largest_pro
