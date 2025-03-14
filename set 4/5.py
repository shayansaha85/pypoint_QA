a = int(input('First number = '))
b = int(input('Second number = '))

print(f'You have entered: a = {a} and b = {b}')

temp = a
a = b
b = temp

print(f'After swapping: a = {a} and b = {b}')