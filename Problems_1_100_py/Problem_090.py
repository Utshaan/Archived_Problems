from itertools import combinations

p = list(combinations(range(10), r=6))
p = list(map(set, p))
for ele in p:
    if 9 in ele:
        ele.add(6)
    if 6 in ele:
        ele.add(9)

ans = 0


def functino(i, j):
    return all(
        (possibilities[x][0] in i and possibilities[x][1] in j)
        or (possibilities[x][0] in j and possibilities[x][1] in i)
        for x in range(9)
    )


possibilities = [
    (0, 1),
    # (1, 0),
    (0, 4),
    # (4, 0),
    (0, 9),
    # (9, 0),
    (1, 6),
    # (6, 1),
    (2, 5),
    # (5, 2),
    (3, 6),
    # (6, 3),
    (4, 9),
    # (9, 4),
    (6, 4),
    # (4, 6),
    (8, 1),
    # (1, 8),
]

for i in p:
    for j in p:
        if functino(i, j):
            ans += 1

print(ans / 2)
