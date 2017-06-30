# coding = utf-8
start = 335
sum_day = 0
for year in range(1901, 2001):
    for month in range(1,13):
        if month in (1, 2, 4, 6, 8, 9, 11):
            start += 31
            if start % 7 == 0:
                sum_day += 1
        if month in (5, 7, 10, 12):
            start += 30
            if start % 7 == 0:
                sum_day += 1
        if month == 3:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 ==  0:
                start += 29
            else:
                start += 28
            if start % 7 == 0:
                sum_day += 1

print sum_day