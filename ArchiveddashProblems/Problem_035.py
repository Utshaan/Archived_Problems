from fpack import primelist_till_x, clockwise_cycle
from time import *

x = int(input("circular prime upper limit: \n"))
t = time()
primes = set(i for i in primelist_till_x(x))
empty = set()

for i in primes:
    if clockwise_cycle(i).issubset(primes):
        empty.add(i)

print(f"{len(empty)} \n time taken = {time() - t}")
