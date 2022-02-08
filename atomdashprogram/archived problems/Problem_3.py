import math
import time 
from fpack import primelist_till_x

x = int(input("Enter the number: "))
t = time.time()
primes = primelist_till_x(math.ceil(math.sqrt(x)))


answer_list = []
for a in primes:
    if x % a == 0:
        answer_list.append(a)
print(f"{max(answer_list)} - Time taken = {time.time()-t}")