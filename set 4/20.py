n = int(input("How many elements do you want? : "))
numbers = []
squares = []

for i in range(n):
    el = int(input(f"Enter the element #{i+1}: "))
    numbers.append(el)

for x in numbers:
    squares.append(x**2)

print("Entered list :",numbers)
print("Square list :",squares)