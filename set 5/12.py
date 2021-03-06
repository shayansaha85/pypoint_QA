n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

minNum = min(n1,n2)
listOfFactors = []

for i in range(1,minNum+1):
    if n1%i==0 and n2%i==0:
        listOfFactors.append(i)

setConvert = set(listOfFactors)

listConvert = list(setConvert)

hcf = 1
for x in listConvert:
    hcf = hcf*x

print("HCF =",hcf)