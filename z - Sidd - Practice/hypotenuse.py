# practice # Sidd

# Exercise 6.2. Use incremental development to write a function returns the length 
# of the hypotenuse of a right triangle given the lengths of the two legs as arguments. 
# Record each stage of the development process as you go.

import math
def hypotenuse(x,y):
	# xsquared = x**2
	# ysquared = y**2
	# sumTotal = xsquared + ysquared
	#hypSide = math.sqrt(sumTotal)
	hypSide = math.sqrt(x**2 + y**2)
	print hypSide
	return 0.0

hypotenuse(3,4)