print max([sum(map(int,list(str(a**b)))) for a in range(1, 100) for b in range(1, 100)])