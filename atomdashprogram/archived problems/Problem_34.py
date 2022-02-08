from time import *
from fpack import sum_facto_digi

t = time()
los = 0
i = 3
while i < 50000:
    if sum_facto_digi(i):
        los += i
    i += 1
print(f'{los}, time taken - {time() - t}')