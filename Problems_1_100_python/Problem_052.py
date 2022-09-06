i = 1
while True:
    if all(set(str(a * i)) == set(str((a + 1) * i)) for a in range(1, 6)):
        print(i)
        raise SystemExit
    else:
        i += 1
