import math
import time

x = int(input("which prime number do you want?"))
f = time.time()
l = [2]


def addprime(x):
    if x > 1:
        for i in range(2, (round(x / 2)) + 1):
            if x % i == 0:
                break
        else:
            l.append(x)
    else:
        return "negetive number"


a = 3
while len(l) < x:
    addprime(a)
    a += 2
print(max(l), "time taken", time.time() - f)
