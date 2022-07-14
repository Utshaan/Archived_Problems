from fractions import Fraction
from math import gcd
from time import time

t = time()
l = []
for i in range(2, 12001):
    for j in range(int(i * 1 / 3) - 2, int(i * 1 / 2) + 2):
        if Fraction(j, i) < 1 / 2 and Fraction(j, i) > 1 / 3 and gcd(i, j) == 1:
            l.append(Fraction(j, i))
l.remove(Fraction(1, 3))
print(len(l), time() - t)
