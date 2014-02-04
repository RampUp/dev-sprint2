# Ex 6.6 palindrome - Sidd Tewari

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if not isinstance(word, str):
		print 'Palindrome is only applicable to strings'
		return None
	elif (len(word) == 0):
		print 'Please provide a valid word - at least one character'
	else:
		if first(word).lower() == last(word).lower():
			if len(middle(word)) == 0 or len(middle(word)) == 1:
				print 'True'
				return
			elif len(middle(word)) > 1:
				is_palindrome(middle(word))
		else:
			print 'False'
			return

is_palindrome('Nitttotttin')
is_palindrome('123')
is_palindrome(123)
is_palindrome('Cat on no tac')
is_palindrome('Cat on no tac')