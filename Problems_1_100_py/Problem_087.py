from fpack import primelist_till_x
from time import time

t = time()
target = 50_000_000
primes = sorted(list(primelist_till_x(int(target ** (1 / 2)))))
num = set()

for i in primes:
    if i**4 > target:
        break
    else:
        for j in primes:
            if j**3 + i**4 > target:
                break
            else:
                for k in primes:
                    n = i**4 + j**3 + k**2
                    if n < 50_000_000:
                        num.add(n)

print(f"Total Numbers = {len(num)},\nTime Taken: {time() - t} seconds")
