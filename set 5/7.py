import math
print('The equation is: ax^2 + bx + c')

print('\nEnter values:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

numerator1 = -b + math.sqrt(b*b - 4*a*c)
numerator2 = -b - math.sqrt(b*b - 4*a*c)
denominator = 2*a

ans1 = numerator1/denominator
ans2 = numerator2/denominator

print(f'x = {ans1}, {ans2}')