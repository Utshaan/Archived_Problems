from math import *
from fpack import divide_primecheck
import time

t = time.time()
current = None
high = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        x = 0
        while divide_primecheck(pow(x,2) + a*x + b):
            x += 1
        if x > high:
            high = x
            current = a*b

print(f'{current} , time taken - {time.time()-t}')