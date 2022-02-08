from fpack import primelist_till_x, divide_primecheck
from time import time

t = time()
def cool(a: int,b: int) -> bool:
    return divide_primecheck(int(str(a)+str(b))) and divide_primecheck(int(str(b)+str(a)))

primeset = list(primelist_till_x(10000))

for a in range(len(primeset)):
    primea = primeset[a]
    for b in range(a+1,len(primeset)):
        primeb = primeset[b]
        if cool(primea,primeb):
            for c in range(b+1,len(primeset)):
                primec = primeset[c]
                if cool(primeb,primec) and cool (primea,primec):
                    for d in range(c+1,len(primeset)):
                        primed = primeset[d]
                        if cool(primec,primed) and cool(primeb,primed) and cool(primea,primed):
                            for e in range(d+1,len(primeset)):
                                primee = primeset[e]
                                if cool(primed,primee) and cool(primec,primee) and cool(primeb,primee) and cool(primea,primee):
                                    print([primea+primeb+primec+primed+primee], time() - t)
                                    raise SystemExit

