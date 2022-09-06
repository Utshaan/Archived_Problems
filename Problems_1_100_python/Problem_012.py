from fpack import triangle_number, factors
import time


x = int(input("At least more than how many factors: "))
t = time.time()
temp = 1
truth = True
while truth == True:
    if len(factors(triangle_number(temp))) > x:
        print(triangle_number(temp), "Time taken = ", time.time() - t)
        truth = False
    else:
        temp += 1
