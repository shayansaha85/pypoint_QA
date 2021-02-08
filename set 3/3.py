def isPrime(n):
    if n==1 or n==0:
        return False
    else:
        c=0
        for i in range(2,n+1):
            if n%i==0:
                c+=1
        if c==1:
            return True
        else:
            return False
            
n = int(input('Enter the quantity of elements: '))
i=0
arr=[]
newArr=[]
print('Enter the values below:')
while i<n:
    el=int(input())
    arr.append(el)
    i=i+1
for i in range(len(arr)):
    if isPrime(arr[i]):
        newArr.append("PRIME")
    else:
        newArr.append("NON-PRIME")

print(newArr)