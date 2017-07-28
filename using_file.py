#!/usr/bin/python

poem = '''\
Programming is fun
When the work is done 
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt','w')
'''
模式可以为读模式(’r’)、写模式(’w’)或追加模式(’a’)
'''
f.write(poem)
f.close()

f = open('poem.txt')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line,end='')
f.close()