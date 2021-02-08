import math

print('Enter the coordinate of centre of the circle')
x0 = float(input('X = '))
y0 = float(input('Y = '))

radii = 3.5

print('Enter the input coordinates')
x = float(input('X = '))
y = float(input('Y = '))

dist_from_centre = math.sqrt(((x-x0)**2)+((y-y0)**2))
if dist_from_centre<radii:
	print('INSIDE')
elif dist_from_centre==radii:
	print("ON")
else:
	print('OUT')