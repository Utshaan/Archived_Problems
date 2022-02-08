def sumofdigits(x):
    x = str(x)
    ans = 0
    for ele in x:
        ans+= int(ele)
    return(ans)

max = 0
for a in range(1,100):
    for b in range(1,100):
        if sumofdigits(a**b) > max:
            max = sumofdigits(a**b)

print(max)