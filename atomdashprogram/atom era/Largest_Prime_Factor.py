import math


def checkprime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return(False)
                break
            else:
                return(True)
    else:
        return(False)


x = math.ceil(float(input("gimme gimme gimme: ")))
f = []
primefactorlist = []
for i in range(2, math.ceil(x/2)+1):
    if x % i == 0:
        f.append(i)
for a in f:
    if checkprime(a):
        primefactorlist.append(a)

print(max(primefactorlist))
print(f)
