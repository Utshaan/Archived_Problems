from math import gcd
from time import time

t = time()
limit = 1_500_001
cool = set()
answerful_list = dict()
ans = 0
for m in range(2, int((limit / 2) ** (1 / 2)) + 2):
    for n in range(1, m):
        if gcd(m, n) == 1 and (m + n) % 2 == 1:
            p = 2 * (m**2 + m * n)
            cool.add(p)
for q in cool:
    for i in range(q, limit + 1, q):
        try:
            answerful_list[i] += 1
        except:
            answerful_list[i] = 1

for item in answerful_list:
    if answerful_list[item] == 1:
        ans += 1


print(ans, time() - t)
