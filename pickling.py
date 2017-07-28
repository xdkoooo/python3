#!/usr/bin/python

import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple','mango','carrot']

#写入一个二进制文件
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist
#读取二进制文件
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)

s = input('Enter someting -->')



