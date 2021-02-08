def a_not_present(s):
    c=0
    for i in range(len(s)):
        if s[i].lower()=='a':
            c+=1
    if c==0:
        return True
    else:
        return False
        
arr = ["apple", "lucifer", "mega", "stock", "bitcoin"]
new = []
for i in range(0,len(arr)):
    if a_not_present(arr[i]):
        new.append(arr[i])
        
print(new)