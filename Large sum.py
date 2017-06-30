# coding = utf-8
import re

with open('sum.txt','r') as sum_num:
    numbers = sum_num.read()
    li = map(int, numbers.split())
    s = sum(li)
    print str(s)[:10]
    s10 = re.findall('\d', str(s))
    sf = 0
    for i in range(10):
        sf = sf * 10 + int(s10[i])
    print sf
