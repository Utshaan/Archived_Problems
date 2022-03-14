from time import time


def once(x):
    return sum(int(i) ** 2 for i in str(x))


def functino(x):
    temp = x
    while True:
        try:
            cool[temp] = cool[x]
            return cool[x]
        except:
            if x == 1:
                cool[temp] = False
                return False
            if x == 89:
                cool[temp] = True
                return True
            x = once(x)


cool = {89: True, 1: False}

t = time()
ans = 0
for i in range(1, 10_000_001):
    if functino(i):
        ans += 1


print(ans, f"Time taken: {time() - t}")
