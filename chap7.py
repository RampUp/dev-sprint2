# Name: Jessie Daubner
# Date: 2 February 2013


# Ex. 7.5
import math

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def estimate_pi():
	k = 0
	final_sum = 0
	constant = (2 * math.sqrt(2)) / 9801

	while True:
		numerator = factorial(4*k) * (1103 + 26390*k)
		denominator = (factorial(k)**4) * (396**(4*k))
		sum = constant * numerator / denominator
		final_sum += sum 
		
		if abs(sum) < 1e-15: break
		k += 1

	return 1 / final_sum, k

def main():
	print estimate_pi()

main()

# How many iterations does it take to converge? - Two