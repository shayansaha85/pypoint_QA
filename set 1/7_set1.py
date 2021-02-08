def isPrime(n):
	c=0
	if n==1 or n==0:
		return False
	else:
		for i in range(2,n+1):
			if n%i==0:
				c=c+1
		if c==1:
			return True
		else:
			return False

n = input('Enter the price : ')
sumOfPrime=0
for i in range(len(n)):
	if isPrime(int(n[i])):
		sumOfPrime+=int(n[i])
perc = sumOfPrime
result=int(n)-int(n)*(perc/100)
print(result)