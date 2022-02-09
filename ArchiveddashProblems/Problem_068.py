from time import time
w1 = time()
p = set(i for i in range(1,11))
l = []
for sum in range(11,30):
    a = 6
    for b in p.difference({a}):
        c = sum - a - b
        if c in p.difference({a,b}):
            for d in p.difference({a,b,c}):
                e = sum - d - c
                if e in p.difference({a,b,c,d}):
                    for g in p.difference({a,b,c,d,e}):
                        f = sum - g - e
                        if f in p.difference({a,b,c,d,e,g}):
                            for h in p.difference({a,b,c,d,e,f,g}):
                                i = sum - g - h
                                if i in p.difference({a,b,c,d,e,f,g,h}):
                                    j = sum - h - b
                                    if j in p.difference({a,b,c,d,e,f,g,h,i}) and all(qwe != 10 for qwe in (b,c,e,g,h)) and min(a,d,f,i,j) == a:
                                        l.append(int(f'{a}{b}{c}{d}{c}{e}{f}{e}{g}{i}{g}{h}{j}{h}{b}'))

print(max(l))
# for sol_list in L:
#     n=sol_list.index(min(sol_list))
#     if n==0:
#         ans_list.append(sol_list)
#     else:
#         ans_list.append(sol_list[n:]+sol_list[:n])
# for sol_list in ans_list:
#     num = ''
#     for sol in sol_list:
#         for x in sol:
#             num += str(x)
#     num_list.append(int(num))

print(time() - w1)