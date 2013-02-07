# practice - Sidd Tewari
#6.2 Incremental development

import math

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	print result
	return result

distance(1, 2, 4, 6)