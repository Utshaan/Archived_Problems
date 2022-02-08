import time
t = time.time()
l = 0
p = []
dicto = {0:'', 1:"one", 2: "two", 3: "three", 4:'four', 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12:"twelve", 13: "thirteen", 14:"fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60:'sixty', 70:'seventy', 80: 'eighty', 90:'ninety', 100:'onehundred', 1000: 'onethousand'}
for i in range(1,1001):
    if i in dicto:
        l+= len(dicto[i])
        p.append(dicto[i])
    else:
        if len(str(i)) == 3:
            if i%100 >=20 or i%100 <11:
                if i%100 != 0:
                    hundreds = int((i - (i%100))/100)
                    tens = int(((i%100) - (i%10)))
                    ones = int(i%10)
                    word = f'{dicto[hundreds]}hundredand{dicto[tens]}{dicto[ones]}'
                    l += len(word)
                    p.append(word)
                else:
                    hundreds = int((i - (i%100))/100)
                    word = f'{dicto[hundreds]}hundred'
                    l += len(word)
                    p.append(word)
            else:
                 hundreds = int((i - (i%100))/100)
                 tensones = int(i%100)
                 word = f'{dicto[hundreds]}hundredand{dicto[tensones]}'
                 p.append(word)
                 l += len(word)
        else:
            tens = int(i - i%10)
            ones = int(i%10)
            word = f'{dicto[tens]}{dicto[ones]}'
            l += len(word)
            p.append(word)
print(l, "time taken = ", time.time() - t)