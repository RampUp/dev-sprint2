# practice - Sidd Tewari 
#6.3 Composition 

import math

def area(radius):
	temp = math.pi * radius**2
	return temp

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result

def circleArea(xc,yc,xp,yp):
	return area(distance(xc, yc, xp, yp))

	# radius = distance(xc,yc,xp,yp)
	# result = area(radius)
	# print result
	# return result

circleArea(1,2,1,6)