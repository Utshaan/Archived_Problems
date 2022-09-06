from fpack import palindrome


def reverse(x):
    x = str(x)[::-1]
    return int(x)


i = 1
op = 0
while i < 10001:
    k = 0
    k += i
    j = 0
    while j < 50:
        k += reverse(k)
        if palindrome(k):
            break
        else:
            j += 1
    if j == 50:
        op += 1
    i += 1

print(op)
