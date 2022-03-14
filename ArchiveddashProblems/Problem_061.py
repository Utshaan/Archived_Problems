from time import time
from fpack import (
    if_heptagonal_number,
    if_hexagonal_number,
    if_triangle_number,
    if_pentagonal_number,
    if_octagonal_number,
)


def checkpurity(answers):
    hmm = []
    chn = dict()
    ans = 0
    for ele in answers:
        if ele in list3:
            hmm.append(3)
            chn[3] = int((-1 + (1 + 8 * ele) ** (1 / 2)) / 2)
        if ele in list4:
            hmm.append(4)
            chn[4] = int(ele ** (1 / 2))
        if ele in list5:
            hmm.append(5)
            chn[5] = int((1 + (24 * ele + 1) ** (1 / 2)) / 6)
        if ele in list6:
            hmm.append(6)
            chn[6] = int((1 + (8 * ele + 1) ** (1 / 2)) / 4)
        if ele in list7:
            hmm.append(7)
            chn[7] = int((3 + (9 + 40 * ele) ** (1 / 2)) / 10)
        if ele in list8:
            hmm.append(8)
            chn[8] = int((1 + (1 + 3 * ele) ** (1 / 2)) / 3)
    if len(set(hmm)) == 6:
        l = [str(e)[0] for e in chn.values()]
        # if len(set(l)) == 6:
        return True, chn
        # else: return False
    else:
        return False


t = time()
megset = set()
list3 = set()
list4 = set()
list5 = set()
list6 = set()
list7 = set()
list8 = set()
for s in range(1000, 10000):
    if if_triangle_number(s) and str(s)[2:3] != "0":
        megset.add(s)
        list3.add(s)
    if (s ** (1 / 2)) % 1 == 0 and str(s)[2:3] != "0":
        megset.add(s)
        list4.add(s)
    if if_pentagonal_number(s) and str(s)[2:3] != "0":
        megset.add(s)
        list5.add(s)
    if if_hexagonal_number(s) and str(s)[2:3] != "0":
        megset.add(s)
        list6.add(s)
    if if_heptagonal_number(s) and str(s)[2:3] != "0":
        megset.add(s)
        list7.add(s)
    if if_octagonal_number(s) and str(s)[2:3] != "0":
        megset.add(s)
        list8.add(s)


for a in list8:
    for b in megset:
        if str(b)[:2] == str(a)[-2:] and b != a:
            for c in megset:
                if str(c)[:2] == str(b)[-2:] and c != b and c != a:
                    for d in megset:
                        if str(d)[:2] == str(c)[-2:] and d != c and d != b and d != a:
                            for e in megset:
                                if (
                                    str(e)[:2] == str(d)[-2:]
                                    and e != d
                                    and e != c
                                    and e != b
                                    and e != a
                                ):
                                    for f in megset:
                                        if (
                                            str(f)[:2] == str(e)[-2:]
                                            and f != e
                                            and f != d
                                            and f != c
                                            and f != b
                                            and f != a
                                            and str(a)[:2] == str(f)[-2:]
                                        ):
                                            loc = [a, b, c, d, e, f]
                                            if checkpurity(loc):
                                                print(
                                                    checkpurity(loc),
                                                    loc,
                                                    sum(loc),
                                                    time() - t,
                                                )
