import time
example = '75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
x = str(input("what is the string?: \n"))
t = time.time()
listy = list(map(int,x.split()))
the_answerful = []
alpha = len(listy)
i = 1
while alpha >0:
    alpha -= i
    i+= 1
for c in range(1,i):
    the_answerful.append(listy[:c])
    del listy[:c]
the_answerful.reverse()
answer = []
for q in range(0,len(the_answerful)-1):
    for p in range(0,len(the_answerful[q])-1):
        if the_answerful[q][p] + the_answerful[q+1][p] > the_answerful[q][p+1] + the_answerful[q+1][p]:
            the_answerful[q+1][p] = the_answerful[q][p] + the_answerful[q+1][p]
        else:
            the_answerful[q+1][p] = the_answerful[q][p+1] + the_answerful[q+1][p]
print(the_answerful[-1][-1], 'time taken = ', time.time()-t)