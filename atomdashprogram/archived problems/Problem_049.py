from fpack import primelist_till_x
from time import time

t = time()
primes = [i for i in primelist_till_x(10000) if len(str(i)) == 4 and i>1487]
for q in range(len(primes)):
    for w in range(q+1,len(primes)):
        a = primes[q]
        b = primes[w]
        if b>a and 2*b-a in primes and set(str(a)) == set(str(b)) == set(str(2*b-a)):
            print(f'{a}{b}{2*b-a}', time()-t)
            raise SystemExit