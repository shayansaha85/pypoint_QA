n = int(input('Enter a number : '))
c = 0
if n<=0:
	print('Inappropriate input for checking this.')
elif n==1:
	print('1 is neither prime nor non-prime.')
else:
	for i in range(2,n+1):
		if n%i==0:
			c+=1
	if c==1:
		print('Prime')
	else:
		print('Non-prime')