from fpack import primelist_till_x
import time


def cycle_len(x):
    i=1
    m = (1000%x)*1000
    while m!=1000:
        m=(m%x)*10
        i +=1
    return i+2
t = time.time()
ans = 0
san = None
for i in primelist_till_x(1000):
    if len(str(i)) == 3:
        san = cycle_len(i)
        if san > ans:
            ans = san
            answer = i
print(answer, 'time taken - ', time.time() - t)