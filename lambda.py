#!/usr/bin/python

def make_repeater(n):
	return lambda s: s * n

twice = make_repeater(2)

print(twice('word'))
print(twice(5))

'''
lambda 创建的比较函数来完成 list.sort() 吗?
points = [ { 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 } ]
# points.sort(lambda a, b : cmp(a['x'], b['x']))
'''

listone = [2,3,4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)

def powersum(power, *args):
	total = 0
	for i in args:
		total += pow(i, power)
	return total

print(powersum(2, 3, 4))

print(powersum(2,10))

exec('print("Hello World")')

print(eval('2*3'))


mylist = ['item']

assert len(mylist) >= 1

i = []

i.append('item')

print(i)

print(repr(i))

print(eval(repr(i)))

eval(repr(i)) == i