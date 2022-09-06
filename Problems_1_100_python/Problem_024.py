from itertools import permutations as P
import time

x = time.time()
print(list(P("0123456789"))[999999], "time taken -", time.time() - x)
