l = []
key = []
thething = []
code=""
message = []
words = []
matrix =""

z = str(input("Message:\n"))
# for i in range(0,len(x)):
#     a = x[i]
#     l.append(a)
#ttaietttb
def Clyde_encrypt(x):
    key = []
    code=""
    thething = []
    l = list(x)

    data = open(r"C:\Users\Utkar\Dropbox\Atom programs\encryption program\codes.txt","r")
    stuff = data.readlines()

    for i in range(0,len(stuff)):
        b = stuff[i]
        key.append(b[0])

    for i in range(0,len(l)):
        for a in range(0,len(key)):
            if l[i] == key[a]:
                c = []
                c.append(a)
                for position, line in enumerate(stuff):
                    if position in c:
                        thething.append(line)

    for i in range(0,len(thething)):
        word = list(thething[i])
        word.pop(0)
        word.pop(0)
        word.pop(0)
        word.pop(0)
        word.pop(-1)
        a = ""
        for j in word:
            a += j
        code += a
    return code

print(Clyde_encrypt(z))

y = str(input("Code:\n"))

def Clyde_decrypt(y):
    
    data = open(r"C:\Users\Utkar\Dropbox\Atom programs\encryption program\codes.txt","r")
    stuff = data.readlines()
    message = []
    words = []
    matrix =""
    ylist = list(y)

    for i in range(0,len(stuff)):
        word = list(stuff[i])
        word.pop(0)
        word.pop(0)
        word.pop(0)
        word.pop(0)
        word.pop(-1)
        q = ""
        for l in word:
            q += l
        words.append(q)

    # weirdwords = ""
    # for i in range(0,len(words)):
    #     i = words[i]
    #     weirdwords += i

    separated_codes = []
    r = 6
    cut_off = 0
    while (y != "") & (cut_off < len(ylist)):
        if y[:r] in words:
            separated_codes.append(y[:r])
            y = y[r:]
        elif y[:r+1] in words:
            separated_codes.append(y[:r+1])
            y = y[r + 1:]
        elif y[:r+2] in words:
            separated_codes.append(y[:r+2])
            y = y[r + 2:]
        elif y[:r+3] in words:
            separated_codes.append(y[:r+3])
            y = y[r + 3:]
        elif y[:r+4] in words:
            separated_codes.append(y[:r+4])
            y = y[r + 4:]
        elif y[:r+5] in words:
            separated_codes.append(y[:r+5])
            y = y[r + 5:]
        elif y[:r+6] in words:
            separated_codes.append(y[:r+6])
            y = y[r + 6:]
        elif y[:r+7] in words:
            separated_codes.append(y[:r+7])
            y = y[r + 7:]
        elif y[:r+8] in words:
            separated_codes.append(y[:r+8])
            y = y[r + 8:]
        cut_off += 6

    # for one_word in range(0,len(words)):
    #     if words[one_word] in y:
    #         print(words[one_word])
            # for f in range(0,len(ylist)):
            #     for i in range(0,len(words[one_word])):
            #         if y[f] == weirdwords[i]:
            #             separated_codes.append(word[one_word])

    for a in range(0,len(separated_codes)):
        for i in range(0,len(stuff)):
            if separated_codes[a] in stuff[i]:
                d = []
                d.append(i)
                for position, line in enumerate(stuff):
                    if position in d:
                        message.append(line)

    for i in range(0,len(message)):
        x = str(message[i])
        z = ""
        for contractor in x[:1]:
            z += contractor
        matrix += z
    return matrix

print(Clyde_decrypt(y))