import time
from fpack import name_value

t = time.time()
with open(r'C:\Users\Utkar\Dropbox\Atom programs\archived problems\read_from_here\p022_names.txt','r') as f:
    data=f.readline()
stuff = str.split(data, '","')
stuff[0] = stuff[0][1:]
stuff[-1] = stuff[-1][:-1]
stuff.sort()
ans = 0
for i in range(len(stuff)):
    ans += name_value(stuff[i])*(i+1)
print(ans, 'time taken = ', time.time() - t)