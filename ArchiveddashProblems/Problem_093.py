from time import time
from itertools import combinations, product, permutations

t1 = time()
iterable = list(combinations(range(1, 10), r=4))

iter_sym = tuple(product(["*", "+", "-", "/"], repeat=3))
p = []
dic = {}
for k in iterable:
    o = list(permutations(k))
    l = set()
    for i in o:
        for s in iter_sym:
            try:
                do1 = eval(f"({i[0]}{s[0]}{i[1]}){s[1]}{i[2]}{s[2]}{i[3]}")
            except:
                pass
            try:
                do2 = eval(f"({i[0]}{s[0]}{i[1]}{s[1]}{i[2]}){s[2]}{i[3]}")
            except:
                pass
            try:
                do3 = eval(f"({i[0]}{s[0]}{i[1]}){s[1]}({i[2]}{s[2]}{i[3]})")
            except:
                pass
            try:
                do4 = eval(f"{i[0]}{s[0]}{i[1]}{s[1]}{i[2]}{s[2]}{i[3]}")
            except:
                pass
            l.add(int(do1)) if do1 > 0 and do1 == int(do1) else 10000
            l.add(int(do2)) if do2 > 0 and do2 == int(do2) else 10000
            l.add(int(do3)) if do3 > 0 and do3 == int(do3) else 10000
            l.add(int(do4)) if do4 > 0 and do4 == int(do4) else 10000
    p.append(tuple(sorted(l)))
    dic[tuple(sorted(l))] = k

high = 0
k = 0
for ele in p:
    start = 1
    while ele[start - 1] == start:
        start += 1
    if high < start:
        high = start
        k = ele

print(
    f"Answer: {sum(i * (10 ** (3 - index)) for index, i in enumerate(dic[k]))},\nTime Taken: {time() - t1}"
)
