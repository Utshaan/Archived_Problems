import time

x = int(input("upper limit: \n"))
start_time = time.time()
marked = [0] * x
value = 3
s = [2]
while value < x:
    if marked[value] == 0:
        s.append(value)
        i = value
        while i < x:
            marked[i] = 1
            i += value
    value += 2
print(f'{s} - Process finished in {time.time() - start_time} seconds')