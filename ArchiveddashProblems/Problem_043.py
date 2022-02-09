from itertools import permutations
from time import time

t1 = time()
primes = [2,3,5,7,11,13,17]
numbers = list(map(lambda i:''.join(i), list(permutations('0123456789'))))
ans = []
for ele in numbers:
    if all((int(ele[i-2:i+1])%primes[i-3]) == 0 for i in range(3,10)):
        ans.append(int(ele))
print(f'{sum(ans)} \n time taken = {time()-t1}')