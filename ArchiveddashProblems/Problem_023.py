import time
from fpack import abundant_numbers

x = time.time()
abundant_numbers = [r for r in range(12, 28124) if abundant_numbers(r)]
bef = set()
for a in abundant_numbers:
    for b in abundant_numbers:
        if a + b > 28123:
            break
        else:
            bef.add(a + b)

ans_list = [r for r in range(1, 28124) if r not in bef]
print(sum(ans_list), "time taken = ", time.time() - x)
