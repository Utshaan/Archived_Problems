import math


x = math.ceil(float(input("Enter the upper limit: ")))
three = 0
five = 0
fifteen = 0
for i in range(1,x+1):
    if i%3==0:
        three = three + i
for i in range(1,x+1):
    if i%5==0:
        five = five + i
for i in range(1,x+1):
    if i%15==0:
        fifteen = fifteen + i
print("The sum is",three+five-fifteen)
