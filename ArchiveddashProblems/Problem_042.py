from time import time
from fpack import triangle_number, name_value

tim = time()
with open(r'C:\Users\Utkar\Dropbox\Atom programs\archived problems\read_from_here\p042_words.txt','r') as f:
    file=f.read()
stuff = str.split(file, '","')
stuff[0] = stuff[0][1:]
stuff[-1] = stuff[-1][:-1]
triangles = [triangle_number(i) for i in range(50)]
i = []
for ele in stuff:
    if name_value(ele) in triangles:
        i.append(ele)
print(f'{len(i)} \n time taken = {time()-tim}')