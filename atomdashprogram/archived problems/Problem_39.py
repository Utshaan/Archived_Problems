from time import time

x = int(input('Max perimeter: \n'))
t = time()
cool = dict()
for a in range(1,x//3):
    for b in range(a,x//2):
        c = (a**2 + b**2)**(1/2)
        cool.setdefault(a+b+c,0 )
        if a+b+c<= x and c%1 == 0:
            cool[a+b+c] = cool.get(a+b+c)+1
ans_dict = dict(map(reversed, cool.items()))
print(f'{ans_dict.get(max(cool.values())),max(cool.values()) } \n time taken = {time()-t}')
