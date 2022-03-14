from time import time
from rich import print

grid_size = 50

num = set()
t = time()
for x1 in range(1, grid_size + 1):
    for y2 in range(1, grid_size + 1):
        num.add((x1, 0, x1, y2))
        num.add((x1, 0, 0, y2))
        for x2 in range(1, x1):
            if y2**2 / (x2 * (x2 - x1)) == -1:
                num.add((x1, 0, x2, y2))
            for y1 in range(1, y2 + 1):
                if y1 * (y2 - y1) / (x1 * (x2 - x1)) == -1:
                    num.add((x1, y1, x2, y2))

for y2 in range(1, grid_size + 1):
    for x1 in range(1, grid_size + 1):
        num.add((x1, y2, 0, y2))
        for y1 in range(1, y2):
            if (y2 - y1) * y1 / (x1**2) == 1:
                num.add((x1, y1, 0, y2))
            for x2 in range(1, x1):
                if y2 * (y2 - y1) / (x2 * (x2 - x1)) == -1:
                    num.add((x1, y1, x2, y2))

print(
    f"Number of right angled triangles: {len(num)},\nTime taken = {time() - t} seconds"
)
