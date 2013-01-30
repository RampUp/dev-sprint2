# Enter your answers for chapter 7 here
# Name: Christopher Van Schyndel

import math
# Ex. 7.5

def estimate_pi():
	left = 2* math.sqrt(2) / 9801.0
	k = 0
	estimate = 0
	# summation infinity -> k = 0
	while True:
		numerator = math.factorial(4*k) * (1103 + 26390*k) 
		denominator = math.factorial(k)**4 * 396 ** (4*k)
		# Overflow error unless calculations are seperated out.
		# step = left * math.factorial(4*k) * (1103 + 26390*k)  / math.factorial(k)**4 * 396 ** (4*k)
		step = left * numerator / denominator
		estimate += step
		k += 1
		if step < 1e-15: 
			break
	print k
	return 1 / estimate


# How many iterations does it take to converge?

print estimate_pi() == math.pi
# It takes 3.