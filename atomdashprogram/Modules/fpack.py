from math import *

print(f"Here's your fannypack")

def primelist_till_x(x):
    marked = [0] * (x+1)
    value = 3
    s = {2}
    while value < x+1:
        if marked[value] == 0:
            s.add(value)
            i = value
            while i < x+1:
                marked[i] = 1
                i += value
        value += 2
    return(s)

def SumofSquares(x):
    S = int(((x)*(x+1)*(2*x+1)/6))
    return(S)

def SquareofSum(x):
    S = int((((x)*(x+1))/2)**2)
    return(S)

def triangle_number(x):
    return(int(x*(x+1)/2))

def if_triangle_number(x):
    num = (-1+(1+8*x)**(1/2))/2
    if num%1 == 0:
        return True
    else: return False

def factors(x):
    factors = []
    for i in range(1,ceil(sqrt(x))+1):
        if x%i == 0:
            factors.append(i)
            factors.append(int(x/i))
    for f in factors:
        if factors.count(f) != 1:
            factors.remove(f)
    return(factors)

def abundant_numbers(x):
    factors = [1]
    for i in range(2,ceil(sqrt(x))+1):
        if x%i == 0:
            factors.append(i)
            factors.append(int(x/i))
    if x < sum(set(factors)):
        return True
    else:
        return False

def Syracuse(x):
    l = []
    l.append(x)
    while x !=1 and x != 0:
        if x % 2 >0:
            x = ((3*x)+1)
            x = round(x)
            l.append(x)
        else:
            x = (x/2)
            x = round(x)
            l.append(x)
    return l

def day_calculator(date,month,year):
    doomsday_dic = {1500: 3, 1600: 2, 1700: 0, 1800: 5, 1900: 3, 2000: 2, 2100: 0, 2200: 5, 2300: 3, 2400: 2, 2500: 0, 2600: 5}
    a = doomsday_dic[year - int(year%100)]
    b = floor((int(year%100))/12)
    c = int((year%100)%12)
    d = floor(c/4)
    doomsday = int((a+b+c+d)%7)
    leapyear = False
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        leapyear = True
    monthful_doomsdays = {1:4 if leapyear == True else 3, 2:29 if leapyear == True else 28, 3:14, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}
    days = {0: 'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
    if date > monthful_doomsdays[month]:
        temp = date + doomsday - monthful_doomsdays[month]
        temp = int(temp%7)
        return(days[temp])
    else:
        temp = monthful_doomsdays[month] - date - doomsday
        temp = int((7 - int(temp%7))%7)
        return(days[temp])

def name_value(name):
    name = name.lower()
    sum = 0
    for letter in name:
        sum += (ord(letter) - 96)
    return sum

def sum_facto_digi(x):
    lis = [ factorial(int(a)) for a in str(x)]
    if sum(lis) == x:
        return True

def divide_primecheck(x):
    if x >= 2:
        for i in range(2,floor(sqrt(x)+1)):
            if x%i==0:
                return False
        return True
    else:
        return False

def clockwise_cycle(x):
    temp = str(x)
    li = set()
    for i in range(len(temp)):
        li.add(int(temp[i+1:]+temp[:i+1]))
    return(li)

def palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True

def delete_from_left(str):
    l = set()
    for i in range(len(str)):
        l.add(int(str[i:]))
    return(l)

def delete_from_right(str):
    l = set()
    for i in range(len(str)):
        l.add(int(str[:i+1]))
    return(l)

def if_pythagorean(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    return False

def pandigital(x):
    li = [1,2,3,4,5,6,7,8,9]
    a = [int(i) for i in str(x)]
    a.sort()
    if a == li[:len(a)]:
        return True

def if_pentagonal_number(x):
    num = (1+(24*x + 1)**(1/2))/6
    if num%1 == 0:
        return True
    else: return False

def if_hexagonal_number(x):
    num = (1+(8*x + 1)**(1/2))/4
    if num%1 == 0:
        return True
    else: return False

def if_heptagonal_number(x):
    if ((3+(9+40*x)**(1/2))/10)%1 == 0:
        return True
    else: return False

def if_octagonal_number(x):
    if ((1+(1+3*x)**(1/2))/3)%1 == 0:
        return True
    else: return False

def is_perfect_cube(number) -> bool:
    """
    Indicates (with True/False) if the provided number is a perfect cube.
    """
    number = abs(number)  # Prevents errors due to negative numbers
    return round(number ** (1 / 3)) ** 3 == number