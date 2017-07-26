#!/usr/bin/python

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1]) 
print('Item 2 is', shoplist[2]) 
print('Item 3 is', shoplist[3]) 
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2]) 
print('Character 0 is', name[0])

print('\n\n\n')
print('Item 1 to 3 is', shoplist[1:3]) 
print('Item 2 to end is', shoplist[2:]) 
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

print('\n\n\n')
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:]) 
print('characters 1 to -1 is', name[1:-1]) 
print('characters start to end is', name[:])

bri = set(['brazil', 'russia', 'india'])
print('india' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))

print(bri & bric)


print('\n\n\n')
name = 'Swaroop'
if name.find('war') != -1:
	print('Yes, it contains the string "war"')

delimiter = '_*_'
print(delimiter.join(shoplist))