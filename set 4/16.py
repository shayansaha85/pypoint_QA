number = input("Enter a number : ")
for i in range(len(number)):
    if number[i]=='0':
        print("Yes it has zero")
        exit(1)

print("It doesn't have zero")