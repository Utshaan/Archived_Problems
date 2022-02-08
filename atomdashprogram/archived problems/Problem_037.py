from fpack import primelist_till_x, delete_from_left, delete_from_right, divide_primecheck
from time import time

x = int(input('Check till where: \n'))
t = time()
l = [i for i in primelist_till_x(x) if len(str(i))>1]
primes = [i for i in primelist_till_x(x)]
main = set()

for i in l:
    almi = delete_from_left(str(i)).union(delete_from_right(str(i)))
    if all(divide_primecheck(i) for i in almi):
        main.add(i)
    if len(main) == 11:
        print(main, sum(main), time() - t)
        raise SystemExit
