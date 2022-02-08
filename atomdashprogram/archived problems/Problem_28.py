import time
ans = 1
x = int(input("What's the square side length: \n"))
t = time.time()
for i in range(3,x+1,2):
    ans +=  2*(2*(i**2) + 3*(1 - i))
print(f'{ans}, time taken - {time.time() -t}')