import time

start = time.time()
answers = []
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        temp = str(i*j)
        if temp == temp[::-1]
        answers.append(temp)
        break

print(max(answers), time.time() - start)
