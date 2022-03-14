from fractions import Fraction
from math import gcd
from time import time

t = time()
l = [3 / 7]
for i in range(10**6 - 100, 10**6 + 1):
    for j in range(int(i * 3 / 7) - 2, int(i * 3 / 7) + 2):
        if Fraction(j, i) < 3 / 7 and gcd(i, j) == 1:
            l.append(Fraction(j, i))

print(sorted(l)[-2], time() - t)
