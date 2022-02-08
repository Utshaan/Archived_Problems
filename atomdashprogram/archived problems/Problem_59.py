from itertools import product, cycle
from time import time

def decrypt(x, cyp):
    ans = ""
    sum = 0
    for a,b in zip(x,cycle(cyp)):
        ans += chr(a^b)
        sum += a^b
    ans += f'\nSum of ASCII of message = {sum}'
    return ans

t = time()
cypher_hit_list = list(product([i for i in range(97,123)], repeat=3))

listopher = set([(i) for i in range(97,123)] + [(i) for i in range(32,91)])

with open(r'C:\Users\Utkar\Dropbox\Atom programs\archived problems\read_from_here\p059_cipher.txt') as file:
    stuff = list(map(int, str.split(file.read(), ',')))

mega = []
ultimate_max = 0
for tup in cypher_hit_list:
    count = 0
    for num,cyp in zip(stuff,cycle(tup)):
        if num^cyp in listopher:
            count += 1
    if count > ultimate_max:
        ultimate_max = count
        mega = tup

print(decrypt(stuff, mega), f'\nTime Taken = {time() - t}')