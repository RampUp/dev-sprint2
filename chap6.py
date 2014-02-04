# Name: Jessie Daubner
# Date: 1 February 2013


# Ex. 6.6
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return  word[1:-1]

def is_palindrome(word):
	first_middle_index = len(word)-1
	if first(word) == last(word):
		if middle(word) == word[-(first_middle_index):-1]:
			return True
	else:
		return False


def main():
	my_word = raw_input("Type a word: ")
	
	print is_palindrome(my_word)

main() 

# When middle is called for a string with one or two letters, it returns an empty string
# since the first index is equal to the second index because there is not true middle.
# Using an empty string causes an index error because empty strings have no length and 
# thus no index value to slice. 


# Ex 6.8

def gcd(a, b):
	while (b != 0):	
		k = a % b
		a = b
		b = k 
	return a 

def main():
	num1, num2 = input("Enter two nonnegative numbers separated by a comma: ")
	gcd(num1, num2)
	print ("The greatest common divisor of " + str(num1) + " and " + str(num2) + " is " + str(gcd(num1, num2)) + ".") 

main()