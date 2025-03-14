user_in = int(input('Enter an integer = '))
digits = 0

while user_in!=0:
    digits+=1
    user_in = user_in//10

print(f'No. of digits = {digits}')