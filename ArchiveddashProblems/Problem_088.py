from time import time
from rich import print


def minimal_prod_sum(product: int, sum: int, count: int, lower_limit: int) -> None:
    k = product - sum + count
    if k < kmax:
        upper_limit[k] = product if product < upper_limit[k] else upper_limit[k]
        for new_factor in range(lower_limit, 2 * kmax // product + 1):
            minimal_prod_sum(
                product * new_factor, sum + new_factor, count + 1, new_factor
            )


t_1 = time()
kmax = 12000
upper_limit = [2 * kmax] * kmax
minimal_prod_sum(1, 1, 1, 2)
print(sum(set(upper_limit[2:])))
print(time() - t_1)
