from time import time
from rich import print

t1,max, t = time(),1_000_000_000_000, [1, 3]
while (1 + (1 + 8 * (t[1]) * (t[1] - 1)) ** (1 / 2)) // 2 < max:
    t[1], t[0] = (6 * t[1] - t[0] - 2), t[1]

print(
    f"[green]{t[1]} [blue]discs[/blue] in {int((1 + (1 + 8*(t[1])*(t[1]-1))**(1/2))//2)} total discs[/green].\nTime taken: {time() -t1}"
)
