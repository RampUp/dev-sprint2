# Enter your answrs for chapter 6 here
# Name: Sidd Tewari


# Ex. 6.6 - Palindrome 

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if not isinstance(word, str):
		return 'Sorry! Palindrome test is only applicable to strings'
	elif (len(word) <= 1):
		return True
	else:
		if first(word).lower() != last(word).lower():
			return False
		return is_palindrome(middle(word))

def tests():
	myTestsList = ['Nitttotttin', '123', 123, 'Cat on no tac', 'Cat on the no tac']
	for i in range (len(myTestsList)):
		print "Is '%s' a palindrome?  " % myTestsList[i] , is_palindrome(myTestsList[i])

tests()

# Q.1. - how to differentiate between the string and int 123 in the result print statements?
# Q.2. - how can I pass a list or array as to the tests function? Just DID!!! WOO!!! How to make it better?

# Ex 6.8

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd (b, a%b)

print gcd (7,21)
