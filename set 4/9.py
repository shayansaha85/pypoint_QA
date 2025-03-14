num = int(input('Enter an integer = '))

print(f'Multiplication table of {num} is :')
for i in range(1,11):
    print(f'{num} x {i}\t=\t{num*i}')