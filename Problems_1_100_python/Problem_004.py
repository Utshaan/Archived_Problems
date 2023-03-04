import time

start = time.time()
answers = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        temp = str(i*j)
        if temp == temp[::-1]:
            answers.append(i*j)
            break

print(max(answers), time.time() - start)
