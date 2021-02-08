def countDigits(n):
    d=0
    while n!=0:
        n=n//10
        d+=1
    return d

def isArmstrong(n):
    result=0
    t=n
    digits=countDigits(n)
    while n!=0:
        r=n%10
        result+=(r**digits)
        n=n//10
    if t==result:
        return True
    else:
        return False

START = int(input('START: '))
END = int(input('END : '))
for i in range(START,END+1):
    if isArmstrong(i):
        print(i)