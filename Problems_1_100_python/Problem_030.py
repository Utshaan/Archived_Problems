import time

sum = 0
i = 2
x = time.time()
l = 0
temp = 0
while sum < 1000000:
    temp = 0
    for a in range(0, len(str(i))):
        temp += int(str(i)[a : a + 1]) ** 5
    if temp == i:
        l += i
        sum = 0
    i += 1
    sum += 1
print(f"{l} , time taken - {time.time()-x}")
