#!/usr/bin/python

zoo = ('python', 'elephant', 'penguin')
print(len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print(len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])

print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo) - 1 + len(new_zoo[2]))


ab = {  'Swaroop' : 'swaroop@swaroopch.com',
        'Larry' : 'larry@wall.org',
		'Matsumoto' : 'matz@ruby-lang.org',
   		'Spammer' : 'spammer@hotmail.com'
}

print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items() :
	print('Content {0} at {1}'.format(name, address))

print('Larry' in ab)