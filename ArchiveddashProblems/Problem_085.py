from time import time
from rich import print
def cl(x,y):
    return abs(2_000_000 - x*y*(x+1)*(y+1)//4)

t = time()
low = 1_000_000
for i in range(1, 2000):
    for j in range(1,2000):
        if cl(i,j) < low:
            low = cl(i,j)
            x,y = i,j

print(f'Area of rectangle: {x*y},\nThe number of rectangles: {x*y*(x+1)*(y+1)//4},\nfor the set: {(x,y)}\nTime taken: {time() -t} seconds')