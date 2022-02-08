from sympy import primefactors
from fpack import primelist_till_x as primo
from time import time

def phi_n(x):
    l = primefactors(x)
    if len(l) == 2:   #because we want to maximize phi(n)
        phi_n = x
        for ele in l:
            phi_n*= (1 - 1/ele)
        return int(phi_n)
    else:
        return 0

def p(x,y):
    return sorted(list(str(x))) == sorted(list(str(y)))


t = time()
# i = 2
# low = 10**7
# num = 0
# while i < 10**7:
#     print(i)
#     if p(i,phi_n(i)) and i/phi_n(i) < low:
#         low = i/phi_n(i)
#         num = i
#     i += 1
i = 10**7 - 1
low = 10**7
num = 0
while True:
    print(i)
    if len(primefactors(i)) == 2:
        if p(i,(primefactors(i)[0]-1)*(primefactors(i)[1]-1)) and primefactors(i)[0]*primefactors(i)[1]/(primefactors(i)[0]-1)*(primefactors(i)[1]-1) < low:
            low = primefactors(i)[0]*primefactors(i)[1]/(primefactors(i)[0]-1)*(primefactors(i)[1]-1)
            num = i
            print('===============>',i)
    i -= 2


# print(primies, time() - t)