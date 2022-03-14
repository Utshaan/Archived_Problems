from fpack import factors
from time import time
from rich.progress import track


def do(x):
    return sum(factors(x)) - x


def chain(x):
    chain_values = [x]
    chain_len = 1
    start = x
    while True:
        x = do_dic[x]
        if x == 0 or x > 1_000_000 or x < start:
            return 0, chain_values
        if x in chain_values:
            if x == start:
                return chain_len, chain_values
            else:
                return 0, chain_values
        chain_values.append(x)
        chain_len += 1

do_dic = dict()
t_1 = time()

for i in track(range(1,1_000_000), description='Tracking....'):
    do_dic[i] = do(i)

high = 0,0

for i in range(11, 1_000_000):
    temp = chain(i)
    if temp[0] > high[0]:
        print(temp[0], i)
        high = temp

print(f'{high[0]} terms in the chain which has minimum = {min(high[1])}\nTime taken = {time() - t_1}')