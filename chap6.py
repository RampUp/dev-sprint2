# Enter your answers for chapter 6 here
# Name: Christopher Van Schyndel


# Ex. 6.6

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

# 1a. Returns an empty string ( no space ), as there is nothing in the middle of a two letter string.
# 1b. Also returns an empty string ( no space ), as you are indexing nothing.

# 2.

# This function takes a string and returns True if it is a Palindrome, and False otherwise.
def is_palindrome(string):
	pass
	length = (len(string) / 2)
	stringchecker1 = ''
	stringchecker2 = ''
	for length in range(length):
		stringchecker1 += string[length]
		stringchecker2 += string[-(length+1)]
	if stringchecker1 == stringchecker2:
		return True
	else:
		return False

# Ex 6.8

# This function finds the greatest common denominator of two integers.
# It should, but will not work for decimals in python.  It is likely that the decimal
# module is required to fix this.  Ex. 1.0 % 2 gives the result 0.2.  However, 1.6 % 2
# gives the result 0.
def gcd(a, b):
	if a != 0 and b != 0:
		r = a % b
		print r
		print str(b)
		if r != 0:
			gcd(b, r)
		else:
			print "The greatest common denominator is " + str(abs(b))
	else:
		print "Cannot find the gcd of 0!"
