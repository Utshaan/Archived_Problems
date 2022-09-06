from rich import print

with open(
    r"D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p081_matrix.txt",
    "r",
) as fl:
    think = fl.readlines()
    usable = []
    test_matrice = []
    for ele in think:
        test_matrice.append(list(map(int, (ele[:-1].split(",")))))
        usable.append(list(map(int, (ele[:-1].split(",")))))


for k in range(80, 1, -1):
    for i in range(80, 1, -1):
        test_matrice[i - 2][79] += test_matrice[i - 1][79]
        test_matrice[79][i - 2] += test_matrice[79][i - 1]
        test_matrice[k - 2][i - 2] += min(
            test_matrice[k - 1][i - 2], test_matrice[k - 2][i - 1]
        )

if __name__ == "__main__":

    print(test_matrice[0][0])
