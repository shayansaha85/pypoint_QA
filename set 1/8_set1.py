s = input('Enter the string : ')
c = input('Enter the character : ')
qty=0
for i in range(len(s)):
	if s[i]==c:
		qty+=1
if qty==0:
	print("Character absent.")
else:
	print(qty)