# Enter your answrs for chapter 6 here
# Name: Elizabeth Tenorio


# Ex. 6.6
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
#print first('biology')
#print last('biology')
# print middle('biology')
# print middle('hit')
# print middle('hi')
# print middle('a')
# print middle('')

# Type these functions into a file named palindrome.py and test them out.
# What happens if you call middle with a string with two letters?
#=> returns an empty string
# One letter?
#=> returns an empty string
# What about the empty string, which is written '' and contains no letters?
#=> returns an empty string

# Write a function called is_palindrome that takes a string argument and returns
# True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length of a string.

def is_palindrome(word):
    if len(word) <=1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

# print is_palindrome('cat') #=>False
# print is_palindrome('noon') #=>True
# print is_palindrome('radar') #=> True



# Ex 6.8
# Write a function called gcd that takes parameters
# a and b and returns their greatest common divisor.

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    elif a > b:
        r = a % b
        if r == 0:
            return b
        else:
            # print r, b
            return gcd(b, r)
    elif b > a:
        a, b = b, a
        return gcd(a,b)


#print gcd(0, 4)
#print gcd(4, 0)
#print gcd(4, 2)
#print gcd(21, 9)
#print gcd(13, 17)
#print gcd(125, 4300)



