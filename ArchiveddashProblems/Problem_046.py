from fpack import divide_primecheck

def Gfollowers(x):
    i = 0
    while x-i > 0:
        if divide_primecheck((x-2*(i**2))):
            return True
        i+=1
    return False

b = 3
while True:
    if not divide_primecheck(b):
        if not Gfollowers(b):
            print(b)
            break
    b+=2