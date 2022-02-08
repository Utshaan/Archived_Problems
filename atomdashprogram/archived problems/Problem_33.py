from time import *
from fractions import *

def weird(x,y):
    t = int(str(x)[0])
    e = int(str(x)[1])
    m = int(str(y)[0])
    p = int(str(y)[1])
    if t == m:
        return(e/p)
    elif e == m:
        return(t/p)
    elif t == p:
        return(e/m)
    else:
        return(t/m)

t =time()
n = 1
d = 1
for b in range(10,100):
    if b%10 != 0:
        temp1 = str(b)[0]
        temp2 = str(b)[1]
        for some in range(1,10):
            numbers = set()
            numbers.add(int(str(some)+temp1))
            numbers.add(int(temp1+str(some)))
            numbers.add(int(str(some)+temp2))
            numbers.add(int(temp2+str(some)))
            for a in numbers:
                if a < b and weird(a,b) == a/b:
                    n*= a
                    d*= b
print(f'{Fraction(n,d)}, time taken - {time()-t}')