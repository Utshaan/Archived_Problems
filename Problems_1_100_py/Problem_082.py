from rich import print
from Problem_081 import usable
from time import time


t1 = time()

zero_matrix = [[0 for _ in range(len(usable))] for _ in range(len(usable))]

for nth_of_column in range(len(usable)):
    zero_matrix[nth_of_column][-1] = usable[nth_of_column][-1]

for column in range(len(usable) - 2, -1, -1):
    upper_layer = [0 for _ in range(len(usable))]
    upper_layer[0] = usable[0][column] + zero_matrix[0][column + 1]

    for rth in range(1, len(usable)):
        upper_layer[rth] = min(
            upper_layer[rth - 1] + usable[rth][column],
            zero_matrix[rth][column + 1] + usable[rth][column],
        )

    zero_matrix[len(usable) - 1][column] = upper_layer[len(usable) - 1]

    for rev_rth in range(len(usable) - 2, -1, -1):
        zero_matrix[rev_rth][column] = min(
            upper_layer[rev_rth],
            usable[rev_rth][column] + zero_matrix[rev_rth + 1][column],
        )

print(min([row[0] for row in zero_matrix]), f"time taken = {time() - t1}")
