from sympy import partition as p; from time import time
t = time()
print(p(100)-1, time() - t)