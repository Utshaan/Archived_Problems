import math
import time
start_time = time.time()
marked = [0] * 2000000
value = 3
s = 2
while value < 2000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 2000000:
            marked[i] = 1
            i += value
    value += 2
print(f'{s} - Process finished in {time.time() - start_time} seconds')