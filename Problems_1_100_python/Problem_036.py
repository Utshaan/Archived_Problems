from fpack import palindrome
from time import *

x = int(input("Double palindrome limit: \n"))
t = time()
sum = 0
for i in range(x):
    if palindrome(bin(i)[2:]) and palindrome(str(i)):
        sum += i
print(f"{sum} \n time taken = {time() - t}")
