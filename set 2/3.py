def decimalToBinary(decimal):
	binary=0
	i=1
	while decimal!=0:
		remainder=decimal%2
		binary=binary+remainder*i
		i=i*10
		decimal=decimal//2
	return binary

input1=int(input('Input : '))
binEq=decimalToBinary(input1)
qty=0
while binEq!=0:
	r=binEq%10
	if r==1:
		qty+=1
	binEq=binEq//10

print(qty)