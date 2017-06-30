# coding = utf-8

Fi = 1
Fj = 1
Fk = 2
k = 3
while Fk < 10 ** 999:
    Fi = Fk
    Fk += Fj
    Fj = Fi
    k += 1
print k