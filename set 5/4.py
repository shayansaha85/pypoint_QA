user_in = int(input('Enter an integer = '))

reversed_num = 0

while user_in!=0:
    remainder = user_in%10
    reversed_num = reversed_num*10 + remainder
    user_in = user_in//10


print(reversed_num)