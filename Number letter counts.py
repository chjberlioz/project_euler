# coding = utf-8

dic_num = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

counts = 0

for i in range(21):
    counts += dic_num[i]

for i in range(21, 100):
    counts += (dic_num[i / 10 * 10] + dic_num[i % 10])

for i in range(100, 1000):
    counts += (dic_num[i / 100] + 7)
    i = i - i / 100 * 100
    if i != 0:
        counts += 3
    if i <= 20:
        counts += dic_num[i]
    else:
        counts += (dic_num[i / 10 * 10] + dic_num[i % 10])

counts += 11
print counts