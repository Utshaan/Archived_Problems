from fpack import primelist_till_x
from time import time

l = primelist_till_x(1000000)
t = time()
ans = 21
top = 0
for low in range(len(l) - 22):
    a = low + ans
    while sum(l[low:a]) < 1000000:
        if sum(l[low:a]) in l and a - low > ans:
            ans = a - low
            top = sum(l[low:a])
        a += 1
print(ans, top, time() - t)
