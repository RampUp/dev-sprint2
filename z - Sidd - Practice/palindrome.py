# Ex 6.6 palindrome - Sidd Tewari

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

def tests(t):
	print ("Is '%s' a palindrome?" % t), is_palindrome(t)

tests('Nitttotttin')
tests('123')
tests(123)
tests('Cat on no tac')
tests('Cat on the no tac')