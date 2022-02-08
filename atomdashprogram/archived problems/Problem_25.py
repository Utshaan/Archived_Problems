import time
fib = [1,1]
i = 1
x = int(input("What is the number of digits: \n"))
t = time.time()
while len(str(fib[i])) < x:
    fib.append(fib[i-1] + fib[i])
    i += 1
print(i+1, 'time taken - ', time.time()-t)