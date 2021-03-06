def is_divisble(l,n):
    count=0
    for x in l:
        if x%n == 0:
            count+=1
    if count==len(l):
        return True
    else:
        return False

print("Enter the numbers separated by space (e.g. 5 16 9 3)")
inputs = input()

numbers = []

for i in inputs.split():
    numbers.append(int(i))

minNum = min(numbers)

factors = []

for i in range(1,minNum):
    if is_divisble(numbers,i):
        factors.append(i)

distinct_factors = list(set(factors))

hcf = 1
for x in distinct_factors:
    hcf = hcf*x

print("HCF =",hcf)