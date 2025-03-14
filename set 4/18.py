n = int(input("How many elements do you want to enter?: "))
elements = []

for i in range(n):
    el = input(f'Enter the element {1+i}: ')
    elements.append(el)
newl = []
distinct_el = list(set(elements))
for x in distinct_el:
    count = elements.count(x)
    newl.append([count,x])

c = []
for x in newl:
    c.append(x[0])

maxElIndex = c.index(max(c))
mostRepeatedEl = newl[maxElIndex][1]
print(mostRepeatedEl)