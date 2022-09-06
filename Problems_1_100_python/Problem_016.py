import time

x = int(input("what is the power: \n"))
t = time.time()
y = str(2**x)
sum = 0
for i in range(len(y)):
    sum += int(y[i])

print(sum, time.time() - t)
