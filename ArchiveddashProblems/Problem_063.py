se = {1,2,3,4,5,6,7,8,9}
i = 1
sum = 0
while True:
    for ele in se:
        if len(str(ele**i)) == i:
            sum += 1
            print(f'{i}^{ele}', sum)
    i += 1