#!/usr/bin/python
def printMax(x, y):
	'''Prints the maximum of the numbers.
	
	The two values must be integers.'''

	x = int(x)
	y = int(y)

	if x > y :
		print(x, 'is maximum')
	else :
		print(y, 'is maximum')

print(printMax(3,5))
print(printMax.__doc__)
