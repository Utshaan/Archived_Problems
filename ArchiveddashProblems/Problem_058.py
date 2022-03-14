from fpack import divide_primecheck


def primeperc(l):
    temp = 0
    for a in l:
        if divide_primecheck(a):
            temp += 1
    return temp * 100 / len(l)


l = {1, 3, 5, 7, 9}
v = [3, 5]
dif = 4
ini = 13
k = 1
while (v[0] / v[1]) * 100 >= 10:
    for i in range(4):
        l.add(ini)
        if divide_primecheck(ini):
            v[0] += 1
        v[1] += 1
        ini += dif
    ini += 2
    dif += 2
    k += 1

print(v)
print(max(l) ** (1 / 2))
