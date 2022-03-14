import time

sot = set()
x = int(input("what is the upper limit for power: \n"))
t = time.time()
for a in range(2, x + 1):
    for b in range(2, x + 1):
        sot.add((a**b))
print(f"{len(sot)} , time taken - {time.time() - t}")
