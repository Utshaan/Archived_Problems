i = 0
j = 0
li = [1, 1]
while j < 1000:
    k = []
    k.extend(li)
    k[1] = sum(li)
    k[0] = li[0] + 2 * li[1]
    j += 1
    li = []
    li.extend(k)
    if len(str(k[0])) > len(str(k[1])):
        i += 1

print(i)
