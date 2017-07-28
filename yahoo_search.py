#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

if sys.version_info[0] != 3:
	sys.exit('This program needs Python 3.0')

import json
import urllib, urllib.parse, urllib.request, urllib.response

SEARCH_BASE = 'http://www.mocky.io/v2/597af778120000a205696cf0'

class YahooSearchError(Exception):
	pass

def search(query,**kwargs):
	kwargs.update({
		'output': 'json',
		})
	url = SEARCH_BASE + '?' + urllib.parse.urlencode(kwargs)

	print(url)
	result = json.load(urllib.request.urlopen(url))
	if 'Error' in result:
		raise YahooSearchError(result['Error'])

	print(result)
	return result

query = input('What do you want to search for?')
dic = search(query)
# for result in dic.items:
print(dic)
	# print('{0}:{1}'.format(result['Title'], result['Url']))




def get_error_details():
	return (2, 'second error details')

errnum, errstr = get_error_details()

print(errnum)
print(errstr)

a, *b = [1, 2, 3, 4]
print(a)
print(b)

c = 5; d = 8
c, d = d, c
print(c)
print(d)

flag = True
if flag: print('Yes')