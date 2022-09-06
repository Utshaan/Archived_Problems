# def continuedfraction(x):
#     p = x**(1/2)
#     l = [int(p)]
#     ok = True
#     a = int(p)
#     rep = [int(1//(p-a)),int(1//((1/(p-a))-(1//(p-a))))]
#     count = 2
#     something = 1/((1/(p-a))-(1//(p-a)))
#     while ok:
#         temp = int(1//(something - int(something)))
#         rep.append(temp)
#         if temp == 2*a:
#             ok = False
#         something = 1/(something - int(something))
#     if len(set(rep)) == 1:
#         rep = [rep[0]]
#     elif rep[2:] == rep[:2]:
#         rep = rep[2:]
#     l.append(rep)
#     return(l)


def continuity(x):
    yes = []
    cool = []
    m = 0
    d = 1
    a = int(x ** (1 / 2))
    yes.append(a)
    while a != 2 * int(((x) ** (1 / 2))):
        m = d * a - m
        d = (x - m**2) / d
        a = int(((x ** (1 / 2)) + m) / d)
        cool.append(a)
    yes.append(cool)
    return yes


ans = 0
t = [a**2 for a in range(101)]
l = [a for a in range(2, 10001) if a not in t]
for a in l:
    if len(continuity(a)[1]) % 2 != 0:
        ans += 1
print(ans)
