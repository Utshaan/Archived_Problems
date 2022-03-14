def if_pentagonal_numbers(x):
    num = (1 + (24 * x + 1) ** (1 / 2)) / 6
    if num % 1 == 0:
        return True
    else:
        return False


a = 1
while True:
    for b in range(1, a):
        an = a * (3 * a - 1) // 2
        bn = b * (3 * b - 1) // 2
        if if_pentagonal_numbers(an + bn) and if_pentagonal_numbers(abs(bn - an)):
            print(abs(bn - an), bn, an)
            break
    a += 1
