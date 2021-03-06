a = int(input('First number = '))
b = int(input('Second number = '))

print(f'You have entered: a = {a} and b = {b}')

a,b = b,a

print(f'After swapping: a = {a} and b = {b}')