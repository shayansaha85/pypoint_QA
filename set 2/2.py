input1=input('Input1 : ')
input2=input('Input2 : ')

chars=[]
for i in range(len(input1)):
	chars.append(input1[i])
j=0
count=0
new=[]
w=0
while j<len(chars):
	p=0
	while p<len(input2):
		if chars[j].lower()==input2[p].lower() and (input2[p].lower() not in new):
			new.append(chars[j].lower())
		p=p+1
	j=j+1
print()

if len(new)!=0:
	print('These characters are common in both the strings')
	print('------------------------------------------------')
	for x in new:
		print(x)
else:
	print('No characters are common')
