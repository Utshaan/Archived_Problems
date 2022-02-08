x = float(input("x1 is"))
y = float(input("y1 is"))
a = float(input("x2 is"))
b = float(input("y2 is"))
c = float(input("x3 is"))
d = float(input("y3 is"))

p = abs((x*(b-d) + a*(d - y) + c*(y - b))*(1/2))
print(p)
