# practice
# Ex 6.3 Page 55, Think Python, Sidd Tewari


#Exercise 6.3 Write a function is_between(x, y, z) that returns True
# if x <= y <= z or False otherwise.

# if is_divisible(x, y):
#     print 'x is divisible by y'

# def is_between(x,y,z):
# 	if (x <= y <= z):
# 		print 'True'
# 	else:
# 		print 'False'
# 	return 0

# is_between(1,2,3)


def is_between(x,y,z):
	return (x <= y <= z)

def call_fn():
	a = is_between(1,2,3)
	print 'a is', a
	b = is_between(4,2,8)
	print b

call_fn()
#is_between(1,2,3)