def Collatz(i):
    L=[]
    while i!=1:
        if i%2==0:
            L.append(int(i))
            i=i/2
        else:
            L.append(int(i))
            i=((3*i)+1)
    return(L)

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


x=int(input("Number Bata: "))
first=Collatz(x)
i=2
while i<len(first) and i>=2: # get pos and prime variables
    if(is_prime_number(first[-i])):
        pos=i
        prime=first[-i]
        i=0
    i += 1

print("The position is",pos,"th from the right and the prime is",prime)

nam = 0
for i in range(1,10):
    z=Collatz(x**i)
    print(z)
    if z[-pos]==prime:
        a=1
    else:
        print("Utkarsh rong haha funi")
        nam += 1

print(nam)