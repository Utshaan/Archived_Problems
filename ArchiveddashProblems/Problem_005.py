import math
import time

n = int(input("n = \n"))
x = 1
t = time.time()
for i in range(1, n + 1):
    x = math.lcm(x, i)
print(f"{x} - Time taken = {time.time()-t}")
