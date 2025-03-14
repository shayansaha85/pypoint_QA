num1 = int(input('First integer = '))
num2 = int(input('Second integer = '))

result = 1

i=0
k=1
while k>0:
    result = max(num1,num2)*k
    if result%num1==0 and result%num2==0:
        break
    k=k+1
print(result)