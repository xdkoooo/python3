#!/usr/bin/python


__test = 8

class Robot:
	'''Represents a robot, with a name.'''

	population = 0

	_price = 100

	def __init__(self,name):
		self.name = name
		print('(Initialize {0})'.format(self.name))

		Robot.population += 1

	def __del__(self):
		print('{0} is being destroyed'.format(self.name))
		Robot.population -= 1

		if Robot.population == 0:
			print('{0} was the last one'.format(self.name))
		else:
			print('There are still {0:d} robots working.'.format(Robot.population))

	def sayHi(self):
		print('Greetings, my master call me {0}'.format(self.name))

	@staticmethod
	def howMany():
		print('We have {0:d} robots'.format(Robot.population))

	# howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3P0')
droid2.sayHi()
Robot.howMany()

# print(droid1.__test)
# print(_price)

print(droid1._price)

print(__test)


print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")

del droid1 
del droid2

Robot.howMany()

print(Robot.__doc__)

