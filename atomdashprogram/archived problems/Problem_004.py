import time
start = time.time()
list = []
answers = []
for i in range(100,1000):
    for j in range(100,1000):
        list.append(i*j)

for i in list:
    if str(i) == str(i)[::-1]:
        answers.append(i)
print(max(answers), time.time()-start)