ask = 'y'

arr = []
while ask.lower()=='y':
    el=input('Enter the next element: ')
    arr.append(el)
    ask=input('Do you want to enter more? (y/n): ')

print(arr)
print('Thanks for entering')