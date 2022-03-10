with open(
    r"D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p089_roman.txt",
    "r",
) as fl:
    l = [i[:-1] for i in fl.readlines()]

extra = 0

for ele in l:
    if "VIIII" in ele:
        extra += 3
    elif "IIII" in ele:
        extra += 2
    if "LXXXX" in ele:
        extra += 3
    elif "XXXX" in ele:
        extra += 2
    if "DCCCC" in ele:
        extra += 3
    elif "CCCC" in ele:
        extra += 2

print(extra)