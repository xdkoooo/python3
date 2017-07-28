#!/usr/bin/python

import string

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	text = text.lower()
	text = text.replace(' ','')
	for char in string.punctuation:
		text = text.replace(char,'')
	return text == reverse(text)

def main():
	something = input('Enter text:')
	if (is_palindrome(something)):
		print('Yes, "{0}" it is palindrome'.format(something))
	else:
		print('No, "{0}" it is not a palindrome'.format(something))


if __name__ == '__main__':
	main()
else:
	print('user_input.py was imported!')
	