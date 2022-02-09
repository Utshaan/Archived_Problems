from math import factorial
def combinations(x,r):
    if x > r:
        return(factorial(x)//(factorial(r)*factorial(x-r)))
    else:
        return 0
j = 0
for x in range(1,101):
    for r in range(x):
        if combinations(x,r) > 1000000:
            j += 1
print(j)