try:
    user_in = int(input('Enter an integer = '))
    result = 1
    for i in range(1,user_in+1):
        result = result*i

    print(f'Factorial ans = {result}')
except ValueError:
    print('Please enter integer values only')