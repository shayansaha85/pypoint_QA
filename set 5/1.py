user_in = input()
reversed_user_in = user_in[::-1]

if user_in == reversed_user_in:
    print('It is a palindrome')
else:
    print('It is not a palindrome')