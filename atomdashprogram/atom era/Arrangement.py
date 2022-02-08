import itertools


word = input("Enter a word: ")
n = int(input("Length of word: "))
pnc = int(input("Enter 1 for permutations, 2 for combinations: "))
letters = list(word)
if n <= len(letters) + 1:
    if pnc == 1:
        ok = list(itertools.permutations(letters, n))
        answer = list(dict.fromkeys(ok))
    elif pnc == 2:
        ok = list(itertools.combinations(letters, n))
        answer = list(dict.fromkeys(ok))
    else:
        print("Retard")
    print(answer, '\nNumber of thingies are:', len(answer))
else:
    print("Retard")
