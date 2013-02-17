# practice - Sidd Tewari 

#EXERCISE 6.1 Write a compare function that returns 1 if x > y, 0 if x == y, and-1 if x < y.
#compare function

def compareTwo(x,y):
	if x > y:
		return 1
	elif x < y:
		return -1
	elif x == y:
		return 0

a = compareTwo(2,3)
b = compareTwo(3,2)
c = compareTwo(3,3)

print a
print b
print c