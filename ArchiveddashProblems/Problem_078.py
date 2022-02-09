from sympy import partition as p; from time import time
t = time()
i = 10
while str(p(i))[-6:] != '000000':
    i += 1
print(f'{p(i)}\n{i} \n{time() - t}')