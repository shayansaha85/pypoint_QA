def qtyOfVowels(s):
	qty=0
	for i in range(len(s)):
		if s[i].lower()=='a' or s[i].lower()=='e' or s[i].lower()=='i' or s[i].lower()=='o' or s[i].lower()=='u':
			qty+=1
	if qty==0:
		print(f'{s} has no vowels')
	else:
		print(f'{s} has {qty} vowels')

s = input('Enter your string : ')
qtyOfVowels(s)