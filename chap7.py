# Enter your answrs for chapter 7 here
# Name: Elizabeth Tenorio


# Ex. 7.5
# The mathematician Srinivasa Ramanujan found an infinite series
# that can be used to generate a numerical approximation of pi:

# Write a function called estimate_pi that uses this formula to
# compute and return an estimate of pi.
# You can check the result by comparing it to math.pi.

import math
# print eval('math.pi')

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
# print factorial(5)

def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    keep_going = True
    while keep_going == True:
        numerator = float(factorial(4*k) * (1103 + 26390 * k))
        #print 'Num: ', numerator
        denominator = float(factorial(k)**4) * 396**(4*k)
        #print 'Den: ', denominator
        term = factor * float(numerator/denominator)
        #print term
        total += term
        k += 1
        if term < 1e-15:
            keep_going == False
            print "Finished at iteration number", k
            break
    return 1 / total

print estimate_pi()

# How many iterations does it take to converge?
# Finished at iteration number 3

