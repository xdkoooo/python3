#!/usr/bin/python

def printMax(a,b):
	if a > b :
		print(a, 'is maximum')
	elif a == b :
		print(a, 'is equal to', b)
	else:
		print(b, 'is maximum')

printMax(3, 5)


x = 50
def func():
	global x
	print('x is',x)
	x = 2
	print('Changed global x to',x)

func()
print('Value of x is', x)


def say(message, times=1):
	print(message * times)

say('Hello')
say('World', 5)

def funcName(a, b=5, c=10):
	pass
funcName(3,7)
funcName(25,c=24)
funcName(c=50, a=100)


def total(initial=5, *numbers, **keywords):
	count = initial
	for number in numbers:
		count += number
	for key in keywords:
		count += keywords[key]
	return count

print(total(10,1,2,3,vegetables=50, fruits=100))


def total2(initial=5, *, vegetables): 
	count = initial 
	count += vegetables 
	return count
print(total2(10,vegetables=50)) #66
#print(total2(10, 1, 2, 3,))



