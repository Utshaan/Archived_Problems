l = []
for i in range(1,35):
    l.append(1)
    l.append(1)
    l.append(2*i)
l[0] = 2
l = l[:100]

t = [0,1]
for i in l[::-1]:
    t[0] = t[1]*i + t[0]
    t = t[::-1]

ans = 0
for i in list(str(t[::-1][0])):
    ans += int(i)

print(ans)