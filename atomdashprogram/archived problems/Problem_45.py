from fpack import if_triangle_number, if_pentagonal_numbers, if_hexagonal_number


a = 166
while True:
    i = a*(3*a - 1)//2
    if if_triangle_number(i) and if_pentagonal_numbers(i) and if_hexagonal_number(i):
        print(i,a)
        break
    a+=1