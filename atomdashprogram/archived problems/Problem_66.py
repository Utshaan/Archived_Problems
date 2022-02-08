def continuity(x):
    yes = []
    cool = []
    m = 0
    d = 1
    a = int(x**(1/2))
    yes.append(a)
    while a != 2*int(((x)**(1/2))):
        m = d*a - m
        d = (x - m**2)/d
        a = int(((x**(1/2))+m)/d)
        yes.append(a)
    return yes


def solutions(x):
    if x in squares:
        return [0,1]
    else:
        l = continuity(x)[0:1] + (continuity(x)[1:])
        c = 1
        a = [l[0],1]
        while True:
            if int((a[0])**2 - x*((a[1])**2)) == 1:
                return([a[0],a[1]])
            else:
                if c > len(l):
                    l.extend((continuity(x)[1:]))
                t = [0,1]
                for i in l[c::-1]:
                    t[0] = t[1]*i + t[0]
                    t = t[::-1]
                t = t[::-1]
                a = t
                c += 1

squares = [i**2 for i in range(1,33)]
values_D = 0
high = 0
for D in range(2,1001):
    if solutions(D)[0] > high:
        high = solutions(D)[0]
        values_D = D

print(values_D)
