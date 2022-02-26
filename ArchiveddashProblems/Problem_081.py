# from rich import print

with open(r'D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p081_matrix.txt', 'r') as fl:
    think = fl.readlines()
    test_matrice = []
    for ele in think:
        test_matrice.append(list(map(int, (ele[:-1].split(',')))))


for ele in test_matrice:
    for i in range(len(ele),0,-1):
        if i >= 2:
            ele[i-2] += ele[i-1]

print(test_matrice)