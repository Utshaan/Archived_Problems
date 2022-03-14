import math
import time

x = int(input("Number of sides of square are: \n"))
t = time.time()
print(
    int((math.factorial(2 * x)) / (math.factorial(x)) ** 2),
    "Time taken = ",
    time.time() - t,
)
