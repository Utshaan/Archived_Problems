from itertools import permutations
from math import *
from fpack import divide_primecheck
from time import time

ti = time()
cool = []
i = 0
for i in range(1,10):
    t = '123456789'[:i]
    l = list(permutations(t))
    for x in range(factorial(i)):
        temp = ''
        for y in range(i):
            temp += l[x][y]
        if divide_primecheck(int(temp)):
            cool.append(int(temp))
print(f'{max(cool)} time taken = {time()-ti}')