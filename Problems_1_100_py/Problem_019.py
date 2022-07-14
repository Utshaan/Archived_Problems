import time
from fpack import day_calculator

sum = 0
t = time.time()
for m in range(1, 13):
    for y in range(1901, 2001):
        if day_calculator(1, m, y) == "Sunday":
            sum += 1
print(sum, "time taken = ", time.time() - t)
