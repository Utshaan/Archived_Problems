from time import time
from math import factorial

def cycle(x: str) -> list:
    l = []
    ele = x
    while ele not in l:
        l.append(ele)
        sum = 0
        t = map(int, list(ele))
        for p in t:
            sum += factorial(p)
        ele = str(sum)
    return(l)

t1 = time()
i = 2
ans = 0
while i <= 10**6:
    if len(cycle(str(i))) == 60:
        ans += 1
    i += 1
print(ans, time() - t1)
