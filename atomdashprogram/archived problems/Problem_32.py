import itertools
from time import *
from itertools import *

t = time()
L = list(permutations('123456789'))
ans = set()

for ele in L:
    if int(ele[0])* int(ele[1]+ele[2]+ele[3]+ele[4]) == int(ele[5]+ele[6]+ele[7]+ele[8]):
        ans.add(int(ele[5]+ele[6]+ele[7]+ele[8]))
    elif int(ele[0]+ele[1])* int(ele[2]+ele[3]+ele[4]) == int(ele[5]+ele[6]+ele[7]+ele[8]):
        ans.add(int(ele[5]+ele[6]+ele[7]+ele[8]))
print(f'{sum(ans)}, time taken - {time()-t}')