from rich import print
from time import time


def squaric_anagram(map: dict, word: str) -> None:
    for key in map:
        word = word.replace(key, map[key])
    return int(word)


t_1 = time()
with open(
    r"D:\utkarsh\Github_Directories\Repo_Archived_Problems\ArchiveddashProblems\read_from_here\p098_words.txt",
    "r",
) as fl:
    string = fl.readlines()[0]
    dictionary = string.split('","')
    dictionary[-1] = dictionary[-1][:-1]
    dictionary[0] = dictionary[0][1:]


l = set()
for ele in dictionary:
    for nele in dictionary:
        if sorted(str(ele)) == sorted(str(nele)) and ele != nele:
            l.add((ele, nele))

k = set()

squares = [i**2 for i in range(10, 31624)]

for ele in l:
    for square in squares:
        if len(set(ele[0])) == len(set(str(square))) and len(ele[0]) == len(
            str(square)
        ):
            map = dict(zip(list(ele[0]), list(str(square))))
            if squaric_anagram(map, ele[1]) in squares and len(str(square)) == len(
                str(squaric_anagram(map, ele[1]))
            ):
                k.add((max(square, squaric_anagram(map, ele[1])), ele))


high = 0, 0
for temp in k:
    if temp[0] > high[0]:
        high = temp
print(
    f"[green]The words:[/green] {high[1]}\n[green]The max value[/green] = {high[0]}\nTime Taken : {time()-t_1}"
)
