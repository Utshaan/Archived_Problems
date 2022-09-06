from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from time import time
from Problem_081 import usable

t = time()
grid = Grid(matrix=usable)
start = grid.node(0, 0)
end = grid.node(len(usable) - 1, len(usable) - 1)
finder = AStarFinder()
path, runs = finder.find_path(start, end, grid)

ans = 0
for y, x in path:
    ans += usable[x][y]

print(ans)
print(f"time taken = {time() - t}")
