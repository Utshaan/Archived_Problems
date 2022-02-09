import time
import math
x = int(input('What is the number: \n'))
t = time.time()
x = str(math.factorial(x))
ans = 0
for i in range(len(x)):
    ans += int(x[i])

print(ans, 'time taken = ', time.time() - t)