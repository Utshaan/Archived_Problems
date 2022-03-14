import time
from fpack import factors

x = int(input("Till where do you want the sum of amicable numbers: \n"))
t = time.time()
ans = 0
for i in range(1, x):
    if sum(factors(sum(factors(i)))) == i and sum(factors(i)) != i:
        ans += i
print(ans, "time taken = ", time.time() - t)
