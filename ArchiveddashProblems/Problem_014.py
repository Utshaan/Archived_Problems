import time
from fpack import Syracuse

x = int(input("What's the limit now?\n"))

ti = time.time()
len_list = 0
this_other_variable = 0

for i in range(0, x):
    if len(Syracuse(i)) > len_list:
        len_list = len(Syracuse(i))
        this_other_variable = i

print(this_other_variable, ",", len_list, "\nTime taken = ", time.time() - ti)
