from time import time
from itertools import product

def pruify(a,b):
    return sorted(list(str(a))) == sorted(list(str(b)))

t = time()
cubes = set([i**3 for i in range(1000,10000)])

for a,b in product(cubes, repeat = 2):
    if b > a:
        if pruify(a,b):
            for c in cubes:
                if c > b:
                    if pruify(b,c):
                        for d in cubes:
                            if d > c:
                                if pruify(c,d):
                                    for e in cubes:
                                        if e > d:
                                            if pruify(d,e):
                                                print(a, time() - t)
                                                raise SystemExit