from math import log10
from time import time
from rich import print

ti = time()
with open(
    r"D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p099_base_exp.txt",
    "r",
) as fl:
    l = fl.read().split("\n")

high = 0
line = 0
for ele in l:
    t = tuple(map(int, (ele.split(","))))
    temp = log10(t[0]) * t[1]
    if temp > high:
        high = temp
        line = l.index(ele) + 1

print(
    f"[green]Line {line} has greatest value = {high} and took {time() - ti} seconds[/green]"
)
