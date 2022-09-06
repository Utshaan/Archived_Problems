from fpack import primelist_till_x, divide_primecheck
from time import time

t1 = time()
x = primelist_till_x(1000000)
primes = [i for i in x if i > 10**4]


def repeat(b):
    a = str(b)
    seto = set(a)
    listo = list(a)
    multi = dict()
    for i in seto:
        multi[i] = listo.count(i)
    return multi


def reverse_dict(x):
    s = dict(map(reversed, x))
    return s


superi = []
ans = []
for ele in primes:
    if max(repeat(ele).values()) >= 3:
        superi.append(ele)
superi.sort()
for i in superi:
    repeatednumbers = []
    repeatkeys = list(repeat(i).keys())
    repeatvalues = list(repeat(i).values())
    for ele in range(len(repeatvalues)):
        if repeatvalues[ele] > 1:
            repeatednumbers.append(repeatkeys[ele])
    store = []
    for rem in repeatednumbers:
        store.append(str(i).replace(str(rem), "*"))
    for j in store:
        if set(j) != {"*"}:
            temp = []
            for r in range(10):
                temp.append(j.replace("*", str(r)))
            perm = [int(k) for k in temp if divide_primecheck(int(k))]
            if len(perm) == 8 and len(str(perm[0])) == len(str(perm[1])):
                print(min(perm))
                print(f"Process finished in {time()-t1}s")
                raise SystemExit()
