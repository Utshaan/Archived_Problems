from rich import print
from time import time

t = time()
max_per = 1_000_000_000

x1, x2, bias, p_bias = 5, 17, -2, -1
num = 0
l = {16, 50}
while 3 * x2 + p_bias < max_per:
    l.add(3 * x2 + p_bias)
    x2, x1, bias, p_bias = 4 * x2 - (x1 + bias), x2, -bias, -p_bias

print(
    f"[green]Sum of perimeters:[/green] {sum(l)},\n[green]Time Taken:[/green] {time() - t}"
)
