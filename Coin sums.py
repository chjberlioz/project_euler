# coding = utf-8

t = 200
w = 0
for t200 in range(t / 200 + 1):
    r200 = t - t200 * 200
    if r200 == 0:
        w += 1
        continue
    for t100 in range(r200 / 100 + 1):
        r100 = r200 - t100 * 100
        if r100 == 0:
            w += 1
            continue
        for t50 in range(r100 / 50 + 1):
            r50 = r100 - t50 * 50
            if r50 == 0:
                w += 1
                continue
            for t20 in range(r50 / 20 + 1):
                r20 = r50 - t20 * 20
                if r20 == 0:
                    w += 1
                    continue
                for t10 in range(r20 / 10 + 1):
                    r10 = r20 - t10 * 10
                    if r10 == 0:
                        w += 1
                        continue
                    for t5 in range(r10 / 5 + 1):
                        r5 = r10 - t5 * 5
                        if r5 == 0:
                            w += 1
                            continue
                        for t2 in range(r5 / 2 + 1):
                            r2 = r5 - t2 * 2
                            if r2 == 0:
                                w += 1
                                continue
                            w += 1
print w