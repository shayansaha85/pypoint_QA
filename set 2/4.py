def decimalToBinary(decimal):
	binary=0
	i=1
	while decimal!=0:
		remainder=decimal%2
		binary=binary+remainder*i
		i=i*10
		decimal=decimal//2
	return binary

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

def digitSum(n):
	sum=0
	while n!=0:
		r=n%10
		sum+=r
		n=n//10
	return sum

input1 = int(input('First integer: '))
input2 = int(input('Second integer: '))

for i in range((input1+1),input2):
	if isPrime(digitSum(decimalToBinary(i))):
		print(i)
