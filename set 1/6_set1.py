n = input('Enter a number : ')
c = 0
for i in range(len(n)-1):
	if n[i]<=n[i+1]:
		c+=1
	
if c==len(n)-1:
	print('OK')
else:
	print('NO')