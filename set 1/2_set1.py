def qtyOfEvenNumbers(n):
	qty=0
	while n!=0:
		r=n%10
		if r%2==0:
			qty+=1
		n=n//10
	print(qty)

n = int(input('Enter a number : '))
qtyOfEvenNumbers(n)