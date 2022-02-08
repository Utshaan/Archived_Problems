from time import *
t = time()
x = ''
for i in range(0,500000):
    x += str(i)
ans = int(x[1])*int(x[10])*int(x[100])*int(x[1000])*int(x[10000])*int(x[100000])*int(x[1000000])
print(f'{ans} \n time taken = {time()-t}')