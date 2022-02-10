from rich import print

with open(r'D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p081_matrix.txt', 'r') as fl:
    think = fl.readlines()
    test_matrice = []
    for ele in think:
        test_matrice.append(list(map(int, (ele[:-1].split(',')))))


x,y = -1,-1
try:
    while test_matrice[x][y] != test_matrice[1][1]:
        if test_matrice[x][y] + test_matrice[x-1][y] > test_matrice[x][y] + test_matrice[x][y-1]:
            test_matrice[x][y-1] += test_matrice[x][y]
            for i in range(len(test_matrice)):
                test_matrice[i] = test_matrice[i][:-1]
        else:
            test_matrice[x-1][y] += test_matrice[x][y]
            test_matrice = test_matrice[:-1]
except:
    ans = 0
    for ele in test_matrice:
        ans += sum(ele)
    print(ans)
# if test_matrice[x][y] + test_matrice[x-1][y] > test_matrice[x][y] + test_matrice[x][y-1]:
#         test_matrice[x][y-1] += test_matrice[x][y]
#         for i in range(len(test_matrice)):
#             test_matrice[i] = test_matrice[i][:-1]
# else:
#     test_matrice[x-1][y] += test_matrice[x][y]
#     test_matrice = test_matrice[:-1]

print(test_matrice)