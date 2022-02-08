from time import time

with open(r"C:\Users\Utkar\Dropbox\Atom programs\archived problems\read_from_here\p067_triangle.txt", 'r') as file:
    stuff = file.readlines()

temp = ''
for ele in stuff:
    temp += ele[:-1] + ' '

x = temp[:-1]
t = time()
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
print(the_answerful[-1][-1], 'time taken = ', time()-t)