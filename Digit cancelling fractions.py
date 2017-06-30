# coding = utf-8
import re

for a in range(10, 100):
    for b in range(a+1, 100):
        la = re.findall(r'\d', str(a))
        lb = re.findall(r'\d', str(b))
        sa = set(la)
        sb = set(lb)
        if len(sa & sb) == 1 and not('0' in sa & sb):
            nla = [i for i in la if not (i in (sa & sb))]
            nlb = [i for i in lb if not (i in (sa & sb))]
            if nla and nlb and a*int(nlb[0]) == b*int(nla[0]):
                print a, b
