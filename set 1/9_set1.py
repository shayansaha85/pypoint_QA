sentence = input('Enter a string (with spaces) : ')
l = []
l = sentence.split()
result_string = ""
for i in range(len(l)):
	result_string+=l[i][0].upper()+l[i][1:len(l[i])].lower()

print(result_string)