from time import time
from rich import print

t = time()


def len(l, bnH):
    x = l**2 + (bnH) ** 2
    return x == (int(x ** (1 / 2))) ** 2


ans = 1975
M = 100

while ans < 1_000_000:
    for bnH in range(3, 2 * M):
        if len(M, bnH):
            if bnH > M:
                ans += M - bnH // 2 + 1 if bnH % 2 == 0 else M - bnH // 2
            else:
                ans += bnH // 2
    M += 1

print(f"M = {M-1},\nTotal solution cuboids = {ans},\nTime Taken: {time() - t} seconds")
