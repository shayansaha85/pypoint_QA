# prime checker function
def is_prime(n):
	if n==0 or n==1:
		return True
	else:
		c=0
		for i in range(2,n+1):
			if n%i==0:
				c+=1
		if c==1:
			return True
		else:
			return False

# extracting nearest greater prime number
def nearest_greater_prime_number(n):
	i=n
	while True:
		i=i+1
		if is_prime(i):
			break
	return i

# extracting first digit
def first_digit(n):
	t=n
	qty=0
	while t!=0:
		t=t//10
		qty+=1
	power=qty-1
	denom=pow(10,power)
	first_d=n//denom
	return first_d

# extracting last digit
def last_digit(n):
	last_d=n%10
	return last_d

# main function
def main_fun(input1):
	if input1<10:
		if is_prime(input1):
			return pow(input1,input1)
		else:
			adjacent_prime=nearest_greater_prime_number(input1)
			return pow(adjacent_prime,adjacent_prime)
	else:
		firstDigit=first_digit(input1)
		lastDigit=last_digit(input1)
		if is_prime(firstDigit) and is_prime(lastDigit):
			return pow(firstDigit,lastDigit)
		elif is_prime(firstDigit) or is_prime(lastDigit):
			if is_prime(firstDigit):
				adjacent_prime=nearest_greater_prime_number(lastDigit)
				return pow(firstDigit,adjacent_prime)
			elif is_prime(lastDigit):
				adjacent_prime=nearest_greater_prime_number(firstDigit)
				return pow(adjacent_prime,lastDigit)

v1=2637
v2=3634
v3=4267
v4=3
v5=4

print(f'Case #1 : {main_fun(v1)}')
print(f'Case #2 : {main_fun(v2)}')
print(f'Case #3 : {main_fun(v3)}')
print(f'Case #4 : {main_fun(v4)}')
print(f'Case #5 : {main_fun(v5)}')
