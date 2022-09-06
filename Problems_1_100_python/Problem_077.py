from time import time
from sympy import primefactors as pf


t = time()
d = {0: 1, 1: 1}


def p(n):
    total = 0
    for k in range(n):
        try:
            total += sum(pf(n - k)) * d[k]
        except:
            total += sum(pf(n - k)) * p(k)
            d[k] = p(k)
    d[n] = total // n
    return total // n


i = 10
while p(i) < 5000:
    i += 1

print(p(i), i, time() - t)
