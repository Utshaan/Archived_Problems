from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec = 105
    ans = 0
    for i in range(1,101):
        if (int(i**(1/2)))**2 == i:
            continue
        else:
            ans+=sum(Decimal(i).sqrt().as_tuple()[1][:100])

print(ans)