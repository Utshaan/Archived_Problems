from time import time
from sympy import primefactors

def phi_n(x):
    l = primefactors(x)
    phi_n = x
    for ele in l:
        phi_n*= (1 - 1/ele)
    return int(phi_n)

t = time()
ans = 0
for i in range(2,10**6 + 1):
    ans += phi_n(i)

print(ans, time() - t)