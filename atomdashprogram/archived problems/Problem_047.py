from sympy import factorint

x = int(input('how many: \n'))
i = 2
while True:
    if all(len(factorint(a)) == x for a in range(i,i+x)):
        print(i)
        break
    i+=1