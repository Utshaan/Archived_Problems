# THIS IS THE SMART METHOD
# from fpack import primelist_till_x
# l = sorted(primelist_till_x(1000))
# pro = 1
# for e in l:
#     pro *= e
#     if pro > 10**6:
#         pro /= e
#         break
# print(pro)


# THIS IS THE ETHICAL ONE
from sympy import primefactors
from time import time


def phi_n(x):
    l = primefactors(x)
    phi_n = x
    for ele in l:
        phi_n *= 1 - 1 / ele
    return int(phi_n)


t = time()
i = 2
high = 0
ans = 0
while i <= 10**6:
    if i / phi_n(i) > high:
        high = i / phi_n(i)
        ans = i
    i += 1

print(ans, time() - t)
