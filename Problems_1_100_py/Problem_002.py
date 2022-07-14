import math


def purify(y):
    return [x for x in y if x % 2 == 0]


x = math.ceil(float(input("enter the limit: ")))
list = [1, 2]
for i in range(2, 10000):
    if list[i - 1] < x:
        list.append(list[i - 1] + list[i - 2])
    else:
        list.pop(i - 1)
        break
print(sum(purify(list)))
