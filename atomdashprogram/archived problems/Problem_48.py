from time import time
t = time()
sum = 0
for i in range(1,1001):
    sum += i**i
print(str(sum)[-10:], time() - t)