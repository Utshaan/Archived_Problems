from time import *

t = time()
multiplier = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 10000):
    if str(i)[0] == "9":
        temp = ""
        for a in multiplier:
            temp += str(i * a)
        s = list(int(i) for i in (temp[:9]))
        s.sort()
        if multiplier == s:
            print(f"{temp[:9],i} \n time taken - {time()-t}")
